"""Bütün dosyalar ve Python sembolleri için kaynakla eşleşen Türkçe eki üret."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/"docs"/"KOD_REHBERI.md"
MANIFEST=ROOT/"docs"/"kod_kapsami.json"
EXCLUDE={".git",".venv","venv","env","__pycache__","exports","scenes",".pytest_cache"}
ROLES={
 "main.py":"Güncel komut satırı girişidir; iot_sim.app.main işlevine aktarır.",
 "CALCULATOR.py":"Bağımsız nesne yönelimli sensör/olay dersi. Güncel uygulama yalnız RateLimiter sınıfını kullanır.",
 "iot_sim/models.py":"Nesne ve kanal türleri ile bütün bileşenlerin paylaştığı durum alanlarını tanımlar.",
 "iot_sim/sensors.py":"Teorik ortam, noktasal cihaz ölçümü, sapma ve enerji tüketimini hesaplar.",
 "iot_sim/simulation.py":"Ekrandan bağımsız deney saati, güncelleme sırası, RNG ve sınırlı geçmişin sahibidir.",
 "iot_sim/alarm_bridge.py":"Tek kanal alarm kararı, durum geçişleri ve tekrarlı bildirim kotasını birleştirir.",
 "iot_sim/operations.py":"Arayüzün ekleme, taşıma, silme, yük ve rota eylemlerine ortak giriş sağlar.",
 "iot_sim/cargo.py":"Drone yükleme kapasitesi ve karşılıklı taşıyıcı referanslarını yönetir.",
 "iot_sim/uav.py":"LOOP/PINGPONG hareketini, engelde durmayı ve yük eşitlemesini uygular.",
 "iot_sim/fire.py":"Yanabilirlik, eşik sıcaklık ve süreye göre ağaçları kaynak yapar.",
 "iot_sim/scene.py":"Başlangıç sahnesinin sürümlü JSON biçimi, doğrulaması ve atomik yazımıdır.",
 "iot_sim/exporter.py":"Her deney için yeni klasör ve dosyalar oluşturur; ölçüm/olay/değişiklikleri yazar.",
 "iot_sim/lessons.py":"Altı Türkçe deneyin yönergeleri ve taze başlangıç sahnelerini üretir.",
 "iot_sim/app.py":"Pygame yaşam döngüsü, pencere, buton eylemleri, klavye/fare ve dosya girişidir.",
 "iot_sim/panel.py":"Nesne, deney ve olay sekmelerini kaydırılabilir içerikle oluşturur.",
 "iot_sim/ui_widgets.py":"Satır sarma, metin ve buton çizimi için ortak bileşenlerdir.",
 "iot_sim/render.py":"Harita, kaynak yarıçapı, teorik katman, nesne ve rota çizimidir.",
 "iot_sim/graphs.py":"Sensör geçmişini kanal/birim bazında ölçüm, teori, eşik ve pil grafiğine dönüştürür.",
 "iot_sim/camera.py":"Ekran ve dünya koordinatları arasındaki dönüşüm ve zoom durumudur.",
 "iot_sim/viz.py":"Yüzeyler için bellekle sınırlı LRU önbelleği ve görsel yardımcı içerir.",
 "iot_sim/assets.py":"İkonları yükler; eksik görselde None ile şekil çizimine geri dönüş sağlar.",
 "iot_sim/engine.py":"Kimlik/konum arama, sınırlandırma ve rota için karo geometrisi sağlar. Eski doğruluk yardımcısı korunmuştur.",
 "iot_sim/constants.py":"Korunmuş sabitler. Yeni ekran boyutu App.layout, zaman adımı Simulation.STEP içindedir.",
 "iot_sim/geom.py":"Korunan çokgen sıralama ve alan yardımcıları; yeni noktadan ölçüm akışına bağlı değildir.",
 "iot_sim/IoT.py":"Bazı model/motor/ölçüm adlarını yeniden sunan korunmuş uyumluluk modülüdür.",
 "iot_sim/__init__.py":"Paketin dışarı sunduğu isimleri tanımlar; pencere açmaz.",
 "tests/test_simulation.py":"Model, alarm, enerji, rota, yük, sahne, kayıt ve deterministik zaman regresyonları.",
 "tests/test_ui.py":"Pygame çizimi ve gerçek olay işleyicisini kontrollü girişlerle sınar.",
 "tools/verify_runtime.py":"Altı sahne ekranı, X11/SDL sürücü bilgisi ve eğitim ölçeğinde performans üretir.",
 "tools/build_guide.py":"Bu ekin envanterini, kod kesitlerini ve kaynak hash manifestini üretir/kontrol eder.",
 "README.md":"Kurulum, giriş komutları ve ayrıntılı rehberlere ulaşım.",
 "PROJE_REHBERI.md":"Kavram, mimari, formül ve kullanıcı senaryolarını adım adım öğreten ana rehber.",
 "UYGULAMA_PLANI.md":"İnceleme kanıtı, kullanıcı kararları, onaylı kapsam ve teslim kaydı.",
 "AGENTS.md":"Repo kapsamında ortak çalışma, yetki ve dokümantasyon talimatları.",
 "requirements.txt":"Pygame sürümünü sabitler; pip tarafından temiz ortam kurulumunda okunur.",
 ".gitignore":"Ortam, önbellek, kullanıcı sahneleri ve deney çıktılarının Git'e eklenmesini önler.",
 "LICENSE":"Projenin MIT lisans koşulları; uygulama davranışı üretmez.",
 "docs/KOD_REHBERI.md":"Bu üretilen ayrıntılı kaynak eki; kaynak değişince üreticiyle yenilenir.",
 "docs/kod_kapsami.json":"Python kaynak hashleri ve sembol konumları; --check ile eşleşme doğrulanır.",
 "docs/DOGRULAMA.md":"Gerçekten yürütülen kontroller ve doğrulanmayan platform/davranış sınırları.",
 "docs/runtime.json":"Son kontrollü X11 deney çalıştırmasının ham ölçüm raporu.",
 "docs/screenshots/deney-atolyesi.png":"Gerçek uygulama çiziminden alınmış belgeleme ekranı; README kullanır.",
}
PURPOSES={
 "clamp":"Sayısal değeri alt ve üst sınır arasında tutar; panel ve konum ayarlarında kullanılır.",
 "accuracy_for_dist":"Eski uzaklık tablosundan yüzde döndürür; yeni noktasal ölçüm bunu kullanmaz.",
 "tile_occupied":"Taşınmayan nesneler arasında hedef karenin dolu olup olmadığını söyler.",
 "find_entity_at":"Bir karenin seçilebilir nesnesinin listedeki indeksini bulur; taşınan yükü atlar.",
 "find_entity_by_id":"Kalıcı nesne kimliğini gerçek nesneye çözer; bulunamazsa None döner.",
 "build_entity_index":"Kimlikten nesneye doğrudan erişim için sözlük üretir.",
 "dist":"İki konum arasındaki Öklid uzaklığını hesaplar.",
 "bresenham_tiles":"Bir doğru boyunca geçilen tam sayı karolarını sırayla üretir; rota engel testinin temelidir.",
 "can_attach_to_uav":"Taşıyıcı türü, yük türü, zaten taşınma ve kapasite kurallarını kontrol eder.",
 "attach_to_uav":"Uygun yükü drone'a bağlar; kimlik listesi, taşıyıcı ve konumu birlikte günceller.",
 "load_icon":"Görüntüyü alfa kanallı yüzeye dönüştürür; yükleme başarısızsa None ile geri dönüşe izin verir.",
 "get_scaled_icon":"Aynı ikon ve boyut için yeniden ölçeklemeyi önbellekten karşılar.",
 "display_name":"Kullanıcı adı varsa kimlikle birlikte, yoksa tür ve kimlikle okunur etiket üretir.",
 "world_to_screen":"Kamera merkezi, görünüm alanı ve zoom ile dünya noktasını piksele çevirir.",
 "screen_to_world":"Ekrandaki fare konumunu kamera dönüşümünün tersiyle dünya koordinatına çevirir.",
 "zoom_at":"Mevcut ölçeği verilen katsayıyla değiştirip izin verilen aralıkta tutar.",
 "clamp_zoom_for_map":"Zoom değerini sınırlar; alternatif sürümde harita boyutunu da dikkate alır.",
 "focus_scene":"Kamerayı sahnedeki görünür nesnelerin ortalamasına taşır.",
 "message":"Kullanıcıya kısa durum/hata mesajı ve görünme süresi ayarlar.",
 "btn":"Butonu çizip eylemini aynı tıklama alanıyla kaydeder; panel kırpmasını uygular.",
 "layout":"Mevcut pencere boyutundan harita, grafik ve sağ panel dikdörtgenlerini hesaplar.",
 "begin_recording":"İlk çalıştırmada başlangıç sahnesini yakalar ve tek sonuç oturumunu modele bağlar.",
 "close_recording":"Sonuç dosyalarını kapatıp aktif exporter bağlantısını kaldırır.",
 "prompt":"Dosya, isim veya tohum girişi için deneyi duraklatır ve yazı kutusunu hazırlar.",
 "submit":"Yazı kutusunu amacına göre doğrular; kaydetme, yükleme, tohum veya isim işlemini yapar.",
 "main":"Komut seçeneklerini/başlangıç nesnelerini kurup programın ana akışını başlatır.",
 "selected":"Seçili kimliği güncel nesneye çözer; eski liste indeksine güvenmez.",
 "snapshot":"Mevcut düzeni canlı geçmişten ayrılmış başlangıç sahnesi olarak kodlar.",
 "_event":"Model olayını açık sonuç oturumuna aktarır; exporter yoksa dosyaya yazmaz.",
 "start_recording":"Exporter'ı modele bağlar ve kayıttan önce oluşmuş ilk durum olaylarını aktarır.",
 "time":"Tam adım sayısını adım süresiyle çarparak simülasyon saniyesini sunar.",
 "alert_count":"Şu anda alarmdaki sensörlerin sayısını verir.",
 "log_lines":"Sınırlı olay kayıtlarından okunur kısa satırlar üretir.",
 "get_sensor_status":"Kimlik için tek ortak durumu döndürür; tanınmayan cihaz ilk ölçümü bekler.",
 "get_limiter_info":"Kalan ve maksimum tekrar bildirim hakkını panel için biçimler.",
 "log_sensor":"Örneğin kanal değerlerini, geçerliliğini, konumunu ve eşiklerini CSV'ye yazar.",
 "log_event":"Bir geçiş/durum olayını CSV'ye yazar ve tamponu boşaltır.",
 "log_change":"Kullanıcı müdahalesini zamanı ve sahne düzeniyle JSONL satırı olarak kaydeder.",
 "flush":"Açık dosyaların Python tamponunu işletim sistemine iletir; tek başına fiziksel disk garantisi değildir.",
 "close":"Kaynakları tekrar çağrılmaya dayanıklı biçimde kapatır ve çıktı konumunu döndürür.",
 "__enter__":"with bloğunun kullanacağı nesneyi döndürür.",
 "__exit__":"with bloğundan normal veya hatalı çıkışta kaynakları kapatır.",
 "__init__":"Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.",
 "__call__":"Nesnenin fonksiyon gibi çağrılmasını alttaki davranışa yönlendirir.",
 "__repr__":"Nesne durumunu hata ayıklamaya uygun metin olarak sunar.",
 "Clog":"Mesajı terminale yazar.",
 "Mlog":"Mesajı sınırlı bellek geçmişine ekler; en eskiyi gerekirse çıkarır.",
 "get_records":"Kayıt listesinin kopyasını döndürür; dışarıdan doğrudan değiştirmeyi önler.",
 "remaining":"Kalan işlem hakkını okur veya tür/negatiflik kontrolüyle günceller.",
 "allow":"Pencereyi yeniler; hak varsa bir azaltıp True, yoksa False verir.",
 "raw":"Ham sensör değerini okur/yazar; temel sınıfta tür ve değer aralığı denetlenir.",
 "name":"Sensör adını okur veya doğrulayarak/proxy aracılığıyla değiştirir.",
 "kind":"Sensör türünü enum üzerinden okur veya doğrular.",
 "offset":"Kalibrasyon sapmasını okur; yazımda sayısal tür ve izin verilen aralık denetlenir.",
 "value":"Ham değer ile sabit kalibrasyon sapmasını toplayarak işlenmiş ölçümü verir.",
 "notify":"Olayı kullanıcıya sunulacak terminal çıktısına dönüştürür.",
 "events":"Saklanan olay sözlüklerinin listesini kopyalayarak sunar.",
 "save":"Olay türünü doğrular ve sınırlı belleğe sözlük olarak kaydeder.",
 "tick":"Bağımsız CALCULATOR örneğinde sensörleri kota ve tek genel eşikle değerlendirir; güncel uygulama bu yolu kullanmaz.",
 "_emit":"Kararlaştırılmış olayı kayda/bildirime aktarır; bulunduğu modülün olay sözleşmesini uygular.",
 "sensor":"Hazır deneylerde benzer sensör nesnelerini okunur parametrelerle kuran yerel yardımcıdır.",
 "point":"Grafik zamanı ve değerini çizim dikdörtgeninin piksel koordinatına çevirir.",
 "build_overlay":"Yalnız görünür alanda teorik kanal değerini örnekleyip renkli yüzey üretir.",
 "text":"Panelin sıradaki metnini sararak çizer ve dikey yerleşim imlecini ilerletir.",
 "heading":"Panel bölüm başlığını çizer ve sonraki satırın konumunu ayarlar.",
 "numeric":"Sayısal değer, azalt/artır eylemleri ve kısa açıklamasını ortak yerleşimle üretir.",
 "setUp":"Her test için bağımsız geçici çıktı alanı ve uygulama örneği hazırlar.",
 "tearDown":"Test kaynaklarını kapatır; geçici sonuç alanını temizler.",
 "click":"Kimlikli butonu görünür hale getirip gerçek olay işleyicisine tıklama yollar.",
 "mapclick":"Dünya koordinatını piksele çevirip harita fare olayını üretir.",
 "key":"Gerçek olay işleyicisine kontrollü tuş olayı yollar.",
 "make":"Alarm testi için tek kanal ve ölçüm değerine sahip bağımsız sensör kurar.",
 "sim":"Drone testleri için hazır hareketli ölçüm sahnesinden yeni simülasyon kurar.",
}


def source_files():
    """Çalışma verilerini hariç tut; gizli eski yedek Python'u kapsa."""
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and not any(part in EXCLUDE for part in p.relative_to(ROOT).parts)
                  and p.suffix not in (".pyc",".pyo"))


def role(path):
    rel=path.relative_to(ROOT).as_posix()
    if rel in ROLES:
        return ROLES[rel]
    if rel.startswith("IoT PyGame/"):
        return ("Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir."
                if path.suffix==".png" else "Korunan eski tek dosyalı simülasyon/yedek. Yeni giriş noktası bu kodu çalıştırmaz; güncel davranış testleri buna uygulanmaz.")
    if path.suffix==".png":
        return f"{path.stem} nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır."
    return "Proje yardımcı/belgeleme dosyası; içerik ve bağlı kullanım kaynak dosyasında görülebilir."


def symbols(node, parents=()):
    """İç işlevleri ve property getter/setterlarını ayrı kaynak konumuyla dolaş."""
    for child in ast.iter_child_nodes(node):
        if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            qualified=".".join((*parents,child.name))
            yield qualified,child
            yield from symbols(child,(*parents,child.name))
        else:
            yield from symbols(child,parents)


def local_nodes(node):
    """Bir işlevin kendi gövdesini dolaş; iç işlevin etkilerini ona yükleme."""
    yield node
    for child in ast.iter_child_nodes(node):
        if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and child is not node:
            continue
        yield from local_nodes(child)


def short(node,limit=220):
    text=ast.unparse(node).replace("\n"," ")
    return text if len(text)<=limit else text[:limit]+"…"


def purpose(node):
    """Kaynak docstring'ini öncele; ortak yöntemlerin öğretici anlamını tamamla."""
    doc=ast.get_docstring(node)
    if doc:
        return " ".join(doc.split())
    name=node.name
    if name in PURPOSES:
        return PURPOSES[name]
    if isinstance(node,ast.ClassDef):
        if any(isinstance(d,ast.Name) and d.id=="dataclass" for d in node.decorator_list):
            return "Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır."
        return "İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir."
    if name.startswith("test_"):
        return "Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar."
    if name.startswith("set_"):
        return "Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir."
    if "toggle" in name:
        return "İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür."
    if name.startswith("draw_"):
        return "Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir."
    return "Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir."


def step_description(stmt):
    """Gövdenin üst düzey adımlarını gerçek ifadeler üzerinden açıkla."""
    if isinstance(stmt,(ast.Assign,ast.AnnAssign,ast.AugAssign)):
        return "Değeri/alanı oluştur veya güncelle: "+short(stmt)
    if isinstance(stmt,ast.If):
        return "Koşula göre yol seç: "+short(stmt.test)
    if isinstance(stmt,(ast.For,ast.AsyncFor)):
        return "Her öğe için işle: "+short(stmt.target)+" ← "+short(stmt.iter)
    if isinstance(stmt,ast.While):
        return "Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: "+short(stmt.test)
    if isinstance(stmt,ast.Return):
        return "Çağırana sonucu döndür: "+(short(stmt.value) if stmt.value else "None")
    if isinstance(stmt,ast.Raise):
        return "Geçersiz durumu hata olarak bildir: "+short(stmt.exc)
    if isinstance(stmt,ast.Try):
        return "Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle."
    if isinstance(stmt,(ast.With,ast.AsyncWith)):
        return "Kaynak yaşam süresini with bloğuyla sınırla: "+", ".join(short(i.context_expr) for i in stmt.items)
    if isinstance(stmt,(ast.FunctionDef,ast.ClassDef,ast.AsyncFunctionDef)):
        return "Yerel yardımcı tanımla: "+stmt.name+"; ayrı sembol kaydı aşağıdadır."
    if isinstance(stmt,ast.Expr) and not isinstance(stmt.value,ast.Constant):
        return "Yan etki/çağrı adımını çalıştır: "+short(stmt.value)
    if isinstance(stmt,(ast.Import,ast.ImportFrom)):
        return "Gereken isimleri içeri al: "+short(stmt)
    if isinstance(stmt,(ast.Break,ast.Continue)):
        return "Döngü akışını değiştir: "+short(stmt)
    if isinstance(stmt,ast.Assert):
        return "Beklenen sonucu doğrula: "+short(stmt.test)
    return None


def render():
    """Dosya haritası, bütün semboller ve tam kod kesitlerini deterministik üret."""
    paths=source_files()
    for future in (OUTPUT,MANIFEST):
        if future not in paths: paths.append(future)
    paths.sort()
    lines=["# Kaynakla eşleşen dosya, sınıf ve fonksiyon rehberi","",
           "[Ana öğretici rehbere dön](../PROJE_REHBERI.md). Bu ek tools/build_guide.py ile üretilir.",
           "Kaynak kesitleri gerçek dosyalardan alınır; gösterimde yalnız satır sonundaki boşluklar temizlenir. Kaynak dosyaları değiştirilmez. Üst düzey adım açıklaması sözdizimini izler; formüllerin ve kullanıcı akışlarının gerekçesi ana rehberdedir.",
           "İç işlevler de listelenir. Aynı adlı property okuma/yazma yöntemleri kaynak satırıyla ayrılır. Satır içi lambda ifadeleri içinde bulundukları kod bloğuyla kapsanır.",
           "Eski alternatif kodun açıklaması mevcut üretim akışına dahil olduğu anlamına gelmez.","","## Dosya haritası","",
           "| Dosya | Neden var, nerede kullanılır? |","|---|---|"]
    manifest={"sources":{},"symbols":[]}
    for path in paths:
        rel=path.relative_to(ROOT).as_posix()
        lines.append(f"| [{rel}](../{quote(rel)}) | {role(path)} |")
    for path in paths:
        if path.suffix!=".py" or not path.exists(): continue
        rel=path.relative_to(ROOT).as_posix()
        source=path.read_text()
        tree=ast.parse(source,filename=rel)
        manifest["sources"][rel]=hashlib.sha256(source.encode()).hexdigest()
        lines+=["",f"## {rel}","",role(path),"","### Dosya düzeyindeki kod",""]
        for stmt in tree.body:
            if isinstance(stmt,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): continue
            segment=ast.get_source_segment(source,stmt) or ""
            if not segment: continue
            lines += [f"Satır {stmt.lineno}: "+(step_description(stmt) or "Modül açıklaması / sabit tanım."),"","\u0060\u0060\u0060python",segment,"\u0060\u0060\u0060",""]
        for qualified,node in symbols(tree):
            entry={"file":rel,"name":qualified,"line":node.lineno,"end":node.end_lineno,"kind":type(node).__name__}
            manifest["symbols"].append(entry)
            lines += [f"### {qualified} — satır {node.lineno}","",purpose(node),""]
            if isinstance(node,ast.ClassDef):
                bases=", ".join(short(base) for base in node.bases) or "Doğrudan object; özel üst sınıf yok"
                lines += [f"**Sınıf ilişkisi:** {bases}. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.",""]
                body=[stmt for stmt in node.body if not isinstance(stmt,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef))]
                code="\n".join(ast.get_source_segment(source,stmt) or "" for stmt in body)
                lines+=["**Alanlar ve sınıf düzeyindeki bloklar:**","","\u0060\u0060\u0060python",code or "# Alanlar __init__ içinde atanır.","\u0060\u0060\u0060",""]
                continue
            args=ast.unparse(node.args)
            own=list(local_nodes(node))
            returns=[short(n.value) if n.value else "None" for n in own if isinstance(n,ast.Return)]
            yields=[short(n.value) if n.value else "None" for n in own if isinstance(n,(ast.Yield,ast.YieldFrom))]
            raises=[short(n.exc) for n in own if isinstance(n,ast.Raise) and n.exc]
            targets=[]
            for n in own:
                if isinstance(n,ast.Assign): targets.extend(short(t) for t in n.targets)
                elif isinstance(n,(ast.AnnAssign,ast.AugAssign)): targets.append(short(n.target))
            calls=list(dict.fromkeys(short(n.func) for n in own if isinstance(n,ast.Call)))
            lines += [f"**Girdiler:** {args or 'Parametre yok'}. self varsa üzerinde işlem yapılan örnektir.",
                      "**Çıktı:** "+("; ".join(dict.fromkeys(returns+yields)) if returns or yields else "Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur."),
                      "**Atanan yerel değerler / durum alanları:** "+(", ".join(dict.fromkeys(targets)) or "Doğrudan atama yok."),
                      "**Bağlandığı işlevler:** "+(", ".join(calls) or "Başka işlev çağrısı yok."),
                      "**Açık hata yolları:** "+("; ".join(dict.fromkeys(raises)) or "Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir."),"","**İşleyiş sırası:**",""]
            descriptions=[step_description(stmt) for stmt in node.body]
            descriptions=[d for d in descriptions if d]
            lines.extend(f"{i}. {description}" for i,description in enumerate(descriptions,1))
            if not descriptions: lines.append("Bu gövde yalnız açıklama veya boş geçiş içerir.")
            lines += ["","**Gerçek kaynak:**","","\u0060\u0060\u0060python",ast.get_source_segment(source,node),"\u0060\u0060\u0060",""]
    lines += ["","## Yenileme ve kapsam kontrolü","",
              f"Bu üretimde {len(manifest['sources'])} Python dosyası ve {len(manifest['symbols'])} sınıf/fonksiyon konumu kapsanır.",
              "Kaynak değişince python -B tools/build_guide.py çalıştır; ardından --check ile aynı kaynak kesitlerinin ve hashlerin korunduğunu doğrula.",""]
    return "\n".join(line.rstrip() for line in "\n".join(lines).splitlines()).rstrip()+"\n",json.dumps(manifest,ensure_ascii=False,indent=2)+"\n"


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    args=parser.parse_args()
    content,manifest=render()
    if args.check:
        if not OUTPUT.exists() or not MANIFEST.exists() or OUTPUT.read_text()!=content or MANIFEST.read_text()!=manifest:
            raise SystemExit("Kaynak rehberi güncel değil: python -B tools/build_guide.py")
        print("Kaynak rehberi, sembol kapsamı ve hashler güncel.")
    else:
        OUTPUT.parent.mkdir(exist_ok=True)
        OUTPUT.write_text(content)
        MANIFEST.write_text(manifest)
        print(f"Üretildi: {OUTPUT}")


if __name__=="__main__":
    main()
