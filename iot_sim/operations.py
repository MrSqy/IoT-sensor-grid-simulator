"""Arayüz girişinden bağımsız, kimliğe dayalı ve bütünlüğü koruyan işlemler."""
from .models import Kind, Entity, SensorProps, SourceProps, UavProps
from .engine import find_entity_by_id, tile_occupied, route_is_valid
from .cargo import attach_to_uav
from .uav import sync_cargo


def add_entity(sim, kind, x, y):
    """Boş ve sınırlar içindeki kareye benzersiz kimlikle nesne ekle."""
    if not (0 <= x < sim.width and 0 <= y < sim.height) or tile_occupied(sim.entities, x, y):
        raise ValueError("Bu kare dolu veya harita dışında.")
    e = Entity(sim.next_id, kind, x, y)
    if kind == Kind.SENSOR:
        e.sensor = SensorProps()
    elif kind in (Kind.SOURCE, Kind.BURNED):
        e.source = SourceProps()
    elif kind == Kind.UAV:
        e.uav = UavProps(x=float(x), y=float(y))
    sim.entities.append(e)
    sim.next_id += 1
    return e


def move_entity(sim, eid, x, y):
    """Drone dahil tek nesneyi taşı; yükleri aynı işlemde eşitle."""
    e = find_entity_by_id(sim.entities, eid)
    if e is None or e.carried_by is not None:
        raise ValueError("Taşınan nesneyi önce drone'dan indir.")
    others = [other for other in sim.entities if other.id != eid]
    if not (0 <= x < sim.width and 0 <= y < sim.height) or tile_occupied(others, x, y):
        raise ValueError("Hedef kare dolu veya harita dışında.")
    e.tx, e.ty = x, y
    if e.uav:
        e.uav.x, e.uav.y = float(x), float(y)
        sync_cargo(sim.entities, e)


def release_cargo(sim, drone, deleting=False):
    """Tüm yükler için önce yer bul; yer yoksa hiçbir bağlantıyı değiştirme."""
    cargo = [find_entity_by_id(sim.entities, cid) for cid in drone.uav.carrying_ids]
    cargo = [e for e in cargo if e is not None]
    occupied = {(e.tx, e.ty) for e in sim.entities if e.carried_by is None
                and not (deleting and e.id == drone.id)}
    candidates = ((abs(x - drone.tx) + abs(y - drone.ty), y, x)
                  for y in range(sim.height) for x in range(sim.width)
                  if (x, y) not in occupied)
    import heapq
    places = heapq.nsmallest(len(cargo), candidates)
    if len(places) < len(cargo):
        raise ValueError("Yükleri bırakacak boş kare yok; işlem yapılmadı.")
    for e, (_, y, x) in zip(cargo, places):
        e.carried_by = None
        e.tx, e.ty = x, y
    drone.uav.carrying_ids.clear()


def delete_entity(sim, eid):
    """Sağ tık ve DEL aynı işlemi çağırır; geçersiz yük referansı bırakmaz."""
    e = find_entity_by_id(sim.entities, eid)
    if e is None:
        return
    if e.uav:
        release_cargo(sim, e, deleting=True)
    if e.carried_by is not None:
        parent = find_entity_by_id(sim.entities, e.carried_by)
        if parent and parent.uav:
            parent.uav.carrying_ids.remove(e.id)
    sim.entities.remove(e)
    sim.alarm.update(sim.entities, sim.time)
    sim.history.pop(eid, None)


def set_route(sim, drone, points):
    """Rota türü ve ilk yaklaşım dahil geçerli rotayı atomik olarak kur."""
    obstacles = {(e.tx, e.ty) for e in sim.entities if e.kind == Kind.OBSTACLE}
    if any(not (0 <= x < sim.width and 0 <= y < sim.height) for x, y in points):
        raise ValueError("Durak harita dışında.")
    if not route_is_valid(points, obstacles, drone.uav.route_mode, (drone.uav.x, drone.uav.y)):
        raise ValueError("En az iki farklı durak gerekli; rota engelden geçemez.")
    drone.uav.route = list(points)
    drone.uav.route_i, drone.uav.route_dir = 0, 1
    drone.uav.blocked_reason = ""


def attach(sim, drone_id, cargo_id):
    """Kapasite ve tür kuralını kontrol ederek yükle."""
    drone = find_entity_by_id(sim.entities, drone_id)
    cargo = find_entity_by_id(sim.entities, cargo_id)
    if not drone or not cargo or not attach_to_uav(sim.entities, drone, cargo):
        raise ValueError("Drone bir sensör veya en fazla üç kaynak taşıyabilir.")
