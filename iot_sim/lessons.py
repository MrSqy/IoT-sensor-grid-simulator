"""Aynı şablonda altı Türkçe deney ve değiştirilebilir başlangıç sahneleri."""
from .models import Entity, Kind, SensorProps, SensorMode, SourceProps, SourceType, GasMode, UavProps, RouteMode
from .scene import to_scene

LESSONS = [
    dict(title="Uzaklık ve ölçüm", goal="Kaynağın etkisi ile cihaz hatasını ayır.",
         steps=["Başlat; Yakın ve Uzak sensörlerinin sıcaklıklarını karşılaştır.",
                "Duraklat; Uzak sensörünü seç, M ile kaynağa yaklaştır ve devam et.",
                "Grafikteki artışı incele. Gürültü sıfırken teorik değer ile ölçüm örtüşür."],
         why="Kaynak katkısı uzaklıkla azalır. Noktasal sensör kendi bulunduğu ortamı ölçer; ayrı bir algılama yarıçapı yoktur."),
    dict(title="Gürültü, kalibrasyon ve alarm", goal="Ölçüm hatasını ve alarmın eşik çevresindeki davranışını gör.",
         steps=["Başlat; grafikte teorik çizgi ile değişken ölçümü karşılaştır.",
                "Sensörde TEMP kanalını seç; kalibrasyonu +10 yap. Ölçüm sürekli yukarı kayar.",
                "Açılış/kapanış eşiklerini farklı ayarla. Tekrar bildirimini ve kotayı değiştir; olay kaydı sürer."],
         why="Rastgele sapma her okumada değişir. Kalibrasyon sabit sapmadır. Ayrı kapanış eşiği alarmın sınırda titreşmesini azaltır."),
    dict(title="Örnekleme ve pil", goal="Daha sık ve daha çok kanallı ölçümün enerji maliyetini karşılaştır.",
         steps=["Başlat; Tek kanal ve Dört kanal sensörlerinin pil grafiğini izle.",
                "Bir sensörün örnekleme aralığını azalt; zaman başına tüketim artar.",
                "Pil bitince durumun Normal değil Pil bitti olduğunu gör; pil ekleyerek ölçümü yeniden başlat."],
         why="Her açık kanal örnek başına enerji tüketir. Örnekleme aralığını uzatmak örnek sayısını azaltır; küçük bir bekleme tüketimi de vardır."),
    dict(title="Bağımsız gaz kanalları", goal="CO, CO₂ ve H₂ kanallarının ayrı değer ve eşiklerini keşfet.",
         steps=["Kaynağı seç; başlangıçta yalnız CO açıktır. Sensörün kanallarını karşılaştır.",
                "Kaynakta CO₂ aç ve yoğunluğunu değiştir; CO ölçümü bundan etkilenmez.",
                "Sensörde bir kanalı kapat. Dosyada boş değer görülür; bu gerçek sıfır ölçüm değildir."],
         why="Her gazın yoğunluğu, yayılım yarıçapı ve alarm eşiği ayrıdır. ppm değerlerinin gaz türü belirtilmeden toplanması alarm anlamı taşımaz."),
    dict(title="Hareketli ölçüm", goal="Drone'un taşıdığı sensörle konuma bağlı ölçüm üret.",
         steps=["Başlat; drone kaynağa yaklaşırken yükteki sensörün grafiğini izle.",
                "Drone'u seç, Yük #2 düğmesiyle sensörü incele. Taşınan sensör de alarm ve kayıt üretir.",
                "Duraklat; drone'u seçip K ile yeni rota çiz, K ile kaydet. Engel ekleyerek durma nedenini gözle."],
         why="Drone konumu sabit simülasyon adımlarıyla değişir. Yükün ölçümü drone'un kesintisiz konumundan hesaplanır."),
    dict(title="Sıcaklık ve tutuşma", goal="Yanabilirlik, sıcaklık ve maruz kalma süresinin birlikte etkisini gör.",
         steps=["Başlat; kaynak yanındaki ağacın maruz kalma süresini izle.",
                "Yanabilir ağaç tutuşurken yanmayan engelin değişmediğini gözle.",
                "Başa dön; ağacın tutuşma sıcaklığını yükselt veya kaynak sıcaklığını azalt ve karşılaştır."],
         why="Bu eğitim kuralında ağaç eşik sıcaklığının üzerinde yeterince uzun kalınca kaynağa dönüşür. Gerçek yangın tahmini değildir."),
]


def lesson_scene(number):
    """1–6 arası hazır sahneyi her çağrıda yeni nesnelerle üret."""
    if not 1 <= number <= 6:
        raise ValueError("Deney numarası 1–6 olmalı.")
    def sensor(eid, x, y, name, modes=None, **settings):
        return Entity(eid, Kind.SENSOR, x, y, name=name,
                      sensor=SensorProps(modes=set(modes or [SensorMode.TEMP]), **settings))
    source = Entity(3, Kind.SOURCE, 12, 12, name="Sıcaklık kaynağı",
                    source=SourceProps(temp_celcius=180, range_tiles=12))
    if number == 1:
        entities = [sensor(1, 10, 12, "Yakın", noise_percent=0), sensor(2, 16, 12, "Uzak", noise_percent=0), source]
    elif number == 2:
        source.tx, source.source.temp_celcius = 10, 75
        s = sensor(1, 12, 12, "Ölçüm deneyi", noise_percent=12)
        s.sensor.thresholds["TEMP"], s.sensor.clear_thresholds["TEMP"] = 62, 55
        entities = [s, source]
    elif number == 3:
        entities = [sensor(1, 10, 12, "Tek kanal", battery=24, sample_interval=1),
                    sensor(2, 14, 12, "Dört kanal", modes=list(SensorMode), battery=24, sample_interval=1)]
    elif number == 4:
        source.source = SourceProps(stype=SourceType.GAS, gas_modes={GasMode.CO})
        source.name = "Gaz kaynağı"
        entities = [sensor(1, 10, 12, "Çoklu gaz", modes=list(SensorMode)), source]
    elif number == 5:
        drone = Entity(1, Kind.UAV, 7, 12, name="Gezgin", uav=UavProps(
            x=7, y=12, route=[(7,12),(18,12)], route_mode=RouteMode.PINGPONG, carrying_ids=[2], speed=2))
        s = sensor(2, 7, 12, "Uçan sensör", noise_percent=0)
        s.carried_by = 1
        source.tx, source.ty = 13, 14
        entities = [drone, s, source]
    else:
        source.source.temp_celcius = 300
        entities = [source, Entity(1, Kind.OBSTACLE, 13, 12, name="Yanabilir ağaç", ignition_seconds=3),
                    Entity(2, Kind.OBSTACLE, 12, 13, name="Yanmayan engel", flammable=False),
                    sensor(4, 16, 12, "Yangın gözlemcisi", noise_percent=0)]
    return to_scene(entities, seed=42, lesson=number)
