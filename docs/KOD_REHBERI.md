# Kaynakla eşleşen dosya, sınıf ve fonksiyon rehberi

[Ana öğretici rehbere dön](../PROJE_REHBERI.md). Bu ek tools/build_guide.py ile üretilir.
Kaynak kesitleri gerçek dosyalardan alınır; gösterimde yalnız satır sonundaki boşluklar temizlenir. Kaynak dosyaları değiştirilmez. Üst düzey adım açıklaması sözdizimini izler; formüllerin ve kullanıcı akışlarının gerekçesi ana rehberdedir.
İç işlevler de listelenir. Aynı adlı property okuma/yazma yöntemleri kaynak satırıyla ayrılır. Satır içi lambda ifadeleri içinde bulundukları kod bloğuyla kapsanır.
Eski alternatif kodun açıklaması mevcut üretim akışına dahil olduğu anlamına gelmez.

## Dosya haritası

| Dosya | Neden var, nerede kullanılır? |
|---|---|
| [.gitignore](../.gitignore) | Ortam, önbellek, kullanıcı sahneleri ve deney çıktılarının Git'e eklenmesini önler. |
| [AGENTS.md](../AGENTS.md) | Repo kapsamında ortak çalışma, yetki ve dokümantasyon talimatları. |
| [CALCULATOR.py](../CALCULATOR.py) | Bağımsız nesne yönelimli sensör/olay dersi. Güncel uygulama yalnız RateLimiter sınıfını kullanır. |
| [IoT PyGame/iot_sim/.main_yedek.py](../IoT%20PyGame/iot_sim/.main_yedek.py) | Korunan eski tek dosyalı simülasyon/yedek. Yeni giriş noktası bu kodu çalıştırmaz; güncel davranış testleri buna uygulanmaz. |
| [IoT PyGame/iot_sim/assets/burned.png](../IoT%20PyGame/iot_sim/assets/burned.png) | Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir. |
| [IoT PyGame/iot_sim/assets/drone.png](../IoT%20PyGame/iot_sim/assets/drone.png) | Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir. |
| [IoT PyGame/iot_sim/assets/obstacle.png](../IoT%20PyGame/iot_sim/assets/obstacle.png) | Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir. |
| [IoT PyGame/iot_sim/assets/sensor.png](../IoT%20PyGame/iot_sim/assets/sensor.png) | Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir. |
| [IoT PyGame/iot_sim/assets/source_gas.png](../IoT%20PyGame/iot_sim/assets/source_gas.png) | Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir. |
| [IoT PyGame/iot_sim/assets/source_temp.png](../IoT%20PyGame/iot_sim/assets/source_temp.png) | Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir. |
| [IoT PyGame/iot_sim/main.py](../IoT%20PyGame/iot_sim/main.py) | Korunan eski tek dosyalı simülasyon/yedek. Yeni giriş noktası bu kodu çalıştırmaz; güncel davranış testleri buna uygulanmaz. |
| [LICENSE](../LICENSE) | Projenin MIT lisans koşulları; uygulama davranışı üretmez. |
| [PROJE_REHBERI.md](../PROJE_REHBERI.md) | Kavram, mimari, formül ve kullanıcı senaryolarını adım adım öğreten ana rehber. |
| [README.md](../README.md) | Kurulum, giriş komutları ve ayrıntılı rehberlere ulaşım. |
| [UYGULAMA_PLANI.md](../UYGULAMA_PLANI.md) | İnceleme kanıtı, kullanıcı kararları, onaylı kapsam ve teslim kaydı. |
| [assets/burned.png](../assets/burned.png) | burned nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır. |
| [assets/drone.png](../assets/drone.png) | drone nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır. |
| [assets/obstacle.png](../assets/obstacle.png) | obstacle nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır. |
| [assets/sensor.png](../assets/sensor.png) | sensor nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır. |
| [assets/source_gas.png](../assets/source_gas.png) | source_gas nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır. |
| [assets/source_temp.png](../assets/source_temp.png) | source_temp nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır. |
| [docs/DOGRULAMA.md](../docs/DOGRULAMA.md) | Gerçekten yürütülen kontroller ve doğrulanmayan platform/davranış sınırları. |
| [docs/KOD_REHBERI.md](../docs/KOD_REHBERI.md) | Bu üretilen ayrıntılı kaynak eki; kaynak değişince üreticiyle yenilenir. |
| [docs/kod_kapsami.json](../docs/kod_kapsami.json) | Python kaynak hashleri ve sembol konumları; --check ile eşleşme doğrulanır. |
| [docs/runtime.json](../docs/runtime.json) | Son kontrollü X11 deney çalıştırmasının ham ölçüm raporu. |
| [docs/screenshots/deney-atolyesi.png](../docs/screenshots/deney-atolyesi.png) | Gerçek uygulama çiziminden alınmış belgeleme ekranı; README kullanır. |
| [iot_sim/IoT.py](../iot_sim/IoT.py) | Bazı model/motor/ölçüm adlarını yeniden sunan korunmuş uyumluluk modülüdür. |
| [iot_sim/__init__.py](../iot_sim/__init__.py) | Paketin dışarı sunduğu isimleri tanımlar; pencere açmaz. |
| [iot_sim/alarm_bridge.py](../iot_sim/alarm_bridge.py) | Tek kanal alarm kararı, durum geçişleri ve tekrarlı bildirim kotasını birleştirir. |
| [iot_sim/app.py](../iot_sim/app.py) | Pygame yaşam döngüsü, pencere, buton eylemleri, klavye/fare ve dosya girişidir. |
| [iot_sim/assets.py](../iot_sim/assets.py) | İkonları yükler; eksik görselde None ile şekil çizimine geri dönüş sağlar. |
| [iot_sim/camera.py](../iot_sim/camera.py) | Ekran ve dünya koordinatları arasındaki dönüşüm ve zoom durumudur. |
| [iot_sim/cargo.py](../iot_sim/cargo.py) | Drone yükleme kapasitesi ve karşılıklı taşıyıcı referanslarını yönetir. |
| [iot_sim/constants.py](../iot_sim/constants.py) | Korunmuş sabitler. Yeni ekran boyutu App.layout, zaman adımı Simulation.STEP içindedir. |
| [iot_sim/engine.py](../iot_sim/engine.py) | Kimlik/konum arama, sınırlandırma ve rota için karo geometrisi sağlar. Eski doğruluk yardımcısı korunmuştur. |
| [iot_sim/exporter.py](../iot_sim/exporter.py) | Her deney için yeni klasör ve dosyalar oluşturur; ölçüm/olay/değişiklikleri yazar. |
| [iot_sim/fire.py](../iot_sim/fire.py) | Yanabilirlik, eşik sıcaklık ve süreye göre ağaçları kaynak yapar. |
| [iot_sim/geom.py](../iot_sim/geom.py) | Korunan çokgen sıralama ve alan yardımcıları; yeni noktadan ölçüm akışına bağlı değildir. |
| [iot_sim/graphs.py](../iot_sim/graphs.py) | Sensör geçmişini kanal/birim bazında ölçüm, teori, eşik ve pil grafiğine dönüştürür. |
| [iot_sim/lessons.py](../iot_sim/lessons.py) | Altı Türkçe deneyin yönergeleri ve taze başlangıç sahnelerini üretir. |
| [iot_sim/models.py](../iot_sim/models.py) | Nesne ve kanal türleri ile bütün bileşenlerin paylaştığı durum alanlarını tanımlar. |
| [iot_sim/operations.py](../iot_sim/operations.py) | Arayüzün ekleme, taşıma, silme, yük ve rota eylemlerine ortak giriş sağlar. |
| [iot_sim/panel.py](../iot_sim/panel.py) | Nesne, deney ve olay sekmelerini kaydırılabilir içerikle oluşturur. |
| [iot_sim/render.py](../iot_sim/render.py) | Harita, kaynak yarıçapı, teorik katman, nesne ve rota çizimidir. |
| [iot_sim/scene.py](../iot_sim/scene.py) | Başlangıç sahnesinin sürümlü JSON biçimi, doğrulaması ve atomik yazımıdır. |
| [iot_sim/sensors.py](../iot_sim/sensors.py) | Teorik ortam, noktasal cihaz ölçümü, sapma ve enerji tüketimini hesaplar. |
| [iot_sim/simulation.py](../iot_sim/simulation.py) | Ekrandan bağımsız deney saati, güncelleme sırası, RNG ve sınırlı geçmişin sahibidir. |
| [iot_sim/uav.py](../iot_sim/uav.py) | LOOP/PINGPONG hareketini, engelde durmayı ve yük eşitlemesini uygular. |
| [iot_sim/ui_widgets.py](../iot_sim/ui_widgets.py) | Satır sarma, metin ve buton çizimi için ortak bileşenlerdir. |
| [iot_sim/viz.py](../iot_sim/viz.py) | Yüzeyler için bellekle sınırlı LRU önbelleği ve görsel yardımcı içerir. |
| [main.py](../main.py) | Güncel komut satırı girişidir; iot_sim.app.main işlevine aktarır. |
| [requirements.txt](../requirements.txt) | Pygame sürümünü sabitler; pip tarafından temiz ortam kurulumunda okunur. |
| [tests/test_simulation.py](../tests/test_simulation.py) | Model, alarm, enerji, rota, yük, sahne, kayıt ve deterministik zaman regresyonları. |
| [tests/test_ui.py](../tests/test_ui.py) | Pygame çizimi ve gerçek olay işleyicisini kontrollü girişlerle sınar. |
| [tools/build_guide.py](../tools/build_guide.py) | Bu ekin envanterini, kod kesitlerini ve kaynak hash manifestini üretir/kontrol eder. |
| [tools/verify_runtime.py](../tools/verify_runtime.py) | Altı sahne ekranı, X11/SDL sürücü bilgisi ve eğitim ölçeğinde performans üretir. |

## CALCULATOR.py

Bağımsız nesne yönelimli sensör/olay dersi. Güncel uygulama yalnız RateLimiter sınıfını kullanır.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: import datetime

```python
import datetime
```

Satır 2: Gereken isimleri içeri al: import time

```python
import time
```

Satır 3: Gereken isimleri içeri al: from enum import Enum

```python
from enum import Enum
```

Satır 285: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__ == "__main__":
    # --- Bileşenler ---
    logger = Logger()
    storage = InMemoryStage()
    notifier = ConsoleNotifier()

    # Rate limiter: her pencere içinde en fazla N sensör işlenir
    limiter = RateLimiter(4)
    limiter.window_seconds = 10  # demo için kısa pencere normalde 60

    # --- Sensörler ---
    # kind: SensorKind.GAS / SensorKind.TEMP
    s1 = Sensor(raw=15, name="MX1", kind=SensorKind.GAS)
    s2 = Sensor(raw=25, name="MX2", kind=SensorKind.GAS)
    s3 = Sensor(raw=95, name="TM3", kind=SensorKind.TEMP)  # ALERT beklenir
    s4 = Sensor(raw=40, name="TM4", kind=SensorKind.TEMP)
    time.sleep(5)
    # Kalibrasyon (offset ile value değişir)
    cs1 = CalibratedSensor(s1, offset=5)
    cs2 = CalibratedSensor(s2, offset=-5)
    cs3 = CalibratedSensor(s3, offset=0)
    cs4 = CalibratedSensor(s4, offset=15)

    engine = EventEngine(
        Csensors=[cs1, cs2, cs3, cs4],
        logger=logger,
        storage=storage,
        notifier=notifier,
        limiter=limiter
    )

    # --- Demo akışı ---
    print("\n=== TICK #1 ===")
    engine.tick()

    # İkinci tick'te bir sensörü ALERT'e sür: raw yükselt
    # (CalibratedSensor proxy setter'ları varsa cs1.raw = 90 da olur)
    s1.raw = 90

    print("\n=== TICK #2 ===")
    engine.tick()

    # --- Son durum özetleri ---
    print("\n=== STORAGE (son 10 event) ===")
    for e in storage.events[-10:]:
        # events dict olarak saklanıyorsa:
        print(e)

    print("\n=== MEMORY LOG (son 20) ===")
    for line in logger.get_records()[-20:]:
        print(line)
```

### Logger — satır 5

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Logger.__init__ — satır 7

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._records
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self._records = []

**Gerçek kaynak:**

```python
def __init__(self):
        self._records = []
```

### Logger.Clog — satır 10

Mesajı terminale yazar.

**Girdiler:** self, msg: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** print
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: print(f'{msg}')

**Gerçek kaynak:**

```python
def Clog(self, msg: str) -> None: # Mesajı ekrana basan fonksiyon
        print(f"{msg}")
```

### Logger.Mlog — satır 13

Mesajı sınırlı bellek geçmişine ekler; en eskiyi gerekirse çıkarır.

**Girdiler:** self, msg: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._records
**Bağlandığı işlevler:** len, self._records.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: len(self._records) >= 100
2. Yan etki/çağrı adımını çalıştır: self._records.append(msg)

**Gerçek kaynak:**

```python
def Mlog(self, msg: str) -> None: # Mesajı kayıtlara yazan fonksiyon
        if len(self._records) >= 100:
            self._records = self._records[1:] # 101 adet kayıt sonrasında eski kayıtlar silinir
        self._records.append(msg)
```

### Logger.get_records — satır 18

Kayıt listesinin kopyasını döndürür; dışarıdan doğrudan değiştirmeyi önler.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** list(self._records)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** list
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: list(self._records)

**Gerçek kaynak:**

```python
def get_records(self) -> list: # Kayıtları döndüren fonksiyon
        return list(self._records)
```

### RateLimiter — satır 22

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### RateLimiter.__init__ — satır 24

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, n: int, clock=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.max_remaining, self.remaining, self.window_seconds, self._clock, self.setTime, self.delta
**Bağlandığı işlevler:** isinstance, TypeError, self._clock
**Açık hata yolları:** TypeError('İşlem hakkı için yanlış veri tipi girildi')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(n, int)
2. Değeri/alanı oluştur veya güncelle: self.max_remaining = n
3. Değeri/alanı oluştur veya güncelle: self.remaining = n
4. Değeri/alanı oluştur veya güncelle: self.window_seconds = 60
5. Değeri/alanı oluştur veya güncelle: self._clock = clock or time.monotonic
6. Değeri/alanı oluştur veya güncelle: self.setTime = self._clock()
7. Değeri/alanı oluştur veya güncelle: self.delta = 0

**Gerçek kaynak:**

```python
def __init__(self, n: int, clock=None):

        if not isinstance(n, int):
            raise TypeError("İşlem hakkı için yanlış veri tipi girildi")

        self.max_remaining = n # İşlem hakkı sayısının sıfırlanacağı sabit değeri tutan değişken
        self.remaining = n # İşlem hakkı sayısının tutulacağı değişken
        self.window_seconds = 60 # İşlem hakkı sayısının sıfırlanması için geçmesi gereken süreyi tutan değişken
        self._clock = clock or time.monotonic
        self.setTime = self._clock()
        self.delta = 0
```

### RateLimiter.remaining — satır 37

Kalan işlem hakkını okur veya tür/negatiflik kontrolüyle günceller.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self._remaining
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self._remaining

**Gerçek kaynak:**

```python
def remaining(self) -> int: # Gizli işlem hakkı sayısını döndüren fonksiyon protokolü
        return self._remaining
```

### RateLimiter.remaining — satır 41

Kalan işlem hakkını okur veya tür/negatiflik kontrolüyle günceller.

**Girdiler:** self, n: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._remaining
**Bağlandığı işlevler:** isinstance, TypeError, ValueError
**Açık hata yolları:** TypeError('İşlem hakkı için yanlış veri tipi girildi'); ValueError('İşlem hakkı negatif olamaz')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(n, int)
2. Koşula göre yol seç: n < 0
3. Değeri/alanı oluştur veya güncelle: self._remaining = n

**Gerçek kaynak:**

```python
def remaining(self, n: int) -> None: # Gizli işlem hakkı sayısını ayarlayan fonksiyon protokolü
        if not isinstance(n, int):
            raise TypeError("İşlem hakkı için yanlış veri tipi girildi")
        if n < 0:
            raise ValueError("İşlem hakkı negatif olamaz")
        self._remaining = n
```

### RateLimiter.allow — satır 48

Pencereyi yeniler; hak varsa bir azaltıp True, yoksa False verir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; True
**Atanan yerel değerler / durum alanları:** self.remaining
**Bağlandığı işlevler:** self.refresh
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.refresh()
2. Koşula göre yol seç: self.remaining <= 0
3. Değeri/alanı oluştur veya güncelle: self.remaining -= 1
4. Çağırana sonucu döndür: True

**Gerçek kaynak:**

```python
def allow(self) -> bool: # İşlem hakkı var mı yok mu test eder
        self.refresh()
        if self.remaining <= 0:
            return False
        self.remaining -= 1
        return True
```

### RateLimiter.refresh — satır 55

Hak tüketmeden, verilen saatle pencereyi yenile.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** current, self.delta, self.remaining, self.setTime
**Bağlandığı işlevler:** self._clock
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: current = self._clock()
2. Değeri/alanı oluştur veya güncelle: self.delta = current - self.setTime
3. Koşula göre yol seç: self.delta >= self.window_seconds

**Gerçek kaynak:**

```python
def refresh(self) -> None:
        """Hak tüketmeden, verilen saatle pencereyi yenile."""
        current = self._clock()
        self.delta = current - self.setTime
        if self.delta >= self.window_seconds:
            self.remaining = self.max_remaining
            self.setTime = current
            self.delta = 0.0
```

### RateLimiter.__call__ — satır 64

Nesnenin fonksiyon gibi çağrılmasını alttaki davranışa yönlendirir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.allow()
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self.allow
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self.allow()

**Gerçek kaynak:**

```python
def __call__(self) -> bool: # Nesne çağrılırsa yapılacak fonksiyonu işaret eder
        return self.allow()
```

### EventType — satır 68

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
CALM = "CALM"
ALERT = "ALERT"
```

### SensorKind — satır 73

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
GAS = "GAS"
TEMP = "TEMP"
```

### Event — satır 78

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Event.__init__ — satır 80

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, Etype: EventType, Ekind: SensorKind, Evalue: float, detecter: str, Ets: datetime.datetime. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.Etype, self.Ekind, self.Evalue, self.Ets, self.detected_from
**Bağlandığı işlevler:** isinstance, TypeError
**Açık hata yolları:** TypeError('Hatalı olay tipi girildi'); TypeError('Hatalı sensör tipi girildi')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(Etype, EventType)
2. Koşula göre yol seç: not isinstance(Ekind, SensorKind)
3. Değeri/alanı oluştur veya güncelle: self.Etype = Etype
4. Değeri/alanı oluştur veya güncelle: self.Ekind = Ekind
5. Değeri/alanı oluştur veya güncelle: self.Evalue = Evalue
6. Değeri/alanı oluştur veya güncelle: self.Ets = Ets
7. Değeri/alanı oluştur veya güncelle: self.detected_from = detecter

**Gerçek kaynak:**

```python
def __init__(self, Etype: EventType, Ekind: SensorKind, Evalue: float, detecter: str, Ets: datetime.datetime):
        if not isinstance(Etype, EventType):
            raise TypeError("Hatalı olay tipi girildi")
        if not isinstance(Ekind, SensorKind):
            raise TypeError("Hatalı sensör tipi girildi")

        self.Etype = Etype # Alarmın varlığını belirleyen değişken
        self.Ekind = Ekind # Alarmın türünü belirleyen değişken
        self.Evalue = Evalue # Alarmın ölçüm değerini tutan değişken
        self.Ets = Ets # Ölçülen değerin hangi tarihte ölçüldüğünü tutan değişken
        self.detected_from = detecter
```

### Sensor — satır 93

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Sensor.__init__ — satır 95

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, raw: float, name: str, kind: SensorKind, min_deger=0, max_deger=100. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.kind, self._min_deger, self._max_deger, self.name, self.raw
**Bağlandığı işlevler:** isinstance, TypeError
**Açık hata yolları:** TypeError('Hatalı alarm ismi girildi')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(kind, SensorKind)
2. Değeri/alanı oluştur veya güncelle: self.kind = kind
3. Değeri/alanı oluştur veya güncelle: self._min_deger = min_deger
4. Değeri/alanı oluştur veya güncelle: self._max_deger = max_deger
5. Değeri/alanı oluştur veya güncelle: self.name = name
6. Değeri/alanı oluştur veya güncelle: self.raw = raw

**Gerçek kaynak:**

```python
def __init__(self, raw: float, name: str, kind: SensorKind, min_deger = 0,max_deger = 100):
        # temp için 0-100, gas için 0-100 o yüzden direkt değerler girildi.
        # Farklı olmaları durumunda sensör tanımlama kısmında değerler verilebilir.
        if not isinstance(kind, SensorKind):
            raise TypeError("Hatalı alarm ismi girildi")
        self.kind = kind
        self._min_deger = min_deger
        self._max_deger = max_deger
        self.name = name # Sensörün adını (kodunu) tutan değişken
        self.raw = raw
```

### Sensor.raw — satır 108

Ham sensör değerini okur/yazar; temel sınıfta tür ve değer aralığı denetlenir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self._raw
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self._raw

**Gerçek kaynak:**

```python
def raw(self) -> float: # Gizli ham değeri döndüren fonksiyon
        return self._raw
```

### Sensor.raw — satır 112

Ham sensör değerini okur/yazar; temel sınıfta tür ve değer aralığı denetlenir.

**Girdiler:** self, x: float. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._raw
**Bağlandığı işlevler:** isinstance, TypeError, ValueError, float
**Açık hata yolları:** TypeError('Hatalı ham değer tipi girildi'); ValueError('Ölçülen ham değer için hatalı değer girildi')

**İşleyiş sırası:**

1. Koşula göre yol seç: not (isinstance(x, float) or isinstance(x, int))
2. Koşula göre yol seç: not self._min_deger <= x <= self._max_deger
3. Değeri/alanı oluştur veya güncelle: self._raw = float(x)

**Gerçek kaynak:**

```python
def raw(self, x: float) -> None:
        if not (isinstance(x, float) or isinstance(x, int)):
            raise TypeError("Hatalı ham değer tipi girildi")
        if not self._min_deger <= x <= self._max_deger:
            raise ValueError("Ölçülen ham değer için hatalı değer girildi")
        self._raw = float(x)
```

### Sensor.name — satır 120

Sensör adını okur veya doğrulayarak/proxy aracılığıyla değiştirir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self._name
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self._name

**Gerçek kaynak:**

```python
def name(self) -> str:
        return self._name
```

### Sensor.name — satır 124

Sensör adını okur veya doğrulayarak/proxy aracılığıyla değiştirir.

**Girdiler:** self, name: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._name
**Bağlandığı işlevler:** isinstance, TypeError
**Açık hata yolları:** TypeError('İsim str olmalı')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(name, str)
2. Değeri/alanı oluştur veya güncelle: self._name = name

**Gerçek kaynak:**

```python
def name(self, name: str) -> None: # Gizli sensör ismini ayarlayan fonksiyon protokolü
        if not isinstance(name,str):
            raise TypeError("İsim str olmalı")
        self._name = name
```

### Sensor.kind — satır 130

Sensör türünü enum üzerinden okur veya doğrular.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self._kind
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self._kind

**Gerçek kaynak:**

```python
def kind(self) -> SensorKind:
        return self._kind
```

### Sensor.kind — satır 134

Sensör türünü enum üzerinden okur veya doğrular.

**Girdiler:** self, kind. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._kind
**Bağlandığı işlevler:** isinstance, TypeError
**Açık hata yolları:** TypeError('Tür tanımsız')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(kind, SensorKind)
2. Değeri/alanı oluştur veya güncelle: self._kind = kind

**Gerçek kaynak:**

```python
def kind(self,kind) -> None:
        if not isinstance(kind, SensorKind):
            raise TypeError("Tür tanımsız")
        self._kind = kind
```

### Sensor.__repr__ — satır 139

Nesne durumunu hata ayıklamaya uygun metin olarak sunar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** f'Sensör adı : {self._name}, ölçülen son ham değeri : {self._raw}, min-max aralığı : {self._min_deger}-{self._max_deger}'
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: f'Sensör adı : {self._name}, ölçülen son ham değeri : {self._raw}, min-max aralığı : {self._min_deger}-{self._max_deger}'

**Gerçek kaynak:**

```python
def __repr__(self) -> str: # Sensör tanımı
        return f"Sensör adı : {self._name}, ölçülen son ham değeri : {self._raw}, min-max aralığı : {self._min_deger}-{self._max_deger}"
```

### CalibratedSensor — satır 143

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Sensor. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### CalibratedSensor.__init__ — satır 145

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, sensor: Sensor, offset: float, min_deger=-20, max_deger=20. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._max_deger, self._min_deger, self.sensor, self.offset
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self._max_deger = max_deger
2. Değeri/alanı oluştur veya güncelle: self._min_deger = min_deger
3. Değeri/alanı oluştur veya güncelle: self.sensor = sensor
4. Değeri/alanı oluştur veya güncelle: self.offset = offset

**Gerçek kaynak:**

```python
def __init__(self, sensor: Sensor, offset: float, min_deger = -20, max_deger = 20):
        self._max_deger = max_deger
        self._min_deger = min_deger
        self.sensor = sensor # Kalibre edilecek sensörü tutan değişken
        self.offset = offset
```

### CalibratedSensor.name — satır 152

Sensör adını okur veya doğrulayarak/proxy aracılığıyla değiştirir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.sensor.name
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self.sensor.name

**Gerçek kaynak:**

```python
def name(self) -> str: # Gizli sensör ismini döndüren fonksiyon protokolü
        return self.sensor.name
```

### CalibratedSensor.name — satır 156

Sensör adını okur veya doğrulayarak/proxy aracılığıyla değiştirir.

**Girdiler:** self, name: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.sensor.name
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.sensor.name = name

**Gerçek kaynak:**

```python
def name(self, name: str) -> None: # Gizli sensör ismini ayarlayan fonksiyon protokolü
        self.sensor.name = name
```

### CalibratedSensor.raw — satır 160

Ham sensör değerini okur/yazar; temel sınıfta tür ve değer aralığı denetlenir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.sensor.raw
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self.sensor.raw

**Gerçek kaynak:**

```python
def raw(self) -> float: # Gizli ham veriyi döndüren fonksiyon protokolü
        return self.sensor.raw
```

### CalibratedSensor.raw — satır 164

Ham sensör değerini okur/yazar; temel sınıfta tür ve değer aralığı denetlenir.

**Girdiler:** self, x: float. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.sensor.raw
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.sensor.raw = x

**Gerçek kaynak:**

```python
def raw(self, x: float) -> None: # Gizli ham veriyi ayarlayan fonksiyon protokolü
        self.sensor.raw = x
```

### CalibratedSensor.offset — satır 168

Kalibrasyon sapmasını okur; yazımda sayısal tür ve izin verilen aralık denetlenir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self._offset
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self._offset

**Gerçek kaynak:**

```python
def offset(self) -> float: # Gizli sapma değerini döndüren fonksiyon protokolü
        return self._offset
```

### CalibratedSensor.offset — satır 172

Kalibrasyon sapmasını okur; yazımda sayısal tür ve izin verilen aralık denetlenir.

**Girdiler:** self, x: float. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._offset
**Bağlandığı işlevler:** isinstance, TypeError, ValueError
**Açık hata yolları:** TypeError('Offset sayısal olmalı'); ValueError('Hatalı sapma değeri girildi')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(x, (int, float))
2. Koşula göre yol seç: not self._min_deger <= x <= self._max_deger
3. Değeri/alanı oluştur veya güncelle: self._offset = x

**Gerçek kaynak:**

```python
def offset(self, x: float) -> None: # Gizli sapma değerini ayarlayan fonksiyon protokolü
        if not isinstance(x, (int, float)):
            raise TypeError("Offset sayısal olmalı")
        if not self._min_deger <= x <= self._max_deger:
            raise ValueError("Hatalı sapma değeri girildi")
        self._offset = x
```

### CalibratedSensor.value — satır 180

Ham değer ile sabit kalibrasyon sapmasını toplayarak işlenmiş ölçümü verir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.raw + self.offset
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self.raw + self.offset

**Gerçek kaynak:**

```python
def value(self) -> float: # Gizli işlenmiş değeri hesaplayıp döndüren fonksiyon protokolü
        return self.raw + self.offset
```

### CalibratedSensor.kind — satır 184

Sensör türünü enum üzerinden okur veya doğrular.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.sensor.kind
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self.sensor.kind

**Gerçek kaynak:**

```python
def kind(self) -> SensorKind:
        return self.sensor.kind
```

### CalibratedSensor.__repr__ — satır 187

Nesne durumunu hata ayıklamaya uygun metin olarak sunar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** f'Sensör adı : {self.name}, ölçülen son işlenmiş değeri : {self.value}, offset : {self.offset}, raw : {self.raw}, offset_aralığı : {self._min_deger}-{self._max_deger}'
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: f'Sensör adı : {self.name}, ölçülen son işlenmiş değeri : {self.value}, offset : {self.offset}, raw : {self.raw}, offset_aralığı : {self._min_deger}-{self._max_deger}'

**Gerçek kaynak:**

```python
def __repr__(self) -> str:
        return (f"Sensör adı : {self.name}, ölçülen son işlenmiş değeri : {self.value}, "f"offset : {self.offset}, raw : {self.raw}, offset_aralığı : {self._min_deger}-{self._max_deger}")
```

### ConsoleNotifier — satır 192

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### ConsoleNotifier.notify — satır 194

Olayı kullanıcıya sunulacak terminal çıktısına dönüştürür.

**Girdiler:** self, event: Event. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Etype, Ekind, Sname, Evalue, Etimestamp
**Bağlandığı işlevler:** print
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: Etype = event.Etype.value
2. Değeri/alanı oluştur veya güncelle: Ekind = event.Ekind.value
3. Değeri/alanı oluştur veya güncelle: Sname = event.detected_from
4. Değeri/alanı oluştur veya güncelle: Evalue = event.Evalue
5. Değeri/alanı oluştur veya güncelle: Etimestamp = event.Ets
6. Yan etki/çağrı adımını çalıştır: print(f'DİKKAT ! {Etype} tipli {Ekind} olayı {Sname} kodlu sensör tarafından ölçüldü. {Etimestamp} tarihli ölçülen veri: {Evalue}')

**Gerçek kaynak:**

```python
def notify(self, event: Event) -> None: # Alarm durumunu detaylarıyla ekrana bastırır
        Etype = event.Etype.value # Alert durumu
        Ekind = event.Ekind.value # Sensör tipini tutar
        Sname = event.detected_from # Sensör adını tutar
        Evalue = event.Evalue # Sensörün işlenmiş değeri
        Etimestamp = event.Ets # Sensörün ölçüm tarihi

        print(f"DİKKAT ! {Etype} tipli {Ekind} olayı {Sname} kodlu sensör tarafından ölçüldü. {Etimestamp} tarihli ölçülen veri: {Evalue}")
```

### InMemoryStage — satır 204

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### InMemoryStage.__init__ — satır 205

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._events
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self._events = []

**Gerçek kaynak:**

```python
def __init__(self):
        self._events = []
```

### InMemoryStage.events — satır 209

Saklanan olay sözlüklerinin listesini kopyalayarak sunar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** list(self._events)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** list
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: list(self._events)

**Gerçek kaynak:**

```python
def events(self) -> list: # Gizli depolama birimini döndüren fonksiyon protokolü
        return list(self._events)
```

### InMemoryStage.save — satır 212

Olay türünü doğrular ve sınırlı belleğe sözlük olarak kaydeder.

**Girdiler:** self, event: Event. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self._events, eventD
**Bağlandığı işlevler:** isinstance, TypeError, len, self._events.append
**Açık hata yolları:** TypeError('Yanlış veri tipi girildi. Depolamak için bir olay lazım')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(event, Event)
2. Koşula göre yol seç: len(self._events) >= 1000
3. Değeri/alanı oluştur veya güncelle: eventD = {'emergency': event.Etype.value, 'type': event.Ekind.value, 'detected_from': event.detected_from, 'value': event.Evalue, 'timestamp': event.Ets}
4. Yan etki/çağrı adımını çalıştır: self._events.append(eventD)

**Gerçek kaynak:**

```python
def save(self, event: Event) -> None: # Olayları depolayan fonksiyon
        if not isinstance(event, Event):
            raise TypeError("Yanlış veri tipi girildi. Depolamak için bir olay lazım")

        if len(self._events) >= 1000:
            self._events = self._events[1:] # 1001 adet olay kaydı sonrası eski kayıtlar silinir

        eventD = {
        "emergency" : event.Etype.value,
        "type" : event.Ekind.value,
        "detected_from": event.detected_from,
        "value": event.Evalue,
        "timestamp": event.Ets
        }

        self._events.append(eventD)
```

### EventEngine — satır 230

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### EventEngine.__init__ — satır 231

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, Csensors: list[Sensor], logger: Logger, storage: InMemoryStage, notifier: ConsoleNotifier, limiter: RateLimiter, threshold: float=80.0. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.Csensors, self.logger, self.storage, self.notifier, self.limiter, self.threshold, self._limiter_log_cooldown_s, self._last_limiter_log_ts
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.Csensors = Csensors
2. Değeri/alanı oluştur veya güncelle: self.logger = logger
3. Değeri/alanı oluştur veya güncelle: self.storage = storage
4. Değeri/alanı oluştur veya güncelle: self.notifier = notifier
5. Değeri/alanı oluştur veya güncelle: self.limiter = limiter
6. Değeri/alanı oluştur veya güncelle: self.threshold = threshold
7. Değeri/alanı oluştur veya güncelle: self._limiter_log_cooldown_s = 5
8. Değeri/alanı oluştur veya güncelle: self._last_limiter_log_ts = None

**Gerçek kaynak:**

```python
def __init__(self, Csensors: list[Sensor], logger: Logger, storage: InMemoryStage, notifier: ConsoleNotifier, limiter: RateLimiter, threshold: float = 80.0):
        self.Csensors = Csensors # Sensör listesi
        self.logger = logger # Logger nesnesi
        self.storage = storage # InMemoryStage nesnesi
        self.notifier = notifier # ConsoleNotifier nesnesi
        self.limiter = limiter # RateLimiter nesnesi
        self.threshold = threshold # Alarm eşik değeri (varsayılan 80, dışarıdan ayarlanabilir)
        self._limiter_log_cooldown_s = 5 # İşlem hakkı sayısının bitiminin tekrar etmesi için geçmesi gereken süreyi tutan değişken
        self._last_limiter_log_ts = None
```

### EventEngine._emit — satır 241

Kararlaştırılmış olayı kayda/bildirime aktarır; bulunduğu modülün olay sözleşmesini uygular.

**Girdiler:** self, Etype: EventType, cs: Sensor, risk: float, isNotify: bool. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** event
**Bağlandığı işlevler:** Event, datetime.datetime.now, self.logger.Clog, self.logger.Mlog, self.storage.save, self.notifier.notify
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.
2. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.
3. Yan etki/çağrı adımını çalıştır: self.logger.Clog(f'{event.Etype.value}:{event.Ekind.value} {cs.name} value={risk:.2f}')
4. Yan etki/çağrı adımını çalıştır: self.logger.Mlog(f'{cs.name} sensörünün olayı değer : {risk} olarak kaydedildi')
5. Koşula göre yol seç: isNotify

**Gerçek kaynak:**

```python
def _emit(self, Etype: EventType, cs: Sensor, risk: float, isNotify: bool) -> None:
    # ALERT ve CALM durumlarını belirten; gerekli log, storage ve notify işlemlerini tutan fonksiyon
    # Bir olayda çıkan hatanın başka sensörleri bozmaması için try-except kullanıldı
        try:
            event = Event(Etype, cs.kind, risk, cs.name, datetime.datetime.now())
        except Exception as e:
            self.logger.Clog(f"{cs.name} sensörünün olayı nesneleştirilemedi!")
            self.logger.Mlog(f"{cs.name} sensörünün olayı nesneleştirilemedi. Hata kodu : {e}")
            return

        try:
            self.storage.save(event)
        except Exception as e:
            self.logger.Clog(f"{cs.name} sensörünün olayı kaydedilemedi!")
            self.logger.Mlog(f"{cs.name} sensörünün olayı kaydedilemedi! Hata kodu : {e}")
            return

        self.logger.Clog(f"{event.Etype.value}:{event.Ekind.value} {cs.name} value={risk:.2f}")

        self.logger.Mlog(f"{cs.name} sensörünün olayı değer : {risk} olarak kaydedildi")

        if isNotify: # ALERT durumunda bildiri yapılması için gerekli bool
            self.notifier.notify(event)
```

### EventEngine.tick — satır 265

Bağımsız CALCULATOR örneğinde sensörleri kota ve tek genel eşikle değerlendirir; güncel uygulama bu yolu kullanmaz.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** risk, current_time, last_time, self._last_limiter_log_ts
**Bağlandığı işlevler:** self.limiter, datetime.datetime.now, (current_time - self._last_limiter_log_ts).total_seconds, max, self.logger.Clog, self.logger.Mlog, self._emit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: cs ← self.Csensors

**Gerçek kaynak:**

```python
def tick(self) -> None: # EventEngine'de kayıtlı tüm sensörlerin verilerini çalıştıran fonksiyon
        for cs in self.Csensors: # Her bir sensör ayrı ayrı işleniyor
            risk = cs.value
            if not self.limiter(): # Eğer işlem hakkı sayısı yetersizse gerekli log işlemleri yapılır
                current_time = datetime.datetime.now()
                last_time = self.limiter.window_seconds - self.limiter.delta
                if (self._last_limiter_log_ts is None or ((current_time - self._last_limiter_log_ts).total_seconds() >= self._limiter_log_cooldown_s)): # İşlem hakkı sayısının bittiğini, sabit bir süre geçmeden tekrar bastırmamak koşuluyla, gerekli log işlemleriyle ekrana basar ve kaydeder. Tazelemeye kalan süreyi de ekrana bastırır
                    last_time = max(last_time,0.0)
                    self.logger.Clog(f"Limiter hakkı kalmadı. Tazelenmeye kalan süre : {last_time:.2f}.")
                    self.logger.Mlog("Limiter nedeniyle bu tick'te kalan sensörler işlenmedi.")
                    self._last_limiter_log_ts = current_time
                break

            else:
                if risk > self.threshold: # Riskli değer
                    self._emit(EventType.ALERT, cs, risk, True)
                else:
                    self._emit(EventType.CALM, cs, risk, False)
```


## IoT PyGame/iot_sim/.main_yedek.py

Korunan eski tek dosyalı simülasyon/yedek. Yeni giriş noktası bu kodu çalıştırmaz; güncel davranış testleri buna uygulanmaz.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: import math

```python
import math
```

Satır 2: Gereken isimleri içeri al: import os

```python
import os
```

Satır 3: Gereken isimleri içeri al: import random

```python
import random
```

Satır 4: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 5: Gereken isimleri içeri al: from dataclasses import dataclass, field

```python
from dataclasses import dataclass, field
```

Satır 6: Gereken isimleri içeri al: from enum import Enum

```python
from enum import Enum
```

Satır 11: Değeri/alanı oluştur veya güncelle: SCREEN_W, SCREEN_H = (1200, 800)

```python
SCREEN_W, SCREEN_H = 1200, 800
```

Satır 12: Değeri/alanı oluştur veya güncelle: PANEL_W = 320

```python
PANEL_W = 320
```

Satır 13: Değeri/alanı oluştur veya güncelle: FPS = 60

```python
FPS = 60
```

Satır 15: Değeri/alanı oluştur veya güncelle: DEFAULT_TILE = 16

```python
DEFAULT_TILE = 16
```

Satır 16: Değeri/alanı oluştur veya güncelle: MAX_ZOOM = 4.0

```python
MAX_ZOOM = 4.0
```

Satır 17: Değeri/alanı oluştur veya güncelle: MIN_ZOOM_FLOOR = 0.15

```python
MIN_ZOOM_FLOOR = 0.15
```

Satır 19: Değeri/alanı oluştur veya güncelle: TICK_SECONDS = 1.0

```python
TICK_SECONDS = 1.0
```

Satır 22: Değeri/alanı oluştur veya güncelle: ACCURACY_BY_DIST = [100, 99, 96, 90, 82, 70, 55]

```python
ACCURACY_BY_DIST = [100, 99, 96, 90, 82, 70, 55]
```

Satır 25: Değeri/alanı oluştur veya güncelle: PAN_SPEED = 1.0

```python
PAN_SPEED = 1.0
```

Satır 26: Değeri/alanı oluştur veya güncelle: PAN_DRAG_THRESHOLD_PX = 4

```python
PAN_DRAG_THRESHOLD_PX = 4
```

Satır 29: Değeri/alanı oluştur veya güncelle: FIELD_STEP_PX = 6

```python
FIELD_STEP_PX = 6
```

Satır 32: Değeri/alanı oluştur veya güncelle: PAD = 20

```python
PAD = 20
```

Satır 33: Değeri/alanı oluştur veya güncelle: SECTION_GAP = 18

```python
SECTION_GAP = 18
```

Satır 36: Değeri/alanı oluştur veya güncelle: PANEL_Y_APPEAR = 370

```python
PANEL_Y_APPEAR = 370
```

Satır 37: Değeri/alanı oluştur veya güncelle: PANEL_Y_GLOBAL_SWITCH = 406

```python
PANEL_Y_GLOBAL_SWITCH = 406
```

Satır 38: Değeri/alanı oluştur veya güncelle: PANEL_Y_SELECTED_TITLE = 450

```python
PANEL_Y_SELECTED_TITLE = 450
```

Satır 39: Değeri/alanı oluştur veya güncelle: PANEL_Y_SELECTED_LABEL = 490

```python
PANEL_Y_SELECTED_LABEL = 490
```

Satır 40: Değeri/alanı oluştur veya güncelle: PANEL_SCROLL_Y0 = 520

```python
PANEL_SCROLL_Y0 = 520
```

Satır 43: Değeri/alanı oluştur veya güncelle: DRAG_THRESHOLD_PX = 6

```python
DRAG_THRESHOLD_PX = 6
```

Satır 1705: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__ == "__main__":
    main()
```

### Kind — satır 48

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
SENSOR = "SENSOR"
SOURCE = "SOURCE"
OBSTACLE = "OBSTACLE"
BURNED = "BURNED"
UAV = "UAV"
```

### SourceType — satır 56

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
TEMP = "TEMP"
GAS = "GAS"
```

### RouteMode — satır 61

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
LOOP = "LOOP"
PINGPONG = "PINGPONG"
```

### SensorProps — satır 67

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
range_tiles: int = 6
efficiency: int = 80
battery: float = 5000.0
active: bool = True
last_temp: float = 0.0
last_gas: float = 0.0
```

### SourceProps — satır 77

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
stype: SourceType = SourceType.TEMP
power: int = 5
range_tiles: int = 8
```

### UavProps — satır 84

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
speed: float = 3.0
route: list[tuple[int, int]] = field(default_factory=list)
route_mode: RouteMode = RouteMode.LOOP
route_dir: int = 1
route_i: int = 0
x: float = 0.0
y: float = 0.0
carrying_ids: list[int] = field(default_factory=list)
```

### Entity — satır 96

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
id: int
kind: Kind
tx: int
ty: int
sensor: SensorProps | None = None
source: SourceProps | None = None
uav: UavProps | None = None
show_effect: bool = True
carried_by: int | None = None
icon_override: str | None = None
```

### clamp — satır 112

Sayısal değeri alt ve üst sınır arasında tutar; panel ve konum ayarlarında kullanılır.

**Girdiler:** v, lo, hi. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** max(lo, min(hi, v))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** max, min
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: max(lo, min(hi, v))

**Gerçek kaynak:**

```python
def clamp(v, lo, hi):
    return max(lo, min(hi, v))
```

### accuracy_for_dist — satır 116

Eski uzaklık tablosundan yüzde döndürür; yeni noktasal ölçüm bunu kullanmaz.

**Girdiler:** d: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** 0; ACCURACY_BY_DIST[d]; ACCURACY_BY_DIST[-1]
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: d >= 8
2. Koşula göre yol seç: d <= 6
3. Çağırana sonucu döndür: ACCURACY_BY_DIST[-1]

**Gerçek kaynak:**

```python
def accuracy_for_dist(d: int) -> int:
    if d >= 8:
        return 0
    if d <= 6:
        return ACCURACY_BY_DIST[d]
    return ACCURACY_BY_DIST[-1]
```

### tile_occupied — satır 124

Taşınmayan nesneler arasında hedef karenin dolu olup olmadığını söyler.

**Girdiler:** entities: list[Entity], tx: int, ty: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** True; False
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: e ← entities
2. Çağırana sonucu döndür: False

**Gerçek kaynak:**

```python
def tile_occupied(entities: list[Entity], tx: int, ty: int) -> bool:
    for e in entities:
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return True
    return False
```

### find_entity_at — satır 133

Bir karenin seçilebilir nesnesinin listedeki indeksini bulur; taşınan yükü atlar.

**Girdiler:** entities: list[Entity], tx: int, ty: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** i; None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** enumerate
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: (i, e) ← enumerate(entities)
2. Çağırana sonucu döndür: None

**Gerçek kaynak:**

```python
def find_entity_at(entities: list[Entity], tx: int, ty: int):
    # Prefer non-carried things for selection
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return i
    return None
```

### find_entity_by_id — satır 143

Kalıcı nesne kimliğini gerçek nesneye çözer; bulunamazsa None döner.

**Girdiler:** entities: list[Entity], eid: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** e; None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: e ← entities
2. Çağırana sonucu döndür: None

**Gerçek kaynak:**

```python
def find_entity_by_id(entities: list[Entity], eid: int) -> Entity | None:
    for e in entities:
        if e.id == eid:
            return e
    return None
```

### dist — satır 150

İki konum arasındaki Öklid uzaklığını hesaplar.

**Girdiler:** a, b. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** math.hypot(a[0] - b[0], a[1] - b[1])
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** math.hypot
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: math.hypot(a[0] - b[0], a[1] - b[1])

**Gerçek kaynak:**

```python
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])
```

### bresenham_tiles — satır 156

Bir doğru boyunca geçilen tam sayı karolarını sırayla üretir; rota engel testinin temelidir.

**Girdiler:** x0: int, y0: int, x1: int, y1: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (x, y)
**Atanan yerel değerler / durum alanları:** dx, dy, sx, sy, err, (x, y), e2, x, y
**Bağlandığı işlevler:** abs
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: dx = abs(x1 - x0)
2. Değeri/alanı oluştur veya güncelle: dy = abs(y1 - y0)
3. Değeri/alanı oluştur veya güncelle: sx = 1 if x0 < x1 else -1
4. Değeri/alanı oluştur veya güncelle: sy = 1 if y0 < y1 else -1
5. Değeri/alanı oluştur veya güncelle: err = dx - dy
6. Değeri/alanı oluştur veya güncelle: x, y = (x0, y0)
7. Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: True

**Gerçek kaynak:**

```python
def bresenham_tiles(x0: int, y0: int, x1: int, y1: int):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
```

### route_is_valid — satır 176

Returns False if any segment intersects an obstacle tile.

**Girdiler:** route_points: list[tuple[int, int]], obstacle_tiles: set[tuple[int, int]]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** True; False
**Atanan yerel değerler / durum alanları:** (x0, y0), (x1, y1)
**Bağlandığı işlevler:** len, range, bresenham_tiles
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: len(route_points) < 2
2. Her öğe için işle: i ← range(1, len(route_points))
3. Çağırana sonucu döndür: True

**Gerçek kaynak:**

```python
def route_is_valid(route_points: list[tuple[int, int]], obstacle_tiles: set[tuple[int, int]]) -> bool:
    """Returns False if any segment intersects an obstacle tile."""
    if len(route_points) < 2:
        return True
    for i in range(1, len(route_points)):
        x0, y0 = route_points[i - 1]
        x1, y1 = route_points[i]
        for (x, y) in bresenham_tiles(x0, y0, x1, y1):
            # allow the starting tile; everything else must be free
            if (x, y) == (x0, y0):
                continue
            if (x, y) in obstacle_tiles:
                return False
    return True
```

### spread_fire — satır 192

Every call (expected every 2s), some obstacles may ignite into TEMP sources.

**Girdiler:** entities: list['Entity']. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** temp_sources, obstacles, best_d, best_src, sp, d, n, p, tree.kind, tree.source, tree.icon_override
**Bağlandığı işlevler:** math.hypot, max, int, float, random.random, SourceProps
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: temp_sources = [e for e in entities if e.kind == Kind.SOURCE and e.source and (e.source.stype == SourceType.TEMP)]
2. Koşula göre yol seç: not temp_sources
3. Değeri/alanı oluştur veya güncelle: obstacles = [e for e in entities if e.kind == Kind.OBSTACLE and e.carried_by is None]
4. Koşula göre yol seç: not obstacles
5. Her öğe için işle: tree ← obstacles

**Gerçek kaynak:**

```python
def spread_fire(entities: list["Entity"]):
    """Every call (expected every 2s), some obstacles may ignite into TEMP sources."""
    temp_sources = [e for e in entities if e.kind == Kind.SOURCE and e.source and e.source.stype == SourceType.TEMP]
    if not temp_sources:
        return

    obstacles = [e for e in entities if e.kind == Kind.OBSTACLE and e.carried_by is None]
    if not obstacles:
        return

    for tree in obstacles:
        # nearest temp source that can reach this tree
        best_d = None
        best_src = None
        for src in temp_sources:
            sp = src.source
            if sp is None:
                continue
            d = math.hypot(tree.tx - src.tx, tree.ty - src.ty)
            if d <= max(1, int(sp.range_tiles)):
                if best_d is None or d < best_d:
                    best_d = d
                    best_src = src

        if best_d is None or best_d <= 0:
            continue

        n = max(1.0, float(best_d))
        p = 1.0 / (n * n)

        if random.random() < p:
            # convert this obstacle into a burned TEMP source
            tree.kind = Kind.SOURCE
            tree.source = SourceProps(stype=SourceType.TEMP, power=3, range_tiles=6)
            tree.icon_override = "burned"
```

### Camera — satır 233

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Camera.__init__ — satır 234

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.x, self.y, self.zoom
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.x = 0.0
2. Değeri/alanı oluştur veya güncelle: self.y = 0.0
3. Değeri/alanı oluştur veya güncelle: self.zoom = 1.0

**Gerçek kaynak:**

```python
def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.zoom = 1.0
```

### Camera.clamp_zoom_for_map — satır 239

Zoom değerini sınırlar; alternatif sürümde harita boyutunu da dikkate alır.

**Girdiler:** self, tile_px: float, map_w: int, map_h: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** view_w, view_h, min_zoom_x, min_zoom_y, min_zoom, self.zoom
**Bağlandığı işlevler:** max, clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: view_w = SCREEN_W - PANEL_W
2. Değeri/alanı oluştur veya güncelle: view_h = SCREEN_H
3. Değeri/alanı oluştur veya güncelle: min_zoom_x = view_w / (tile_px * max(1, map_w))
4. Değeri/alanı oluştur veya güncelle: min_zoom_y = view_h / (tile_px * max(1, map_h))
5. Değeri/alanı oluştur veya güncelle: min_zoom = max(min_zoom_x, min_zoom_y, MIN_ZOOM_FLOOR)
6. Değeri/alanı oluştur veya güncelle: self.zoom = clamp(self.zoom, min_zoom, MAX_ZOOM)

**Gerçek kaynak:**

```python
def clamp_zoom_for_map(self, tile_px: float, map_w: int, map_h: int):
        view_w = SCREEN_W - PANEL_W
        view_h = SCREEN_H
        min_zoom_x = view_w / (tile_px * max(1, map_w))
        min_zoom_y = view_h / (tile_px * max(1, map_h))
        min_zoom = max(min_zoom_x, min_zoom_y, MIN_ZOOM_FLOOR)
        self.zoom = clamp(self.zoom, min_zoom, MAX_ZOOM)
```

### Camera.zoom_at — satır 247

Mevcut ölçeği verilen katsayıyla değiştirip izin verilen aralıkta tutar.

**Girdiler:** self, zoom_factor: float, tile_px: float, map_w: int, map_h: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.zoom
**Bağlandığı işlevler:** self.clamp_zoom_for_map
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.zoom *= zoom_factor
2. Yan etki/çağrı adımını çalıştır: self.clamp_zoom_for_map(tile_px, map_w, map_h)

**Gerçek kaynak:**

```python
def zoom_at(self, zoom_factor: float, tile_px: float, map_w: int, map_h: int):
        self.zoom *= zoom_factor
        self.clamp_zoom_for_map(tile_px, map_w, map_h)
```

### Camera.screen_to_world — satır 251

Ekrandaki fare konumunu kamera dönüşümünün tersiyle dünya koordinatına çevirir.

**Girdiler:** self, screen_pos: tuple[int, int], tile_px: float. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (wx, wy)
**Atanan yerel değerler / durum alanları:** (sx, sy), cx, cy, dx, dy, wx, wy
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sx, sy = screen_pos
2. Değeri/alanı oluştur veya güncelle: cx = (SCREEN_W - PANEL_W) / 2
3. Değeri/alanı oluştur veya güncelle: cy = SCREEN_H / 2
4. Değeri/alanı oluştur veya güncelle: dx = sx - cx
5. Değeri/alanı oluştur veya güncelle: dy = sy - cy
6. Değeri/alanı oluştur veya güncelle: wx = dx / (tile_px * self.zoom) + self.x
7. Değeri/alanı oluştur veya güncelle: wy = dy / (tile_px * self.zoom) + self.y
8. Çağırana sonucu döndür: (wx, wy)

**Gerçek kaynak:**

```python
def screen_to_world(self, screen_pos: tuple[int, int], tile_px: float) -> tuple[float, float]:
        sx, sy = screen_pos
        cx = (SCREEN_W - PANEL_W) / 2
        cy = SCREEN_H / 2
        dx = sx - cx
        dy = sy - cy
        wx = dx / (tile_px * self.zoom) + self.x
        wy = dy / (tile_px * self.zoom) + self.y
        return wx, wy
```

### simulate_tick — satır 265

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** entities: list[Entity], dt_seconds: float. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sources, s, rng, eff, base, mult, drain, s.battery, s.active, s.last_temp, s.last_gas, temp_val, gas_val, sp, d, src_rng, d_eff, d_eff_i, acc, power, att, contrib
**Bağlandığı işlevler:** max, int, clamp, math.hypot, math.floor, accuracy_for_dist
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sources = [e for e in entities if e.kind == Kind.SOURCE and e.source is not None]
2. Her öğe için işle: e ← entities

**Gerçek kaynak:**

```python
def simulate_tick(entities: list[Entity], dt_seconds: float):
    sources = [e for e in entities if e.kind == Kind.SOURCE and e.source is not None]

    for e in entities:
        if e.kind != Kind.SENSOR or e.sensor is None:
            continue

        s = e.sensor
        rng = max(1, int(s.range_tiles))
        eff = clamp(int(s.efficiency), 1, 100)

        # Battery drain: n^2 per second, multiplied by inefficiency
        base = rng * rng
        mult = 1.0 + (100 - eff) / 100.0
        drain = base * mult * dt_seconds

        if s.battery <= 0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_gas = 0.0
            continue

        s.battery -= drain
        if s.battery <= 0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_gas = 0.0
            continue

        s.active = True

        temp_val = 0.0
        gas_val = 0.0

        for src_ent in sources:
            sp = src_ent.source
            if sp is None:
                continue

            d = math.hypot(e.tx - src_ent.tx, e.ty - src_ent.ty)
            src_rng = max(1, int(sp.range_tiles))

            # Effective distance from sensor to nearest point of source influence:
            d_eff = max(0.0, d - src_rng)
            if d_eff > rng:
                continue

            d_eff_i = int(math.floor(d_eff + 1e-6))
            acc = accuracy_for_dist(d_eff_i)
            if acc <= 0:
                continue

            power = clamp(int(sp.power), 1, 10)

            att = 1.0 - (d_eff / src_rng)
            if att < 0:
                att = 0.0

            contrib = power * att * (acc / 100.0)

            if sp.stype == SourceType.TEMP:
                temp_val += contrib
            else:
                gas_val += contrib

        s.last_temp = temp_val
        s.last_gas = gas_val
```

### update_uavs — satır 336

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** entities: list[Entity], dt: float, map_w: int, map_h: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** up, speed, remaining, up.route_i, target_i, (tx, ty), dx, dy, d, next_i, up.route_dir, step, up.x, up.y, u.tx, u.ty, ce, ce.tx, ce.ty
**Bağlandığı işlevler:** len, clamp, int, math.hypot, min, round, find_entity_by_id
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: u ← entities

**Gerçek kaynak:**

```python
def update_uavs(entities: list[Entity], dt: float, map_w: int, map_h: int):
    for u in entities:
        if u.kind != Kind.UAV or u.uav is None:
            continue
        up = u.uav
        if not up.route or len(up.route) < 2:
            continue

        speed = clamp(up.speed, 1.0, 10.0)
        remaining = speed * dt  # tiles to move this frame

        while remaining > 1e-6:
            # Clamp waypoint index
            up.route_i = int(clamp(up.route_i, 0, len(up.route) - 1))
            target_i = up.route_i
            tx, ty = up.route[target_i]
            dx = tx - up.x
            dy = ty - up.y
            d = math.hypot(dx, dy)

            if d < 1e-6:
                # reached this waypoint, choose next
                next_i = target_i + up.route_dir

                if up.route_mode == RouteMode.LOOP:
                    if next_i >= len(up.route):
                        next_i = 0
                    if next_i < 0:
                        next_i = len(up.route) - 1
                    up.route_i = next_i

                else:  # PINGPONG
                    if next_i >= len(up.route) or next_i < 0:
                        up.route_dir *= -1
                        next_i = target_i + up.route_dir
                        next_i = int(clamp(next_i, 0, len(up.route) - 1))
                    up.route_i = next_i
                continue

            step = min(remaining, d)
            up.x += (dx / d) * step
            up.y += (dy / d) * step
            remaining -= step

        # Keep inside map bounds
        up.x = clamp(up.x, 0.0, map_w - 1.0)
        up.y = clamp(up.y, 0.0, map_h - 1.0)

        # Update tile coords for rendering/selection
        u.tx = int(round(up.x))
        u.ty = int(round(up.y))
        u.tx = int(clamp(u.tx, 0, map_w - 1))
        u.ty = int(clamp(u.ty, 0, map_h - 1))

        # Move carried items with UAV (and effects center becomes UAV center because tx/ty follow)
        for cid in up.carrying_ids:
            ce = find_entity_by_id(entities, cid)
            if ce is None:
                continue
            ce.tx = u.tx
            ce.ty = u.ty
```

### draw_button — satır 402

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, text, font, active=False. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** label
**Bağlandığı işlevler:** pygame.draw.rect, font.render, screen.blit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (225, 225, 225) if active else (90, 90, 100), rect, 2 if active else 1, border_radius=10)
3. Değeri/alanı oluştur veya güncelle: label = font.render(text, True, (235, 235, 235))
4. Yan etki/çağrı adımını çalıştır: screen.blit(label, (rect.x + 12, rect.y + 9))

**Gerçek kaynak:**

```python
def draw_button(screen, rect, text, font, active=False):
    pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
    pygame.draw.rect(
        screen,
        (225, 225, 225) if active else (90, 90, 100),
        rect,
        2 if active else 1,
        border_radius=10,
    )
    label = font.render(text, True, (235, 235, 235))
    screen.blit(label, (rect.x + 12, rect.y + 9))
```

### draw_small_btn — satır 415

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, text, font. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** label, (lw, lh)
**Bağlandığı işlevler:** pygame.draw.rect, font.render, label.get_size, screen.blit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (50, 50, 55), rect, border_radius=6)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=6)
3. Değeri/alanı oluştur veya güncelle: label = font.render(text, True, (240, 240, 240))
4. Değeri/alanı oluştur veya güncelle: lw, lh = label.get_size()
5. Yan etki/çağrı adımını çalıştır: screen.blit(label, (rect.centerx - lw // 2, rect.centery - lh // 2))

**Gerçek kaynak:**

```python
def draw_small_btn(screen, rect, text, font):
    pygame.draw.rect(screen, (50, 50, 55), rect, border_radius=6)
    pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=6)
    label = font.render(text, True, (240, 240, 240))
    lw, lh = label.get_size()
    screen.blit(label, (rect.centerx - lw // 2, rect.centery - lh // 2))
```

### draw_switch — satır 423

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, on: bool. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** bg, border, on_col, inner, knob_r, kx, ky
**Bağlandığı işlevler:** pygame.draw.rect, rect.inflate, pygame.draw.circle
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: bg = (50, 50, 55)
2. Değeri/alanı oluştur veya güncelle: border = (120, 120, 130)
3. Değeri/alanı oluştur veya güncelle: on_col = (120, 210, 150)
4. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, bg, rect, border_radius=999)
5. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, border, rect, 1, border_radius=999)
6. Değeri/alanı oluştur veya güncelle: inner = rect.inflate(-4, -4)
7. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, on_col if on else (70, 70, 80), inner, border_radius=999)
8. Değeri/alanı oluştur veya güncelle: knob_r = inner.height // 2 - 1
9. Değeri/alanı oluştur veya güncelle: kx = inner.right - knob_r - 2 if on else inner.left + knob_r + 2
10. Değeri/alanı oluştur veya güncelle: ky = inner.centery
11. Yan etki/çağrı adımını çalıştır: pygame.draw.circle(screen, (235, 235, 235), (kx, ky), knob_r)

**Gerçek kaynak:**

```python
def draw_switch(screen, rect, on: bool):
    # pill
    bg = (50, 50, 55)
    border = (120, 120, 130)
    on_col = (120, 210, 150)
    pygame.draw.rect(screen, bg, rect, border_radius=999)
    pygame.draw.rect(screen, border, rect, 1, border_radius=999)
    inner = rect.inflate(-4, -4)
    pygame.draw.rect(screen, on_col if on else (70, 70, 80), inner, border_radius=999)

    # knob
    knob_r = inner.height // 2 - 1
    kx = inner.right - knob_r - 2 if on else inner.left + knob_r + 2
    ky = inner.centery
    pygame.draw.circle(screen, (235, 235, 235), (kx, ky), knob_r)
```

### draw_section_title — satır 440

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, x, y, title, font, small. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** screen.blit, font.render, pygame.draw.line
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: screen.blit(font.render(title, True, (245, 245, 245)), (x, y))
2. Yan etki/çağrı adımını çalıştır: pygame.draw.line(screen, (45, 45, 55), (x, y + 26), (x + PANEL_W - 2 * PAD, y + 26), 1)

**Gerçek kaynak:**

```python
def draw_section_title(screen, x, y, title, font, small):
    screen.blit(font.render(title, True, (245, 245, 245)), (x, y))
    pygame.draw.line(screen, (45, 45, 55), (x, y + 26), (x + PANEL_W - 2 * PAD, y + 26), 1)
```

### draw_segmented — satır 445

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, options: list[str], selected_idx: int, font_small. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** seg_rects
**Atanan yerel değerler / durum alanları:** n, seg_w, seg_rects, r, txt
**Bağlandığı işlevler:** pygame.draw.rect, len, range, pygame.Rect, seg_rects.append, r.inflate, font_small.render, screen.blit, txt.get_width, txt.get_height
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=10)
3. Değeri/alanı oluştur veya güncelle: n = len(options)
4. Değeri/alanı oluştur veya güncelle: seg_w = rect.width // n
5. Değeri/alanı oluştur veya güncelle: seg_rects = []
6. Her öğe için işle: i ← range(n)
7. Çağırana sonucu döndür: seg_rects

**Gerçek kaynak:**

```python
def draw_segmented(screen, rect, options: list[str], selected_idx: int, font_small):
    # background
    pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
    pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=10)
    n = len(options)
    seg_w = rect.width // n
    seg_rects = []
    for i in range(n):
        r = pygame.Rect(rect.x + i * seg_w, rect.y, seg_w, rect.height)
        seg_rects.append(r)

        if i == selected_idx:
            pygame.draw.rect(screen, (70, 70, 78), r.inflate(-2, -2), border_radius=8)

        txt = font_small.render(options[i], True, (235, 235, 235))
        screen.blit(txt, (r.centerx - txt.get_width() // 2, r.centery - txt.get_height() // 2))
    return seg_rects
```

### build_panel_layout — satır 467

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** entities, selected_tool, selected_entity_idx, panel_x, small, font, show_effect_global: bool, uav_focus_cargo_id: int | None, collapsed_cargo_ids: set[int]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (tool_buttons, clickables, global_rows, entity_rows, sw, None, None, content_bottom); (tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom)
**Atanan yerel değerler / durum alanları:** tool_buttons, clickables, global_rows, entity_rows, global_sw_rect, attr_y, sw, content_bottom, e, ent_sw_y, ent_sw, y, back, s, src, seg_rect, up, mode_sw, slot_w, slots, r, clr, ce, rect, label, tog, is_collapsed, src2, s2
**Bağlandığı işlevler:** pygame.Rect, global_rows.append, clickables.append, len, max, entity_rows.append, add_numeric_row, str, set_range, set_eff, int, set_batt, set_power, set_srange, set_speed, range, slots.append, list, find_entity_by_id, set_power2, set_srange2, set_range2, set_eff2
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: tool_buttons = [(Kind.SENSOR, pygame.Rect(panel_x + PAD, 70, PANEL_W - 2 * PAD, 40), 'Ekle: IoT Sensör'), (Kind.SOURCE, pygame.Rect(panel_x + PAD, 120, PANEL_W - 2 * PAD, 40), 'Ekle: Kaynak'), (Kind.OBSTACLE, pygame.Rect…
2. Değeri/alanı oluştur veya güncelle: clickables: list[tuple[pygame.Rect, callable]] = []
3. Değeri/alanı oluştur veya güncelle: global_rows = []
4. Değeri/alanı oluştur veya güncelle: entity_rows = []
5. Değeri/alanı oluştur veya güncelle: global_sw_rect = None
6. Değeri/alanı oluştur veya güncelle: attr_y = PANEL_Y_GLOBAL_SWITCH
7. Değeri/alanı oluştur veya güncelle: sw = pygame.Rect(panel_x + PAD, attr_y, 44, 24)
8. Yan etki/çağrı adımını çalıştır: global_rows.append(('switch', sw, 'Etki yarıçaplarını göster', show_effect_global))
9. Yan etki/çağrı adımını çalıştır: clickables.append((sw, None))
10. Koşula göre yol seç: selected_entity_idx is None or not 0 <= selected_entity_idx < len(entities)
11. Değeri/alanı oluştur veya güncelle: e = entities[selected_entity_idx]
12. Değeri/alanı oluştur veya güncelle: ent_sw_y = PANEL_SCROLL_Y0
13. Değeri/alanı oluştur veya güncelle: ent_sw = pygame.Rect(panel_x + PAD, ent_sw_y, 44, 24)
14. Yan etki/çağrı adımını çalıştır: entity_rows.append(('switch', ent_sw, 'Bu nesnenin etkisini göster', e.show_effect))
15. Yerel yardımcı tanımla: toggle_entity_effect; ayrı sembol kaydı aşağıdadır.
16. Yan etki/çağrı adımını çalıştır: clickables.append((ent_sw, toggle_entity_effect))
17. Değeri/alanı oluştur veya güncelle: y = ent_sw_y + 40
18. Koşula göre yol seç: e.carried_by is not None
19. Yerel yardımcı tanımla: add_numeric_row; ayrı sembol kaydı aşağıdadır.
20. Koşula göre yol seç: e.kind == Kind.SENSOR and e.sensor
21. Değeri/alanı oluştur veya güncelle: content_bottom = 0
22. Her öğe için işle: row ← global_rows + entity_rows
23. Çağırana sonucu döndür: (tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom)

**Gerçek kaynak:**

```python
def build_panel_layout(entities, selected_tool, selected_entity_idx, panel_x, small, font,
                       show_effect_global: bool, uav_focus_cargo_id: int | None,
                       collapsed_cargo_ids: set[int]):
    tool_buttons = [
        (Kind.SENSOR, pygame.Rect(panel_x + PAD, 70, PANEL_W - 2 * PAD, 40), "Ekle: IoT Sensör"),
        (Kind.SOURCE, pygame.Rect(panel_x + PAD, 120, PANEL_W - 2 * PAD, 40), "Ekle: Kaynak"),
        (Kind.OBSTACLE, pygame.Rect(panel_x + PAD, 170, PANEL_W - 2 * PAD, 40), "Ekle: Engel (Ağaç)"),
        (Kind.BURNED, pygame.Rect(panel_x + PAD, 220, PANEL_W - 2 * PAD, 40), "Ekle: Burned (Yanık)"),
        (Kind.UAV, pygame.Rect(panel_x + PAD, 270, PANEL_W - 2 * PAD, 40), "Ekle: İHA (Drone)"),
    ]

    clickables: list[tuple[pygame.Rect, callable]] = []
    global_rows = []
    entity_rows = []
    global_sw_rect = None

    # Global switch row
    attr_y = PANEL_Y_GLOBAL_SWITCH
    sw = pygame.Rect(panel_x + PAD, attr_y, 44, 24)
    global_rows.append(("switch", sw, "Etki yarıçaplarını göster", show_effect_global))
    clickables.append((sw, None))  # placeholder

    if selected_entity_idx is None or not (0 <= selected_entity_idx < len(entities)):
        # content bottom for scrolling
        content_bottom = 0
        for row in global_rows:
            if row[0] == "switch":
                content_bottom = max(content_bottom, row[1].bottom)
        return tool_buttons, clickables, global_rows, entity_rows, sw, None, None, content_bottom

    e = entities[selected_entity_idx]

    # Per-entity switch
    ent_sw_y = PANEL_SCROLL_Y0
    ent_sw = pygame.Rect(panel_x + PAD, ent_sw_y, 44, 24)
    entity_rows.append(("switch", ent_sw, "Bu nesnenin etkisini göster", e.show_effect))

    def toggle_entity_effect():
        e.show_effect = not e.show_effect

    clickables.append((ent_sw, toggle_entity_effect))

    y = ent_sw_y + 40

    # If this entity is being carried, offer a quick "back to UAV" button
    if e.carried_by is not None:
        back = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
        entity_rows.append(("button", back, f"İHA'ya dön (#{e.carried_by})"))
        clickables.append((back, ("select_entity_id", e.carried_by)))
        y += 42
        entity_rows.append(("text", y, f"Not: Bu nesne İHA #{e.carried_by} üzerinde taşınıyor."))
        y += 22

    def add_numeric_row(label, value_str, dec_fn, inc_fn, step_hint=None):
        nonlocal y
        text_surf = small.render(f"{label}: {value_str}", True, (220, 220, 220))
        h = text_surf.get_height()
        btn_y = y + h + 6
        minus = pygame.Rect(panel_x + PAD, btn_y, 30, 26)
        plus = pygame.Rect(panel_x + PAD + 38, btn_y, 30, 26)
        clickables.append((minus, dec_fn))
        clickables.append((plus, inc_fn))
        entity_rows.append(("numeric", y, f"{label}: {value_str}", minus, plus, step_hint))
        y = btn_y + 26 + 12

    if e.kind == Kind.SENSOR and e.sensor:
        s = e.sensor
        entity_rows.append(("text", y, f"Aktif: {'Evet' if s.active else 'Hayır'}"))
        y += 22

        def set_range(d):
            s.range_tiles = clamp(s.range_tiles + d, 1, 50)
            if s.battery > 0:
                s.active = True

        def set_eff(d):
            s.efficiency = clamp(s.efficiency + d, 1, 100)

        def set_batt(d):
            s.battery = max(0.0, s.battery + float(d))
            if s.battery > 0:
                s.active = True

        add_numeric_row("Menzil", str(s.range_tiles),
                        dec_fn=lambda: set_range(-1),
                        inc_fn=lambda: set_range(+1))
        add_numeric_row("Verimlilik", str(s.efficiency),
                        dec_fn=lambda: set_eff(-5),
                        inc_fn=lambda: set_eff(+5),
                        step_hint="(±5)")
        add_numeric_row("Pil", str(int(s.battery)),
                        dec_fn=lambda: set_batt(-250),
                        inc_fn=lambda: set_batt(+250),
                        step_hint="(±250)")

        entity_rows.append(("text", y, f"Son TEMP: {s.last_temp:.2f}"))
        y += 18
        entity_rows.append(("text", y, f"Son GAS : {s.last_gas:.2f}"))

    elif e.kind == Kind.SOURCE and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip:"))
        y += 18

        seg_rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 32)
        # placeholder rects produced in draw step; click handling uses stored rectangles
        entity_rows.append(("segmented", seg_rect, ["TEMP", "GAS"], 0 if src.stype == SourceType.TEMP else 1))
        y += 44

        def set_power(d):
            src.power = clamp(src.power + d, 1, 10)

        def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)

        add_numeric_row("Güç", str(src.power),
                        dec_fn=lambda: set_power(-1),
                        inc_fn=lambda: set_power(+1))
        add_numeric_row("Menzil", str(src.range_tiles),
                        dec_fn=lambda: set_srange(-1),
                        inc_fn=lambda: set_srange(+1))


    elif e.kind == Kind.BURNED and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip: TEMP (burned)"))
        y += 22

        def set_power(d):
            src.power = clamp(src.power + d, 1, 10)

        def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)

        add_numeric_row("Güç", str(src.power),
                        dec_fn=lambda: set_power(-1),
                        inc_fn=lambda: set_power(+1))
        add_numeric_row("Menzil", str(src.range_tiles),
                        dec_fn=lambda: set_srange(-1),
                        inc_fn=lambda: set_srange(+1))

    elif e.kind == Kind.UAV and e.uav:
        up = e.uav

        entity_rows.append(("text", y, "Rota: K ile düzenle (İHA seçiliyken)"))
        y += 18
        entity_rows.append(("text", y, f"Waypoint sayısı: {len(up.route)}"))
        y += 22

        def set_speed(d):
            up.speed = clamp(up.speed + d, 1.0, 10.0)

        add_numeric_row("Hız (tile/s)", f"{up.speed:.1f}",
                        dec_fn=lambda: set_speed(-0.5),
                        inc_fn=lambda: set_speed(+0.5),
                        step_hint="(±0.5)")

        # route mode switch
        mode_sw = pygame.Rect(panel_x + PAD, y + 2, 44, 24)
        entity_rows.append(("mode_switch", mode_sw, "Tersine takip (PingPong)", up.route_mode == RouteMode.PINGPONG))

        def toggle_mode():
            up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
            up.route_dir = 1

        clickables.append((mode_sw, toggle_mode))
        y += 40

        # Cargo slots (drag-drop)
        entity_rows.append(("text", y, "Taşınanlar (sürükle-bırak):"))
        y += 18

        slot_w = (PANEL_W - 2 * PAD - 10) // 3
        slots = []
        for i in range(3):
            r = pygame.Rect(panel_x + PAD + i * (slot_w + 5), y, slot_w, 42)
            slots.append(r)
        entity_rows.append(("cargo_slots", slots))
        y += 54

        # Clear button
        clr = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
        entity_rows.append(("button", clr, "Taşınanları Temizle"))

        def clear_cargo():
            # detach carried
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce:
                    ce.carried_by = None
            up.carrying_ids.clear()

        clickables.append((clr, clear_cargo))
        y += 42

        # Quick access buttons for carried items (edit without detaching)
        if up.carrying_ids:
            entity_rows.append(("text", y, "Taşınan nesneler (düzenle):"))
            y += 18
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce is None:
                    continue
                rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
                label = f"Düzenle: {ce.kind.value} #{ce.id}"
                entity_rows.append(("carry_edit_btn", rect, label, cid))
                clickables.append((rect, ("uav_focus_cargo", cid)))
                y += 38

        # Focused cargo details (show under UAV props, without changing selection)
        if uav_focus_cargo_id is not None and uav_focus_cargo_id in list(up.carrying_ids):
            ce = find_entity_by_id(entities, uav_focus_cargo_id)
            if ce is not None:
                y += 4
                entity_rows.append(("text", y, f"{ce.kind.value} özellikleri:"))
                tog = pygame.Rect(panel_x + PAD + 170, y - 2, 90, 22)
                is_collapsed = (ce.id in collapsed_cargo_ids)
                entity_rows.append(("cargo_toggle", tog, "KAPAT" if not is_collapsed else "AÇ"))
                def _toggle_cargo(cid=ce.id):
                    if cid in collapsed_cargo_ids:
                        collapsed_cargo_ids.remove(cid)
                    else:
                        collapsed_cargo_ids.add(cid)
                clickables.append((tog, _toggle_cargo))
                y += 26

                if ce.id not in collapsed_cargo_ids:
                    if ce.kind == Kind.SOURCE and ce.source:
                        src2 = ce.source
                        entity_rows.append(("text", y, f"Tip: {src2.stype.value}"))
                        y += 18

                        def set_power2(d):
                            src2.power = clamp(src2.power + d, 1, 10)
                        def set_srange2(d):
                            src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)

                        add_numeric_row("Güç", str(src2.power),
                                        dec_fn=lambda: set_power2(-1),
                                        inc_fn=lambda: set_power2(+1))
                        add_numeric_row("Menzil", str(src2.range_tiles),
                                        dec_fn=lambda: set_srange2(-1),
                                        inc_fn=lambda: set_srange2(+1))

                    elif ce.kind == Kind.SENSOR and ce.sensor:
                        s2 = ce.sensor
                        def set_range2(d):
                            s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
                            if s2.battery > 0:
                                s2.active = True
                        def set_eff2(d):
                            s2.efficiency = clamp(s2.efficiency + d, 1, 100)

                        add_numeric_row("Menzil", str(s2.range_tiles),
                                        dec_fn=lambda: set_range2(-1),
                                        inc_fn=lambda: set_range2(+1))
                        add_numeric_row("Verimlilik", str(s2.efficiency),
                                        dec_fn=lambda: set_eff2(-5),
                                        inc_fn=lambda: set_eff2(+5),
                                        step_hint="(±5)")

    elif e.kind == Kind.OBSTACLE:
        entity_rows.append(("text", y, "Engel: şimdilik sadece blok objesi."))
        y += 18
        entity_rows.append(("text", y, "Sonraki adım: LOS ile zayıflatma."))

    # content bottom for scrolling (panel absolute coords)
    content_bottom = 0
    for row in global_rows + entity_rows:
        if row[0] in ("switch", "mode_switch"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "text":
            content_bottom = max(content_bottom, row[1] + 28)
        elif row[0] == "numeric":
            content_bottom = max(content_bottom, row[1] + 60)
        elif row[0] in ("button", "carry_edit_btn", "segmented", "cargo_toggle"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "cargo_slots":
            for r in row[1]:
                content_bottom = max(content_bottom, r.bottom)
    return tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom
```

### build_panel_layout.toggle_entity_effect — satır 504

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** e.show_effect
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e.show_effect = not e.show_effect

**Gerçek kaynak:**

```python
def toggle_entity_effect():
        e.show_effect = not e.show_effect
```

### build_panel_layout.add_numeric_row — satır 520

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** label, value_str, dec_fn, inc_fn, step_hint=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** text_surf, h, btn_y, minus, plus, y
**Bağlandığı işlevler:** small.render, text_surf.get_height, pygame.Rect, clickables.append, entity_rows.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: text_surf = small.render(f'{label}: {value_str}', True, (220, 220, 220))
2. Değeri/alanı oluştur veya güncelle: h = text_surf.get_height()
3. Değeri/alanı oluştur veya güncelle: btn_y = y + h + 6
4. Değeri/alanı oluştur veya güncelle: minus = pygame.Rect(panel_x + PAD, btn_y, 30, 26)
5. Değeri/alanı oluştur veya güncelle: plus = pygame.Rect(panel_x + PAD + 38, btn_y, 30, 26)
6. Yan etki/çağrı adımını çalıştır: clickables.append((minus, dec_fn))
7. Yan etki/çağrı adımını çalıştır: clickables.append((plus, inc_fn))
8. Yan etki/çağrı adımını çalıştır: entity_rows.append(('numeric', y, f'{label}: {value_str}', minus, plus, step_hint))
9. Değeri/alanı oluştur veya güncelle: y = btn_y + 26 + 12

**Gerçek kaynak:**

```python
def add_numeric_row(label, value_str, dec_fn, inc_fn, step_hint=None):
        nonlocal y
        text_surf = small.render(f"{label}: {value_str}", True, (220, 220, 220))
        h = text_surf.get_height()
        btn_y = y + h + 6
        minus = pygame.Rect(panel_x + PAD, btn_y, 30, 26)
        plus = pygame.Rect(panel_x + PAD + 38, btn_y, 30, 26)
        clickables.append((minus, dec_fn))
        clickables.append((plus, inc_fn))
        entity_rows.append(("numeric", y, f"{label}: {value_str}", minus, plus, step_hint))
        y = btn_y + 26 + 12
```

### build_panel_layout.set_range — satır 537

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s.range_tiles, s.active
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s.range_tiles = clamp(s.range_tiles + d, 1, 50)
2. Koşula göre yol seç: s.battery > 0

**Gerçek kaynak:**

```python
def set_range(d):
            s.range_tiles = clamp(s.range_tiles + d, 1, 50)
            if s.battery > 0:
                s.active = True
```

### build_panel_layout.set_eff — satır 542

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s.efficiency
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s.efficiency = clamp(s.efficiency + d, 1, 100)

**Gerçek kaynak:**

```python
def set_eff(d):
            s.efficiency = clamp(s.efficiency + d, 1, 100)
```

### build_panel_layout.set_batt — satır 545

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s.battery, s.active
**Bağlandığı işlevler:** max, float
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s.battery = max(0.0, s.battery + float(d))
2. Koşula göre yol seç: s.battery > 0

**Gerçek kaynak:**

```python
def set_batt(d):
            s.battery = max(0.0, s.battery + float(d))
            if s.battery > 0:
                s.active = True
```

### build_panel_layout.set_power — satır 576

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.power
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.power = clamp(src.power + d, 1, 10)

**Gerçek kaynak:**

```python
def set_power(d):
            src.power = clamp(src.power + d, 1, 10)
```

### build_panel_layout.set_srange — satır 579

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.range_tiles
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.range_tiles = clamp(src.range_tiles + d, 1, 80)

**Gerçek kaynak:**

```python
def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)
```

### build_panel_layout.set_power — satır 595

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.power
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.power = clamp(src.power + d, 1, 10)

**Gerçek kaynak:**

```python
def set_power(d):
            src.power = clamp(src.power + d, 1, 10)
```

### build_panel_layout.set_srange — satır 598

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.range_tiles
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.range_tiles = clamp(src.range_tiles + d, 1, 80)

**Gerçek kaynak:**

```python
def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)
```

### build_panel_layout.set_speed — satır 616

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** up.speed
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: up.speed = clamp(up.speed + d, 1.0, 10.0)

**Gerçek kaynak:**

```python
def set_speed(d):
            up.speed = clamp(up.speed + d, 1.0, 10.0)
```

### build_panel_layout.toggle_mode — satır 628

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** up.route_mode, up.route_dir
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
2. Değeri/alanı oluştur veya güncelle: up.route_dir = 1

**Gerçek kaynak:**

```python
def toggle_mode():
            up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
            up.route_dir = 1
```

### build_panel_layout.clear_cargo — satır 651

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** ce, ce.carried_by
**Bağlandığı işlevler:** list, find_entity_by_id, up.carrying_ids.clear
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: cid ← list(up.carrying_ids)
2. Yan etki/çağrı adımını çalıştır: up.carrying_ids.clear()

**Gerçek kaynak:**

```python
def clear_cargo():
            # detach carried
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce:
                    ce.carried_by = None
            up.carrying_ids.clear()
```

### build_panel_layout._toggle_cargo — satır 685

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** cid=ce.id. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** collapsed_cargo_ids.remove, collapsed_cargo_ids.add
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: cid in collapsed_cargo_ids

**Gerçek kaynak:**

```python
def _toggle_cargo(cid=ce.id):
                    if cid in collapsed_cargo_ids:
                        collapsed_cargo_ids.remove(cid)
                    else:
                        collapsed_cargo_ids.add(cid)
```

### build_panel_layout.set_power2 — satır 699

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src2.power
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src2.power = clamp(src2.power + d, 1, 10)

**Gerçek kaynak:**

```python
def set_power2(d):
                            src2.power = clamp(src2.power + d, 1, 10)
```

### build_panel_layout.set_srange2 — satır 701

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src2.range_tiles
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)

**Gerçek kaynak:**

```python
def set_srange2(d):
                            src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)
```

### build_panel_layout.set_range2 — satır 713

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s2.range_tiles, s2.active
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
2. Koşula göre yol seç: s2.battery > 0

**Gerçek kaynak:**

```python
def set_range2(d):
                            s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
                            if s2.battery > 0:
                                s2.active = True
```

### build_panel_layout.set_eff2 — satır 717

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s2.efficiency
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s2.efficiency = clamp(s2.efficiency + d, 1, 100)

**Gerçek kaynak:**

```python
def set_eff2(d):
                            s2.efficiency = clamp(s2.efficiency + d, 1, 100)
```

### load_icon — satır 753

Görüntüyü alfa kanallı yüzeye dönüştürür; yükleme başarısızsa None ile geri dönüşe izin verir.

**Girdiler:** path: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** pygame.image.load(path).convert_alpha(); None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** pygame.image.load(path).convert_alpha, pygame.image.load
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def load_icon(path: str):
    try:
        return pygame.image.load(path).convert_alpha()
    except Exception:
        return None
```

### get_scaled_icon — satır 760

Aynı ikon ve boyut için yeniden ölçeklemeyi önbellekten karşılar.

**Girdiler:** cache: dict, key: str, surf, size: tuple[int, int]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None; cache[k]
**Atanan yerel değerler / durum alanları:** k, cache[k]
**Bağlandığı işlevler:** pygame.transform.smoothscale
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: surf is None
2. Değeri/alanı oluştur veya güncelle: k = (key, size[0], size[1])
3. Koşula göre yol seç: k in cache
4. Değeri/alanı oluştur veya güncelle: cache[k] = pygame.transform.smoothscale(surf, size)
5. Çağırana sonucu döndür: cache[k]

**Gerçek kaynak:**

```python
def get_scaled_icon(cache: dict, key: str, surf, size: tuple[int, int]):
    if surf is None:
        return None
    k = (key, size[0], size[1])
    if k in cache:
        return cache[k]
    cache[k] = pygame.transform.smoothscale(surf, size)
    return cache[k]
```

### draw_dashed_circle — satır 773

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** surface: pygame.Surface, center: tuple[int, int], radius: int, color: tuple[int, int, int, int], dash_deg: int=12, gap_deg: int=10, width: int=2. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** (cx, cy), step, a1, pts, samples, t, ang, x, y
**Bağlandığı işlevler:** range, max, math.radians, int, round, math.cos, math.sin, pts.append, len, pygame.draw.lines
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: radius <= 0
2. Değeri/alanı oluştur veya güncelle: cx, cy = center
3. Değeri/alanı oluştur veya güncelle: step = dash_deg + gap_deg
4. Her öğe için işle: a0 ← range(0, 360, step)

**Gerçek kaynak:**

```python
def draw_dashed_circle(surface: pygame.Surface, center: tuple[int, int], radius: int,
                       color: tuple[int, int, int, int], dash_deg: int = 12, gap_deg: int = 10, width: int = 2):
    if radius <= 0:
        return
    cx, cy = center
    step = dash_deg + gap_deg
    for a0 in range(0, 360, step):
        a1 = a0 + dash_deg
        pts = []
        samples = max(4, dash_deg // 2)
        for i in range(samples + 1):
            t = i / samples
            ang = math.radians(a0 + (a1 - a0) * t)
            x = cx + int(round(math.cos(ang) * radius))
            y = cy + int(round(math.sin(ang) * radius))
            pts.append((x, y))
        if len(pts) >= 2:
            pygame.draw.lines(surface, color, False, pts, width)
```

### make_gauss_field_surface — satır 793

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** cache: dict, key: tuple, radius_px: int, rgba: tuple[int, int, int, int]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None; cache[key]; surf
**Atanan yerel değerler / durum alanları:** size, surf, cx, cy, max_a, (r_col, g_col, b_col, _), sigma, a, core_a, cache[key]
**Bağlandığı işlevler:** pygame.Surface, range, int, math.exp, pygame.draw.circle, min, max
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: radius_px <= 0
2. Koşula göre yol seç: key in cache
3. Değeri/alanı oluştur veya güncelle: size = radius_px * 2 + 1
4. Değeri/alanı oluştur veya güncelle: surf = pygame.Surface((size, size), pygame.SRCALPHA)
5. Değeri/alanı oluştur veya güncelle: cx = cy = radius_px
6. Değeri/alanı oluştur veya güncelle: max_a = rgba[3]
7. Değeri/alanı oluştur veya güncelle: r_col, g_col, b_col, _ = rgba
8. Değeri/alanı oluştur veya güncelle: sigma = radius_px / 2.2
9. Koşula göre yol seç: sigma < 1
10. Her öğe için işle: r ← range(radius_px, 0, -FIELD_STEP_PX)
11. Değeri/alanı oluştur veya güncelle: core_a = min(255, max_a)
12. Yan etki/çağrı adımını çalıştır: pygame.draw.circle(surf, (r_col, g_col, b_col, core_a), (cx, cy), max(1, radius_px // 10))
13. Değeri/alanı oluştur veya güncelle: cache[key] = surf
14. Çağırana sonucu döndür: surf

**Gerçek kaynak:**

```python
def make_gauss_field_surface(cache: dict, key: tuple, radius_px: int, rgba: tuple[int, int, int, int]):
    if radius_px <= 0:
        return None
    if key in cache:
        return cache[key]

    size = radius_px * 2 + 1
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx = cy = radius_px

    max_a = rgba[3]
    r_col, g_col, b_col, _ = rgba

    sigma = radius_px / 2.2
    if sigma < 1:
        sigma = 1.0

    for r in range(radius_px, 0, -FIELD_STEP_PX):
        a = int(max_a * math.exp(- (r * r) / (2.0 * sigma * sigma)))
        if a <= 0:
            continue
        pygame.draw.circle(surf, (r_col, g_col, b_col, a), (cx, cy), r)

    core_a = min(255, max_a)
    pygame.draw.circle(surf, (r_col, g_col, b_col, core_a), (cx, cy), max(1, radius_px // 10))

    cache[key] = surf
    return surf
```

### draw_route_overlay — satır 827

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, cam: Camera, tile_px: float, route_points: list[tuple[int, int]], map_w: int, map_h: int, panel_x: int, line_color: tuple[int, int, int]=(220, 220, 230), point_color: tuple[int, int, int]=(240, 240, 240), start_color: tuple[int, int, int]=(80, 170, 255). self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** view_w, view_h, view_cx, view_cy, pts, (sx, sy)
**Bağlandığı işlevler:** world_to_screen, pts.append, len, pygame.draw.lines, enumerate, pygame.draw.circle
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: not route_points
2. Değeri/alanı oluştur veya güncelle: view_w = SCREEN_W - PANEL_W
3. Değeri/alanı oluştur veya güncelle: view_h = SCREEN_H
4. Değeri/alanı oluştur veya güncelle: view_cx = view_w / 2
5. Değeri/alanı oluştur veya güncelle: view_cy = view_h / 2
6. Yerel yardımcı tanımla: world_to_screen; ayrı sembol kaydı aşağıdadır.
7. Değeri/alanı oluştur veya güncelle: pts = []
8. Her öğe için işle: (tx, ty) ← route_points
9. Koşula göre yol seç: len(pts) >= 2
10. Her öğe için işle: (i, p) ← enumerate(pts)

**Gerçek kaynak:**

```python
def draw_route_overlay(screen, cam: Camera, tile_px: float, route_points: list[tuple[int, int]],
                       map_w: int, map_h: int, panel_x: int,
                       line_color: tuple[int, int, int] = (220, 220, 230),
                       point_color: tuple[int, int, int] = (240, 240, 240),
                       start_color: tuple[int, int, int] = (80, 170, 255)):
    if not route_points:
        return
    view_w = SCREEN_W - PANEL_W
    view_h = SCREEN_H
    view_cx = view_w / 2
    view_cy = view_h / 2

    def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))

    pts = []
    for (tx, ty) in route_points:
        sx, sy = world_to_screen(tx + 0.5, ty + 0.5)
        pts.append((sx, sy))

    if len(pts) >= 2:
        pygame.draw.lines(screen, line_color, False, pts, 2)

    for i, p in enumerate(pts):
        if i == 0:
            pygame.draw.circle(screen, start_color, p, 6)
            pygame.draw.circle(screen, (10, 10, 12), p, 6, 2)
        else:
            pygame.draw.circle(screen, point_color, p, 4)
```

### draw_route_overlay.world_to_screen — satır 839

Kamera merkezi, görünüm alanı ve zoom ile dünya noktasını piksele çevirir.

**Girdiler:** wx, wy. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (int(round(sx)), int(round(sy)))
**Atanan yerel değerler / durum alanları:** sx, sy
**Bağlandığı işlevler:** int, round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
2. Değeri/alanı oluştur veya güncelle: sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
3. Çağırana sonucu döndür: (int(round(sx)), int(round(sy)))

**Gerçek kaynak:**

```python
def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))
```

### draw_world — satır 860

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, cam: Camera, tile_px: float, show_grid: bool, entities: list[Entity], hover_tx, hover_ty, selected_entity_idx: int | None, map_w: int, map_h: int, icons: dict, icon_cache: dict, show_effect_global: bool, field_cache: dict, route_preview: list[tuple[int, int]] | None=None, route_preview_invalid: bool=False. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** view_w, view_h, view_cx, view_cy, tw, th, tiles_x, tiles_y, x0, x1, y0, y1, (sx, sy), rect, sp, radius_px, base_rgb, alpha, blob, (cx_s, cy_s), max_r, col, (hsx, hsy), r, icon_key, icon_src, scaled, up, pad, cs, slots_pos, slots_pos_1, slots_pos_2, slots_pos_3, carried, sensor_carried, source_carried, nsrc, (px, py), icon_key2, icon_src2, sc, c
**Bağlandığı işlevler:** max, int, clamp, range, world_to_screen, pygame.Rect, pygame.draw.rect, round, make_gauss_field_surface, screen.blit, blob.get_rect, draw_dashed_circle, draw_route_overlay, enumerate, icons.get, get_scaled_icon, min, find_entity_by_id, len, sc.get_rect
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: view_w = SCREEN_W - PANEL_W
2. Değeri/alanı oluştur veya güncelle: view_h = SCREEN_H
3. Değeri/alanı oluştur veya güncelle: view_cx = view_w / 2
4. Değeri/alanı oluştur veya güncelle: view_cy = view_h / 2
5. Yerel yardımcı tanımla: world_to_screen; ayrı sembol kaydı aşağıdadır.
6. Değeri/alanı oluştur veya güncelle: tw = max(1, int(tile_px * cam.zoom))
7. Değeri/alanı oluştur veya güncelle: th = max(1, int(tile_px * cam.zoom))
8. Değeri/alanı oluştur veya güncelle: tiles_x = int(view_w / (tile_px * cam.zoom)) + 4
9. Değeri/alanı oluştur veya güncelle: tiles_y = int(view_h / (tile_px * cam.zoom)) + 4
10. Değeri/alanı oluştur veya güncelle: x0 = clamp(int(cam.x) - tiles_x // 2, 0, map_w - 1)
11. Değeri/alanı oluştur veya güncelle: x1 = clamp(int(cam.x) + tiles_x // 2, 0, map_w - 1)
12. Değeri/alanı oluştur veya güncelle: y0 = clamp(int(cam.y) - tiles_y // 2, 0, map_h - 1)
13. Değeri/alanı oluştur veya güncelle: y1 = clamp(int(cam.y) + tiles_y // 2, 0, map_h - 1)
14. Her öğe için işle: ty ← range(y0, y1 + 1)
15. Koşula göre yol seç: show_effect_global
16. Koşula göre yol seç: route_preview
17. Koşula göre yol seç: hover_tx is not None and hover_ty is not None
18. Her öğe için işle: (i, e) ← enumerate(entities)

**Gerçek kaynak:**

```python
def draw_world(screen, cam: Camera, tile_px: float, show_grid: bool,
               entities: list[Entity], hover_tx, hover_ty, selected_entity_idx: int | None,
               map_w: int, map_h: int, icons: dict, icon_cache: dict,
               show_effect_global: bool, field_cache: dict,
               route_preview: list[tuple[int, int]] | None = None,
               route_preview_invalid: bool = False):

    view_w = SCREEN_W - PANEL_W
    view_h = SCREEN_H
    view_cx = view_w / 2
    view_cy = view_h / 2

    def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))

    tw = max(1, int(tile_px * cam.zoom))
    th = max(1, int(tile_px * cam.zoom))

    tiles_x = int(view_w / (tile_px * cam.zoom)) + 4
    tiles_y = int(view_h / (tile_px * cam.zoom)) + 4

    x0 = clamp(int(cam.x) - tiles_x // 2, 0, map_w - 1)
    x1 = clamp(int(cam.x) + tiles_x // 2, 0, map_w - 1)
    y0 = clamp(int(cam.y) - tiles_y // 2, 0, map_h - 1)
    y1 = clamp(int(cam.y) + tiles_y // 2, 0, map_h - 1)

    # Tiles + grid
    for ty in range(y0, y1 + 1):
        for tx in range(x0, x1 + 1):
            sx, sy = world_to_screen(tx, ty)
            rect = pygame.Rect(sx, sy, tw, th)

            pygame.draw.rect(screen, (24, 24, 28) if (tx + ty) % 2 == 0 else (22, 22, 26), rect)
            if show_grid:
                pygame.draw.rect(screen, (35, 35, 40), rect, 1)

    # Effects (behind entities)
    if show_effect_global:
        for e in entities:
            if not e.show_effect:
                continue
            if e.kind == Kind.SOURCE and e.source is not None:
                sp = e.source
                radius_px = int(round(sp.range_tiles * tile_px * cam.zoom))
                if radius_px <= 0:
                    continue

                base_rgb = (255, 170, 60) if sp.stype == SourceType.TEMP else (90, 220, 120)
                alpha = int(clamp(40 + sp.power * 16, 40, 220))

                blob = make_gauss_field_surface(
                    field_cache,
                    key=("blob", sp.stype.value, radius_px, alpha),
                    radius_px=radius_px,
                    rgba=(base_rgb[0], base_rgb[1], base_rgb[2], alpha),
                )
                if blob is None:
                    continue

                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)
                screen.blit(blob, blob.get_rect(center=(cx_s, cy_s)))

        for e in entities:
            if not e.show_effect:
                continue
            if e.kind == Kind.SENSOR and e.sensor is not None and e.sensor.active:
                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)
                max_r = max(1, int(e.sensor.range_tiles))
                for r_tiles in range(1, max_r + 1):
                    radius_px = int(round(r_tiles * tile_px * cam.zoom))
                    draw_dashed_circle(screen, (cx_s, cy_s), radius_px, (255, 255, 255, 90))

    # Route preview overlay
    if route_preview:
        col = (220, 60, 60) if route_preview_invalid else (220, 220, 230)
        draw_route_overlay(screen, cam, tile_px, route_preview, map_w, map_h, SCREEN_W - PANEL_W, line_color=col)

    # Hover highlight
    if hover_tx is not None and hover_ty is not None:
        hsx, hsy = world_to_screen(hover_tx, hover_ty)
        pygame.draw.rect(screen, (245, 245, 245), pygame.Rect(hsx, hsy, tw, th), 2)

    # Entities
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue  # carried items are drawn on UAV

        if not (0 <= e.tx < map_w and 0 <= e.ty < map_h):
            continue

        sx, sy = world_to_screen(e.tx, e.ty)
        r = pygame.Rect(sx, sy, tw, th)

        icon_key = None
        icon_src = None

        if e.kind == Kind.SENSOR:
            icon_key = "sensor"
            icon_src = icons.get("sensor")
        elif e.kind == Kind.OBSTACLE:
            icon_key = "obstacle"
            icon_src = icons.get("obstacle")
        elif e.kind == Kind.SOURCE and e.source:
            if e.source.stype == SourceType.TEMP:
                if e.icon_override == "burned":
                    icon_key = "burned"
                    icon_src = icons.get("burned")
                else:
                    icon_key = "source_temp"
                    icon_src = icons.get("source_temp")
            else:
                icon_key = "source_gas"
                icon_src = icons.get("source_gas")
        elif e.kind == Kind.UAV:
            icon_key = "drone"
            icon_src = icons.get("drone")

        scaled = get_scaled_icon(icon_cache, icon_key or "none", icon_src, (tw, th))

        if scaled is not None:
            screen.blit(scaled, (r.x, r.y))
        else:
            if e.kind == Kind.OBSTACLE:
                pygame.draw.rect(screen, (40, 90, 45), r)
            elif e.kind == Kind.SOURCE:
                pygame.draw.rect(
                    screen,
                    (150, 70, 70) if e.source and e.source.stype == SourceType.TEMP else (150, 120, 70),
                    r
                )
            elif e.kind == Kind.SENSOR:
                pygame.draw.rect(screen, (70, 70, 90) if e.sensor and not e.sensor.active else (60, 120, 170), r)
            elif e.kind == Kind.UAV:
                pygame.draw.rect(screen, (160, 160, 180), r)

        # Draw carried items on UAV
        if e.kind == Kind.UAV and e.uav:
            up = e.uav
            # anchor points relative to UAV rect
            pad = int(0.4 * min(tw, th))
            # small icon size
            cs = max(8, int(min(tw, th) * 0.45))
            # positions
            slots_pos = []
            # 1: top center
            slots_pos_1 = [(r.centerx, r.y + pad)]
            # 2: top-left & top-right
            slots_pos_2 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad)]
            # 3: top-left, top-right, bottom-center
            slots_pos_3 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad), (r.centerx, r.bottom - pad)]

            carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
            carried = [c for c in carried if c is not None]

            # If sensor carried, draw under UAV
            sensor_carried = [c for c in carried if c.kind == Kind.SENSOR]
            source_carried = [c for c in carried if c.kind == Kind.SOURCE]

            # Draw sources on top
            nsrc = len(source_carried)
            if nsrc == 1:
                slots_pos = slots_pos_1
            elif nsrc == 2:
                slots_pos = slots_pos_2
            elif nsrc >= 3:
                slots_pos = slots_pos_3

            for idx_s, c in enumerate(source_carried[:3]):
                px, py = slots_pos[idx_s]
                icon_key2 = ("burned" if c.icon_override == "burned" else ("source_temp" if c.source and c.source.stype == SourceType.TEMP else "source_gas"))
                icon_src2 = icons.get(icon_key2)
                sc = get_scaled_icon(icon_cache, f"carry_{icon_key2}", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(px, py)))

            # Draw sensor under UAV (center bottom)
            if sensor_carried:
                c = sensor_carried[0]
                icon_src2 = icons.get("sensor")
                sc = get_scaled_icon(icon_cache, "carry_sensor", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(r.centerx, r.bottom + cs // 3)))

        if selected_entity_idx == i:
            pygame.draw.rect(screen, (240, 240, 240), r, 2)
```

### draw_world.world_to_screen — satır 872

Kamera merkezi, görünüm alanı ve zoom ile dünya noktasını piksele çevirir.

**Girdiler:** wx, wy. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (int(round(sx)), int(round(sy)))
**Atanan yerel değerler / durum alanları:** sx, sy
**Bağlandığı işlevler:** int, round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
2. Değeri/alanı oluştur veya güncelle: sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
3. Çağırana sonucu döndür: (int(round(sx)), int(round(sy)))

**Gerçek kaynak:**

```python
def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))
```

### can_attach_to_uav — satır 1052

Taşıyıcı türü, yük türü, zaten taşınma ve kapasite kurallarını kontrol eder.

**Girdiler:** entities: list[Entity], uav: Entity, candidate: Entity. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; True; nsrc < 3
**Atanan yerel değerler / durum alanları:** up, carried, have_sensor, have_source, nsrc
**Bağlandığı işlevler:** find_entity_by_id, any, sum
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: uav.kind != Kind.UAV or uav.uav is None
2. Koşula göre yol seç: candidate.kind not in (Kind.SOURCE, Kind.SENSOR)
3. Koşula göre yol seç: candidate.carried_by is not None
4. Değeri/alanı oluştur veya güncelle: up = uav.uav
5. Değeri/alanı oluştur veya güncelle: carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
6. Değeri/alanı oluştur veya güncelle: carried = [c for c in carried if c is not None]
7. Değeri/alanı oluştur veya güncelle: have_sensor = any((c.kind == Kind.SENSOR for c in carried))
8. Değeri/alanı oluştur veya güncelle: have_source = any((c.kind == Kind.SOURCE for c in carried))
9. Koşula göre yol seç: candidate.kind == Kind.SENSOR
10. Koşula göre yol seç: have_sensor
11. Değeri/alanı oluştur veya güncelle: nsrc = sum((1 for c in carried if c.kind == Kind.SOURCE))
12. Çağırana sonucu döndür: nsrc < 3

**Gerçek kaynak:**

```python
def can_attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if uav.kind != Kind.UAV or uav.uav is None:
        return False
    if candidate.kind not in (Kind.SOURCE, Kind.SENSOR):
        return False
    if candidate.carried_by is not None:
        return False

    up = uav.uav
    carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
    carried = [c for c in carried if c is not None]

    have_sensor = any(c.kind == Kind.SENSOR for c in carried)
    have_source = any(c.kind == Kind.SOURCE for c in carried)

    if candidate.kind == Kind.SENSOR:
        # Must be empty OR already sensor? (only 1 sensor total)
        if have_source:
            return False
        if have_sensor:
            return False
        return True

    # candidate is SOURCE
    if have_sensor:
        return False
    # max 3 sources
    nsrc = sum(1 for c in carried if c.kind == Kind.SOURCE)
    return nsrc < 3
```

### attach_to_uav — satır 1083

Uygun yükü drone'a bağlar; kimlik listesi, taşıyıcı ve konumu birlikte günceller.

**Girdiler:** entities: list[Entity], uav: Entity, candidate: Entity. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; True
**Atanan yerel değerler / durum alanları:** up, candidate.carried_by, candidate.tx, candidate.ty
**Bağlandığı işlevler:** can_attach_to_uav, up.carrying_ids.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: not can_attach_to_uav(entities, uav, candidate)
2. Değeri/alanı oluştur veya güncelle: up = uav.uav
3. Koşula göre yol seç: up is None
4. Yan etki/çağrı adımını çalıştır: up.carrying_ids.append(candidate.id)
5. Değeri/alanı oluştur veya güncelle: candidate.carried_by = uav.id
6. Değeri/alanı oluştur veya güncelle: candidate.tx = uav.tx
7. Değeri/alanı oluştur veya güncelle: candidate.ty = uav.ty
8. Çağırana sonucu döndür: True

**Gerçek kaynak:**

```python
def attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if not can_attach_to_uav(entities, uav, candidate):
        return False
    up = uav.uav
    if up is None:
        return False
    up.carrying_ids.append(candidate.id)
    candidate.carried_by = uav.id
    candidate.tx = uav.tx
    candidate.ty = uav.ty
    return True
```

### main — satır 1099

Komut seçeneklerini/başlangıç nesnelerini kurup programın ana akışını başlatır.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** screen, clock, font, small, (MAP_W, MAP_H), tile_px, cam, cam.x, cam.y, show_grid, show_effect_global, entities, next_id, selected_tool, selected_entity_idx, uav_focus_cargo_id, collapsed_cargo_ids, sim_running, sim_time, tick_accum, spread_accum, left_down, left_down_pos, dragging_entity_idx, dragging_start, dragging_active, route_editing, route_edit_points, route_backup, route_edit_uav_id, route_preview_invalid, ui_msg_text, ui_msg_timer, icons, icon_cache, field_cache, panel_x, SCROLL_Y0, panel_scroll, last_selected_entity_id, running, dt, (mx, my), hover_tx, hover_ty, (wx, wy), ht, hy, (hover_tx, hover_ty), (tool_buttons, panel_clickables, global_rows, entity_rows, global_sw_rect, ent_sw_rect, selected_entity, panel_content_bottom), panel_clickables[idx], cur_sel_id, cargo_slots, dying, parent, dying.carried_by, ce, ce.carried_by, e, e.uav.route, e.uav.route_mode, e.uav.route_i, e.uav.route_dir, scroll_step, scroll_bottom_limit, max_scroll, mods, ctrl, shift, pan_tiles, idx, uav_ent, cand, clicked, rr, target_id, seg_rect, half, e.source.stype, (tx, ty), obstacles_set, idx_here, up, bp, preview, banner, msg, y_off, box_w, box, sim_label, (_, sw_rect, text, on), label, seg_rects_live, scroll_clip, prev_clip, rtype, (_, sw_rect, label_text, on), sw_r, (_, rect, label_text), (_, rect, label_text, _cid), (_, y, label_text, minus_rect, plus_rect, step_hint), ry, m2, p2, (_, rect, options, current), (_, y, t), slots, idx_txt, icon_key2, icon_src2, sc, letter, txt, d, stats, hint_lines, hint_y0
**Bağlandığı işlevler:** pygame.init, pygame.display.set_mode, pygame.display.set_caption, pygame.time.Clock, pygame.font.SysFont, Camera, cam.clamp_zoom_for_map, set, load_icon, os.path.join, clock.tick, pygame.mouse.get_pos, max, cam.screen_to_world, int, math.floor, update_uavs, simulate_tick, spread_fire, build_panel_layout, enumerate, len, pygame.event.get, route_edit_points.clear, find_entity_by_id, parent.uav.carrying_ids.remove, list, dying.uav.carrying_ids.clear, entities.pop, push_msg, min, pygame.key.get_mods, cam.zoom_at, icon_cache.clear, field_cache.clear, clamp, find_entity_at, any, r.move(0, -panel_scroll).collidepoint, r.move, attach_to_uav, r.collidepoint, rr.collidepoint, callable, action, isinstance, seg_rect.move, seg_rect.collidepoint, route_edit_points.append, route_is_valid, entities.append, Entity, SensorProps, SourceProps, UavProps, float, abs, screen.fill, draw_world, pygame.Surface, banner.fill, screen.blit, small.render, box.fill, pygame.draw.rect, pygame.draw.line, font.render, draw_button, draw_section_title, draw_switch, pygame.Rect, screen.get_clip, screen.set_clip, sw_rect.move, rect.move, draw_small_btn, minus_rect.move, plus_rect.move, str, draw_segmented, slots.append, icons.get, get_scaled_icon, sc.get_rect, txt.get_rect, pygame.draw.circle, pygame.display.flip, pygame.quit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.init()
2. Değeri/alanı oluştur veya güncelle: screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
3. Yan etki/çağrı adımını çalıştır: pygame.display.set_caption('IoT Grid Sim (NO ROTATE)')
4. Değeri/alanı oluştur veya güncelle: clock = pygame.time.Clock()
5. Değeri/alanı oluştur veya güncelle: font = pygame.font.SysFont('DejaVu Sans', 18)
6. Değeri/alanı oluştur veya güncelle: small = pygame.font.SysFont('DejaVu Sans', 14)
7. Değeri/alanı oluştur veya güncelle: MAP_W, MAP_H = (200, 200)
8. Değeri/alanı oluştur veya güncelle: tile_px = DEFAULT_TILE
9. Değeri/alanı oluştur veya güncelle: cam = Camera()
10. Yan etki/çağrı adımını çalıştır: cam.clamp_zoom_for_map(tile_px, MAP_W, MAP_H)
11. Değeri/alanı oluştur veya güncelle: cam.x = (MAP_W - 1) / 2
12. Değeri/alanı oluştur veya güncelle: cam.y = (MAP_H - 1) / 2
13. Değeri/alanı oluştur veya güncelle: show_grid = True
14. Değeri/alanı oluştur veya güncelle: show_effect_global = True
15. Değeri/alanı oluştur veya güncelle: entities: list[Entity] = []
16. Değeri/alanı oluştur veya güncelle: next_id = 1
17. Değeri/alanı oluştur veya güncelle: selected_tool: Kind | None = None
18. Değeri/alanı oluştur veya güncelle: selected_entity_idx: int | None = None
19. Değeri/alanı oluştur veya güncelle: uav_focus_cargo_id: int | None = None
20. Değeri/alanı oluştur veya güncelle: collapsed_cargo_ids: set[int] = set()
21. Değeri/alanı oluştur veya güncelle: sim_running = False
22. Değeri/alanı oluştur veya güncelle: sim_time = 0.0
23. Değeri/alanı oluştur veya güncelle: tick_accum = 0.0
24. Değeri/alanı oluştur veya güncelle: spread_accum = 0.0
25. Değeri/alanı oluştur veya güncelle: left_down = False
26. Değeri/alanı oluştur veya güncelle: left_down_pos = (0, 0)
27. Değeri/alanı oluştur veya güncelle: dragging_entity_idx: int | None = None
28. Değeri/alanı oluştur veya güncelle: dragging_start = (0, 0)
29. Değeri/alanı oluştur veya güncelle: dragging_active = False
30. Değeri/alanı oluştur veya güncelle: route_editing = False
31. Değeri/alanı oluştur veya güncelle: route_edit_points: list[tuple[int, int]] = []
32. Değeri/alanı oluştur veya güncelle: route_backup: list[tuple[int, int]] = []
33. Değeri/alanı oluştur veya güncelle: route_edit_uav_id: int | None = None
34. Değeri/alanı oluştur veya güncelle: route_preview_invalid = False
35. Değeri/alanı oluştur veya güncelle: ui_msg_text = ''
36. Değeri/alanı oluştur veya güncelle: ui_msg_timer = 0.0
37. Değeri/alanı oluştur veya güncelle: icons = {'sensor': load_icon(os.path.join('assets', 'sensor.png')), 'source_temp': load_icon(os.path.join('assets', 'source_temp.png')), 'source_gas': load_icon(os.path.join('assets', 'source_gas.png')), 'obstacle': load…
38. Değeri/alanı oluştur veya güncelle: icon_cache: dict = {}
39. Değeri/alanı oluştur veya güncelle: field_cache: dict = {}
40. Değeri/alanı oluştur veya güncelle: panel_x = SCREEN_W - PANEL_W
41. Değeri/alanı oluştur veya güncelle: SCROLL_Y0 = PANEL_SCROLL_Y0
42. Değeri/alanı oluştur veya güncelle: panel_scroll = 0
43. Değeri/alanı oluştur veya güncelle: last_selected_entity_id = None
44. Yerel yardımcı tanımla: push_msg; ayrı sembol kaydı aşağıdadır.
45. Değeri/alanı oluştur veya güncelle: running = True
46. Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: running
47. Yan etki/çağrı adımını çalıştır: pygame.quit()

**Gerçek kaynak:**

```python
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("IoT Grid Sim (NO ROTATE)")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("DejaVu Sans", 18)
    small = pygame.font.SysFont("DejaVu Sans", 14)

    MAP_W, MAP_H = 200, 200
    tile_px = DEFAULT_TILE

    cam = Camera()
    cam.clamp_zoom_for_map(tile_px, MAP_W, MAP_H)
    cam.x = (MAP_W - 1) / 2
    cam.y = (MAP_H - 1) / 2

    show_grid = True
    show_effect_global = True

    entities: list[Entity] = []
    next_id = 1

    selected_tool: Kind | None = None
    selected_entity_idx: int | None = None

    # Panel: when UAV selected, you can click a carried item to show its details below UAV properties
    uav_focus_cargo_id: int | None = None
    collapsed_cargo_ids: set[int] = set()

    sim_running = False
    sim_time = 0.0
    tick_accum = 0.0
    spread_accum = 0.0

    # Left mouse state (click / drag)
    left_down = False
    left_down_pos = (0, 0)

    # Drag state (entity -> panel slots)
    dragging_entity_idx: int | None = None
    dragging_start = (0, 0)
    dragging_active = False

    # Route edit
    route_editing = False
    route_edit_points: list[tuple[int, int]] = []
    route_backup: list[tuple[int, int]] = []
    route_edit_uav_id: int | None = None
    route_preview_invalid = False

    ui_msg_text = ""
    ui_msg_timer = 0.0

    # Assets (optional)
    icons = {
        "sensor": load_icon(os.path.join("assets", "sensor.png")),
        "source_temp": load_icon(os.path.join("assets", "source_temp.png")),
        "source_gas": load_icon(os.path.join("assets", "source_gas.png")),
        "obstacle": load_icon(os.path.join("assets", "obstacle.png")),
        "burned": load_icon(os.path.join("assets", "burned.png")),
        "drone": load_icon(os.path.join("assets", "drone.png")),  # <= senin istediğin
    }
    icon_cache: dict = {}
    field_cache: dict = {}

    panel_x = SCREEN_W - PANEL_W
    SCROLL_Y0 = PANEL_SCROLL_Y0

    panel_scroll = 0
    last_selected_entity_id = None

    def push_msg(text: str, secs: float = 2.0):
        nonlocal ui_msg_text, ui_msg_timer
        ui_msg_text = text
        ui_msg_timer = secs

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        mx, my = pygame.mouse.get_pos()

        if ui_msg_timer > 0.0:
            ui_msg_timer = max(0.0, ui_msg_timer - dt)

        # Hover tile
        hover_tx = None
        hover_ty = None
        if mx < panel_x:
            wx, wy = cam.screen_to_world((mx, my), tile_px)
            ht = int(math.floor(wx + 1e-6))
            hy = int(math.floor(wy + 1e-6))
            if 0 <= ht < MAP_W and 0 <= hy < MAP_H:
                hover_tx, hover_ty = ht, hy

        # Per-frame UAV motion (only when sim is running)
        if sim_running:
            update_uavs(entities, dt, MAP_W, MAP_H)

        # Simulation tick
        if sim_running:
            tick_accum += dt
            while tick_accum >= TICK_SECONDS:
                tick_accum -= TICK_SECONDS
                sim_time += TICK_SECONDS
                simulate_tick(entities, TICK_SECONDS)
                spread_accum += TICK_SECONDS
                while spread_accum >= 2.0:
                    spread_accum -= 2.0
                    spread_fire(entities)

        tool_buttons, panel_clickables, global_rows, entity_rows, global_sw_rect, ent_sw_rect, selected_entity, panel_content_bottom = build_panel_layout(
            entities, selected_tool, selected_entity_idx, panel_x, small, font, show_effect_global, uav_focus_cargo_id, collapsed_cargo_ids
        )

        # Wire global switch callback
        for idx, (r, action) in enumerate(panel_clickables):
            if r == global_sw_rect:
                def _toggle_global():
                    nonlocal show_effect_global
                    show_effect_global = not show_effect_global
                panel_clickables[idx] = (r, _toggle_global)
                break

        # Reset panel scroll / UAV cargo focus when selection changes
        cur_sel_id = entities[selected_entity_idx].id if (selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities)) else None
        if cur_sel_id != last_selected_entity_id:
            panel_scroll = 0
            uav_focus_cargo_id = None
            last_selected_entity_id = cur_sel_id
        # Identify cargo slot rects for drop detection
        cargo_slots: list[pygame.Rect] = []
        for row in entity_rows:
            if row[0] == "cargo_slots":
                cargo_slots = row[1]
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    show_grid = not show_grid
                elif event.key == pygame.K_SPACE:
                    sim_running = not sim_running
                elif event.key == pygame.K_ESCAPE:
                    selected_tool = None
                    selected_entity_idx = None
                    route_editing = False
                    route_preview_invalid = False
                    route_edit_points.clear()
                    route_backup = []
                    route_edit_uav_id = None
                elif event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        # detach cargo if deleting UAV
                        dying = entities[selected_entity_idx]
                        # If deleting a carried entity, unlink it from the UAV cargo list
                        if dying.carried_by is not None:
                            parent = find_entity_by_id(entities, dying.carried_by)
                            if parent and parent.kind == Kind.UAV and parent.uav:
                                if dying.id in parent.uav.carrying_ids:
                                    parent.uav.carrying_ids.remove(dying.id)
                            dying.carried_by = None

                        if dying.kind == Kind.UAV and dying.uav:
                            for cid in list(dying.uav.carrying_ids):
                                ce = find_entity_by_id(entities, cid)
                                if ce:
                                    ce.carried_by = None
                            dying.uav.carrying_ids.clear()
                        entities.pop(selected_entity_idx)
                        selected_entity_idx = None
                elif event.key == pygame.K_k:
                    # UAV route edit toggle (only when UAV selected)
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        e = entities[selected_entity_idx]
                        if e.kind == Kind.UAV and e.uav is not None:
                            if not route_editing:
                                # Enter edit mode: start collecting waypoints
                                route_editing = True
                                route_edit_points = []
                                route_preview_invalid = False
                                route_backup = list(e.uav.route)
                                route_edit_uav_id = e.id
                            else:
                                # Exit edit mode:
                                # - If user provided <2 points, treat as cancel (keep old route)
                                # - Otherwise finalize new route for the same UAV
                                if route_edit_uav_id == e.id and len(route_edit_points) >= 2 and (not route_preview_invalid):
                                    e.uav.route = list(route_edit_points)
                                    if e.uav.route and e.uav.route[0] == e.uav.route[-1]:
                                        e.uav.route_mode = RouteMode.LOOP
                                    else:
                                        e.uav.route_mode = RouteMode.PINGPONG
                                    e.uav.route_i = 0
                                    e.uav.route_dir = 1
                                else:
                                    e.uav.route = list(route_backup)
                                    if route_edit_uav_id == e.id and len(route_edit_points) >= 2 and route_preview_invalid:
                                        push_msg("Rota engelin üzerinden geçiyor. Tekrar dene.")

                                route_editing = False
                                route_preview_invalid = False
                                route_edit_points = []
                                route_backup = []
                                route_edit_uav_id = None
                        else:
                            # If somehow K is pressed while editing but UAV not selected, just cancel edit mode.
                            if route_editing:
                                route_editing = False
                                route_preview_invalid = False
                                route_edit_points = []
                                route_backup = []
                                route_edit_uav_id = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Wheel: zoom on world, scroll on panel (when an entity is selected)
                if event.button in (4, 5):
                    # Panel scroll (only when an entity is selected)
                    if mx >= panel_x and selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        scroll_step = 40
                        if event.button == 4:
                            panel_scroll = max(0, panel_scroll - scroll_step)
                        else:
                            scroll_bottom_limit = SCREEN_H - 20
                            max_scroll = max(0, panel_content_bottom - scroll_bottom_limit)
                            panel_scroll = min(max_scroll, panel_scroll + scroll_step)
                    else:
                        mods = pygame.key.get_mods()
                        ctrl = (mods & pygame.KMOD_CTRL) != 0
                        shift = (mods & pygame.KMOD_SHIFT) != 0

                        if ctrl:
                            # Ctrl + Wheel => zoom
                            if event.button == 4:
                                cam.zoom_at(1.12, tile_px, MAP_W, MAP_H)
                            else:
                                cam.zoom_at(1 / 1.12, tile_px, MAP_W, MAP_H)
                            icon_cache.clear()
                            field_cache.clear()
                        else:
                            # Wheel => move map (Shift => horizontal)
                            pan_tiles = 6.0 / max(0.2, cam.zoom)
                            if shift:
                                cam.x += (-pan_tiles if event.button == 4 else pan_tiles)
                            else:
                                cam.y += (-pan_tiles if event.button == 4 else pan_tiles)

                            cam.x = clamp(cam.x, 0.0, MAP_W - 1.0)
                            cam.y = clamp(cam.y, 0.0, MAP_H - 1.0)

                # Left press: start possible drag
                elif event.button == 1:
                    left_down = True
                    left_down_pos = (mx, my)

                    # potential entity drag start (only on map)
                    if mx < panel_x and hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        dragging_entity_idx = idx
                        dragging_start = (mx, my)
                        dragging_active = False

                # Right click: delete entity on hovered tile
                elif event.button == 3 and mx < panel_x:
                    if hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        if idx is not None:
                            entities.pop(idx)
                            if selected_entity_idx == idx:
                                selected_entity_idx = None
                            elif selected_entity_idx is not None and selected_entity_idx > idx:
                                selected_entity_idx -= 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if left_down:
                        # If dragging entity to panel
                        if dragging_entity_idx is not None and dragging_active:
                            if mx >= panel_x and cargo_slots and selected_entity_idx is not None:
                                uav_ent = entities[selected_entity_idx]
                                cand = entities[dragging_entity_idx]
                                # drop into any slot rect
                                if any(r.move(0, -panel_scroll).collidepoint(mx, my) for r in cargo_slots):
                                    if uav_ent.kind == Kind.UAV:
                                        attach_to_uav(entities, uav_ent, cand)

                        else:
                            if mx >= panel_x:
                                # Panel click
                                clicked = False

                                for k, r, _ in tool_buttons:
                                    if r.collidepoint(mx, my):
                                        selected_tool = k
                                        selected_entity_idx = None
                                        uav_focus_cargo_id = None
                                        panel_scroll = 0
                                        clicked = True
                                        break
                                if clicked:
                                    left_down = False
                                    dragging_entity_idx = None
                                    dragging_active = False
                                    continue

                                # Panel element clicks (with scroll offset for entity section)
                                for r, action in panel_clickables:
                                    rr = r
                                    if selected_entity_idx is not None and rr.y >= SCROLL_Y0:
                                        rr = r.move(0, -panel_scroll)

                                    if rr.collidepoint(mx, my):
                                        if callable(action):
                                            action()
                                        elif isinstance(action, tuple) and len(action) >= 2:
                                            if action[0] == "select_entity_id":
                                                target_id = action[1]
                                                for ii, ee in enumerate(entities):
                                                    if ee.id == target_id:
                                                        selected_entity_idx = ii
                                                        selected_tool = None
                                                        break
                                            elif action[0] == "uav_focus_cargo":
                                                uav_focus_cargo_id = action[1]
                                        clicked = True
                                        break

                                # Source segmented clicks (handled here)
                                if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                    e = entities[selected_entity_idx]
                                    if e.kind == Kind.SOURCE and e.source:
                                        for row in entity_rows:
                                            if row[0] == "segmented":
                                                seg_rect = row[1]
                                                if selected_entity_idx is not None and seg_rect.y >= SCROLL_Y0:
                                                    seg_rect = seg_rect.move(0, -panel_scroll)
                                                if seg_rect.collidepoint(mx, my):
                                                    # determine segment
                                                    half = seg_rect.width // 2
                                                    if mx < seg_rect.x + half:
                                                        e.source.stype = SourceType.TEMP
                                                    else:
                                                        e.source.stype = SourceType.GAS
                                                    clicked = True
                                                break
                            else:
                                # Map click: place/select or route edit point
                                if hover_tx is not None:
                                    tx, ty = hover_tx, hover_ty

                                    if route_editing:
                                        # add waypoint (avoid obstacles)
                                        obstacles_set = {(o.tx, o.ty) for o in entities if o.kind == Kind.OBSTACLE and o.carried_by is None}
                                        if (tx, ty) in obstacles_set:
                                            push_msg("Engelin üstüne waypoint koyamazsın. Tekrar dene.")
                                        else:
                                            route_edit_points.append((tx, ty))
                                            route_preview_invalid = (not route_is_valid(route_edit_points, obstacles_set))
                                            if route_preview_invalid:
                                                push_msg("Rota engelin üzerinden geçiyor. Tekrar dene.")
                                    else:
                                        if selected_tool is not None:
                                            # If you click an existing entity while a tool is selected, just select it.
                                            idx_here = find_entity_at(entities, tx, ty)
                                            if idx_here is not None:
                                                selected_entity_idx = idx_here
                                            else:
                                                if selected_tool == Kind.SENSOR:
                                                    entities.append(Entity(id=next_id, kind=Kind.SENSOR, tx=tx, ty=ty, sensor=SensorProps()))
                                                    next_id += 1
                                                elif selected_tool == Kind.SOURCE:
                                                    entities.append(Entity(id=next_id, kind=Kind.SOURCE, tx=tx, ty=ty, source=SourceProps()))
                                                    next_id += 1
                                                elif selected_tool == Kind.OBSTACLE:
                                                    entities.append(Entity(id=next_id, kind=Kind.OBSTACLE, tx=tx, ty=ty))
                                                    next_id += 1
                                                elif selected_tool == Kind.UAV:
                                                    up = UavProps(speed=3.0, x=float(tx), y=float(ty))
                                                    entities.append(Entity(id=next_id, kind=Kind.UAV, tx=tx, ty=ty, uav=up))
                                                    next_id += 1
                                                elif selected_tool == Kind.BURNED:
                                                    bp = SourceProps(stype=SourceType.TEMP, power=3, range_tiles=3)
                                                    entities.append(Entity(id=next_id, kind=Kind.BURNED, tx=tx, ty=ty, source=bp, icon_override='burned'))
                                                    next_id += 1

                                        else:
                                            selected_entity_idx = find_entity_at(entities, tx, ty)

                    left_down = False
                    dragging_entity_idx = None
                    dragging_active = False

            elif event.type == pygame.MOUSEMOTION:
                if left_down:
                    # Detect entity drag (only for UAV cargo)
                    if dragging_entity_idx is not None and not dragging_active:
                        if abs(mx - dragging_start[0]) >= DRAG_THRESHOLD_PX or abs(my - dragging_start[1]) >= DRAG_THRESHOLD_PX:
                            # Start drag ONLY if selected is UAV and candidate is draggable
                            if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                uav_ent = entities[selected_entity_idx]
                                cand = entities[dragging_entity_idx]
                                if uav_ent.kind == Kind.UAV and cand.kind in (Kind.SOURCE, Kind.SENSOR) and cand.carried_by is None:
                                    dragging_active = True

        # =============================
        # DRAW
        # =============================
        screen.fill((18, 18, 22))

        # Route preview points (editing) or show selected UAV route (optional)
        preview = route_edit_points if route_editing else None

        draw_world(
            screen, cam, tile_px, show_grid,
            entities, hover_tx, hover_ty, selected_entity_idx,
            MAP_W, MAP_H, icons, icon_cache,
            show_effect_global, field_cache,
            route_preview=preview,
            route_preview_invalid=route_preview_invalid
        )

        # Route edit banner (top-left of world view)
        if route_editing:
            banner = pygame.Surface((SCREEN_W - PANEL_W, 34), pygame.SRCALPHA)
            banner.fill((0, 0, 0, 120))
            screen.blit(banner, (0, 0))
            msg = "ROTA DÜZENLEME MODU: Haritaya tıkla waypoint ekle | K: Bitir/İptal"
            screen.blit(small.render(msg, True, (245, 245, 245)), (12, 9))

        # Toast / warning message (top-left)
        if ui_msg_timer > 0.0 and ui_msg_text:
            y_off = 38 if route_editing else 8
            box_w = min(720, SCREEN_W - PANEL_W - 24)
            box = pygame.Surface((box_w, 30), pygame.SRCALPHA)
            box.fill((0, 0, 0, 160))
            screen.blit(box, (12, y_off))
            screen.blit(small.render(ui_msg_text, True, (245, 245, 245)), (20, y_off + 8))

        # Panel background
        pygame.draw.rect(screen, (14, 14, 16), (panel_x, 0, PANEL_W, SCREEN_H))
        pygame.draw.line(screen, (60, 60, 70), (panel_x, 0), (panel_x, SCREEN_H), 2)

        # Tools
        screen.blit(font.render("Araçlar", True, (240, 240, 240)), (panel_x + PAD, 25))
        for k, r, label in tool_buttons:
            draw_button(screen, r, label, font, active=(selected_tool == k))

        # Sim status
        sim_label = "RUNNING" if sim_running else "PAUSED"
        screen.blit(small.render(f"Sim: {sim_label}  (Space)", True, (220, 220, 220)), (panel_x + PAD, 320))
        screen.blit(small.render(f"Zaman: {sim_time:.0f}s", True, (200, 200, 200)), (panel_x + PAD, 340))

                # Appearance section (global)
        draw_section_title(screen, panel_x + PAD, PANEL_Y_APPEAR, "Görünüm", font, small)
        for row in global_rows:
            if row[0] == "switch":
                _, sw_rect, text, on = row
                draw_switch(screen, sw_rect, on)
                screen.blit(small.render(text, True, (200, 200, 200)), (sw_rect.right + 10, sw_rect.y + 4))

        # Selected section
        draw_section_title(screen, panel_x + PAD, PANEL_Y_SELECTED_TITLE, "Seçili", font, small)

        if selected_entity_idx is None or not (0 <= selected_entity_idx < len(entities)):
            screen.blit(small.render("Yok (haritadan bir entity seç)", True, (180, 180, 180)),
                        (panel_x + PAD, PANEL_Y_SELECTED_LABEL))
        else:
            e = entities[selected_entity_idx]
            label = f"{e.kind.value} @ ({e.tx},{e.ty})"
            if e.carried_by is not None:
                label += f"  [İHA #{e.carried_by} üzerinde]"
            screen.blit(small.render(label, True, (210, 210, 210)), (panel_x + PAD, PANEL_Y_SELECTED_LABEL))

            # Entity rows (scrollable)
            seg_rects_live = None

            scroll_clip = pygame.Rect(panel_x, SCROLL_Y0, PANEL_W, SCREEN_H - SCROLL_Y0)
            prev_clip = screen.get_clip()
            screen.set_clip(scroll_clip)

            for row in entity_rows:
                rtype = row[0]

                if rtype == "switch":
                    _, sw_rect, label_text, on = row
                    sw_r = sw_rect.move(0, -panel_scroll) if sw_rect.y >= SCROLL_Y0 else sw_rect
                    draw_switch(screen, sw_r, on)
                    screen.blit(small.render(label_text, True, (200, 200, 200)), (sw_r.right + 10, sw_r.y + 4))

                elif rtype == "mode_switch":
                    _, sw_rect, label_text, on = row
                    sw_r = sw_rect.move(0, -panel_scroll) if sw_rect.y >= SCROLL_Y0 else sw_rect
                    draw_switch(screen, sw_r, on)
                    screen.blit(small.render(label_text, True, (200, 200, 200)), (sw_r.right + 10, sw_r.y + 4))

                elif rtype == "button":
                    _, rect, label_text = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "carry_edit_btn":
                    _, rect, label_text, _cid = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "cargo_toggle":
                    _, rect, label_text = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "numeric":
                    # ("numeric", y, "Label: value", minus_rect, plus_rect, step_hint)
                    _, y, label_text, minus_rect, plus_rect, step_hint = row
                    ry = y - panel_scroll if y >= SCROLL_Y0 else y
                    m2 = minus_rect.move(0, -panel_scroll) if minus_rect.y >= SCROLL_Y0 else minus_rect
                    p2 = plus_rect.move(0, -panel_scroll) if plus_rect.y >= SCROLL_Y0 else plus_rect

                    screen.blit(small.render(label_text, True, (210, 210, 210)), (panel_x + PAD, ry))
                    draw_small_btn(screen, m2, "-", small)
                    draw_small_btn(screen, p2, "+", small)
                    if step_hint:
                        screen.blit(small.render(str(step_hint), True, (170, 170, 170)), (p2.right + 8, p2.y + 6))

                elif rtype == "segmented":
                    # ("segmented", rect, options, selected_idx)
                    _, rect, options, current = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_segmented(screen, rr, options, current, small)

                elif rtype == "text":
                    _, y, t = row
                    ry = y - panel_scroll if y >= SCROLL_Y0 else y
                    screen.blit(small.render(t, True, (180, 180, 180)), (panel_x + PAD, ry))

                elif rtype == "cargo_slots":
                    # ("cargo_slots", [rect, rect, rect])
                    slots = []
                    for r in row[1]:
                        slots.append(r.move(0, -panel_scroll) if r.y >= SCROLL_Y0 else r)

                    for i_slot, r in enumerate(slots):
                        pygame.draw.rect(screen, (55, 55, 55), r, border_radius=8)
                        pygame.draw.rect(screen, (90, 90, 90), r, width=2, border_radius=8)
                        idx_txt = small.render(str(i_slot + 1), True, (120, 120, 120))
                        screen.blit(idx_txt, (r.x + 6, r.y + 6))

                    uav_ent = entities[selected_entity_idx]
                    if uav_ent.uav:
                        for i_slot, cid in enumerate(uav_ent.uav.carrying_ids[:3]):
                            if i_slot >= len(slots):
                                break
                            ce = find_entity_by_id(entities, cid)
                            if ce is None:
                                continue

                            icon_key2 = None
                            if ce.kind == Kind.SENSOR:
                                icon_key2 = "sensor"
                            elif ce.kind == Kind.SOURCE and ce.source:
                                if ce.icon_override == "burned":
                                    icon_key2 = "burned"
                                else:
                                    icon_key2 = "source_temp" if ce.source.stype == SourceType.TEMP else "source_gas"

                            icon_src2 = icons.get(icon_key2) if icon_key2 else None
                            sc = get_scaled_icon(icon_cache, f"panel_{icon_key2}", icon_src2, (26, 26))

                            if sc is not None:
                                screen.blit(sc, sc.get_rect(center=slots[i_slot].center))
                            else:
                                letter = "S" if ce.kind == Kind.SENSOR else ("T" if (ce.source and ce.source.stype == SourceType.TEMP) else "G")
                                txt = small.render(letter, True, (235, 235, 235))
                                screen.blit(txt, txt.get_rect(center=slots[i_slot].center))

            screen.set_clip(prev_clip)


        # Drag ghost
        if dragging_entity_idx is not None and dragging_active:
            d = entities[dragging_entity_idx]
            # simple ghost circle
            pygame.draw.circle(screen, (240, 240, 240), (mx, my), 10, 2)

        # Footer
        stats = f"Map: {MAP_W}x{MAP_H} | Zoom: {cam.zoom:.2f} | Entities: {len(entities)}"
        screen.blit(small.render(stats, True, (180, 180, 180)), (20, SCREEN_H - 26))

        hint_lines = [
            "Sol tık: Seç / (Araç seçiliyken) Ekle | Sağ tık: Sil | DEL/BKSP: Seçiliyi sil",
            "Wheel: Haritayı kaydır | Shift+Wheel: Yatay | Ctrl+Wheel: Zoom",
            "G: Izgara | Space: Sim (RUN/PAUSE)",
            "İHA seçiliyken: K rota edit (tıkla waypoint ekle, K ile bitir)",
            "Kaynak/Sensör: Haritadan sürükle -> İHA panelindeki slotlara bırak",
        ]
        hint_y0 = SCREEN_H - 26 - 8 - 18 * len(hint_lines)
        for i, line in enumerate(hint_lines):
            screen.blit(small.render(line, True, (170, 170, 170)), (20, hint_y0 + 18 * i))

        pygame.display.flip()

    pygame.quit()
```

### main.push_msg — satır 1171

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** text: str, secs: float=2.0. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** ui_msg_text, ui_msg_timer
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: ui_msg_text = text
2. Değeri/alanı oluştur veya güncelle: ui_msg_timer = secs

**Gerçek kaynak:**

```python
def push_msg(text: str, secs: float = 2.0):
        nonlocal ui_msg_text, ui_msg_timer
        ui_msg_text = text
        ui_msg_timer = secs
```

### main._toggle_global — satır 1217

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** show_effect_global
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: show_effect_global = not show_effect_global

**Gerçek kaynak:**

```python
def _toggle_global():
                    nonlocal show_effect_global
                    show_effect_global = not show_effect_global
```


## IoT PyGame/iot_sim/main.py

Korunan eski tek dosyalı simülasyon/yedek. Yeni giriş noktası bu kodu çalıştırmaz; güncel davranış testleri buna uygulanmaz.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: import math

```python
import math
```

Satır 2: Gereken isimleri içeri al: import os

```python
import os
```

Satır 3: Gereken isimleri içeri al: import random

```python
import random
```

Satır 4: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 5: Gereken isimleri içeri al: from dataclasses import dataclass, field

```python
from dataclasses import dataclass, field
```

Satır 6: Gereken isimleri içeri al: from enum import Enum

```python
from enum import Enum
```

Satır 11: Değeri/alanı oluştur veya güncelle: SCREEN_W, SCREEN_H = (1200, 800)

```python
SCREEN_W, SCREEN_H = 1200, 800
```

Satır 12: Değeri/alanı oluştur veya güncelle: PANEL_W = 320

```python
PANEL_W = 320
```

Satır 13: Değeri/alanı oluştur veya güncelle: FPS = 60

```python
FPS = 60
```

Satır 15: Değeri/alanı oluştur veya güncelle: DEFAULT_TILE = 16

```python
DEFAULT_TILE = 16
```

Satır 16: Değeri/alanı oluştur veya güncelle: MAX_ZOOM = 4.0

```python
MAX_ZOOM = 4.0
```

Satır 17: Değeri/alanı oluştur veya güncelle: MIN_ZOOM_FLOOR = 0.15

```python
MIN_ZOOM_FLOOR = 0.15
```

Satır 19: Değeri/alanı oluştur veya güncelle: TICK_SECONDS = 1.0

```python
TICK_SECONDS = 1.0
```

Satır 22: Değeri/alanı oluştur veya güncelle: ACCURACY_BY_DIST = [100, 99, 96, 90, 82, 70, 55]

```python
ACCURACY_BY_DIST = [100, 99, 96, 90, 82, 70, 55]
```

Satır 25: Değeri/alanı oluştur veya güncelle: PAN_SPEED = 1.0

```python
PAN_SPEED = 1.0
```

Satır 26: Değeri/alanı oluştur veya güncelle: PAN_DRAG_THRESHOLD_PX = 4

```python
PAN_DRAG_THRESHOLD_PX = 4
```

Satır 29: Değeri/alanı oluştur veya güncelle: FIELD_STEP_PX = 6

```python
FIELD_STEP_PX = 6
```

Satır 32: Değeri/alanı oluştur veya güncelle: PAD = 20

```python
PAD = 20
```

Satır 33: Değeri/alanı oluştur veya güncelle: SECTION_GAP = 18

```python
SECTION_GAP = 18
```

Satır 36: Değeri/alanı oluştur veya güncelle: PANEL_Y_APPEAR = 370

```python
PANEL_Y_APPEAR = 370
```

Satır 37: Değeri/alanı oluştur veya güncelle: PANEL_Y_GLOBAL_SWITCH = 406

```python
PANEL_Y_GLOBAL_SWITCH = 406
```

Satır 38: Değeri/alanı oluştur veya güncelle: PANEL_Y_SELECTED_TITLE = 450

```python
PANEL_Y_SELECTED_TITLE = 450
```

Satır 39: Değeri/alanı oluştur veya güncelle: PANEL_Y_SELECTED_LABEL = 490

```python
PANEL_Y_SELECTED_LABEL = 490
```

Satır 40: Değeri/alanı oluştur veya güncelle: PANEL_SCROLL_Y0 = 520

```python
PANEL_SCROLL_Y0 = 520
```

Satır 43: Değeri/alanı oluştur veya güncelle: DRAG_THRESHOLD_PX = 6

```python
DRAG_THRESHOLD_PX = 6
```

Satır 1729: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__ == "__main__":
    main()
```

### Kind — satır 48

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
SENSOR = "SENSOR"
SOURCE = "SOURCE"
OBSTACLE = "OBSTACLE"
BURNED = "BURNED"
UAV = "UAV"
```

### SourceType — satır 56

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
TEMP = "TEMP"
GAS = "GAS"
```

### RouteMode — satır 61

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
LOOP = "LOOP"
PINGPONG = "PINGPONG"
```

### SensorProps — satır 67

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
range_tiles: int = 6
efficiency: int = 80
battery: float = 5000.0
active: bool = True
last_temp: float = 0.0
last_gas: float = 0.0
```

### SourceProps — satır 77

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
stype: SourceType = SourceType.TEMP
power: int = 5
range_tiles: int = 8
```

### UavProps — satır 84

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
speed: float = 3.0
route: list[tuple[int, int]] = field(default_factory=list)
route_mode: RouteMode = RouteMode.LOOP
route_dir: int = 1
route_i: int = 0
x: float = 0.0
y: float = 0.0
carrying_ids: list[int] = field(default_factory=list)
show_route: bool = True
```

### Entity — satır 97

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
id: int
kind: Kind
tx: int
ty: int
sensor: SensorProps | None = None
source: SourceProps | None = None
uav: UavProps | None = None
show_effect: bool = True
carried_by: int | None = None
icon_override: str | None = None
```

### clamp — satır 113

Sayısal değeri alt ve üst sınır arasında tutar; panel ve konum ayarlarında kullanılır.

**Girdiler:** v, lo, hi. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** max(lo, min(hi, v))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** max, min
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: max(lo, min(hi, v))

**Gerçek kaynak:**

```python
def clamp(v, lo, hi):
    return max(lo, min(hi, v))
```

### accuracy_for_dist — satır 117

Eski uzaklık tablosundan yüzde döndürür; yeni noktasal ölçüm bunu kullanmaz.

**Girdiler:** d: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** 0; ACCURACY_BY_DIST[d]; ACCURACY_BY_DIST[-1]
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: d >= 8
2. Koşula göre yol seç: d <= 6
3. Çağırana sonucu döndür: ACCURACY_BY_DIST[-1]

**Gerçek kaynak:**

```python
def accuracy_for_dist(d: int) -> int:
    if d >= 8:
        return 0
    if d <= 6:
        return ACCURACY_BY_DIST[d]
    return ACCURACY_BY_DIST[-1]
```

### tile_occupied — satır 125

Taşınmayan nesneler arasında hedef karenin dolu olup olmadığını söyler.

**Girdiler:** entities: list[Entity], tx: int, ty: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** True; False
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: e ← entities
2. Çağırana sonucu döndür: False

**Gerçek kaynak:**

```python
def tile_occupied(entities: list[Entity], tx: int, ty: int) -> bool:
    for e in entities:
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return True
    return False
```

### find_entity_at — satır 134

Bir karenin seçilebilir nesnesinin listedeki indeksini bulur; taşınan yükü atlar.

**Girdiler:** entities: list[Entity], tx: int, ty: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** i; None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** enumerate
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: (i, e) ← enumerate(entities)
2. Çağırana sonucu döndür: None

**Gerçek kaynak:**

```python
def find_entity_at(entities: list[Entity], tx: int, ty: int):
    # Prefer non-carried things for selection
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return i
    return None
```

### find_entity_by_id — satır 144

Kalıcı nesne kimliğini gerçek nesneye çözer; bulunamazsa None döner.

**Girdiler:** entities: list[Entity], eid: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** e; None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: e ← entities
2. Çağırana sonucu döndür: None

**Gerçek kaynak:**

```python
def find_entity_by_id(entities: list[Entity], eid: int) -> Entity | None:
    for e in entities:
        if e.id == eid:
            return e
    return None
```

### dist — satır 151

İki konum arasındaki Öklid uzaklığını hesaplar.

**Girdiler:** a, b. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** math.hypot(a[0] - b[0], a[1] - b[1])
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** math.hypot
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: math.hypot(a[0] - b[0], a[1] - b[1])

**Gerçek kaynak:**

```python
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])
```

### bresenham_tiles — satır 157

Bir doğru boyunca geçilen tam sayı karolarını sırayla üretir; rota engel testinin temelidir.

**Girdiler:** x0: int, y0: int, x1: int, y1: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (x, y)
**Atanan yerel değerler / durum alanları:** dx, dy, sx, sy, err, (x, y), e2, x, y
**Bağlandığı işlevler:** abs
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: dx = abs(x1 - x0)
2. Değeri/alanı oluştur veya güncelle: dy = abs(y1 - y0)
3. Değeri/alanı oluştur veya güncelle: sx = 1 if x0 < x1 else -1
4. Değeri/alanı oluştur veya güncelle: sy = 1 if y0 < y1 else -1
5. Değeri/alanı oluştur veya güncelle: err = dx - dy
6. Değeri/alanı oluştur veya güncelle: x, y = (x0, y0)
7. Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: True

**Gerçek kaynak:**

```python
def bresenham_tiles(x0: int, y0: int, x1: int, y1: int):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
```

### route_is_valid — satır 177

Returns False if any segment intersects an obstacle tile.

**Girdiler:** route_points: list[tuple[int, int]], obstacle_tiles: set[tuple[int, int]]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** True; False
**Atanan yerel değerler / durum alanları:** (x0, y0), (x1, y1)
**Bağlandığı işlevler:** len, range, bresenham_tiles
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: len(route_points) < 2
2. Her öğe için işle: i ← range(1, len(route_points))
3. Çağırana sonucu döndür: True

**Gerçek kaynak:**

```python
def route_is_valid(route_points: list[tuple[int, int]], obstacle_tiles: set[tuple[int, int]]) -> bool:
    """Returns False if any segment intersects an obstacle tile."""
    if len(route_points) < 2:
        return True
    for i in range(1, len(route_points)):
        x0, y0 = route_points[i - 1]
        x1, y1 = route_points[i]
        for (x, y) in bresenham_tiles(x0, y0, x1, y1):
            # allow the starting tile; everything else must be free
            if (x, y) == (x0, y0):
                continue
            if (x, y) in obstacle_tiles:
                return False
    return True
```

### spread_fire — satır 193

Every call (expected every 2s), some obstacles may ignite into TEMP sources.

**Girdiler:** entities: list['Entity']. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** temp_sources, obstacles, best_d, best_src, sp, d, n, p, tree.kind, tree.source, tree.icon_override
**Bağlandığı işlevler:** math.hypot, max, int, float, random.random, SourceProps
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: temp_sources = [e for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source and (e.source.stype == SourceType.TEMP)]
2. Koşula göre yol seç: not temp_sources
3. Değeri/alanı oluştur veya güncelle: obstacles = [e for e in entities if e.kind == Kind.OBSTACLE and e.carried_by is None]
4. Koşula göre yol seç: not obstacles
5. Her öğe için işle: tree ← obstacles

**Gerçek kaynak:**

```python
def spread_fire(entities: list["Entity"]):
    """Every call (expected every 2s), some obstacles may ignite into TEMP sources."""
    temp_sources = [e for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source and e.source.stype == SourceType.TEMP]
    if not temp_sources:
        return

    obstacles = [e for e in entities if e.kind == Kind.OBSTACLE and e.carried_by is None]
    if not obstacles:
        return

    for tree in obstacles:
        # nearest temp source that can reach this tree
        best_d = None
        best_src = None
        for src in temp_sources:
            sp = src.source
            if sp is None:
                continue
            d = math.hypot(tree.tx - src.tx, tree.ty - src.ty)
            if d <= max(1, int(sp.range_tiles)):
                if best_d is None or d < best_d:
                    best_d = d
                    best_src = src

        if best_d is None or best_d <= 0:
            continue

        n = max(1.0, float(best_d))
        p = 1.0 / (n * n)

        if random.random() < p:
            # convert this obstacle into a burned TEMP source
            tree.kind = Kind.SOURCE
            tree.source = SourceProps(stype=SourceType.TEMP, power=3, range_tiles=6)
            tree.icon_override = "burned"
```

### Camera — satır 234

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Camera.__init__ — satır 235

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.x, self.y, self.zoom
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.x = 0.0
2. Değeri/alanı oluştur veya güncelle: self.y = 0.0
3. Değeri/alanı oluştur veya güncelle: self.zoom = 1.0

**Gerçek kaynak:**

```python
def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.zoom = 1.0
```

### Camera.clamp_zoom_for_map — satır 240

Zoom değerini sınırlar; alternatif sürümde harita boyutunu da dikkate alır.

**Girdiler:** self, tile_px: float, map_w: int, map_h: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** view_w, view_h, min_zoom_x, min_zoom_y, min_zoom, self.zoom
**Bağlandığı işlevler:** max, clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: view_w = SCREEN_W - PANEL_W
2. Değeri/alanı oluştur veya güncelle: view_h = SCREEN_H
3. Değeri/alanı oluştur veya güncelle: min_zoom_x = view_w / (tile_px * max(1, map_w))
4. Değeri/alanı oluştur veya güncelle: min_zoom_y = view_h / (tile_px * max(1, map_h))
5. Değeri/alanı oluştur veya güncelle: min_zoom = max(min_zoom_x, min_zoom_y, MIN_ZOOM_FLOOR)
6. Değeri/alanı oluştur veya güncelle: self.zoom = clamp(self.zoom, min_zoom, MAX_ZOOM)

**Gerçek kaynak:**

```python
def clamp_zoom_for_map(self, tile_px: float, map_w: int, map_h: int):
        view_w = SCREEN_W - PANEL_W
        view_h = SCREEN_H
        min_zoom_x = view_w / (tile_px * max(1, map_w))
        min_zoom_y = view_h / (tile_px * max(1, map_h))
        min_zoom = max(min_zoom_x, min_zoom_y, MIN_ZOOM_FLOOR)
        self.zoom = clamp(self.zoom, min_zoom, MAX_ZOOM)
```

### Camera.zoom_at — satır 248

Mevcut ölçeği verilen katsayıyla değiştirip izin verilen aralıkta tutar.

**Girdiler:** self, zoom_factor: float, tile_px: float, map_w: int, map_h: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.zoom
**Bağlandığı işlevler:** self.clamp_zoom_for_map
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.zoom *= zoom_factor
2. Yan etki/çağrı adımını çalıştır: self.clamp_zoom_for_map(tile_px, map_w, map_h)

**Gerçek kaynak:**

```python
def zoom_at(self, zoom_factor: float, tile_px: float, map_w: int, map_h: int):
        self.zoom *= zoom_factor
        self.clamp_zoom_for_map(tile_px, map_w, map_h)
```

### Camera.screen_to_world — satır 252

Ekrandaki fare konumunu kamera dönüşümünün tersiyle dünya koordinatına çevirir.

**Girdiler:** self, screen_pos: tuple[int, int], tile_px: float. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (wx, wy)
**Atanan yerel değerler / durum alanları:** (sx, sy), cx, cy, dx, dy, wx, wy
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sx, sy = screen_pos
2. Değeri/alanı oluştur veya güncelle: cx = (SCREEN_W - PANEL_W) / 2
3. Değeri/alanı oluştur veya güncelle: cy = SCREEN_H / 2
4. Değeri/alanı oluştur veya güncelle: dx = sx - cx
5. Değeri/alanı oluştur veya güncelle: dy = sy - cy
6. Değeri/alanı oluştur veya güncelle: wx = dx / (tile_px * self.zoom) + self.x
7. Değeri/alanı oluştur veya güncelle: wy = dy / (tile_px * self.zoom) + self.y
8. Çağırana sonucu döndür: (wx, wy)

**Gerçek kaynak:**

```python
def screen_to_world(self, screen_pos: tuple[int, int], tile_px: float) -> tuple[float, float]:
        sx, sy = screen_pos
        cx = (SCREEN_W - PANEL_W) / 2
        cy = SCREEN_H / 2
        dx = sx - cx
        dy = sy - cy
        wx = dx / (tile_px * self.zoom) + self.x
        wy = dy / (tile_px * self.zoom) + self.y
        return wx, wy
```

### simulate_tick — satır 266

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** entities: list[Entity], dt_seconds: float. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sources, s, rng, eff, base, mult, drain, s.battery, s.active, s.last_temp, s.last_gas, temp_val, gas_val, sp, d, src_rng, d_eff, d_eff_i, acc, power, att, contrib
**Bağlandığı işlevler:** max, int, clamp, math.hypot, math.floor, accuracy_for_dist
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sources = [e for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source is not None]
2. Her öğe için işle: e ← entities

**Gerçek kaynak:**

```python
def simulate_tick(entities: list[Entity], dt_seconds: float):
    sources = [e for e in entities if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source is not None]

    for e in entities:
        if e.kind != Kind.SENSOR or e.sensor is None:
            continue

        s = e.sensor
        rng = max(1, int(s.range_tiles))
        eff = clamp(int(s.efficiency), 1, 100)

        # Battery drain: n^2 per second, multiplied by inefficiency
        base = rng * rng
        mult = 1.0 + (100 - eff) / 100.0
        drain = base * mult * dt_seconds

        if s.battery <= 0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_gas = 0.0
            continue

        s.battery -= drain
        if s.battery <= 0:
            s.battery = 0.0
            s.active = False
            s.last_temp = 0.0
            s.last_gas = 0.0
            continue

        s.active = True

        temp_val = 0.0
        gas_val = 0.0

        for src_ent in sources:
            sp = src_ent.source
            if sp is None:
                continue

            d = math.hypot(e.tx - src_ent.tx, e.ty - src_ent.ty)
            src_rng = max(1, int(sp.range_tiles))

            # Effective distance from sensor to nearest point of source influence:
            d_eff = max(0.0, d - src_rng)
            if d_eff > rng:
                continue

            d_eff_i = int(math.floor(d_eff + 1e-6))
            acc = accuracy_for_dist(d_eff_i)
            if acc <= 0:
                continue

            power = clamp(int(sp.power), 1, 10)

            att = 1.0 - (d_eff / src_rng)
            if att < 0:
                att = 0.0

            contrib = power * att * (acc / 100.0)

            if sp.stype == SourceType.TEMP:
                temp_val += contrib
            else:
                gas_val += contrib

        s.last_temp = temp_val
        s.last_gas = gas_val
```

### update_uavs — satır 337

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** entities: list[Entity], dt: float, map_w: int, map_h: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** up, speed, remaining, up.route_i, target_i, (tx, ty), dx, dy, d, next_i, up.route_dir, step, up.x, up.y, u.tx, u.ty, ce, ce.tx, ce.ty
**Bağlandığı işlevler:** len, clamp, int, math.hypot, min, round, find_entity_by_id
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: u ← entities

**Gerçek kaynak:**

```python
def update_uavs(entities: list[Entity], dt: float, map_w: int, map_h: int):
    for u in entities:
        if u.kind != Kind.UAV or u.uav is None:
            continue
        up = u.uav
        if not up.route or len(up.route) < 2:
            continue

        speed = clamp(up.speed, 1.0, 10.0)
        remaining = speed * dt  # tiles to move this frame

        while remaining > 1e-6:
            # Clamp waypoint index
            up.route_i = int(clamp(up.route_i, 0, len(up.route) - 1))
            target_i = up.route_i
            tx, ty = up.route[target_i]
            dx = tx - up.x
            dy = ty - up.y
            d = math.hypot(dx, dy)

            if d < 1e-6:
                # reached this waypoint, choose next
                next_i = target_i + up.route_dir

                if up.route_mode == RouteMode.LOOP:
                    if next_i >= len(up.route):
                        next_i = 0
                    if next_i < 0:
                        next_i = len(up.route) - 1
                    up.route_i = next_i

                else:  # PINGPONG
                    if next_i >= len(up.route) or next_i < 0:
                        up.route_dir *= -1
                        next_i = target_i + up.route_dir
                        next_i = int(clamp(next_i, 0, len(up.route) - 1))
                    up.route_i = next_i
                continue

            step = min(remaining, d)
            up.x += (dx / d) * step
            up.y += (dy / d) * step
            remaining -= step

        # Keep inside map bounds
        up.x = clamp(up.x, 0.0, map_w - 1.0)
        up.y = clamp(up.y, 0.0, map_h - 1.0)

        # Update tile coords for rendering/selection
        u.tx = int(round(up.x))
        u.ty = int(round(up.y))
        u.tx = int(clamp(u.tx, 0, map_w - 1))
        u.ty = int(clamp(u.ty, 0, map_h - 1))

        # Move carried items with UAV (and effects center becomes UAV center because tx/ty follow)
        for cid in up.carrying_ids:
            ce = find_entity_by_id(entities, cid)
            if ce is None:
                continue
            ce.tx = u.tx
            ce.ty = u.ty
```

### draw_button — satır 403

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, text, font, active=False. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** label
**Bağlandığı işlevler:** pygame.draw.rect, font.render, screen.blit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (225, 225, 225) if active else (90, 90, 100), rect, 2 if active else 1, border_radius=10)
3. Değeri/alanı oluştur veya güncelle: label = font.render(text, True, (235, 235, 235))
4. Yan etki/çağrı adımını çalıştır: screen.blit(label, (rect.x + 12, rect.y + 9))

**Gerçek kaynak:**

```python
def draw_button(screen, rect, text, font, active=False):
    pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
    pygame.draw.rect(
        screen,
        (225, 225, 225) if active else (90, 90, 100),
        rect,
        2 if active else 1,
        border_radius=10,
    )
    label = font.render(text, True, (235, 235, 235))
    screen.blit(label, (rect.x + 12, rect.y + 9))
```

### draw_small_btn — satır 416

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, text, font. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** label, (lw, lh)
**Bağlandığı işlevler:** pygame.draw.rect, font.render, label.get_size, screen.blit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (50, 50, 55), rect, border_radius=6)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=6)
3. Değeri/alanı oluştur veya güncelle: label = font.render(text, True, (240, 240, 240))
4. Değeri/alanı oluştur veya güncelle: lw, lh = label.get_size()
5. Yan etki/çağrı adımını çalıştır: screen.blit(label, (rect.centerx - lw // 2, rect.centery - lh // 2))

**Gerçek kaynak:**

```python
def draw_small_btn(screen, rect, text, font):
    pygame.draw.rect(screen, (50, 50, 55), rect, border_radius=6)
    pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=6)
    label = font.render(text, True, (240, 240, 240))
    lw, lh = label.get_size()
    screen.blit(label, (rect.centerx - lw // 2, rect.centery - lh // 2))
```

### draw_switch — satır 424

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, on: bool. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** bg, border, on_col, inner, knob_r, kx, ky
**Bağlandığı işlevler:** pygame.draw.rect, rect.inflate, pygame.draw.circle
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: bg = (50, 50, 55)
2. Değeri/alanı oluştur veya güncelle: border = (120, 120, 130)
3. Değeri/alanı oluştur veya güncelle: on_col = (120, 210, 150)
4. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, bg, rect, border_radius=999)
5. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, border, rect, 1, border_radius=999)
6. Değeri/alanı oluştur veya güncelle: inner = rect.inflate(-4, -4)
7. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, on_col if on else (70, 70, 80), inner, border_radius=999)
8. Değeri/alanı oluştur veya güncelle: knob_r = inner.height // 2 - 1
9. Değeri/alanı oluştur veya güncelle: kx = inner.right - knob_r - 2 if on else inner.left + knob_r + 2
10. Değeri/alanı oluştur veya güncelle: ky = inner.centery
11. Yan etki/çağrı adımını çalıştır: pygame.draw.circle(screen, (235, 235, 235), (kx, ky), knob_r)

**Gerçek kaynak:**

```python
def draw_switch(screen, rect, on: bool):
    # pill
    bg = (50, 50, 55)
    border = (120, 120, 130)
    on_col = (120, 210, 150)
    pygame.draw.rect(screen, bg, rect, border_radius=999)
    pygame.draw.rect(screen, border, rect, 1, border_radius=999)
    inner = rect.inflate(-4, -4)
    pygame.draw.rect(screen, on_col if on else (70, 70, 80), inner, border_radius=999)

    # knob
    knob_r = inner.height // 2 - 1
    kx = inner.right - knob_r - 2 if on else inner.left + knob_r + 2
    ky = inner.centery
    pygame.draw.circle(screen, (235, 235, 235), (kx, ky), knob_r)
```

### draw_section_title — satır 441

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, x, y, title, font, small. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** screen.blit, font.render, pygame.draw.line
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: screen.blit(font.render(title, True, (245, 245, 245)), (x, y))
2. Yan etki/çağrı adımını çalıştır: pygame.draw.line(screen, (45, 45, 55), (x, y + 26), (x + PANEL_W - 2 * PAD, y + 26), 1)

**Gerçek kaynak:**

```python
def draw_section_title(screen, x, y, title, font, small):
    screen.blit(font.render(title, True, (245, 245, 245)), (x, y))
    pygame.draw.line(screen, (45, 45, 55), (x, y + 26), (x + PANEL_W - 2 * PAD, y + 26), 1)
```

### draw_segmented — satır 446

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, rect, options: list[str], selected_idx: int, font_small. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** seg_rects
**Atanan yerel değerler / durum alanları:** n, seg_w, seg_rects, r, txt
**Bağlandığı işlevler:** pygame.draw.rect, len, range, pygame.Rect, seg_rects.append, r.inflate, font_small.render, screen.blit, txt.get_width, txt.get_height
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=10)
3. Değeri/alanı oluştur veya güncelle: n = len(options)
4. Değeri/alanı oluştur veya güncelle: seg_w = rect.width // n
5. Değeri/alanı oluştur veya güncelle: seg_rects = []
6. Her öğe için işle: i ← range(n)
7. Çağırana sonucu döndür: seg_rects

**Gerçek kaynak:**

```python
def draw_segmented(screen, rect, options: list[str], selected_idx: int, font_small):
    # background
    pygame.draw.rect(screen, (45, 45, 50), rect, border_radius=10)
    pygame.draw.rect(screen, (120, 120, 130), rect, 1, border_radius=10)
    n = len(options)
    seg_w = rect.width // n
    seg_rects = []
    for i in range(n):
        r = pygame.Rect(rect.x + i * seg_w, rect.y, seg_w, rect.height)
        seg_rects.append(r)

        if i == selected_idx:
            pygame.draw.rect(screen, (70, 70, 78), r.inflate(-2, -2), border_radius=8)

        txt = font_small.render(options[i], True, (235, 235, 235))
        screen.blit(txt, (r.centerx - txt.get_width() // 2, r.centery - txt.get_height() // 2))
    return seg_rects
```

### build_panel_layout — satır 468

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** entities, selected_tool, selected_entity_idx, panel_x, small, font, show_effect_global: bool, uav_focus_cargo_id: int | None, collapsed_cargo_ids: set[int]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (tool_buttons, clickables, global_rows, entity_rows, sw, None, None, content_bottom); (tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom)
**Atanan yerel değerler / durum alanları:** tool_buttons, clickables, global_rows, entity_rows, global_sw_rect, attr_y, sw, content_bottom, e, ent_sw_y, ent_sw, y, back, s, src, seg_rect, up, route_sw, mode_sw, slot_w, slots, r, clr, ce, rect, label, tog, is_collapsed, src2, s2
**Bağlandığı işlevler:** pygame.Rect, global_rows.append, clickables.append, len, max, entity_rows.append, add_numeric_row, str, set_range, set_eff, int, set_batt, set_power, set_srange, set_speed, range, slots.append, list, find_entity_by_id, set_power2, set_srange2, set_range2, set_eff2
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: tool_buttons = [(Kind.SENSOR, pygame.Rect(panel_x + PAD, 70, PANEL_W - 2 * PAD, 40), 'Ekle: IoT Sensör'), (Kind.SOURCE, pygame.Rect(panel_x + PAD, 120, PANEL_W - 2 * PAD, 40), 'Ekle: Kaynak'), (Kind.OBSTACLE, pygame.Rect…
2. Değeri/alanı oluştur veya güncelle: clickables: list[tuple[pygame.Rect, callable]] = []
3. Değeri/alanı oluştur veya güncelle: global_rows = []
4. Değeri/alanı oluştur veya güncelle: entity_rows = []
5. Değeri/alanı oluştur veya güncelle: global_sw_rect = None
6. Değeri/alanı oluştur veya güncelle: attr_y = PANEL_Y_GLOBAL_SWITCH
7. Değeri/alanı oluştur veya güncelle: sw = pygame.Rect(panel_x + PAD, attr_y, 44, 24)
8. Yan etki/çağrı adımını çalıştır: global_rows.append(('switch', sw, 'Etki yarıçaplarını göster', show_effect_global))
9. Yan etki/çağrı adımını çalıştır: clickables.append((sw, None))
10. Koşula göre yol seç: selected_entity_idx is None or not 0 <= selected_entity_idx < len(entities)
11. Değeri/alanı oluştur veya güncelle: e = entities[selected_entity_idx]
12. Değeri/alanı oluştur veya güncelle: ent_sw_y = PANEL_SCROLL_Y0
13. Değeri/alanı oluştur veya güncelle: ent_sw = pygame.Rect(panel_x + PAD, ent_sw_y, 44, 24)
14. Yan etki/çağrı adımını çalıştır: entity_rows.append(('switch', ent_sw, 'Bu nesnenin etkisini göster', e.show_effect))
15. Yerel yardımcı tanımla: toggle_entity_effect; ayrı sembol kaydı aşağıdadır.
16. Yan etki/çağrı adımını çalıştır: clickables.append((ent_sw, toggle_entity_effect))
17. Değeri/alanı oluştur veya güncelle: y = ent_sw_y + 40
18. Koşula göre yol seç: e.carried_by is not None
19. Yerel yardımcı tanımla: add_numeric_row; ayrı sembol kaydı aşağıdadır.
20. Koşula göre yol seç: e.kind == Kind.SENSOR and e.sensor
21. Değeri/alanı oluştur veya güncelle: content_bottom = 0
22. Her öğe için işle: row ← global_rows + entity_rows
23. Çağırana sonucu döndür: (tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom)

**Gerçek kaynak:**

```python
def build_panel_layout(entities, selected_tool, selected_entity_idx, panel_x, small, font,
                       show_effect_global: bool, uav_focus_cargo_id: int | None,
                       collapsed_cargo_ids: set[int]):
    tool_buttons = [
        (Kind.SENSOR, pygame.Rect(panel_x + PAD, 70, PANEL_W - 2 * PAD, 40), "Ekle: IoT Sensör"),
        (Kind.SOURCE, pygame.Rect(panel_x + PAD, 120, PANEL_W - 2 * PAD, 40), "Ekle: Kaynak"),
        (Kind.OBSTACLE, pygame.Rect(panel_x + PAD, 170, PANEL_W - 2 * PAD, 40), "Ekle: Engel (Ağaç)"),
        (Kind.BURNED, pygame.Rect(panel_x + PAD, 220, PANEL_W - 2 * PAD, 40), "Ekle: Burned (Yanık)"),
        (Kind.UAV, pygame.Rect(panel_x + PAD, 270, PANEL_W - 2 * PAD, 40), "Ekle: İHA (Drone)"),
    ]

    clickables: list[tuple[pygame.Rect, callable]] = []
    global_rows = []
    entity_rows = []
    global_sw_rect = None

    # Global switch row
    attr_y = PANEL_Y_GLOBAL_SWITCH
    sw = pygame.Rect(panel_x + PAD, attr_y, 44, 24)
    global_rows.append(("switch", sw, "Etki yarıçaplarını göster", show_effect_global))
    clickables.append((sw, None))  # placeholder

    if selected_entity_idx is None or not (0 <= selected_entity_idx < len(entities)):
        # content bottom for scrolling
        content_bottom = 0
        for row in global_rows:
            if row[0] == "switch":
                content_bottom = max(content_bottom, row[1].bottom)
        return tool_buttons, clickables, global_rows, entity_rows, sw, None, None, content_bottom

    e = entities[selected_entity_idx]

    # Per-entity switch
    ent_sw_y = PANEL_SCROLL_Y0
    ent_sw = pygame.Rect(panel_x + PAD, ent_sw_y, 44, 24)
    entity_rows.append(("switch", ent_sw, "Bu nesnenin etkisini göster", e.show_effect))

    def toggle_entity_effect():
        e.show_effect = not e.show_effect

    clickables.append((ent_sw, toggle_entity_effect))

    y = ent_sw_y + 40

    # If this entity is being carried, offer a quick "back to UAV" button
    if e.carried_by is not None:
        back = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
        entity_rows.append(("button", back, f"İHA'ya dön (#{e.carried_by})"))
        clickables.append((back, ("select_entity_id", e.carried_by)))
        y += 42
        entity_rows.append(("text", y, f"Not: Bu nesne İHA #{e.carried_by} üzerinde taşınıyor."))
        y += 22

    def add_numeric_row(label, value_str, dec_fn, inc_fn, step_hint=None):
        nonlocal y
        text_surf = small.render(f"{label}: {value_str}", True, (220, 220, 220))
        h = text_surf.get_height()
        btn_y = y + h + 6
        minus = pygame.Rect(panel_x + PAD, btn_y, 30, 26)
        plus = pygame.Rect(panel_x + PAD + 38, btn_y, 30, 26)
        clickables.append((minus, dec_fn))
        clickables.append((plus, inc_fn))
        entity_rows.append(("numeric", y, f"{label}: {value_str}", minus, plus, step_hint))
        y = btn_y + 26 + 12

    if e.kind == Kind.SENSOR and e.sensor:
        s = e.sensor
        entity_rows.append(("text", y, f"Aktif: {'Evet' if s.active else 'Hayır'}"))
        y += 22

        def set_range(d):
            s.range_tiles = clamp(s.range_tiles + d, 1, 50)
            if s.battery > 0:
                s.active = True

        def set_eff(d):
            s.efficiency = clamp(s.efficiency + d, 1, 100)

        def set_batt(d):
            s.battery = max(0.0, s.battery + float(d))
            if s.battery > 0:
                s.active = True

        add_numeric_row("Menzil", str(s.range_tiles),
                        dec_fn=lambda: set_range(-1),
                        inc_fn=lambda: set_range(+1))
        add_numeric_row("Verimlilik", str(s.efficiency),
                        dec_fn=lambda: set_eff(-5),
                        inc_fn=lambda: set_eff(+5),
                        step_hint="(±5)")
        add_numeric_row("Pil", str(int(s.battery)),
                        dec_fn=lambda: set_batt(-250),
                        inc_fn=lambda: set_batt(+250),
                        step_hint="(±250)")

        entity_rows.append(("text", y, f"Son TEMP: {s.last_temp:.2f}"))
        y += 18
        entity_rows.append(("text", y, f"Son GAS : {s.last_gas:.2f}"))

    elif e.kind == Kind.SOURCE and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip:"))
        y += 18

        seg_rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 32)
        # placeholder rects produced in draw step; click handling uses stored rectangles
        entity_rows.append(("segmented", seg_rect, ["TEMP", "GAS"], 0 if src.stype == SourceType.TEMP else 1))
        y += 44

        def set_power(d):
            src.power = clamp(src.power + d, 1, 10)

        def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)

        add_numeric_row("Güç", str(src.power),
                        dec_fn=lambda: set_power(-1),
                        inc_fn=lambda: set_power(+1))
        add_numeric_row("Menzil", str(src.range_tiles),
                        dec_fn=lambda: set_srange(-1),
                        inc_fn=lambda: set_srange(+1))


    elif e.kind == Kind.BURNED and e.source:
        src = e.source
        entity_rows.append(("text", y, "Tip: TEMP (burned)"))
        y += 22

        def set_power(d):
            src.power = clamp(src.power + d, 1, 10)

        def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)

        add_numeric_row("Güç", str(src.power),
                        dec_fn=lambda: set_power(-1),
                        inc_fn=lambda: set_power(+1))
        add_numeric_row("Menzil", str(src.range_tiles),
                        dec_fn=lambda: set_srange(-1),
                        inc_fn=lambda: set_srange(+1))

    elif e.kind == Kind.UAV and e.uav:
        up = e.uav

        entity_rows.append(("text", y, "Rota: K ile düzenle (İHA seçiliyken)"))
        y += 18
        entity_rows.append(("text", y, f"Waypoint sayısı: {len(up.route)}"))
        y += 22

        def set_speed(d):
            up.speed = clamp(up.speed + d, 1.0, 10.0)

        add_numeric_row("Hız (tile/s)", f"{up.speed:.1f}",
                        dec_fn=lambda: set_speed(-0.5),
                        inc_fn=lambda: set_speed(+0.5),
                        step_hint="(±0.5)")

        # route visibility switch
        route_sw = pygame.Rect(panel_x + PAD, y + 2, 44, 24)
        entity_rows.append(("switch", route_sw, "Rotayı göster (mavi başlangıç)", up.show_route))

        def toggle_route():
            up.show_route = not up.show_route

        clickables.append((route_sw, toggle_route))
        y += 40

        # route mode switch
        mode_sw = pygame.Rect(panel_x + PAD, y + 2, 44, 24)
        entity_rows.append(("mode_switch", mode_sw, "Tersine takip (PingPong)", up.route_mode == RouteMode.PINGPONG))

        def toggle_mode():
            up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
            up.route_dir = 1

        clickables.append((mode_sw, toggle_mode))
        y += 40

        # Cargo slots (drag-drop)
        entity_rows.append(("text", y, "Taşınanlar (sürükle-bırak):"))
        y += 18

        slot_w = (PANEL_W - 2 * PAD - 10) // 3
        slots = []
        for i in range(3):
            r = pygame.Rect(panel_x + PAD + i * (slot_w + 5), y, slot_w, 42)
            slots.append(r)
        entity_rows.append(("cargo_slots", slots))
        y += 54

        # Clear button
        clr = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
        entity_rows.append(("button", clr, "Taşınanları Temizle"))

        def clear_cargo():
            # detach carried
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce:
                    ce.carried_by = None
            up.carrying_ids.clear()

        clickables.append((clr, clear_cargo))
        y += 42

        # Quick access buttons for carried items (edit without detaching)
        if up.carrying_ids:
            entity_rows.append(("text", y, "Taşınan nesneler (düzenle):"))
            y += 18
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce is None:
                    continue
                rect = pygame.Rect(panel_x + PAD, y, PANEL_W - 2 * PAD, 30)
                label = f"Düzenle: {ce.kind.value} #{ce.id}"
                entity_rows.append(("carry_edit_btn", rect, label, cid))
                clickables.append((rect, ("uav_focus_cargo", cid)))
                y += 38

        # Focused cargo details (show under UAV props, without changing selection)
        if uav_focus_cargo_id is not None and uav_focus_cargo_id in list(up.carrying_ids):
            ce = find_entity_by_id(entities, uav_focus_cargo_id)
            if ce is not None:
                y += 4
                entity_rows.append(("text", y, f"{ce.kind.value} özellikleri:"))
                tog = pygame.Rect(panel_x + PAD + 170, y - 2, 90, 22)
                is_collapsed = (ce.id in collapsed_cargo_ids)
                entity_rows.append(("cargo_toggle", tog, "KAPAT" if not is_collapsed else "AÇ"))
                def _toggle_cargo(cid=ce.id):
                    if cid in collapsed_cargo_ids:
                        collapsed_cargo_ids.remove(cid)
                    else:
                        collapsed_cargo_ids.add(cid)
                clickables.append((tog, _toggle_cargo))
                y += 26

                if ce.id not in collapsed_cargo_ids:
                    if ce.kind in (Kind.SOURCE, Kind.BURNED) and ce.source:
                        src2 = ce.source
                        entity_rows.append(("text", y, f"Tip: {src2.stype.value}"))
                        y += 18

                        def set_power2(d):
                            src2.power = clamp(src2.power + d, 1, 10)
                        def set_srange2(d):
                            src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)

                        add_numeric_row("Güç", str(src2.power),
                                        dec_fn=lambda: set_power2(-1),
                                        inc_fn=lambda: set_power2(+1))
                        add_numeric_row("Menzil", str(src2.range_tiles),
                                        dec_fn=lambda: set_srange2(-1),
                                        inc_fn=lambda: set_srange2(+1))

                    elif ce.kind == Kind.SENSOR and ce.sensor:
                        s2 = ce.sensor
                        def set_range2(d):
                            s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
                            if s2.battery > 0:
                                s2.active = True
                        def set_eff2(d):
                            s2.efficiency = clamp(s2.efficiency + d, 1, 100)

                        add_numeric_row("Menzil", str(s2.range_tiles),
                                        dec_fn=lambda: set_range2(-1),
                                        inc_fn=lambda: set_range2(+1))
                        add_numeric_row("Verimlilik", str(s2.efficiency),
                                        dec_fn=lambda: set_eff2(-5),
                                        inc_fn=lambda: set_eff2(+5),
                                        step_hint="(±5)")

    elif e.kind == Kind.OBSTACLE:
        entity_rows.append(("text", y, "Engel: şimdilik sadece blok objesi."))
        y += 18
        entity_rows.append(("text", y, "Sonraki adım: LOS ile zayıflatma."))

    # content bottom for scrolling (panel absolute coords)
    content_bottom = 0
    for row in global_rows + entity_rows:
        if row[0] in ("switch", "mode_switch"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "text":
            content_bottom = max(content_bottom, row[1] + 28)
        elif row[0] == "numeric":
            content_bottom = max(content_bottom, row[1] + 60)
        elif row[0] in ("button", "carry_edit_btn", "segmented", "cargo_toggle"):
            content_bottom = max(content_bottom, row[1].bottom)
        elif row[0] == "cargo_slots":
            for r in row[1]:
                content_bottom = max(content_bottom, r.bottom)
    return tool_buttons, clickables, global_rows, entity_rows, sw, ent_sw, e, content_bottom
```

### build_panel_layout.toggle_entity_effect — satır 505

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** e.show_effect
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e.show_effect = not e.show_effect

**Gerçek kaynak:**

```python
def toggle_entity_effect():
        e.show_effect = not e.show_effect
```

### build_panel_layout.add_numeric_row — satır 521

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** label, value_str, dec_fn, inc_fn, step_hint=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** text_surf, h, btn_y, minus, plus, y
**Bağlandığı işlevler:** small.render, text_surf.get_height, pygame.Rect, clickables.append, entity_rows.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: text_surf = small.render(f'{label}: {value_str}', True, (220, 220, 220))
2. Değeri/alanı oluştur veya güncelle: h = text_surf.get_height()
3. Değeri/alanı oluştur veya güncelle: btn_y = y + h + 6
4. Değeri/alanı oluştur veya güncelle: minus = pygame.Rect(panel_x + PAD, btn_y, 30, 26)
5. Değeri/alanı oluştur veya güncelle: plus = pygame.Rect(panel_x + PAD + 38, btn_y, 30, 26)
6. Yan etki/çağrı adımını çalıştır: clickables.append((minus, dec_fn))
7. Yan etki/çağrı adımını çalıştır: clickables.append((plus, inc_fn))
8. Yan etki/çağrı adımını çalıştır: entity_rows.append(('numeric', y, f'{label}: {value_str}', minus, plus, step_hint))
9. Değeri/alanı oluştur veya güncelle: y = btn_y + 26 + 12

**Gerçek kaynak:**

```python
def add_numeric_row(label, value_str, dec_fn, inc_fn, step_hint=None):
        nonlocal y
        text_surf = small.render(f"{label}: {value_str}", True, (220, 220, 220))
        h = text_surf.get_height()
        btn_y = y + h + 6
        minus = pygame.Rect(panel_x + PAD, btn_y, 30, 26)
        plus = pygame.Rect(panel_x + PAD + 38, btn_y, 30, 26)
        clickables.append((minus, dec_fn))
        clickables.append((plus, inc_fn))
        entity_rows.append(("numeric", y, f"{label}: {value_str}", minus, plus, step_hint))
        y = btn_y + 26 + 12
```

### build_panel_layout.set_range — satır 538

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s.range_tiles, s.active
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s.range_tiles = clamp(s.range_tiles + d, 1, 50)
2. Koşula göre yol seç: s.battery > 0

**Gerçek kaynak:**

```python
def set_range(d):
            s.range_tiles = clamp(s.range_tiles + d, 1, 50)
            if s.battery > 0:
                s.active = True
```

### build_panel_layout.set_eff — satır 543

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s.efficiency
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s.efficiency = clamp(s.efficiency + d, 1, 100)

**Gerçek kaynak:**

```python
def set_eff(d):
            s.efficiency = clamp(s.efficiency + d, 1, 100)
```

### build_panel_layout.set_batt — satır 546

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s.battery, s.active
**Bağlandığı işlevler:** max, float
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s.battery = max(0.0, s.battery + float(d))
2. Koşula göre yol seç: s.battery > 0

**Gerçek kaynak:**

```python
def set_batt(d):
            s.battery = max(0.0, s.battery + float(d))
            if s.battery > 0:
                s.active = True
```

### build_panel_layout.set_power — satır 577

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.power
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.power = clamp(src.power + d, 1, 10)

**Gerçek kaynak:**

```python
def set_power(d):
            src.power = clamp(src.power + d, 1, 10)
```

### build_panel_layout.set_srange — satır 580

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.range_tiles
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.range_tiles = clamp(src.range_tiles + d, 1, 80)

**Gerçek kaynak:**

```python
def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)
```

### build_panel_layout.set_power — satır 596

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.power
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.power = clamp(src.power + d, 1, 10)

**Gerçek kaynak:**

```python
def set_power(d):
            src.power = clamp(src.power + d, 1, 10)
```

### build_panel_layout.set_srange — satır 599

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src.range_tiles
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src.range_tiles = clamp(src.range_tiles + d, 1, 80)

**Gerçek kaynak:**

```python
def set_srange(d):
            src.range_tiles = clamp(src.range_tiles + d, 1, 80)
```

### build_panel_layout.set_speed — satır 617

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** up.speed
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: up.speed = clamp(up.speed + d, 1.0, 10.0)

**Gerçek kaynak:**

```python
def set_speed(d):
            up.speed = clamp(up.speed + d, 1.0, 10.0)
```

### build_panel_layout.toggle_route — satır 629

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** up.show_route
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: up.show_route = not up.show_route

**Gerçek kaynak:**

```python
def toggle_route():
            up.show_route = not up.show_route
```

### build_panel_layout.toggle_mode — satır 639

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** up.route_mode, up.route_dir
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
2. Değeri/alanı oluştur veya güncelle: up.route_dir = 1

**Gerçek kaynak:**

```python
def toggle_mode():
            up.route_mode = RouteMode.LOOP if up.route_mode == RouteMode.PINGPONG else RouteMode.PINGPONG
            up.route_dir = 1
```

### build_panel_layout.clear_cargo — satır 662

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** ce, ce.carried_by
**Bağlandığı işlevler:** list, find_entity_by_id, up.carrying_ids.clear
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: cid ← list(up.carrying_ids)
2. Yan etki/çağrı adımını çalıştır: up.carrying_ids.clear()

**Gerçek kaynak:**

```python
def clear_cargo():
            # detach carried
            for cid in list(up.carrying_ids):
                ce = find_entity_by_id(entities, cid)
                if ce:
                    ce.carried_by = None
            up.carrying_ids.clear()
```

### build_panel_layout._toggle_cargo — satır 696

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** cid=ce.id. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** collapsed_cargo_ids.remove, collapsed_cargo_ids.add
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: cid in collapsed_cargo_ids

**Gerçek kaynak:**

```python
def _toggle_cargo(cid=ce.id):
                    if cid in collapsed_cargo_ids:
                        collapsed_cargo_ids.remove(cid)
                    else:
                        collapsed_cargo_ids.add(cid)
```

### build_panel_layout.set_power2 — satır 710

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src2.power
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src2.power = clamp(src2.power + d, 1, 10)

**Gerçek kaynak:**

```python
def set_power2(d):
                            src2.power = clamp(src2.power + d, 1, 10)
```

### build_panel_layout.set_srange2 — satır 712

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** src2.range_tiles
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)

**Gerçek kaynak:**

```python
def set_srange2(d):
                            src2.range_tiles = clamp(src2.range_tiles + d, 1, 80)
```

### build_panel_layout.set_range2 — satır 724

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s2.range_tiles, s2.active
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
2. Koşula göre yol seç: s2.battery > 0

**Gerçek kaynak:**

```python
def set_range2(d):
                            s2.range_tiles = clamp(s2.range_tiles + d, 1, 50)
                            if s2.battery > 0:
                                s2.active = True
```

### build_panel_layout.set_eff2 — satır 728

Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.

**Girdiler:** d. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s2.efficiency
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s2.efficiency = clamp(s2.efficiency + d, 1, 100)

**Gerçek kaynak:**

```python
def set_eff2(d):
                            s2.efficiency = clamp(s2.efficiency + d, 1, 100)
```

### load_icon — satır 764

Görüntüyü alfa kanallı yüzeye dönüştürür; yükleme başarısızsa None ile geri dönüşe izin verir.

**Girdiler:** path: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** pygame.image.load(path).convert_alpha(); None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** pygame.image.load(path).convert_alpha, pygame.image.load
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def load_icon(path: str):
    try:
        return pygame.image.load(path).convert_alpha()
    except Exception:
        return None
```

### get_scaled_icon — satır 771

Aynı ikon ve boyut için yeniden ölçeklemeyi önbellekten karşılar.

**Girdiler:** cache: dict, key: str, surf, size: tuple[int, int]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None; cache[k]
**Atanan yerel değerler / durum alanları:** k, cache[k]
**Bağlandığı işlevler:** pygame.transform.smoothscale
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: surf is None
2. Değeri/alanı oluştur veya güncelle: k = (key, size[0], size[1])
3. Koşula göre yol seç: k in cache
4. Değeri/alanı oluştur veya güncelle: cache[k] = pygame.transform.smoothscale(surf, size)
5. Çağırana sonucu döndür: cache[k]

**Gerçek kaynak:**

```python
def get_scaled_icon(cache: dict, key: str, surf, size: tuple[int, int]):
    if surf is None:
        return None
    k = (key, size[0], size[1])
    if k in cache:
        return cache[k]
    cache[k] = pygame.transform.smoothscale(surf, size)
    return cache[k]
```

### draw_dashed_circle — satır 784

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** surface: pygame.Surface, center: tuple[int, int], radius: int, color: tuple[int, int, int, int], dash_deg: int=12, gap_deg: int=10, width: int=2. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** (cx, cy), step, a1, pts, samples, t, ang, x, y
**Bağlandığı işlevler:** range, max, math.radians, int, round, math.cos, math.sin, pts.append, len, pygame.draw.lines
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: radius <= 0
2. Değeri/alanı oluştur veya güncelle: cx, cy = center
3. Değeri/alanı oluştur veya güncelle: step = dash_deg + gap_deg
4. Her öğe için işle: a0 ← range(0, 360, step)

**Gerçek kaynak:**

```python
def draw_dashed_circle(surface: pygame.Surface, center: tuple[int, int], radius: int,
                       color: tuple[int, int, int, int], dash_deg: int = 12, gap_deg: int = 10, width: int = 2):
    if radius <= 0:
        return
    cx, cy = center
    step = dash_deg + gap_deg
    for a0 in range(0, 360, step):
        a1 = a0 + dash_deg
        pts = []
        samples = max(4, dash_deg // 2)
        for i in range(samples + 1):
            t = i / samples
            ang = math.radians(a0 + (a1 - a0) * t)
            x = cx + int(round(math.cos(ang) * radius))
            y = cy + int(round(math.sin(ang) * radius))
            pts.append((x, y))
        if len(pts) >= 2:
            pygame.draw.lines(surface, color, False, pts, width)
```

### make_gauss_field_surface — satır 804

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** cache: dict, key: tuple, radius_px: int, rgba: tuple[int, int, int, int]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None; cache[key]; surf
**Atanan yerel değerler / durum alanları:** size, surf, cx, cy, max_a, (r_col, g_col, b_col, _), sigma, a, core_a, cache[key]
**Bağlandığı işlevler:** pygame.Surface, range, int, math.exp, pygame.draw.circle, min, max
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: radius_px <= 0
2. Koşula göre yol seç: key in cache
3. Değeri/alanı oluştur veya güncelle: size = radius_px * 2 + 1
4. Değeri/alanı oluştur veya güncelle: surf = pygame.Surface((size, size), pygame.SRCALPHA)
5. Değeri/alanı oluştur veya güncelle: cx = cy = radius_px
6. Değeri/alanı oluştur veya güncelle: max_a = rgba[3]
7. Değeri/alanı oluştur veya güncelle: r_col, g_col, b_col, _ = rgba
8. Değeri/alanı oluştur veya güncelle: sigma = radius_px / 2.2
9. Koşula göre yol seç: sigma < 1
10. Her öğe için işle: r ← range(radius_px, 0, -FIELD_STEP_PX)
11. Değeri/alanı oluştur veya güncelle: core_a = min(255, max_a)
12. Yan etki/çağrı adımını çalıştır: pygame.draw.circle(surf, (r_col, g_col, b_col, core_a), (cx, cy), max(1, radius_px // 10))
13. Değeri/alanı oluştur veya güncelle: cache[key] = surf
14. Çağırana sonucu döndür: surf

**Gerçek kaynak:**

```python
def make_gauss_field_surface(cache: dict, key: tuple, radius_px: int, rgba: tuple[int, int, int, int]):
    if radius_px <= 0:
        return None
    if key in cache:
        return cache[key]

    size = radius_px * 2 + 1
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    cx = cy = radius_px

    max_a = rgba[3]
    r_col, g_col, b_col, _ = rgba

    sigma = radius_px / 2.2
    if sigma < 1:
        sigma = 1.0

    for r in range(radius_px, 0, -FIELD_STEP_PX):
        a = int(max_a * math.exp(- (r * r) / (2.0 * sigma * sigma)))
        if a <= 0:
            continue
        pygame.draw.circle(surf, (r_col, g_col, b_col, a), (cx, cy), r)

    core_a = min(255, max_a)
    pygame.draw.circle(surf, (r_col, g_col, b_col, core_a), (cx, cy), max(1, radius_px // 10))

    cache[key] = surf
    return surf
```

### draw_route_overlay — satır 838

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, cam: Camera, tile_px: float, route_points: list[tuple[int, int]], map_w: int, map_h: int, panel_x: int, line_color: tuple[int, int, int]=(220, 220, 230), point_color: tuple[int, int, int]=(240, 240, 240), start_color: tuple[int, int, int]=(80, 170, 255). self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** view_w, view_h, view_cx, view_cy, pts, (sx, sy)
**Bağlandığı işlevler:** world_to_screen, pts.append, len, pygame.draw.lines, enumerate, pygame.draw.circle
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: not route_points
2. Değeri/alanı oluştur veya güncelle: view_w = SCREEN_W - PANEL_W
3. Değeri/alanı oluştur veya güncelle: view_h = SCREEN_H
4. Değeri/alanı oluştur veya güncelle: view_cx = view_w / 2
5. Değeri/alanı oluştur veya güncelle: view_cy = view_h / 2
6. Yerel yardımcı tanımla: world_to_screen; ayrı sembol kaydı aşağıdadır.
7. Değeri/alanı oluştur veya güncelle: pts = []
8. Her öğe için işle: (tx, ty) ← route_points
9. Koşula göre yol seç: len(pts) >= 2
10. Her öğe için işle: (i, p) ← enumerate(pts)

**Gerçek kaynak:**

```python
def draw_route_overlay(screen, cam: Camera, tile_px: float, route_points: list[tuple[int, int]],
                       map_w: int, map_h: int, panel_x: int,
                       line_color: tuple[int, int, int] = (220, 220, 230),
                       point_color: tuple[int, int, int] = (240, 240, 240),
                       start_color: tuple[int, int, int] = (80, 170, 255)):
    if not route_points:
        return
    view_w = SCREEN_W - PANEL_W
    view_h = SCREEN_H
    view_cx = view_w / 2
    view_cy = view_h / 2

    def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))

    pts = []
    for (tx, ty) in route_points:
        sx, sy = world_to_screen(tx + 0.5, ty + 0.5)
        pts.append((sx, sy))

    if len(pts) >= 2:
        pygame.draw.lines(screen, line_color, False, pts, 2)

    for i, p in enumerate(pts):
        if i == 0:
            pygame.draw.circle(screen, start_color, p, 6)
            pygame.draw.circle(screen, (10, 10, 12), p, 6, 2)
        else:
            pygame.draw.circle(screen, point_color, p, 4)
```

### draw_route_overlay.world_to_screen — satır 850

Kamera merkezi, görünüm alanı ve zoom ile dünya noktasını piksele çevirir.

**Girdiler:** wx, wy. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (int(round(sx)), int(round(sy)))
**Atanan yerel değerler / durum alanları:** sx, sy
**Bağlandığı işlevler:** int, round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
2. Değeri/alanı oluştur veya güncelle: sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
3. Çağırana sonucu döndür: (int(round(sx)), int(round(sy)))

**Gerçek kaynak:**

```python
def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))
```

### draw_world — satır 871

Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.

**Girdiler:** screen, cam: Camera, tile_px: float, show_grid: bool, entities: list[Entity], hover_tx, hover_ty, selected_entity_idx: int | None, map_w: int, map_h: int, icons: dict, icon_cache: dict, show_effect_global: bool, field_cache: dict, route_preview: list[tuple[int, int]] | None=None, route_preview_invalid: bool=False. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** view_w, view_h, view_cx, view_cy, tw, th, tiles_x, tiles_y, x0, x1, y0, y1, (sx, sy), rect, sp, radius_px, base_rgb, alpha, blob, (cx_s, cy_s), max_r, up, col, (hsx, hsy), r, icon_key, icon_src, scaled, pad, cs, slots_pos, slots_pos_1, slots_pos_2, slots_pos_3, carried, sensor_carried, source_carried, nsrc, (px, py), icon_key2, icon_src2, sc, c
**Bağlandığı işlevler:** max, int, clamp, range, world_to_screen, pygame.Rect, pygame.draw.rect, round, make_gauss_field_surface, screen.blit, blob.get_rect, draw_dashed_circle, len, draw_route_overlay, enumerate, icons.get, get_scaled_icon, min, find_entity_by_id, sc.get_rect
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: view_w = SCREEN_W - PANEL_W
2. Değeri/alanı oluştur veya güncelle: view_h = SCREEN_H
3. Değeri/alanı oluştur veya güncelle: view_cx = view_w / 2
4. Değeri/alanı oluştur veya güncelle: view_cy = view_h / 2
5. Yerel yardımcı tanımla: world_to_screen; ayrı sembol kaydı aşağıdadır.
6. Değeri/alanı oluştur veya güncelle: tw = max(1, int(tile_px * cam.zoom))
7. Değeri/alanı oluştur veya güncelle: th = max(1, int(tile_px * cam.zoom))
8. Değeri/alanı oluştur veya güncelle: tiles_x = int(view_w / (tile_px * cam.zoom)) + 4
9. Değeri/alanı oluştur veya güncelle: tiles_y = int(view_h / (tile_px * cam.zoom)) + 4
10. Değeri/alanı oluştur veya güncelle: x0 = clamp(int(cam.x) - tiles_x // 2, 0, map_w - 1)
11. Değeri/alanı oluştur veya güncelle: x1 = clamp(int(cam.x) + tiles_x // 2, 0, map_w - 1)
12. Değeri/alanı oluştur veya güncelle: y0 = clamp(int(cam.y) - tiles_y // 2, 0, map_h - 1)
13. Değeri/alanı oluştur veya güncelle: y1 = clamp(int(cam.y) + tiles_y // 2, 0, map_h - 1)
14. Her öğe için işle: ty ← range(y0, y1 + 1)
15. Koşula göre yol seç: show_effect_global
16. Her öğe için işle: ent ← entities
17. Koşula göre yol seç: route_preview
18. Koşula göre yol seç: hover_tx is not None and hover_ty is not None
19. Her öğe için işle: (i, e) ← enumerate(entities)

**Gerçek kaynak:**

```python
def draw_world(screen, cam: Camera, tile_px: float, show_grid: bool,
               entities: list[Entity], hover_tx, hover_ty, selected_entity_idx: int | None,
               map_w: int, map_h: int, icons: dict, icon_cache: dict,
               show_effect_global: bool, field_cache: dict,
               route_preview: list[tuple[int, int]] | None = None,
               route_preview_invalid: bool = False):

    view_w = SCREEN_W - PANEL_W
    view_h = SCREEN_H
    view_cx = view_w / 2
    view_cy = view_h / 2

    def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))

    tw = max(1, int(tile_px * cam.zoom))
    th = max(1, int(tile_px * cam.zoom))

    tiles_x = int(view_w / (tile_px * cam.zoom)) + 4
    tiles_y = int(view_h / (tile_px * cam.zoom)) + 4

    x0 = clamp(int(cam.x) - tiles_x // 2, 0, map_w - 1)
    x1 = clamp(int(cam.x) + tiles_x // 2, 0, map_w - 1)
    y0 = clamp(int(cam.y) - tiles_y // 2, 0, map_h - 1)
    y1 = clamp(int(cam.y) + tiles_y // 2, 0, map_h - 1)

    # Tiles + grid
    for ty in range(y0, y1 + 1):
        for tx in range(x0, x1 + 1):
            sx, sy = world_to_screen(tx, ty)
            rect = pygame.Rect(sx, sy, tw, th)

            pygame.draw.rect(screen, (24, 24, 28) if (tx + ty) % 2 == 0 else (22, 22, 26), rect)
            if show_grid:
                pygame.draw.rect(screen, (35, 35, 40), rect, 1)

    # Effects (behind entities)
    if show_effect_global:
        for e in entities:
            if not e.show_effect:
                continue
            if e.kind in (Kind.SOURCE, Kind.BURNED) and e.source is not None:
                sp = e.source
                radius_px = int(round(sp.range_tiles * tile_px * cam.zoom))
                if radius_px <= 0:
                    continue

                base_rgb = (255, 170, 60) if sp.stype == SourceType.TEMP else (90, 220, 120)
                alpha = int(clamp(40 + sp.power * 16, 40, 220))

                blob = make_gauss_field_surface(
                    field_cache,
                    key=("blob", sp.stype.value, radius_px, alpha),
                    radius_px=radius_px,
                    rgba=(base_rgb[0], base_rgb[1], base_rgb[2], alpha),
                )
                if blob is None:
                    continue

                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)
                screen.blit(blob, blob.get_rect(center=(cx_s, cy_s)))

        for e in entities:
            if not e.show_effect:
                continue
            if e.kind == Kind.SENSOR and e.sensor is not None and e.sensor.active:
                cx_s, cy_s = world_to_screen(e.tx + 0.5, e.ty + 0.5)
                max_r = max(1, int(e.sensor.range_tiles))
                for r_tiles in range(1, max_r + 1):
                    radius_px = int(round(r_tiles * tile_px * cam.zoom))
                    draw_dashed_circle(screen, (cx_s, cy_s), radius_px, (255, 255, 255, 90))


    # UAV route overlays (per-UAV toggle)
    for ent in entities:
        if ent.kind == Kind.UAV and ent.uav is not None:
            up = ent.uav
            if up.show_route and up.route and len(up.route) >= 1:
                draw_route_overlay(screen, cam, tile_px, up.route, map_w, map_h, SCREEN_W - PANEL_W)

    # Route preview overlay
    if route_preview:
        col = (220, 60, 60) if route_preview_invalid else (220, 220, 230)
        draw_route_overlay(screen, cam, tile_px, route_preview, map_w, map_h, SCREEN_W - PANEL_W, line_color=col)

    # Hover highlight
    if hover_tx is not None and hover_ty is not None:
        hsx, hsy = world_to_screen(hover_tx, hover_ty)
        pygame.draw.rect(screen, (245, 245, 245), pygame.Rect(hsx, hsy, tw, th), 2)

    # Entities
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue  # carried items are drawn on UAV

        if not (0 <= e.tx < map_w and 0 <= e.ty < map_h):
            continue

        sx, sy = world_to_screen(e.tx, e.ty)
        r = pygame.Rect(sx, sy, tw, th)

        icon_key = None
        icon_src = None

        if e.kind == Kind.SENSOR:
            icon_key = "sensor"
            icon_src = icons.get("sensor")
        elif e.kind == Kind.OBSTACLE:
            icon_key = "obstacle"
            icon_src = icons.get("obstacle")
        elif e.kind == Kind.SOURCE and e.source:
            if e.source.stype == SourceType.TEMP:
                if e.icon_override == "burned":
                    icon_key = "burned"
                    icon_src = icons.get("burned")
                else:
                    icon_key = "source_temp"
                    icon_src = icons.get("source_temp")
            else:
                icon_key = "source_gas"
                icon_src = icons.get("source_gas")
        elif e.kind == Kind.BURNED and e.source:
            icon_key = "burned"
            icon_src = icons.get("burned")
        elif e.kind == Kind.UAV:
            icon_key = "drone"
            icon_src = icons.get("drone")

        scaled = get_scaled_icon(icon_cache, icon_key or "none", icon_src, (tw, th))

        if scaled is not None:
            screen.blit(scaled, (r.x, r.y))
        else:
            if e.kind == Kind.OBSTACLE:
                pygame.draw.rect(screen, (40, 90, 45), r)
            elif e.kind == Kind.SOURCE:
                pygame.draw.rect(
                    screen,
                    (150, 70, 70) if e.source and e.source.stype == SourceType.TEMP else (150, 120, 70),
                    r
                )
            elif e.kind == Kind.BURNED:
                pygame.draw.rect(screen, (150, 70, 70), r)
            elif e.kind == Kind.SENSOR:
                pygame.draw.rect(screen, (70, 70, 90) if e.sensor and not e.sensor.active else (60, 120, 170), r)
            elif e.kind == Kind.UAV:
                pygame.draw.rect(screen, (160, 160, 180), r)

        # Draw carried items on UAV
        if e.kind == Kind.UAV and e.uav:
            up = e.uav
            # anchor points relative to UAV rect
            pad = int(0.4 * min(tw, th))
            # small icon size
            cs = max(8, int(min(tw, th) * 0.45))
            # positions
            slots_pos = []
            # 1: top center
            slots_pos_1 = [(r.centerx, r.y + pad)]
            # 2: top-left & top-right
            slots_pos_2 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad)]
            # 3: top-left, top-right, bottom-center
            slots_pos_3 = [(r.x + pad, r.y + pad), (r.right - pad, r.y + pad), (r.centerx, r.bottom - pad)]

            carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
            carried = [c for c in carried if c is not None]

            # If sensor carried, draw under UAV
            sensor_carried = [c for c in carried if c.kind == Kind.SENSOR]
            source_carried = [c for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED)]

            # Draw sources on top
            nsrc = len(source_carried)
            if nsrc == 1:
                slots_pos = slots_pos_1
            elif nsrc == 2:
                slots_pos = slots_pos_2
            elif nsrc >= 3:
                slots_pos = slots_pos_3

            for idx_s, c in enumerate(source_carried[:3]):
                px, py = slots_pos[idx_s]
                icon_key2 = ("burned" if (c.kind == Kind.BURNED or c.icon_override == "burned") else ("source_temp" if c.source and c.source.stype == SourceType.TEMP else "source_gas"))
                icon_src2 = icons.get(icon_key2)
                sc = get_scaled_icon(icon_cache, f"carry_{icon_key2}", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(px, py)))

            # Draw sensor under UAV (center bottom)
            if sensor_carried:
                c = sensor_carried[0]
                icon_src2 = icons.get("sensor")
                sc = get_scaled_icon(icon_cache, "carry_sensor", icon_src2, (cs, cs))
                if sc:
                    screen.blit(sc, sc.get_rect(center=(r.centerx, r.bottom + cs // 3)))

        if selected_entity_idx == i:
            pygame.draw.rect(screen, (240, 240, 240), r, 2)
```

### draw_world.world_to_screen — satır 883

Kamera merkezi, görünüm alanı ve zoom ile dünya noktasını piksele çevirir.

**Girdiler:** wx, wy. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (int(round(sx)), int(round(sy)))
**Atanan yerel değerler / durum alanları:** sx, sy
**Bağlandığı işlevler:** int, round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
2. Değeri/alanı oluştur veya güncelle: sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
3. Çağırana sonucu döndür: (int(round(sx)), int(round(sy)))

**Gerçek kaynak:**

```python
def world_to_screen(wx, wy):
        sx = view_cx + (wx - cam.x) * tile_px * cam.zoom
        sy = view_cy + (wy - cam.y) * tile_px * cam.zoom
        return int(round(sx)), int(round(sy))
```

### can_attach_to_uav — satır 1076

Taşıyıcı türü, yük türü, zaten taşınma ve kapasite kurallarını kontrol eder.

**Girdiler:** entities: list[Entity], uav: Entity, candidate: Entity. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; True; nsrc < 3
**Atanan yerel değerler / durum alanları:** up, carried, have_sensor, have_source, nsrc
**Bağlandığı işlevler:** find_entity_by_id, any, sum
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: uav.kind != Kind.UAV or uav.uav is None
2. Koşula göre yol seç: candidate.kind not in (Kind.SOURCE, Kind.SENSOR, Kind.BURNED)
3. Koşula göre yol seç: candidate.carried_by is not None
4. Değeri/alanı oluştur veya güncelle: up = uav.uav
5. Değeri/alanı oluştur veya güncelle: carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
6. Değeri/alanı oluştur veya güncelle: carried = [c for c in carried if c is not None]
7. Değeri/alanı oluştur veya güncelle: have_sensor = any((c.kind == Kind.SENSOR for c in carried))
8. Değeri/alanı oluştur veya güncelle: have_source = any((c.kind in (Kind.SOURCE, Kind.BURNED) for c in carried))
9. Koşula göre yol seç: candidate.kind == Kind.SENSOR
10. Koşula göre yol seç: have_sensor
11. Değeri/alanı oluştur veya güncelle: nsrc = sum((1 for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED)))
12. Çağırana sonucu döndür: nsrc < 3

**Gerçek kaynak:**

```python
def can_attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if uav.kind != Kind.UAV or uav.uav is None:
        return False
    if candidate.kind not in (Kind.SOURCE, Kind.SENSOR, Kind.BURNED):
        return False
    if candidate.carried_by is not None:
        return False

    up = uav.uav
    carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
    carried = [c for c in carried if c is not None]

    have_sensor = any(c.kind == Kind.SENSOR for c in carried)
    have_source = any(c.kind in (Kind.SOURCE, Kind.BURNED) for c in carried)

    if candidate.kind == Kind.SENSOR:
        # Must be empty OR already sensor? (only 1 sensor total)
        if have_source:
            return False
        if have_sensor:
            return False
        return True

    # candidate is SOURCE
    if have_sensor:
        return False
    # max 3 sources
    nsrc = sum(1 for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED))
    return nsrc < 3
```

### attach_to_uav — satır 1107

Uygun yükü drone'a bağlar; kimlik listesi, taşıyıcı ve konumu birlikte günceller.

**Girdiler:** entities: list[Entity], uav: Entity, candidate: Entity. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; True
**Atanan yerel değerler / durum alanları:** up, candidate.carried_by, candidate.tx, candidate.ty
**Bağlandığı işlevler:** can_attach_to_uav, up.carrying_ids.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: not can_attach_to_uav(entities, uav, candidate)
2. Değeri/alanı oluştur veya güncelle: up = uav.uav
3. Koşula göre yol seç: up is None
4. Yan etki/çağrı adımını çalıştır: up.carrying_ids.append(candidate.id)
5. Değeri/alanı oluştur veya güncelle: candidate.carried_by = uav.id
6. Değeri/alanı oluştur veya güncelle: candidate.tx = uav.tx
7. Değeri/alanı oluştur veya güncelle: candidate.ty = uav.ty
8. Çağırana sonucu döndür: True

**Gerçek kaynak:**

```python
def attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if not can_attach_to_uav(entities, uav, candidate):
        return False
    up = uav.uav
    if up is None:
        return False
    up.carrying_ids.append(candidate.id)
    candidate.carried_by = uav.id
    candidate.tx = uav.tx
    candidate.ty = uav.ty
    return True
```

### main — satır 1123

Komut seçeneklerini/başlangıç nesnelerini kurup programın ana akışını başlatır.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** screen, clock, font, small, (MAP_W, MAP_H), tile_px, cam, cam.x, cam.y, show_grid, show_effect_global, entities, next_id, selected_tool, selected_entity_idx, uav_focus_cargo_id, collapsed_cargo_ids, sim_running, sim_time, tick_accum, spread_accum, left_down, left_down_pos, dragging_entity_idx, dragging_start, dragging_active, route_editing, route_edit_points, route_backup, route_edit_uav_id, route_preview_invalid, ui_msg_text, ui_msg_timer, icons, icon_cache, field_cache, panel_x, SCROLL_Y0, panel_scroll, last_selected_entity_id, running, dt, (mx, my), hover_tx, hover_ty, (wx, wy), ht, hy, (hover_tx, hover_ty), (tool_buttons, panel_clickables, global_rows, entity_rows, global_sw_rect, ent_sw_rect, selected_entity, panel_content_bottom), panel_clickables[idx], cur_sel_id, cargo_slots, dying, parent, dying.carried_by, ce, ce.carried_by, e, e.uav.route, e.uav.route_mode, e.uav.route_i, e.uav.route_dir, scroll_step, scroll_bottom_limit, max_scroll, mods, ctrl, shift, pan_tiles, idx, uav_ent, cand, clicked, rr, target_id, seg_rect, half, e.source.stype, (tx, ty), obstacles_set, idx_here, up, bp, preview, banner, msg, y_off, box_w, box, sim_label, (_, sw_rect, text, on), label, seg_rects_live, scroll_clip, prev_clip, rtype, (_, sw_rect, label_text, on), sw_r, (_, rect, label_text), (_, rect, label_text, _cid), (_, y, label_text, minus_rect, plus_rect, step_hint), ry, m2, p2, (_, rect, options, current), (_, y, t), slots, idx_txt, icon_key2, icon_src2, sc, letter, txt, d, stats, hint_lines, hint_y0
**Bağlandığı işlevler:** pygame.init, pygame.display.set_mode, pygame.display.set_caption, pygame.time.Clock, pygame.font.SysFont, Camera, cam.clamp_zoom_for_map, set, load_icon, os.path.join, clock.tick, pygame.mouse.get_pos, max, cam.screen_to_world, int, math.floor, update_uavs, simulate_tick, spread_fire, build_panel_layout, enumerate, len, pygame.event.get, route_edit_points.clear, find_entity_by_id, parent.uav.carrying_ids.remove, list, dying.uav.carrying_ids.clear, entities.pop, push_msg, min, pygame.key.get_mods, cam.zoom_at, icon_cache.clear, field_cache.clear, clamp, find_entity_at, any, r.move(0, -panel_scroll).collidepoint, r.move, attach_to_uav, r.collidepoint, rr.collidepoint, callable, action, isinstance, seg_rect.move, seg_rect.collidepoint, route_edit_points.append, route_is_valid, entities.append, Entity, SensorProps, SourceProps, UavProps, float, abs, screen.fill, draw_world, pygame.Surface, banner.fill, screen.blit, small.render, box.fill, pygame.draw.rect, pygame.draw.line, font.render, draw_button, draw_section_title, draw_switch, pygame.Rect, screen.get_clip, screen.set_clip, sw_rect.move, rect.move, draw_small_btn, minus_rect.move, plus_rect.move, str, draw_segmented, slots.append, icons.get, get_scaled_icon, sc.get_rect, txt.get_rect, pygame.draw.circle, pygame.display.flip, pygame.quit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.init()
2. Değeri/alanı oluştur veya güncelle: screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
3. Yan etki/çağrı adımını çalıştır: pygame.display.set_caption('IoT Grid Sim (NO ROTATE)')
4. Değeri/alanı oluştur veya güncelle: clock = pygame.time.Clock()
5. Değeri/alanı oluştur veya güncelle: font = pygame.font.SysFont('DejaVu Sans', 18)
6. Değeri/alanı oluştur veya güncelle: small = pygame.font.SysFont('DejaVu Sans', 14)
7. Değeri/alanı oluştur veya güncelle: MAP_W, MAP_H = (200, 200)
8. Değeri/alanı oluştur veya güncelle: tile_px = DEFAULT_TILE
9. Değeri/alanı oluştur veya güncelle: cam = Camera()
10. Yan etki/çağrı adımını çalıştır: cam.clamp_zoom_for_map(tile_px, MAP_W, MAP_H)
11. Değeri/alanı oluştur veya güncelle: cam.x = (MAP_W - 1) / 2
12. Değeri/alanı oluştur veya güncelle: cam.y = (MAP_H - 1) / 2
13. Değeri/alanı oluştur veya güncelle: show_grid = True
14. Değeri/alanı oluştur veya güncelle: show_effect_global = True
15. Değeri/alanı oluştur veya güncelle: entities: list[Entity] = []
16. Değeri/alanı oluştur veya güncelle: next_id = 1
17. Değeri/alanı oluştur veya güncelle: selected_tool: Kind | None = None
18. Değeri/alanı oluştur veya güncelle: selected_entity_idx: int | None = None
19. Değeri/alanı oluştur veya güncelle: uav_focus_cargo_id: int | None = None
20. Değeri/alanı oluştur veya güncelle: collapsed_cargo_ids: set[int] = set()
21. Değeri/alanı oluştur veya güncelle: sim_running = False
22. Değeri/alanı oluştur veya güncelle: sim_time = 0.0
23. Değeri/alanı oluştur veya güncelle: tick_accum = 0.0
24. Değeri/alanı oluştur veya güncelle: spread_accum = 0.0
25. Değeri/alanı oluştur veya güncelle: left_down = False
26. Değeri/alanı oluştur veya güncelle: left_down_pos = (0, 0)
27. Değeri/alanı oluştur veya güncelle: dragging_entity_idx: int | None = None
28. Değeri/alanı oluştur veya güncelle: dragging_start = (0, 0)
29. Değeri/alanı oluştur veya güncelle: dragging_active = False
30. Değeri/alanı oluştur veya güncelle: route_editing = False
31. Değeri/alanı oluştur veya güncelle: route_edit_points: list[tuple[int, int]] = []
32. Değeri/alanı oluştur veya güncelle: route_backup: list[tuple[int, int]] = []
33. Değeri/alanı oluştur veya güncelle: route_edit_uav_id: int | None = None
34. Değeri/alanı oluştur veya güncelle: route_preview_invalid = False
35. Değeri/alanı oluştur veya güncelle: ui_msg_text = ''
36. Değeri/alanı oluştur veya güncelle: ui_msg_timer = 0.0
37. Değeri/alanı oluştur veya güncelle: icons = {'sensor': load_icon(os.path.join('assets', 'sensor.png')), 'source_temp': load_icon(os.path.join('assets', 'source_temp.png')), 'source_gas': load_icon(os.path.join('assets', 'source_gas.png')), 'obstacle': load…
38. Değeri/alanı oluştur veya güncelle: icon_cache: dict = {}
39. Değeri/alanı oluştur veya güncelle: field_cache: dict = {}
40. Değeri/alanı oluştur veya güncelle: panel_x = SCREEN_W - PANEL_W
41. Değeri/alanı oluştur veya güncelle: SCROLL_Y0 = PANEL_SCROLL_Y0
42. Değeri/alanı oluştur veya güncelle: panel_scroll = 0
43. Değeri/alanı oluştur veya güncelle: last_selected_entity_id = None
44. Yerel yardımcı tanımla: push_msg; ayrı sembol kaydı aşağıdadır.
45. Değeri/alanı oluştur veya güncelle: running = True
46. Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: running
47. Yan etki/çağrı adımını çalıştır: pygame.quit()

**Gerçek kaynak:**

```python
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("IoT Grid Sim (NO ROTATE)")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("DejaVu Sans", 18)
    small = pygame.font.SysFont("DejaVu Sans", 14)

    MAP_W, MAP_H = 200, 200
    tile_px = DEFAULT_TILE

    cam = Camera()
    cam.clamp_zoom_for_map(tile_px, MAP_W, MAP_H)
    cam.x = (MAP_W - 1) / 2
    cam.y = (MAP_H - 1) / 2

    show_grid = True
    show_effect_global = True

    entities: list[Entity] = []
    next_id = 1

    selected_tool: Kind | None = None
    selected_entity_idx: int | None = None

    # Panel: when UAV selected, you can click a carried item to show its details below UAV properties
    uav_focus_cargo_id: int | None = None
    collapsed_cargo_ids: set[int] = set()

    sim_running = False
    sim_time = 0.0
    tick_accum = 0.0
    spread_accum = 0.0

    # Left mouse state (click / drag)
    left_down = False
    left_down_pos = (0, 0)

    # Drag state (entity -> panel slots)
    dragging_entity_idx: int | None = None
    dragging_start = (0, 0)
    dragging_active = False

    # Route edit
    route_editing = False
    route_edit_points: list[tuple[int, int]] = []
    route_backup: list[tuple[int, int]] = []
    route_edit_uav_id: int | None = None
    route_preview_invalid = False

    ui_msg_text = ""
    ui_msg_timer = 0.0

    # Assets (optional)
    icons = {
        "sensor": load_icon(os.path.join("assets", "sensor.png")),
        "source_temp": load_icon(os.path.join("assets", "source_temp.png")),
        "source_gas": load_icon(os.path.join("assets", "source_gas.png")),
        "obstacle": load_icon(os.path.join("assets", "obstacle.png")),
        "burned": load_icon(os.path.join("assets", "burned.png")),
        "drone": load_icon(os.path.join("assets", "drone.png")),  # <= senin istediğin
    }
    icon_cache: dict = {}
    field_cache: dict = {}

    panel_x = SCREEN_W - PANEL_W
    SCROLL_Y0 = PANEL_SCROLL_Y0

    panel_scroll = 0
    last_selected_entity_id = None

    def push_msg(text: str, secs: float = 2.0):
        nonlocal ui_msg_text, ui_msg_timer
        ui_msg_text = text
        ui_msg_timer = secs

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        mx, my = pygame.mouse.get_pos()

        if ui_msg_timer > 0.0:
            ui_msg_timer = max(0.0, ui_msg_timer - dt)

        # Hover tile
        hover_tx = None
        hover_ty = None
        if mx < panel_x:
            wx, wy = cam.screen_to_world((mx, my), tile_px)
            ht = int(math.floor(wx + 1e-6))
            hy = int(math.floor(wy + 1e-6))
            if 0 <= ht < MAP_W and 0 <= hy < MAP_H:
                hover_tx, hover_ty = ht, hy

        # Per-frame UAV motion (only when sim is running)
        if sim_running:
            update_uavs(entities, dt, MAP_W, MAP_H)

        # Simulation tick
        if sim_running:
            tick_accum += dt
            while tick_accum >= TICK_SECONDS:
                tick_accum -= TICK_SECONDS
                sim_time += TICK_SECONDS
                simulate_tick(entities, TICK_SECONDS)
                spread_accum += TICK_SECONDS
                while spread_accum >= 2.0:
                    spread_accum -= 2.0
                    spread_fire(entities)

        tool_buttons, panel_clickables, global_rows, entity_rows, global_sw_rect, ent_sw_rect, selected_entity, panel_content_bottom = build_panel_layout(
            entities, selected_tool, selected_entity_idx, panel_x, small, font, show_effect_global, uav_focus_cargo_id, collapsed_cargo_ids
        )

        # Wire global switch callback
        for idx, (r, action) in enumerate(panel_clickables):
            if r == global_sw_rect:
                def _toggle_global():
                    nonlocal show_effect_global
                    show_effect_global = not show_effect_global
                panel_clickables[idx] = (r, _toggle_global)
                break

        # Reset panel scroll / UAV cargo focus when selection changes
        cur_sel_id = entities[selected_entity_idx].id if (selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities)) else None
        if cur_sel_id != last_selected_entity_id:
            panel_scroll = 0
            uav_focus_cargo_id = None
            last_selected_entity_id = cur_sel_id
        # Identify cargo slot rects for drop detection
        cargo_slots: list[pygame.Rect] = []
        for row in entity_rows:
            if row[0] == "cargo_slots":
                cargo_slots = row[1]
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    show_grid = not show_grid
                elif event.key == pygame.K_SPACE:
                    sim_running = not sim_running
                elif event.key == pygame.K_ESCAPE:
                    selected_tool = None
                    selected_entity_idx = None
                    route_editing = False
                    route_preview_invalid = False
                    route_edit_points.clear()
                    route_backup = []
                    route_edit_uav_id = None
                elif event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        # detach cargo if deleting UAV
                        dying = entities[selected_entity_idx]
                        # If deleting a carried entity, unlink it from the UAV cargo list
                        if dying.carried_by is not None:
                            parent = find_entity_by_id(entities, dying.carried_by)
                            if parent and parent.kind == Kind.UAV and parent.uav:
                                if dying.id in parent.uav.carrying_ids:
                                    parent.uav.carrying_ids.remove(dying.id)
                            dying.carried_by = None

                        if dying.kind == Kind.UAV and dying.uav:
                            for cid in list(dying.uav.carrying_ids):
                                ce = find_entity_by_id(entities, cid)
                                if ce:
                                    ce.carried_by = None
                            dying.uav.carrying_ids.clear()
                        entities.pop(selected_entity_idx)
                        selected_entity_idx = None
                elif event.key == pygame.K_k:
                    # UAV route edit toggle (only when UAV selected)
                    if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        e = entities[selected_entity_idx]
                        if e.kind == Kind.UAV and e.uav is not None:
                            if not route_editing:
                                # Enter edit mode: start collecting waypoints
                                route_editing = True
                                route_edit_points = []
                                route_preview_invalid = False
                                route_backup = list(e.uav.route)
                                route_edit_uav_id = e.id
                            else:
                                # Exit edit mode:
                                # - If user provided <2 points, treat as cancel (keep old route)
                                # - Otherwise finalize new route for the same UAV
                                if route_edit_uav_id == e.id and len(route_edit_points) >= 2 and (not route_preview_invalid):
                                    e.uav.route = list(route_edit_points)
                                    if e.uav.route and e.uav.route[0] == e.uav.route[-1]:
                                        e.uav.route_mode = RouteMode.LOOP
                                    else:
                                        e.uav.route_mode = RouteMode.PINGPONG
                                    e.uav.route_i = 0
                                    e.uav.route_dir = 1
                                else:
                                    e.uav.route = list(route_backup)
                                    if route_edit_uav_id == e.id and len(route_edit_points) >= 2 and route_preview_invalid:
                                        push_msg("Rota engelin üzerinden geçiyor. Tekrar dene.")

                                route_editing = False
                                route_preview_invalid = False
                                route_edit_points = []
                                route_backup = []
                                route_edit_uav_id = None
                        else:
                            # If somehow K is pressed while editing but UAV not selected, just cancel edit mode.
                            if route_editing:
                                route_editing = False
                                route_preview_invalid = False
                                route_edit_points = []
                                route_backup = []
                                route_edit_uav_id = None

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Wheel: zoom on world, scroll on panel (when an entity is selected)
                if event.button in (4, 5):
                    # Panel scroll (only when an entity is selected)
                    if mx >= panel_x and selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                        scroll_step = 40
                        if event.button == 4:
                            panel_scroll = max(0, panel_scroll - scroll_step)
                        else:
                            scroll_bottom_limit = SCREEN_H - 20
                            max_scroll = max(0, panel_content_bottom - scroll_bottom_limit)
                            panel_scroll = min(max_scroll, panel_scroll + scroll_step)
                    else:
                        mods = pygame.key.get_mods()
                        ctrl = (mods & pygame.KMOD_CTRL) != 0
                        shift = (mods & pygame.KMOD_SHIFT) != 0

                        if ctrl:
                            # Ctrl + Wheel => zoom
                            if event.button == 4:
                                cam.zoom_at(1.12, tile_px, MAP_W, MAP_H)
                            else:
                                cam.zoom_at(1 / 1.12, tile_px, MAP_W, MAP_H)
                            icon_cache.clear()
                            field_cache.clear()
                        else:
                            # Wheel => move map (Shift => horizontal)
                            pan_tiles = 6.0 / max(0.2, cam.zoom)
                            if shift:
                                cam.x += (-pan_tiles if event.button == 4 else pan_tiles)
                            else:
                                cam.y += (-pan_tiles if event.button == 4 else pan_tiles)

                            cam.x = clamp(cam.x, 0.0, MAP_W - 1.0)
                            cam.y = clamp(cam.y, 0.0, MAP_H - 1.0)

                # Left press: start possible drag
                elif event.button == 1:
                    left_down = True
                    left_down_pos = (mx, my)

                    # potential entity drag start (only on map)
                    if mx < panel_x and hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        dragging_entity_idx = idx
                        dragging_start = (mx, my)
                        dragging_active = False

                # Right click: delete entity on hovered tile
                elif event.button == 3 and mx < panel_x:
                    if hover_tx is not None:
                        idx = find_entity_at(entities, hover_tx, hover_ty)
                        if idx is not None:
                            entities.pop(idx)
                            if selected_entity_idx == idx:
                                selected_entity_idx = None
                            elif selected_entity_idx is not None and selected_entity_idx > idx:
                                selected_entity_idx -= 1

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if left_down:
                        # If dragging entity to panel
                        if dragging_entity_idx is not None and dragging_active:
                            if mx >= panel_x and cargo_slots and selected_entity_idx is not None:
                                uav_ent = entities[selected_entity_idx]
                                cand = entities[dragging_entity_idx]
                                # drop into any slot rect
                                if any(r.move(0, -panel_scroll).collidepoint(mx, my) for r in cargo_slots):
                                    if uav_ent.kind == Kind.UAV:
                                        attach_to_uav(entities, uav_ent, cand)

                        else:
                            if mx >= panel_x:
                                # Panel click
                                clicked = False

                                for k, r, _ in tool_buttons:
                                    if r.collidepoint(mx, my):
                                        selected_tool = k
                                        selected_entity_idx = None
                                        uav_focus_cargo_id = None
                                        panel_scroll = 0
                                        clicked = True
                                        break
                                if clicked:
                                    left_down = False
                                    dragging_entity_idx = None
                                    dragging_active = False
                                    continue

                                # Panel element clicks (with scroll offset for entity section)
                                for r, action in panel_clickables:
                                    rr = r
                                    if selected_entity_idx is not None and rr.y >= SCROLL_Y0:
                                        rr = r.move(0, -panel_scroll)

                                    if rr.collidepoint(mx, my):
                                        if callable(action):
                                            action()
                                        elif isinstance(action, tuple) and len(action) >= 2:
                                            if action[0] == "select_entity_id":
                                                target_id = action[1]
                                                for ii, ee in enumerate(entities):
                                                    if ee.id == target_id:
                                                        selected_entity_idx = ii
                                                        selected_tool = None
                                                        break
                                            elif action[0] == "uav_focus_cargo":
                                                uav_focus_cargo_id = action[1]
                                        clicked = True
                                        break

                                # Source segmented clicks (handled here)
                                if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                    e = entities[selected_entity_idx]
                                    if e.kind == Kind.SOURCE and e.source:
                                        for row in entity_rows:
                                            if row[0] == "segmented":
                                                seg_rect = row[1]
                                                if selected_entity_idx is not None and seg_rect.y >= SCROLL_Y0:
                                                    seg_rect = seg_rect.move(0, -panel_scroll)
                                                if seg_rect.collidepoint(mx, my):
                                                    # determine segment
                                                    half = seg_rect.width // 2
                                                    if mx < seg_rect.x + half:
                                                        e.source.stype = SourceType.TEMP
                                                    else:
                                                        e.source.stype = SourceType.GAS
                                                    clicked = True
                                                break
                            else:
                                # Map click: place/select or route edit point
                                if hover_tx is not None:
                                    tx, ty = hover_tx, hover_ty

                                    if route_editing:
                                        # add waypoint (avoid obstacles)
                                        obstacles_set = {(o.tx, o.ty) for o in entities if o.kind == Kind.OBSTACLE and o.carried_by is None}
                                        if (tx, ty) in obstacles_set:
                                            push_msg("Engelin üstüne waypoint koyamazsın. Tekrar dene.")
                                        else:
                                            route_edit_points.append((tx, ty))
                                            route_preview_invalid = (not route_is_valid(route_edit_points, obstacles_set))
                                            if route_preview_invalid:
                                                push_msg("Rota engelin üzerinden geçiyor. Tekrar dene.")
                                    else:
                                        if selected_tool is not None:
                                            # If you click an existing entity while a tool is selected, just select it.
                                            idx_here = find_entity_at(entities, tx, ty)
                                            if idx_here is not None:
                                                selected_entity_idx = idx_here
                                            else:
                                                if selected_tool == Kind.SENSOR:
                                                    entities.append(Entity(id=next_id, kind=Kind.SENSOR, tx=tx, ty=ty, sensor=SensorProps()))
                                                    next_id += 1
                                                elif selected_tool == Kind.SOURCE:
                                                    entities.append(Entity(id=next_id, kind=Kind.SOURCE, tx=tx, ty=ty, source=SourceProps()))
                                                    next_id += 1
                                                elif selected_tool == Kind.OBSTACLE:
                                                    entities.append(Entity(id=next_id, kind=Kind.OBSTACLE, tx=tx, ty=ty))
                                                    next_id += 1
                                                elif selected_tool == Kind.UAV:
                                                    up = UavProps(speed=3.0, x=float(tx), y=float(ty))
                                                    entities.append(Entity(id=next_id, kind=Kind.UAV, tx=tx, ty=ty, uav=up))
                                                    next_id += 1
                                                elif selected_tool == Kind.BURNED:
                                                    bp = SourceProps(stype=SourceType.TEMP, power=3, range_tiles=3)
                                                    entities.append(Entity(id=next_id, kind=Kind.BURNED, tx=tx, ty=ty, source=bp, icon_override='burned'))
                                                    next_id += 1

                                        else:
                                            selected_entity_idx = find_entity_at(entities, tx, ty)

                    left_down = False
                    dragging_entity_idx = None
                    dragging_active = False

            elif event.type == pygame.MOUSEMOTION:
                if left_down:
                    # Detect entity drag (only for UAV cargo)
                    if dragging_entity_idx is not None and not dragging_active:
                        if abs(mx - dragging_start[0]) >= DRAG_THRESHOLD_PX or abs(my - dragging_start[1]) >= DRAG_THRESHOLD_PX:
                            # Start drag ONLY if selected is UAV and candidate is draggable
                            if selected_entity_idx is not None and 0 <= selected_entity_idx < len(entities):
                                uav_ent = entities[selected_entity_idx]
                                cand = entities[dragging_entity_idx]
                                if uav_ent.kind == Kind.UAV and cand.kind in (Kind.SOURCE, Kind.SENSOR) and cand.carried_by is None:
                                    dragging_active = True

        # =============================
        # DRAW
        # =============================
        screen.fill((18, 18, 22))

        # Route preview points (editing) or show selected UAV route (optional)
        preview = route_edit_points if route_editing else None

        draw_world(
            screen, cam, tile_px, show_grid,
            entities, hover_tx, hover_ty, selected_entity_idx,
            MAP_W, MAP_H, icons, icon_cache,
            show_effect_global, field_cache,
            route_preview=preview,
            route_preview_invalid=route_preview_invalid
        )

        # Route edit banner (top-left of world view)
        if route_editing:
            banner = pygame.Surface((SCREEN_W - PANEL_W, 34), pygame.SRCALPHA)
            banner.fill((0, 0, 0, 120))
            screen.blit(banner, (0, 0))
            msg = "ROTA DÜZENLEME MODU: Haritaya tıkla waypoint ekle | K: Bitir/İptal"
            screen.blit(small.render(msg, True, (245, 245, 245)), (12, 9))

        # Toast / warning message (top-left)
        if ui_msg_timer > 0.0 and ui_msg_text:
            y_off = 38 if route_editing else 8
            box_w = min(720, SCREEN_W - PANEL_W - 24)
            box = pygame.Surface((box_w, 30), pygame.SRCALPHA)
            box.fill((0, 0, 0, 160))
            screen.blit(box, (12, y_off))
            screen.blit(small.render(ui_msg_text, True, (245, 245, 245)), (20, y_off + 8))

        # Panel background
        pygame.draw.rect(screen, (14, 14, 16), (panel_x, 0, PANEL_W, SCREEN_H))
        pygame.draw.line(screen, (60, 60, 70), (panel_x, 0), (panel_x, SCREEN_H), 2)

        # Tools
        screen.blit(font.render("Araçlar", True, (240, 240, 240)), (panel_x + PAD, 25))
        for k, r, label in tool_buttons:
            draw_button(screen, r, label, font, active=(selected_tool == k))

        # Sim status
        sim_label = "RUNNING" if sim_running else "PAUSED"
        screen.blit(small.render(f"Sim: {sim_label}  (Space)", True, (220, 220, 220)), (panel_x + PAD, 320))
        screen.blit(small.render(f"Zaman: {sim_time:.0f}s", True, (200, 200, 200)), (panel_x + PAD, 340))

                # Appearance section (global)
        draw_section_title(screen, panel_x + PAD, PANEL_Y_APPEAR, "Görünüm", font, small)
        for row in global_rows:
            if row[0] == "switch":
                _, sw_rect, text, on = row
                draw_switch(screen, sw_rect, on)
                screen.blit(small.render(text, True, (200, 200, 200)), (sw_rect.right + 10, sw_rect.y + 4))

        # Selected section
        draw_section_title(screen, panel_x + PAD, PANEL_Y_SELECTED_TITLE, "Seçili", font, small)

        if selected_entity_idx is None or not (0 <= selected_entity_idx < len(entities)):
            screen.blit(small.render("Yok (haritadan bir entity seç)", True, (180, 180, 180)),
                        (panel_x + PAD, PANEL_Y_SELECTED_LABEL))
        else:
            e = entities[selected_entity_idx]
            label = f"{e.kind.value} @ ({e.tx},{e.ty})"
            if e.carried_by is not None:
                label += f"  [İHA #{e.carried_by} üzerinde]"
            screen.blit(small.render(label, True, (210, 210, 210)), (panel_x + PAD, PANEL_Y_SELECTED_LABEL))

            # Entity rows (scrollable)
            seg_rects_live = None

            scroll_clip = pygame.Rect(panel_x, SCROLL_Y0, PANEL_W, SCREEN_H - SCROLL_Y0)
            prev_clip = screen.get_clip()
            screen.set_clip(scroll_clip)

            for row in entity_rows:
                rtype = row[0]

                if rtype == "switch":
                    _, sw_rect, label_text, on = row
                    sw_r = sw_rect.move(0, -panel_scroll) if sw_rect.y >= SCROLL_Y0 else sw_rect
                    draw_switch(screen, sw_r, on)
                    screen.blit(small.render(label_text, True, (200, 200, 200)), (sw_r.right + 10, sw_r.y + 4))

                elif rtype == "mode_switch":
                    _, sw_rect, label_text, on = row
                    sw_r = sw_rect.move(0, -panel_scroll) if sw_rect.y >= SCROLL_Y0 else sw_rect
                    draw_switch(screen, sw_r, on)
                    screen.blit(small.render(label_text, True, (200, 200, 200)), (sw_r.right + 10, sw_r.y + 4))

                elif rtype == "button":
                    _, rect, label_text = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "carry_edit_btn":
                    _, rect, label_text, _cid = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "cargo_toggle":
                    _, rect, label_text = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_small_btn(screen, rr, label_text, small)

                elif rtype == "numeric":
                    # ("numeric", y, "Label: value", minus_rect, plus_rect, step_hint)
                    _, y, label_text, minus_rect, plus_rect, step_hint = row
                    ry = y - panel_scroll if y >= SCROLL_Y0 else y
                    m2 = minus_rect.move(0, -panel_scroll) if minus_rect.y >= SCROLL_Y0 else minus_rect
                    p2 = plus_rect.move(0, -panel_scroll) if plus_rect.y >= SCROLL_Y0 else plus_rect

                    screen.blit(small.render(label_text, True, (210, 210, 210)), (panel_x + PAD, ry))
                    draw_small_btn(screen, m2, "-", small)
                    draw_small_btn(screen, p2, "+", small)
                    if step_hint:
                        screen.blit(small.render(str(step_hint), True, (170, 170, 170)), (p2.right + 8, p2.y + 6))

                elif rtype == "segmented":
                    # ("segmented", rect, options, selected_idx)
                    _, rect, options, current = row
                    rr = rect.move(0, -panel_scroll) if rect.y >= SCROLL_Y0 else rect
                    draw_segmented(screen, rr, options, current, small)

                elif rtype == "text":
                    _, y, t = row
                    ry = y - panel_scroll if y >= SCROLL_Y0 else y
                    screen.blit(small.render(t, True, (180, 180, 180)), (panel_x + PAD, ry))

                elif rtype == "cargo_slots":
                    # ("cargo_slots", [rect, rect, rect])
                    slots = []
                    for r in row[1]:
                        slots.append(r.move(0, -panel_scroll) if r.y >= SCROLL_Y0 else r)

                    for i_slot, r in enumerate(slots):
                        pygame.draw.rect(screen, (55, 55, 55), r, border_radius=8)
                        pygame.draw.rect(screen, (90, 90, 90), r, width=2, border_radius=8)
                        idx_txt = small.render(str(i_slot + 1), True, (120, 120, 120))
                        screen.blit(idx_txt, (r.x + 6, r.y + 6))

                    uav_ent = entities[selected_entity_idx]
                    if uav_ent.uav:
                        for i_slot, cid in enumerate(uav_ent.uav.carrying_ids[:3]):
                            if i_slot >= len(slots):
                                break
                            ce = find_entity_by_id(entities, cid)
                            if ce is None:
                                continue

                            icon_key2 = None
                            if ce.kind == Kind.SENSOR:
                                icon_key2 = "sensor"
                            elif ce.kind in (Kind.SOURCE, Kind.BURNED) and ce.source:
                                if ce.icon_override == "burned":
                                    icon_key2 = "burned"
                                else:
                                    icon_key2 = "source_temp" if ce.source.stype == SourceType.TEMP else "source_gas"

                            icon_src2 = icons.get(icon_key2) if icon_key2 else None
                            sc = get_scaled_icon(icon_cache, f"panel_{icon_key2}", icon_src2, (26, 26))

                            if sc is not None:
                                screen.blit(sc, sc.get_rect(center=slots[i_slot].center))
                            else:
                                letter = "S" if ce.kind == Kind.SENSOR else ("T" if (ce.source and ce.source.stype == SourceType.TEMP) else "G")
                                txt = small.render(letter, True, (235, 235, 235))
                                screen.blit(txt, txt.get_rect(center=slots[i_slot].center))

            screen.set_clip(prev_clip)


        # Drag ghost
        if dragging_entity_idx is not None and dragging_active:
            d = entities[dragging_entity_idx]
            # simple ghost circle
            pygame.draw.circle(screen, (240, 240, 240), (mx, my), 10, 2)

        # Footer
        stats = f"Map: {MAP_W}x{MAP_H} | Zoom: {cam.zoom:.2f} | Entities: {len(entities)}"
        screen.blit(small.render(stats, True, (180, 180, 180)), (20, SCREEN_H - 26))

        hint_lines = [
            "Sol tık: Seç / (Araç seçiliyken) Ekle | Sağ tık: Sil | DEL/BKSP: Seçiliyi sil",
            "Wheel: Haritayı kaydır | Shift+Wheel: Yatay | Ctrl+Wheel: Zoom",
            "G: Izgara | Space: Sim (RUN/PAUSE)",
            "İHA seçiliyken: K rota edit (tıkla waypoint ekle, K ile bitir)",
            "Kaynak/Sensör: Haritadan sürükle -> İHA panelindeki slotlara bırak",
        ]
        hint_y0 = SCREEN_H - 26 - 8 - 18 * len(hint_lines)
        for i, line in enumerate(hint_lines):
            screen.blit(small.render(line, True, (170, 170, 170)), (20, hint_y0 + 18 * i))

        pygame.display.flip()

    pygame.quit()
```

### main.push_msg — satır 1195

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** text: str, secs: float=2.0. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** ui_msg_text, ui_msg_timer
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: ui_msg_text = text
2. Değeri/alanı oluştur veya güncelle: ui_msg_timer = secs

**Gerçek kaynak:**

```python
def push_msg(text: str, secs: float = 2.0):
        nonlocal ui_msg_text, ui_msg_timer
        ui_msg_text = text
        ui_msg_timer = secs
```

### main._toggle_global — satır 1241

İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** show_effect_global
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: show_effect_global = not show_effect_global

**Gerçek kaynak:**

```python
def _toggle_global():
                    nonlocal show_effect_global
                    show_effect_global = not show_effect_global
```


## iot_sim/IoT.py

Bazı model/motor/ölçüm adlarını yeniden sunan korunmuş uyumluluk modülüdür.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: from .models import *

```python
from .models import *
```

Satır 2: Gereken isimleri içeri al: from .engine import *

```python
from .engine import *
```

Satır 3: Gereken isimleri içeri al: from .sensors import *

```python
from .sensors import *
```


## iot_sim/__init__.py

Paketin dışarı sunduğu isimleri tanımlar; pencere açmaz.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: from .models import *

```python
from .models import *
```

Satır 2: Gereken isimleri içeri al: from .engine import *

```python
from .engine import *
```

Satır 3: Gereken isimleri içeri al: from .sensors import *

```python
from .sensors import *
```

Satır 4: Gereken isimleri içeri al: from .alarm_bridge import AlarmBridge

```python
from .alarm_bridge import AlarmBridge
```


## iot_sim/alarm_bridge.py

Tek kanal alarm kararı, durum geçişleri ve tekrarlı bildirim kotasını birleştirir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Tek alarm kararı; geçiş kaydı kotadan bağımsız, yalnız tekrarlar sınırlı."""
```

Satır 2: Gereken isimleri içeri al: from collections import deque

```python
from collections import deque
```

Satır 3: Gereken isimleri içeri al: from CALCULATOR import RateLimiter

```python
from CALCULATOR import RateLimiter
```

Satır 4: Gereken isimleri içeri al: from .sensors import VALUE_ATTR

```python
from .sensors import VALUE_ATTR
```

Satır 6: Değeri/alanı oluştur veya güncelle: STATUS_LABELS = {'WAITING': 'İlk ölçüm bekleniyor', 'OFF': 'Kapalı', 'EMPTY': 'Pil bitti', 'NORMAL': 'Normal', 'ALERT': 'Alarm'}

```python
STATUS_LABELS = {"WAITING": "İlk ölçüm bekleniyor", "OFF": "Kapalı", "EMPTY": "Pil bitti",
                 "NORMAL": "Normal", "ALERT": "Alarm"}
```

### AlarmBridge — satır 10

Sensör durumlarını, sınırlı olay geçmişini ve bildirim kotasını yönetir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
"""Sensör durumlarını, sınırlı olay geçmişini ve bildirim kotasını yönetir."""
```

### AlarmBridge.__init__ — satır 12

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, rate_limit=40, window_seconds=60, on_event=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.now, self.window_seconds, self.on_event, self.events, self.notifications, self.active_alerts, self.limiter_exhausted, self.states, self.flags, self.slots, self.last_written, self.last_repeat, self.total_events
**Bağlandığı işlevler:** deque
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.now = 0.0
2. Değeri/alanı oluştur veya güncelle: self.window_seconds = window_seconds
3. Değeri/alanı oluştur veya güncelle: self.on_event = on_event
4. Değeri/alanı oluştur veya güncelle: self.events = deque(maxlen=1000)
5. Değeri/alanı oluştur veya güncelle: self.notifications = deque(maxlen=200)
6. Değeri/alanı oluştur veya güncelle: self.active_alerts = {}
7. Değeri/alanı oluştur veya güncelle: self.limiter_exhausted = {}
8. Değeri/alanı oluştur veya güncelle: self.states = {}
9. Değeri/alanı oluştur veya güncelle: self.flags = {}
10. Değeri/alanı oluştur veya güncelle: self.slots = {}
11. Değeri/alanı oluştur veya güncelle: self.last_written = {}
12. Değeri/alanı oluştur veya güncelle: self.last_repeat = {}
13. Değeri/alanı oluştur veya güncelle: self.total_events = 0

**Gerçek kaynak:**

```python
def __init__(self, rate_limit=40, window_seconds=60, on_event=None):
        self.now = 0.0
        self.window_seconds = window_seconds
        self.on_event = on_event
        self.events = deque(maxlen=1000)
        self.notifications = deque(maxlen=200)
        self.active_alerts = {}
        self.limiter_exhausted = {}
        self.states = {}
        self.flags = {}
        self.slots = {}
        self.last_written = {}
        self.last_repeat = {}
        self.total_events = 0
```

### AlarmBridge._emit — satır 27

Kararlaştırılmış olayı kayda/bildirime aktarır; bulunduğu modülün olay sözleşmesini uygular.

**Girdiler:** self, e, channel, kind, value, details. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** event
**Atanan yerel değerler / durum alanları:** event, self.total_events
**Bağlandığı işlevler:** dict, round, self.events.append, self.on_event, self.notifications.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: event = dict(t=round(self.now, 6), sensor_id=e.id, sensor_name=e.name, channel=channel, kind=kind, value=value, details=details)
2. Yan etki/çağrı adımını çalıştır: self.events.append(event)
3. Değeri/alanı oluştur veya güncelle: self.total_events += 1
4. Koşula göre yol seç: self.on_event
5. Koşula göre yol seç: kind in ('ALERT', 'CALM')
6. Çağırana sonucu döndür: event

**Gerçek kaynak:**

```python
def _emit(self, e, channel, kind, value, details):
        event = dict(t=round(self.now, 6), sensor_id=e.id, sensor_name=e.name,
                     channel=channel, kind=kind, value=value, details=details)
        self.events.append(event)
        self.total_events += 1
        if self.on_event:
            self.on_event(event)
        if kind in ("ALERT", "CALM"):
            self.notifications.append(event)
        return event
```

### AlarmBridge.update — satır 38

Geçerli örnekleri ortak eşik/histerezis kuralıyla değerlendir.

**Girdiler:** self, entities, sim_time. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.now, ids, s, self.slots[e.id], self.slots[e.id].window_seconds, self.slots[e.id].remaining, limiter, limiter.max_remaining, limiter.remaining, previous, current, channel, value, alarm, s.status, self.active_alerts[e.id], last, self.last_repeat[e.id], (self.flags[e.id], self.states[e.id]), s.limit, self.last_written[e.id], self.limiter_exhausted[e.id]
**Bağlandığı işlevler:** list, RateLimiter, min, max, limiter.refresh, self.flags.get, set, sorted, getattr, current.add, self._emit, STATUS_LABELS.get, self.states.get, self.last_repeat.get, limiter.allow, self.notifications.append, dict, ','.join, self.active_alerts.pop, self.last_repeat.pop, self.limiter_exhausted.pop
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.now = sim_time
2. Değeri/alanı oluştur veya güncelle: ids = {e.id for e in entities if e.sensor}
3. Her öğe için işle: mapping ← (self.states, self.flags, self.slots, self.last_written, self.last_repeat, self.active_alerts, self.limiter_exhausted)
4. Her öğe için işle: e ← entities

**Gerçek kaynak:**

```python
def update(self, entities, sim_time):
        """Geçerli örnekleri ortak eşik/histerezis kuralıyla değerlendir."""
        self.now = sim_time
        ids = {e.id for e in entities if e.sensor}
        for mapping in (self.states, self.flags, self.slots, self.last_written,
                        self.last_repeat, self.active_alerts, self.limiter_exhausted):
            for eid in list(mapping):
                if eid not in ids:
                    del mapping[eid]
        for e in entities:
            s = e.sensor
            if s is None:
                continue
            if e.id not in self.slots:
                self.slots[e.id] = RateLimiter(s.max_limit, clock=lambda: self.now)
                self.slots[e.id].window_seconds = self.window_seconds
                self.slots[e.id].remaining = min(s.limit, s.max_limit)
            limiter = self.slots[e.id]
            limiter.max_remaining = s.max_limit
            if e.id in self.last_written and s.limit != self.last_written[e.id]:
                limiter.remaining = min(s.max_limit, max(0, s.limit))
            limiter.remaining = min(limiter.remaining, s.max_limit)
            limiter.refresh()
            previous = self.flags.get(e.id, set())
            current = set()
            if s.valid:
                for mode in sorted(s.modes, key=lambda m: m.value):
                    channel = mode.value
                    value = getattr(s, VALUE_ATTR[channel])
                    if value is None:
                        continue
                    alarm = value >= s.thresholds[channel] if channel not in previous else value >= s.clear_thresholds[channel]
                    if alarm:
                        current.add(channel)
                    if alarm != (channel in previous):
                        self._emit(e, channel, "ALERT" if alarm else "CALM", value,
                                   "Alarm başladı" if alarm else "Alarm sona erdi")
                for removed in previous - {m.value for m in s.modes}:
                    self._emit(e, removed, "UNAVAILABLE", None, "Kanal kapatıldı")
                s.status = "ALERT" if current else "NORMAL"
            elif previous:
                self._emit(e, "", "UNAVAILABLE", None, STATUS_LABELS.get(s.status, s.status))
            if self.states.get(e.id) != s.status:
                self._emit(e, "", "STATUS", None, STATUS_LABELS.get(s.status, s.status))
            if current:
                self.active_alerts[e.id] = sorted(current)
                last = self.last_repeat.get(e.id, self.now)
                if current != previous:
                    last = self.now
                if s.repeat_seconds > 0 and self.now - last + 1e-9 >= s.repeat_seconds:
                    if limiter.allow():
                        self.notifications.append(dict(t=self.now, sensor_id=e.id, channel=",".join(sorted(current)),
                                                       kind="REPEAT", details="Alarm devam ediyor", value=None))
                    last = self.now
                self.last_repeat[e.id] = last
            else:
                self.active_alerts.pop(e.id, None)
                self.last_repeat.pop(e.id, None)
            self.flags[e.id], self.states[e.id] = current, s.status
            s.limit = self.last_written[e.id] = limiter.remaining
            if limiter.remaining == 0:
                self.limiter_exhausted[e.id] = True
            else:
                self.limiter_exhausted.pop(e.id, None)
```

### AlarmBridge.alert_count — satır 104

Şu anda alarmdaki sensörlerin sayısını verir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** len(self.active_alerts)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** len
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: len(self.active_alerts)

**Gerçek kaynak:**

```python
def alert_count(self):
        return len(self.active_alerts)
```

### AlarmBridge.log_lines — satır 108

Sınırlı olay kayıtlarından okunur kısa satırlar üretir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** [f'{e['t']:.1f}s #{e['sensor_id']} {e['channel']} {e['kind']} {e['details']}' for e in self.events]
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: [f'{e['t']:.1f}s #{e['sensor_id']} {e['channel']} {e['kind']} {e['details']}' for e in self.events]

**Gerçek kaynak:**

```python
def log_lines(self):
        return [f"{e['t']:.1f}s #{e['sensor_id']} {e['channel']} {e['kind']} {e['details']}"
                for e in self.events]
```

### AlarmBridge.get_sensor_status — satır 112

Kimlik için tek ortak durumu döndürür; tanınmayan cihaz ilk ölçümü bekler.

**Girdiler:** self, entity_id. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.states.get(entity_id, 'WAITING')
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self.states.get
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self.states.get(entity_id, 'WAITING')

**Gerçek kaynak:**

```python
def get_sensor_status(self, entity_id):
        return self.states.get(entity_id, "WAITING")
```

### AlarmBridge.get_limiter_info — satır 115

Kalan ve maksimum tekrar bildirim hakkını panel için biçimler.

**Girdiler:** self, entity_id. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** f'Tekrar bildirimi: {limiter.remaining}/{limiter.max_remaining}' if limiter else ''
**Atanan yerel değerler / durum alanları:** limiter
**Bağlandığı işlevler:** self.slots.get
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: limiter = self.slots.get(entity_id)
2. Çağırana sonucu döndür: f'Tekrar bildirimi: {limiter.remaining}/{limiter.max_remaining}' if limiter else ''

**Gerçek kaynak:**

```python
def get_limiter_info(self, entity_id):
        limiter = self.slots.get(entity_id)
        return f"Tekrar bildirimi: {limiter.remaining}/{limiter.max_remaining}" if limiter else ""
```


## iot_sim/app.py

Pygame yaşam döngüsü, pencere, buton eylemleri, klavye/fare ve dosya girişidir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Pygame deney uygulaması: girdi, sabit saatli model ve responsive görünüm."""
```

Satır 2: Gereken isimleri içeri al: import argparse

```python
import argparse
```

Satır 3: Gereken isimleri içeri al: import math

```python
import math
```

Satır 4: Gereken isimleri içeri al: from pathlib import Path

```python
from pathlib import Path
```

Satır 5: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 6: Gereken isimleri içeri al: from .models import Kind, SensorMode, GasMode, SourceType, RouteMode

```python
from .models import Kind, SensorMode, GasMode, SourceType, RouteMode
```

Satır 7: Gereken isimleri içeri al: from .simulation import Simulation

```python
from .simulation import Simulation
```

Satır 8: Gereken isimleri içeri al: from .scene import load_scene, save_scene, to_scene, parse_scene

```python
from .scene import load_scene, save_scene, to_scene, parse_scene
```

Satır 9: Gereken isimleri içeri al: from .lessons import lesson_scene, LESSONS

```python
from .lessons import lesson_scene, LESSONS
```

Satır 10: Gereken isimleri içeri al: from .exporter import Exporter, ROOT

```python
from .exporter import Exporter, ROOT
```

Satır 11: Gereken isimleri içeri al: from .engine import find_entity_at, find_entity_by_id, clamp

```python
from .engine import find_entity_at, find_entity_by_id, clamp
```

Satır 12: Gereken isimleri içeri al: from . import operations

```python
from . import operations
```

Satır 13: Gereken isimleri içeri al: from .camera import Camera

```python
from .camera import Camera
```

Satır 14: Gereken isimleri içeri al: from .panel import Inspector

```python
from .panel import Inspector
```

Satır 15: Gereken isimleri içeri al: from .render import draw_world

```python
from .render import draw_world
```

Satır 16: Gereken isimleri içeri al: from .graphs import draw_graph

```python
from .graphs import draw_graph
```

Satır 17: Gereken isimleri içeri al: from .assets import load_icon

```python
from .assets import load_icon
```

Satır 18: Gereken isimleri içeri al: from .ui_widgets import button, text_block, BG, TEXT, MUTED, ACCENT

```python
from .ui_widgets import button, text_block, BG, TEXT, MUTED, ACCENT
```

Satır 20: Değeri/alanı oluştur veya güncelle: SPEEDS = (0.25, 1, 2, 5)

```python
SPEEDS=(.25,1,2,5)
```

Satır 503: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__=="__main__":
    main()
```

### App — satır 23

Ekran ve olay sahipliği; model kuralları Simulation/operations içindedir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
"""Ekran ve olay sahipliği; model kuralları Simulation/operations içindedir."""
```

### App.__init__ — satır 25

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, scene=None, out_dir=None, size=(1360, 900). self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.screen, self.font, self.small, self.tiny, self.title_font, self.clock, self.sim, self.out_dir, self.exporter, self.last_output, self.running, self.playing, self.speed, self.selected_id, self.tool, self.tab, self.inspector, self.cam, self.buttons, self.channel, self.show_theory, self.show_field, self.show_grid, self.filter_selected, self.filter_kind, self.mode, self.mode_id, self.route_points, self.drag_origin, self.pan_anchor, self.modal, self.input_text, self.toast, self.toast_until, self.icons
**Bağlandığı işlevler:** pygame.init, pygame.display.set_mode, pygame.display.set_caption, pygame.font.SysFont, pygame.time.Clock, Simulation, lesson_scene, Inspector, Camera, pygame.time.get_ticks, load_icon, str, self.focus_scene
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.init()
2. Değeri/alanı oluştur veya güncelle: self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
3. Yan etki/çağrı adımını çalıştır: pygame.display.set_caption('IoT Deney Atölyesi')
4. Değeri/alanı oluştur veya güncelle: self.font = pygame.font.SysFont('DejaVu Sans', 19)
5. Değeri/alanı oluştur veya güncelle: self.small = pygame.font.SysFont('DejaVu Sans', 14)
6. Değeri/alanı oluştur veya güncelle: self.tiny = pygame.font.SysFont('DejaVu Sans', 12)
7. Değeri/alanı oluştur veya güncelle: self.title_font = pygame.font.SysFont('DejaVu Sans', 25, bold=True)
8. Değeri/alanı oluştur veya güncelle: self.clock = pygame.time.Clock()
9. Değeri/alanı oluştur veya güncelle: self.sim = Simulation(scene if scene is not None else lesson_scene(1))
10. Değeri/alanı oluştur veya güncelle: self.out_dir = out_dir
11. Değeri/alanı oluştur veya güncelle: self.exporter = None
12. Değeri/alanı oluştur veya güncelle: self.last_output = None
13. Değeri/alanı oluştur veya güncelle: self.running = True
14. Değeri/alanı oluştur veya güncelle: self.playing = False
15. Değeri/alanı oluştur veya güncelle: self.speed = 1
16. Değeri/alanı oluştur veya güncelle: self.selected_id = None
17. Değeri/alanı oluştur veya güncelle: self.tool = None
18. Değeri/alanı oluştur veya güncelle: self.tab = 'lesson'
19. Değeri/alanı oluştur veya güncelle: self.inspector = Inspector()
20. Değeri/alanı oluştur veya güncelle: self.cam = Camera()
21. Değeri/alanı oluştur veya güncelle: self.buttons = {}
22. Değeri/alanı oluştur veya güncelle: self.channel = 'TEMP'
23. Değeri/alanı oluştur veya güncelle: self.show_theory = True
24. Değeri/alanı oluştur veya güncelle: self.show_field = False
25. Değeri/alanı oluştur veya güncelle: self.show_grid = True
26. Değeri/alanı oluştur veya güncelle: self.filter_selected = False
27. Değeri/alanı oluştur veya güncelle: self.filter_kind = 'Tümü'
28. Değeri/alanı oluştur veya güncelle: self.mode = None
29. Değeri/alanı oluştur veya güncelle: self.mode_id = None
30. Değeri/alanı oluştur veya güncelle: self.route_points = []
31. Değeri/alanı oluştur veya güncelle: self.drag_origin = None
32. Değeri/alanı oluştur veya güncelle: self.pan_anchor = None
33. Değeri/alanı oluştur veya güncelle: self.modal = None
34. Değeri/alanı oluştur veya güncelle: self.input_text = ''
35. Değeri/alanı oluştur veya güncelle: self.toast = 'Bir deney seç veya Başlat ile uzaklık deneyini çalıştır.'
36. Değeri/alanı oluştur veya güncelle: self.toast_until = pygame.time.get_ticks() + 6000
37. Değeri/alanı oluştur veya güncelle: self.icons = {key: load_icon(str(ROOT / 'assets' / (key + '.png'))) for key in ('sensor', 'source_temp', 'source_gas', 'obstacle', 'burned', 'drone')}
38. Yan etki/çağrı adımını çalıştır: self.focus_scene()

**Gerçek kaynak:**

```python
def __init__(self, scene=None, out_dir=None, size=(1360,900)):
        pygame.init()
        self.screen=pygame.display.set_mode(size,pygame.RESIZABLE)
        pygame.display.set_caption("IoT Deney Atölyesi")
        self.font=pygame.font.SysFont("DejaVu Sans",19)
        self.small=pygame.font.SysFont("DejaVu Sans",14)
        self.tiny=pygame.font.SysFont("DejaVu Sans",12)
        self.title_font=pygame.font.SysFont("DejaVu Sans",25,bold=True)
        self.clock=pygame.time.Clock()
        self.sim=Simulation(scene if scene is not None else lesson_scene(1))
        self.out_dir=out_dir
        self.exporter=None
        self.last_output=None
        self.running=True
        self.playing=False
        self.speed=1
        self.selected_id=None
        self.tool=None
        self.tab="lesson"
        self.inspector=Inspector()
        self.cam=Camera()
        self.buttons={}
        self.channel="TEMP"
        self.show_theory=True
        self.show_field=False
        self.show_grid=True
        self.filter_selected=False
        self.filter_kind="Tümü"
        self.mode=None
        self.mode_id=None
        self.route_points=[]
        self.drag_origin=None
        self.pan_anchor=None
        self.modal=None
        self.input_text=""
        self.toast="Bir deney seç veya Başlat ile uzaklık deneyini çalıştır."
        self.toast_until=pygame.time.get_ticks()+6000
        self.icons={key:load_icon(str(ROOT/"assets"/(key+".png")))
                    for key in ("sensor","source_temp","source_gas","obstacle","burned","drone")}
        self.focus_scene()
```

### App.selected — satır 67

Seçili kimliği güncel nesneye çözer; eski liste indeksine güvenmez.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** find_entity_by_id(self.sim.entities, self.selected_id)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** find_entity_by_id
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: find_entity_by_id(self.sim.entities, self.selected_id)

**Gerçek kaynak:**

```python
def selected(self):
        return find_entity_by_id(self.sim.entities,self.selected_id)
```

### App.focus_scene — satır 70

Kamerayı sahnedeki görünür nesnelerin ortalamasına taşır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** visible, self.cam.x, self.cam.y
**Bağlandığı işlevler:** sum, len
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: visible = [e for e in self.sim.entities if e.carried_by is None]
2. Değeri/alanı oluştur veya güncelle: self.cam.x = sum((e.tx + 0.5 for e in visible)) / len(visible) if visible else 100
3. Değeri/alanı oluştur veya güncelle: self.cam.y = sum((e.ty + 0.5 for e in visible)) / len(visible) if visible else 100

**Gerçek kaynak:**

```python
def focus_scene(self):
        visible=[e for e in self.sim.entities if e.carried_by is None]
        self.cam.x=sum(e.tx+.5 for e in visible)/len(visible) if visible else 100
        self.cam.y=sum(e.ty+.5 for e in visible)/len(visible) if visible else 100
```

### App.message — satır 75

Kullanıcıya kısa durum/hata mesajı ve görünme süresi ayarlar.

**Girdiler:** self, text. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.toast, self.toast_until
**Bağlandığı işlevler:** str, pygame.time.get_ticks
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.toast = str(text)
2. Değeri/alanı oluştur veya güncelle: self.toast_until = pygame.time.get_ticks() + 6000

**Gerçek kaynak:**

```python
def message(self,text):
        self.toast=str(text)
        self.toast_until=pygame.time.get_ticks()+6000
```

### App.btn — satır 79

Butonu çizip eylemini aynı tıklama alanıyla kaydeder; panel kırpmasını uygular.

**Girdiler:** self, key, rect, label, action, active=False, clip=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** hit, self.buttons[key]
**Bağlandığı işlevler:** button, rect.clip
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: button(self.screen, rect, label, self.small, active)
2. Değeri/alanı oluştur veya güncelle: hit = rect.clip(clip) if clip else rect
3. Koşula göre yol seç: hit.width and hit.height

**Gerçek kaynak:**

```python
def btn(self,key,rect,label,action,active=False,clip=None):
        button(self.screen,rect,label,self.small,active)
        hit=rect.clip(clip) if clip else rect
        if hit.width and hit.height:
            self.buttons[key]=(hit,action)
```

### App.layout — satır 85

Mevcut pencere boyutundan harita, grafik ve sağ panel dikdörtgenlerini hesaplar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** (width, height), panel_w, self.panel_rect, map_w, graph_h, self.cam.viewport, self.graph_rect, self.graph_rect.height
**Bağlandığı işlevler:** self.screen.get_size, pygame.Rect, max, min
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: width, height = self.screen.get_size()
2. Değeri/alanı oluştur veya güncelle: panel_w = 360 if width >= 1200 else 320
3. Değeri/alanı oluştur veya güncelle: self.panel_rect = pygame.Rect(width - panel_w - 16, 154, panel_w, height - 180)
4. Değeri/alanı oluştur veya güncelle: map_w = self.panel_rect.x - 34
5. Değeri/alanı oluştur veya güncelle: graph_h = 218
6. Değeri/alanı oluştur veya güncelle: self.cam.viewport = pygame.Rect(18, 154, map_w, max(100, height - 154 - graph_h - 40))
7. Değeri/alanı oluştur veya güncelle: self.graph_rect = pygame.Rect(18, self.cam.viewport.bottom + 12, map_w, graph_h)
8. Değeri/alanı oluştur veya güncelle: self.graph_rect.height = min(graph_h, height - self.graph_rect.y - 22)

**Gerçek kaynak:**

```python
def layout(self):
        width,height=self.screen.get_size()
        panel_w=360 if width>=1200 else 320
        self.panel_rect=pygame.Rect(width-panel_w-16,154,panel_w,height-180)
        map_w=self.panel_rect.x-34
        graph_h=218
        self.cam.viewport=pygame.Rect(18,154,map_w,max(100,height-154-graph_h-40))
        self.graph_rect=pygame.Rect(18,self.cam.viewport.bottom+12,map_w,graph_h)
        self.graph_rect.height=min(graph_h,height-self.graph_rect.y-22)
```

### App.draw — satır 95

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.buttons, screen, (width, height), caption, label, actions, x, tools, w, description, graph, gap, bw, sensor, history, tag, footer, box, shade, box.center, labels, display
**Bağlandığı işlevler:** self.layout, screen.fill, screen.get_size, screen.blit, self.title_font.render, self.small.render, label.get_width, self.btn, pygame.Rect, draw_world, text_block, min, enumerate, next, find_entity_by_id, self.sim.history.get, draw_graph, self.tiny.render, tag.get_width, self.inspector.draw, pygame.time.get_ticks, pygame.draw.rect, pygame.Surface, shade.fill, screen.get_rect, self.small.size, pygame.display.flip
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.layout()
2. Değeri/alanı oluştur veya güncelle: self.buttons = {}
3. Değeri/alanı oluştur veya güncelle: screen = self.screen
4. Yan etki/çağrı adımını çalıştır: screen.fill(BG)
5. Değeri/alanı oluştur veya güncelle: width, height = screen.get_size()
6. Yan etki/çağrı adımını çalıştır: screen.blit(self.title_font.render('IoT Deney Atölyesi', True, TEXT), (18, 15))
7. Değeri/alanı oluştur veya güncelle: caption = f'{('ÇALIŞIYOR' if self.playing else 'DURAKLATILDI')}   •   {self.sim.time:.2f} s   •   {self.sim.alarm.alert_count} alarm'
8. Değeri/alanı oluştur veya güncelle: label = self.small.render(caption, True, ACCENT)
9. Yan etki/çağrı adımını çalıştır: screen.blit(label, (width - label.get_width() - 18, 24))
10. Değeri/alanı oluştur veya güncelle: actions = [('play', 'Duraklat' if self.playing else 'Başlat', ('play',), 98), ('step', 'Tek adım', ('step',), 90), ('reset', 'Başa dön', ('reset',), 94), ('speed', f'Hız {self.speed:g}×', ('speed',), 82), ('seed', f'Tohu…
11. Değeri/alanı oluştur veya güncelle: x = 18
12. Her öğe için işle: (key, label, action, w) ← actions
13. Değeri/alanı oluştur veya güncelle: tools = [('select', 'Seç', None), ('sensor', 'Sensör', Kind.SENSOR), ('source', 'Kaynak', Kind.SOURCE), ('obstacle', 'Engel / Ağaç', Kind.OBSTACLE), ('drone', 'Drone', Kind.UAV)]
14. Değeri/alanı oluştur veya güncelle: x = 18
15. Her öğe için işle: (key, label, kind) ← tools
16. Yan etki/çağrı adımını çalıştır: self.btn('field', pygame.Rect(x + 4, 108, 150, 30), 'Teorik alan ' + ('Açık' if self.show_field else 'Kapalı'), ('field',), self.show_field)
17. Yan etki/çağrı adımını çalıştır: self.btn('center', pygame.Rect(x + 162, 108, 90, 30), 'Ortala', ('center',))
18. Yan etki/çağrı adımını çalıştır: draw_world(screen, self.cam, self.sim, self.selected_id, self.icons, self.tiny, layer=self.channel if self.channel != 'BATTERY' else 'TEMP', show_field=self.show_field, route_preview=self.route_points, show_grid=self.sho…
19. Koşula göre yol seç: self.mode
20. Değeri/alanı oluştur veya güncelle: graph = self.graph_rect
21. Değeri/alanı oluştur veya güncelle: gap = 6
22. Değeri/alanı oluştur veya güncelle: bw = min(89, (graph.width - 140) // 5)
23. Her öğe için işle: (i, key) ← enumerate(('TEMP', 'CO', 'CO2', 'H2', 'BATTERY'))
24. Yan etki/çağrı adımını çalıştır: self.btn('theory', pygame.Rect(graph.right - 130, graph.y, 130, 29), 'Teorik çizgi', ('theory',), self.show_theory)
25. Değeri/alanı oluştur veya güncelle: sensor = self.selected
26. Koşula göre yol seç: sensor and sensor.uav
27. Koşula göre yol seç: not sensor or not sensor.sensor
28. Değeri/alanı oluştur veya güncelle: history = self.sim.history.get(sensor.id, []) if sensor else []
29. Yan etki/çağrı adımını çalıştır: draw_graph(screen, pygame.Rect(graph.x, graph.y + 36, graph.width, graph.height - 36), history, self.channel, self.tiny, self.show_theory)
30. Koşula göre yol seç: sensor
31. Yan etki/çağrı adımını çalıştır: self.inspector.draw(self, self.panel_rect)
32. Değeri/alanı oluştur veya güncelle: footer = 'Space: çalıştır  •  N: adım  •  M: taşı  •  K: rota  •  Orta tuş: kaydır  •  Tekerlek: zoom'
33. Yan etki/çağrı adımını çalıştır: screen.blit(self.tiny.render(footer, True, MUTED), (18, height - 17))
34. Koşula göre yol seç: self.toast and pygame.time.get_ticks() < self.toast_until
35. Koşula göre yol seç: self.modal
36. Yan etki/çağrı adımını çalıştır: pygame.display.flip()

**Gerçek kaynak:**

```python
def draw(self):
        self.layout()
        self.buttons={}
        screen=self.screen
        screen.fill(BG)
        width,height=screen.get_size()
        screen.blit(self.title_font.render("IoT Deney Atölyesi",True,TEXT),(18,15))
        caption=f"{'ÇALIŞIYOR' if self.playing else 'DURAKLATILDI'}   •   {self.sim.time:.2f} s   •   {self.sim.alarm.alert_count} alarm"
        label=self.small.render(caption,True,ACCENT)
        screen.blit(label,(width-label.get_width()-18,24))
        actions=[
            ("play","Duraklat" if self.playing else "Başlat",("play",),98),
            ("step","Tek adım",("step",),90),("reset","Başa dön",("reset",),94),
            ("speed",f"Hız {self.speed:g}×",("speed",),82),
            ("seed",f"Tohum {self.sim.seed}",("seed",),112),
            ("new","Yeni",("new",),64),("save","Kaydet",("save",),78),
            ("load","Yükle",("load",),78),("lessons","Deneyler",("tab","lesson"),96)]
        x=18
        for key,label,action,w in actions:
            self.btn(key,pygame.Rect(x,62,w,34),label,action,self.playing if key=="play" else False)
            x+=w+7
        tools=[("select","Seç",None),("sensor","Sensör",Kind.SENSOR),("source","Kaynak",Kind.SOURCE),
               ("obstacle","Engel / Ağaç",Kind.OBSTACLE),("drone","Drone",Kind.UAV)]
        x=18
        for key,label,kind in tools:
            w=112 if key=="obstacle" else 85
            self.btn("tool_"+key,pygame.Rect(x,108,w,30),label,("tool",kind),self.tool==kind)
            x+=w+6
        self.btn("field",pygame.Rect(x+4,108,150,30),"Teorik alan "+("Açık" if self.show_field else "Kapalı"),("field",),self.show_field)
        self.btn("center",pygame.Rect(x+162,108,90,30),"Ortala",("center",))
        draw_world(screen,self.cam,self.sim,self.selected_id,self.icons,self.tiny,
                   layer=self.channel if self.channel!="BATTERY" else "TEMP",
                   show_field=self.show_field,route_preview=self.route_points,show_grid=self.show_grid)
        if self.mode:
            description={"move":"TAŞI • Hedef kareye tıkla. Esc: iptal",
                         "route":"ROTA • Durak ekle; K: kaydet; Esc: iptal",
                         "attach":"YÜKLE • Sensör veya kaynağa tıkla; Esc: iptal"}[self.mode]
            text_block(screen,description,self.cam.viewport.x+12,self.cam.viewport.y+12,
                       self.cam.viewport.width-24,self.small,(255,215,130))
        graph=self.graph_rect
        gap=6
        bw=min(89,(graph.width-140)//5)
        for i,key in enumerate(("TEMP","CO","CO2","H2","BATTERY")):
            self.btn("channel_"+key,pygame.Rect(graph.x+i*(bw+gap),graph.y,bw,29),
                     "Pil" if key=="BATTERY" else key,("channel",key),self.channel==key)
        self.btn("theory",pygame.Rect(graph.right-130,graph.y,130,29),"Teorik çizgi",("theory",),self.show_theory)
        sensor=self.selected
        if sensor and sensor.uav:
            sensor=next((find_entity_by_id(self.sim.entities,cid) for cid in sensor.uav.carrying_ids
                         if find_entity_by_id(self.sim.entities,cid).sensor),None)
        if not sensor or not sensor.sensor:
            sensor=next((e for e in self.sim.entities if e.sensor),None)
        history=self.sim.history.get(sensor.id,[]) if sensor else []
        draw_graph(screen,pygame.Rect(graph.x,graph.y+36,graph.width,graph.height-36),
                   history,self.channel,self.tiny,self.show_theory)
        if sensor:
            tag=self.tiny.render(sensor.display_name,True,MUTED)
            screen.blit(tag,(graph.right-tag.get_width()-12,graph.y+46))
        self.inspector.draw(self,self.panel_rect)
        footer="Space: çalıştır  •  N: adım  •  M: taşı  •  K: rota  •  Orta tuş: kaydır  •  Tekerlek: zoom"
        screen.blit(self.tiny.render(footer,True,MUTED),(18,height-17))
        if self.toast and pygame.time.get_ticks()<self.toast_until:
            box=pygame.Rect(self.cam.viewport.x+8,self.cam.viewport.bottom-90,self.cam.viewport.width-16,80)
            pygame.draw.rect(screen,(28,44,58),box,border_radius=8)
            text_block(screen,self.toast,box.x+12,box.y+10,box.width-24,self.small)
        if self.modal:
            shade=pygame.Surface(screen.get_size(),pygame.SRCALPHA)
            shade.fill((0,0,0,180))
            screen.blit(shade,(0,0))
            box=pygame.Rect(0,0,min(780,width-60),220)
            box.center=screen.get_rect().center
            pygame.draw.rect(screen,(30,44,60),box,border_radius=14)
            labels={"save":"Başlangıç sahnesini kaydet (.json)","load":"Sahne yükle (.json)",
                    "seed":"Yeni deney tohumu (0–4294967295)","rename":"Nesne adı"}
            text_block(screen,labels[self.modal],box.x+20,box.y+20,box.width-40,self.font)
            # Son karakterler görünür; tam yol input_text içinde korunur.
            display=self.input_text
            while self.small.size(display+"|")[0]>box.width-40: display=display[1:]
            text_block(screen,display+"|",box.x+20,box.y+85,box.width-40,self.small,ACCENT)
            text_block(screen,"Enter: uygula   •   Esc: iptal",box.x+20,box.bottom-48,box.width-40,self.small,MUTED)
        pygame.display.flip()
```

### App.begin_recording — satır 177

İlk çalıştırmada başlangıç sahnesini yakalar ve tek sonuç oturumunu modele bağlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.sim.baseline, self.exporter, self.last_output
**Bağlandığı işlevler:** self.sim.snapshot, Exporter, self.sim.start_recording
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: self.exporter is None

**Gerçek kaynak:**

```python
def begin_recording(self):
        if self.exporter is None:
            if self.sim.time==0:
                self.sim.baseline=self.sim.snapshot()
            self.exporter=Exporter(self.out_dir,scene=self.sim.snapshot())
            self.sim.start_recording(self.exporter)
            self.last_output=self.exporter.directory
```

### App.close_recording — satır 185

Sonuç dosyalarını kapatıp aktif exporter bağlantısını kaldırır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.last_output, self.exporter, self.sim.exporter
**Bağlandığı işlevler:** self.exporter.close
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: self.exporter

**Gerçek kaynak:**

```python
def close_recording(self):
        if self.exporter:
            self.last_output=self.exporter.close()
            self.exporter=None
            self.sim.exporter=None
```

### App.change — satır 191

Editör değişikliklerini deney çıktısında zamanıyla kaydet.

**Girdiler:** self, description. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.sim.revision, self.sim.baseline
**Bağlandığı işlevler:** self.sim.snapshot, self.exporter.log_change
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.sim.revision += 1
2. Koşula göre yol seç: self.sim.time == 0
3. Koşula göre yol seç: self.exporter

**Gerçek kaynak:**

```python
def change(self,description):
        """Editör değişikliklerini deney çıktısında zamanıyla kaydet."""
        self.sim.revision += 1
        if self.sim.time==0:
            self.sim.baseline=self.sim.snapshot()
        if self.exporter:
            self.exporter.log_change(self.sim.time,description,self.sim.snapshot())
```

### App.replace_sim — satır 199

Yeni sahne önce tamamen doğrulanır; sonra eski oturum kapatılır.

**Girdiler:** self, scene. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** candidate, self.sim, self.playing, self.selected_id, self.mode, self.mode_id, self.route_points, self.inspector.scroll
**Bağlandığı işlevler:** Simulation, self.close_recording, self.focus_scene
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: candidate = Simulation(scene)
2. Yan etki/çağrı adımını çalıştır: self.close_recording()
3. Değeri/alanı oluştur veya güncelle: self.sim = candidate
4. Değeri/alanı oluştur veya güncelle: self.playing = False
5. Değeri/alanı oluştur veya güncelle: self.selected_id = None
6. Değeri/alanı oluştur veya güncelle: self.mode = None
7. Değeri/alanı oluştur veya güncelle: self.mode_id = None
8. Değeri/alanı oluştur veya güncelle: self.route_points = []
9. Değeri/alanı oluştur veya güncelle: self.inspector.scroll = 0
10. Yan etki/çağrı adımını çalıştır: self.focus_scene()

**Gerçek kaynak:**

```python
def replace_sim(self,scene):
        """Yeni sahne önce tamamen doğrulanır; sonra eski oturum kapatılır."""
        candidate=Simulation(scene)
        self.close_recording()
        self.sim=candidate
        self.playing=False
        self.selected_id=None
        self.mode=None
        self.mode_id=None
        self.route_points=[]
        self.inspector.scroll=0
        self.focus_scene()
```

### App.prompt — satır 212

Dosya, isim veya tohum girişi için deneyi duraklatır ve yazı kutusunu hazırlar.

**Girdiler:** self, kind. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.playing, self.modal, self.input_text
**Bağlandığı işlevler:** str
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.playing = False
2. Değeri/alanı oluştur veya güncelle: self.modal = kind
3. Değeri/alanı oluştur veya güncelle: self.input_text = str(ROOT / 'scenes' / 'deney.json') if kind in ('load', 'save') else str(self.sim.seed) if kind == 'seed' else self.selected.name

**Gerçek kaynak:**

```python
def prompt(self,kind):
        self.playing=False
        self.modal=kind
        self.input_text=str(ROOT/"scenes"/"deney.json") if kind in ("load","save") else str(self.sim.seed) if kind=="seed" else self.selected.name
```

### App.submit — satır 217

Yazı kutusunu amacına göre doğrular; kaydetme, yükleme, tohum veya isim işlemini yapar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** kind, value, path, seed, scene, scene['seed'], self.selected.name, self.modal
**Bağlandığı işlevler:** self.input_text.strip, Path(value).expanduser, Path, path.suffix.lower, ValueError, save_scene, self.sim.snapshot, self.message, self.replace_sim, load_scene, int, len, self.change
**Açık hata yolları:** ValueError('Dosya uzantısı .json olmalı.'); ValueError('İsim en fazla 80 karakter olabilir.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: kind = self.modal
2. Değeri/alanı oluştur veya güncelle: value = self.input_text.strip()
3. Koşula göre yol seç: kind == 'save'
4. Değeri/alanı oluştur veya güncelle: self.modal = None

**Gerçek kaynak:**

```python
def submit(self):
        kind=self.modal
        value=self.input_text.strip()
        if kind=="save":
            path=Path(value).expanduser()
            if path.suffix.lower()!=".json": raise ValueError("Dosya uzantısı .json olmalı.")
            save_scene(path,self.sim.snapshot())
            self.message(f"Sahne kaydedildi: {path}")
        elif kind=="load":
            self.replace_sim(load_scene(Path(value).expanduser()))
            self.message("Sahne doğrulandı ve yüklendi.")
        elif kind=="seed":
            seed=int(value)
            scene=self.sim.snapshot()
            scene["seed"]=seed
            self.replace_sim(scene)
            self.message("Tohum değişti; yeni başlangıç oluşturuldu.")
        elif kind=="rename" and self.selected:
            if len(value)>80: raise ValueError("İsim en fazla 80 karakter olabilir.")
            self.selected.name=value
            self.change("rename")
        self.modal=None
```

### App.action — satır 240

Buton ve kısayolları aynı işlem yoluna yönlendir.

**Girdiler:** self, action. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** (name, *args), e, self.playing, interval, baseline, self.speed, self.tab, self.inspector.scroll, self.tool, self.mode, self.route_points, self.show_field, self.show_theory, self.channel, self.filter_selected, values, self.filter_kind, self.selected_id, (self.mode, self.mode_id), e.uav.route_mode, e.uav.route_dir, e.uav.route, e.uav.blocked_reason, mode, e.source.stype, target, (key, delta, low, high), (attribute, channel), values[channel], target.clear_thresholds[channel], value, target.limit
**Bağlandığı işlevler:** self.begin_recording, self.sim.advance, self.replace_sim, self.message, SPEEDS.index, len, to_scene, self.prompt, lesson_scene, self.focus_scene, values.index, ValueError, operations.delete_entity, self.change, operations.set_route, operations.release_cargo, e.sensor.modes.symmetric_difference_update, invalidate, self.sim.alarm.update, e.source.gas_modes.symmetric_difference_update, setattr, getattr, key.split, round, clamp, min, type, int
**Açık hata yolları:** ValueError('Önce yükü indir.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: name, *args = action
2. Değeri/alanı oluştur veya güncelle: e = self.selected
3. Koşula göre yol seç: name == 'play'

**Gerçek kaynak:**

```python
def action(self,action):
        """Buton ve kısayolları aynı işlem yoluna yönlendir."""
        name,*args=action
        e=self.selected
        if name=="play":
            if not self.playing: self.begin_recording()
            self.playing=not self.playing
        elif name=="step":
            self.playing=False
            self.begin_recording()
            interval=e.sensor.sample_interval if e and e.sensor else 1
            self.sim.advance(interval)
        elif name=="reset":
            baseline=self.sim.baseline
            self.replace_sim(baseline)
            self.message("Aynı başlangıç ve tohum yeniden kuruldu.")
        elif name=="speed":
            self.speed=SPEEDS[(SPEEDS.index(self.speed)+1)%len(SPEEDS)]
        elif name=="new":
            self.replace_sim(to_scene([],seed=self.sim.seed))
            self.tab="properties"
            self.message("Boş deney; araç seçip nesne ekle.")
        elif name in ("save","load","seed","rename"):
            if name!="rename" or e: self.prompt(name)
        elif name=="lesson":
            self.replace_sim(lesson_scene(args[0]))
            self.tab="lesson"
            self.message(LESSONS[args[0]-1]["goal"])
        elif name=="tab":
            self.tab=args[0]
            self.inspector.scroll=0
        elif name=="tool":
            self.tool=args[0]
            self.mode=None
            self.route_points=[]
            self.tab="properties"
        elif name=="field": self.show_field=not self.show_field
        elif name=="theory": self.show_theory=not self.show_theory
        elif name=="center": self.focus_scene()
        elif name=="channel": self.channel=args[0]
        elif name=="filter_sensor": self.filter_selected=not self.filter_selected
        elif name=="filter_kind":
            values=("Tümü","ALERT","CALM","STATUS","UNAVAILABLE","FIRE")
            self.filter_kind=values[(values.index(self.filter_kind)+1)%len(values)]
        elif name=="select":
            self.selected_id=args[0]
            self.tool=None
            self.inspector.scroll=0
        elif e:
            self.playing=False
            if name=="move":
                if e.carried_by: raise ValueError("Önce yükü indir.")
                self.mode,self.mode_id="move",e.id
            elif name=="delete":
                operations.delete_entity(self.sim,e.id)
                self.selected_id=None
                self.mode=None
                self.route_points=[]
                self.change("delete")
            elif name=="route" and e.uav:
                if self.mode=="route" and self.mode_id==e.id:
                    operations.set_route(self.sim,e,self.route_points)
                    self.mode=None
                    self.route_points=[]
                    self.change("route")
                else:
                    self.mode,self.mode_id="route",e.id
                    self.route_points=[]
            elif name=="attach" and e.uav:
                self.mode,self.mode_id="attach",e.id
            elif name=="release" and e.uav:
                operations.release_cargo(self.sim,e)
                self.change("release")
            elif name=="route_mode" and e.uav:
                e.uav.route_mode=RouteMode.PINGPONG if e.uav.route_mode==RouteMode.LOOP else RouteMode.LOOP
                e.uav.route_dir=1
                self.change(name)
            elif name=="route_clear" and e.uav:
                e.uav.route=[]
                e.uav.blocked_reason=""
                self.change(name)
            elif name=="sensor_mode":
                mode=args[0]
                e.sensor.modes.symmetric_difference_update({mode})
                # Kanal kapatınca geçmiş okumayı geçerli tutma.
                from .sensors import invalidate
                invalidate(e.sensor,"WAITING" if e.sensor.modes else "OFF")
                self.sim.alarm.update(self.sim.entities,self.sim.time)
                self.change(name)
            elif name=="gas_mode":
                e.source.gas_modes.symmetric_difference_update({args[0]})
                self.change(name)
            elif name=="source_type":
                e.source.stype=SourceType.GAS if e.source.stype==SourceType.TEMP else SourceType.TEMP
                self.change(name)
            elif name=="toggle":
                target=e.sensor or e.uav
                setattr(target,args[0],not getattr(target,args[0]))
                if e.sensor:
                    from .sensors import invalidate
                    invalidate(e.sensor,"WAITING" if e.sensor.enabled else "OFF")
                    self.sim.alarm.update(self.sim.entities,self.sim.time)
                self.change(name)
            elif name=="entity_toggle":
                setattr(e,args[0],not getattr(e,args[0]))
                self.change(name)
            elif name=="adjust":
                key,delta,low,high=args
                target=e.sensor or e.source or e.uav or e
                if "." in key:
                    attribute,channel=key.split(".")
                    values=getattr(target,attribute)
                    values[channel]=round(clamp(values[channel]+delta,low,high),6)
                    if attribute in ("thresholds","clear_thresholds"):
                        target.clear_thresholds[channel]=min(target.clear_thresholds[channel],target.thresholds[channel])
                else:
                    value=round(clamp(getattr(target,key)+delta,low,high),6)
                    if type(getattr(target,key)) is int: value=int(value)
                    setattr(target,key,value)
                    if key=="max_limit": target.limit=min(target.limit,target.max_limit)
                self.change(key)
                self.message("Ayar güncellendi. Devam et veya Tek adım ile etkisini gözle.")
```

### App.map_click — satır 363

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** self, pos. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** (wx, wy), (x, y), index, hit, self.mode, e, self.selected_id, self.tool, self.tab, self.inspector.scroll
**Bağlandığı işlevler:** self.cam.screen_to_world, math.floor, find_entity_at, operations.move_entity, self.change, ValueError, operations.attach, self.route_points.append, operations.add_entity
**Açık hata yolları:** ValueError('Bir sensör veya kaynak seç.'); ValueError('Aynı durağı arka arkaya ekleme.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: wx, wy = self.cam.screen_to_world(pos)
2. Değeri/alanı oluştur veya güncelle: x, y = (math.floor(wx), math.floor(wy))
3. Koşula göre yol seç: not (0 <= x < self.sim.width and 0 <= y < self.sim.height)
4. Değeri/alanı oluştur veya güncelle: index = find_entity_at(self.sim.entities, x, y)
5. Değeri/alanı oluştur veya güncelle: hit = self.sim.entities[index] if index is not None else None
6. Koşula göre yol seç: self.mode == 'move'
7. Değeri/alanı oluştur veya güncelle: self.inspector.scroll = 0

**Gerçek kaynak:**

```python
def map_click(self,pos):
        wx,wy=self.cam.screen_to_world(pos)
        x,y=math.floor(wx),math.floor(wy)
        if not (0<=x<self.sim.width and 0<=y<self.sim.height): return
        index=find_entity_at(self.sim.entities,x,y)
        hit=self.sim.entities[index] if index is not None else None
        if self.mode=="move":
            operations.move_entity(self.sim,self.mode_id,x,y)
            self.mode=None
            self.change("move")
        elif self.mode=="attach":
            if hit is None: raise ValueError("Bir sensör veya kaynak seç.")
            operations.attach(self.sim,self.mode_id,hit.id)
            self.mode=None
            self.change("attach")
        elif self.mode=="route":
            if self.route_points and self.route_points[-1]==(x,y):
                raise ValueError("Aynı durağı arka arkaya ekleme.")
            self.route_points.append((x,y))
        elif self.tool is not None and hit is None:
            e=operations.add_entity(self.sim,self.tool,x,y)
            self.selected_id=e.id
            self.change("add")
        else:
            self.selected_id=hit.id if hit else None
            self.tool=None
            self.tab="properties"
        self.inspector.scroll=0
```

### App.process_event — satır 392

Gerçek event.pos kullan; aynı karedeki olaylar birbirinin koordinatını almaz.

**Girdiler:** self, event. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** self.running, self.screen, self.modal, self.input_text, mods, mapping, self.mode, self.mode_id, self.route_points, self.tool, self.show_grid, pos, self.inspector.scroll, (wx, wy), idx, hit, self.drag_origin, self.selected_id, self.pan_anchor, delta, (drone, cargo, start), (dx, dy), self.cam.x, self.cam.y
**Bağlandığı işlevler:** pygame.display.set_mode, max, self.submit, event.unicode.isprintable, len, getattr, pygame.key.get_mods, self.action, pygame.mouse.get_pos, self.panel_rect.collidepoint, clamp, self.cam.viewport.collidepoint, self.cam.zoom_at, reversed, list, self.buttons.values, rect.collidepoint, self.cam.screen_to_world, find_entity_at, math.floor, self.map_click, operations.attach, self.change, self.message, str
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def process_event(self,event):
        """Gerçek event.pos kullan; aynı karedeki olaylar birbirinin koordinatını almaz."""
        try:
            if event.type==pygame.QUIT:
                self.running=False
            elif event.type==pygame.VIDEORESIZE:
                self.screen=pygame.display.set_mode((max(1024,event.w),max(720,event.h)),pygame.RESIZABLE)
            elif self.modal:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: self.modal=None
                    elif event.key==pygame.K_RETURN: self.submit()
                    elif event.key==pygame.K_BACKSPACE: self.input_text=self.input_text[:-1]
                    elif event.unicode and event.unicode.isprintable() and len(self.input_text)<4096:
                        self.input_text+=event.unicode
            elif event.type==pygame.KEYDOWN:
                mods=getattr(event,"mod",pygame.key.get_mods())
                mapping={pygame.K_SPACE:("play",),pygame.K_n:("step",),pygame.K_m:("move",),
                         pygame.K_k:("route",),pygame.K_DELETE:("delete",),pygame.K_BACKSPACE:("delete",)}
                if event.key==pygame.K_ESCAPE:
                    self.mode=None
                    self.mode_id=None
                    self.route_points=[]
                    self.tool=None
                elif mods & pygame.KMOD_CTRL and event.key in (pygame.K_s,pygame.K_o):
                    self.action(("save" if event.key==pygame.K_s else "load",))
                elif event.key==pygame.K_g: self.show_grid=not self.show_grid
                elif event.key in mapping: self.action(mapping[event.key])
            elif event.type==pygame.MOUSEWHEEL:
                pos=pygame.mouse.get_pos()
                if self.panel_rect.collidepoint(pos):
                    self.inspector.scroll=clamp(self.inspector.scroll-event.y*60,0,self.inspector.bottom)
                elif self.cam.viewport.collidepoint(pos): self.cam.zoom_at(1.12**event.y)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos
                if event.button==1:
                    for rect,action in reversed(list(self.buttons.values())):
                        if rect.collidepoint(pos):
                            self.action(action)
                            return
                    if self.cam.viewport.collidepoint(pos):
                        # Seçili drone korunurken nesneyi panel üstüne sürükleme.
                        wx,wy=self.cam.screen_to_world(pos)
                        idx=find_entity_at(self.sim.entities,math.floor(wx),math.floor(wy))
                        hit=self.sim.entities[idx] if idx is not None else None
                        if not self.mode and self.selected and self.selected.uav and hit and (hit.sensor or hit.source):
                            self.drag_origin=(self.selected_id,hit.id,pos)
                        else: self.map_click(pos)
                elif event.button==3 and self.cam.viewport.collidepoint(pos):
                    wx,wy=self.cam.screen_to_world(pos)
                    idx=find_entity_at(self.sim.entities,math.floor(wx),math.floor(wy))
                    if idx is not None:
                        self.selected_id=self.sim.entities[idx].id
                        self.action(("delete",))
                elif event.button==2 and self.cam.viewport.collidepoint(pos):
                    self.pan_anchor=pos
                elif event.button in (4,5):
                    delta=1 if event.button==4 else -1
                    if self.panel_rect.collidepoint(pos): self.inspector.scroll=clamp(self.inspector.scroll-delta*60,0,self.inspector.bottom)
                    elif self.cam.viewport.collidepoint(pos): self.cam.zoom_at(1.12**delta)
            elif event.type==pygame.MOUSEBUTTONUP:
                if event.button==2: self.pan_anchor=None
                if event.button==1 and self.drag_origin:
                    drone,cargo,start=self.drag_origin
                    self.drag_origin=None
                    if self.panel_rect.collidepoint(event.pos):
                        operations.attach(self.sim,drone,cargo)
                        self.change("attach")
                    else: self.map_click(event.pos)
            elif event.type==pygame.MOUSEMOTION and self.pan_anchor:
                dx,dy=event.pos[0]-self.pan_anchor[0],event.pos[1]-self.pan_anchor[1]
                self.cam.x=clamp(self.cam.x-dx/(24*self.cam.zoom),0,self.sim.width)
                self.cam.y=clamp(self.cam.y-dy/(24*self.cam.zoom),0,self.sim.height)
                self.pan_anchor=event.pos
        except (ValueError,OSError) as exc:
            self.message(str(exc))
```

### App.run — satır 468

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** self, max_frames=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** frames, dt
**Bağlandığı işlevler:** self.clock.tick, self.draw, pygame.event.get, self.process_event, self.sim.advance, min, self.close_recording, pygame.quit
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: frames = 0
2. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def run(self,max_frames=None):
        frames=0
        try:
            while self.running and (max_frames is None or frames<max_frames):
                dt=self.clock.tick(60)/1000
                self.draw()
                for event in pygame.event.get(): self.process_event(event)
                if self.playing: self.sim.advance(min(dt,.25)*self.speed)
                frames+=1
        finally:
            self.close_recording()
            pygame.quit()
```

### main — satır 482

Komut seçeneklerini/başlangıç nesnelerini kurup programın ana akışını başlatır.

**Girdiler:** argv=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** parser, args, scene, scene['seed'], sim
**Bağlandığı işlevler:** argparse.ArgumentParser, parser.add_argument, range, parser.parse_args, load_scene, lesson_scene, Simulation, Exporter, sim.start_recording, sim.advance, print, App(scene, args.out_dir).run, App
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: parser = argparse.ArgumentParser(description='Öğretici IoT deney ortamı')
2. Yan etki/çağrı adımını çalıştır: parser.add_argument('--lesson', type=int, choices=range(1, 7), default=1)
3. Yan etki/çağrı adımını çalıştır: parser.add_argument('--scene', type=Path)
4. Yan etki/çağrı adımını çalıştır: parser.add_argument('--seed', type=int)
5. Yan etki/çağrı adımını çalıştır: parser.add_argument('--out-dir', type=Path)
6. Yan etki/çağrı adımını çalıştır: parser.add_argument('--seconds', type=float, help='Pencere açmadan belirtilen simülasyon süresini çalıştır.')
7. Yan etki/çağrı adımını çalıştır: parser.add_argument('--smoke-frames', type=int, help=argparse.SUPPRESS)
8. Değeri/alanı oluştur veya güncelle: args = parser.parse_args(argv)
9. Değeri/alanı oluştur veya güncelle: scene = load_scene(args.scene) if args.scene else lesson_scene(args.lesson)
10. Koşula göre yol seç: args.seed is not None
11. Koşula göre yol seç: args.seconds is not None

**Gerçek kaynak:**

```python
def main(argv=None):
    parser=argparse.ArgumentParser(description="Öğretici IoT deney ortamı")
    parser.add_argument("--lesson",type=int,choices=range(1,7),default=1)
    parser.add_argument("--scene",type=Path)
    parser.add_argument("--seed",type=int)
    parser.add_argument("--out-dir",type=Path)
    parser.add_argument("--seconds",type=float,help="Pencere açmadan belirtilen simülasyon süresini çalıştır.")
    parser.add_argument("--smoke-frames",type=int,help=argparse.SUPPRESS)
    args=parser.parse_args(argv)
    scene=load_scene(args.scene) if args.scene else lesson_scene(args.lesson)
    if args.seed is not None: scene["seed"]=args.seed
    if args.seconds is not None:
        sim=Simulation(scene)
        with Exporter(args.out_dir,scene=scene) as exporter:
            sim.start_recording(exporter)
            sim.advance(args.seconds)
            print(f"{sim.time:.2f} simülasyon saniyesi • {sim.alarm.total_events} olay • {exporter.directory}")
    else:
        App(scene,args.out_dir).run(args.smoke_frames)
```


## iot_sim/assets.py

İkonları yükler; eksik görselde None ile şekil çizimine geri dönüş sağlar.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: import pygame

```python
import pygame
```

### load_icon — satır 4

Görüntüyü alfa kanallı yüzeye dönüştürür; yükleme başarısızsa None ile geri dönüşe izin verir.

**Girdiler:** path: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** pygame.image.load(path).convert_alpha(); None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** pygame.image.load(path).convert_alpha, pygame.image.load
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def load_icon(path: str):
    try:
        return pygame.image.load(path).convert_alpha()
    except Exception:
        return None
```

### get_scaled_icon — satır 11

Aynı ikon ve boyut için yeniden ölçeklemeyi önbellekten karşılar.

**Girdiler:** cache: dict, key: str, surf, size: tuple[int, int]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None; cache[k]
**Atanan yerel değerler / durum alanları:** k, cache[k]
**Bağlandığı işlevler:** pygame.transform.smoothscale
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: surf is None
2. Değeri/alanı oluştur veya güncelle: k = (key, size[0], size[1])
3. Koşula göre yol seç: k in cache
4. Değeri/alanı oluştur veya güncelle: cache[k] = pygame.transform.smoothscale(surf, size)
5. Çağırana sonucu döndür: cache[k]

**Gerçek kaynak:**

```python
def get_scaled_icon(cache: dict, key: str, surf, size: tuple[int, int]):
    if surf is None:
        return None

    k = (key, size[0], size[1])
    if k in cache:
        return cache[k]

    cache[k] = pygame.transform.smoothscale(surf, size)
    return cache[k]
```


## iot_sim/camera.py

Ekran ve dünya koordinatları arasındaki dönüşüm ve zoom durumudur.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Boyutu değişen görünümde dünya/ekran koordinat dönüşümü."""
```

Satır 2: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 3: Gereken isimleri içeri al: from .engine import clamp

```python
from .engine import clamp
```

### Camera — satır 6

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Camera.__init__ — satır 7

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** (self.x, self.y, self.zoom), self.viewport
**Bağlandığı işlevler:** pygame.Rect
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.x, self.y, self.zoom = (12.0, 12.0, 1.4)
2. Değeri/alanı oluştur veya güncelle: self.viewport = pygame.Rect(0, 100, 800, 600)

**Gerçek kaynak:**

```python
def __init__(self):
        self.x, self.y, self.zoom = 12.0, 12.0, 1.4
        self.viewport = pygame.Rect(0, 100, 800, 600)
```

### Camera.world_to_screen — satır 11

Kamera merkezi, görünüm alanı ve zoom ile dünya noktasını piksele çevirir.

**Girdiler:** self, x, y, tile_px=24. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (round(self.viewport.centerx + (x - self.x) * tile_px * self.zoom), round(self.viewport.centery + (y - self.y) * tile_px * self.zoom))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: (round(self.viewport.centerx + (x - self.x) * tile_px * self.zoom), round(self.viewport.centery + (y - self.y) * tile_px * self.zoom))

**Gerçek kaynak:**

```python
def world_to_screen(self, x, y, tile_px=24):
        return (round(self.viewport.centerx + (x-self.x)*tile_px*self.zoom),
                round(self.viewport.centery + (y-self.y)*tile_px*self.zoom))
```

### Camera.screen_to_world — satır 15

Ekrandaki fare konumunu kamera dönüşümünün tersiyle dünya koordinatına çevirir.

**Girdiler:** self, pos, tile_px=24. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** ((pos[0] - self.viewport.centerx) / (tile_px * self.zoom) + self.x, (pos[1] - self.viewport.centery) / (tile_px * self.zoom) + self.y)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: ((pos[0] - self.viewport.centerx) / (tile_px * self.zoom) + self.x, (pos[1] - self.viewport.centery) / (tile_px * self.zoom) + self.y)

**Gerçek kaynak:**

```python
def screen_to_world(self, pos, tile_px=24):
        return ((pos[0]-self.viewport.centerx)/(tile_px*self.zoom)+self.x,
                (pos[1]-self.viewport.centery)/(tile_px*self.zoom)+self.y)
```

### Camera.zoom_at — satır 19

Mevcut ölçeği verilen katsayıyla değiştirip izin verilen aralıkta tutar.

**Girdiler:** self, factor, tile_px=24, map_w=200, map_h=200. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.zoom
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.zoom = clamp(self.zoom * factor, 0.35, 3.5)

**Gerçek kaynak:**

```python
def zoom_at(self, factor, tile_px=24, map_w=200, map_h=200):
        self.zoom = clamp(self.zoom * factor, .35, 3.5)
```

### Camera.clamp_zoom_for_map — satır 22

Zoom değerini sınırlar; alternatif sürümde harita boyutunu da dikkate alır.

**Girdiler:** self, tile_px, map_w, map_h. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.zoom
**Bağlandığı işlevler:** clamp
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.zoom = clamp(self.zoom, 0.35, 3.5)

**Gerçek kaynak:**

```python
def clamp_zoom_for_map(self, tile_px, map_w, map_h):
        self.zoom = clamp(self.zoom, .35, 3.5)
```


## iot_sim/cargo.py

Drone yükleme kapasitesi ve karşılıklı taşıyıcı referanslarını yönetir.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: from .models import Entity, Kind

```python
from .models import Entity, Kind
```

Satır 2: Gereken isimleri içeri al: from .engine import find_entity_by_id

```python
from .engine import find_entity_by_id
```

### can_attach_to_uav — satır 5

Taşıyıcı türü, yük türü, zaten taşınma ve kapasite kurallarını kontrol eder.

**Girdiler:** entities: list[Entity], uav: Entity, candidate: Entity. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; True; nsrc < 3
**Atanan yerel değerler / durum alanları:** up, carried, have_sensor, have_source, nsrc
**Bağlandığı işlevler:** find_entity_by_id, any, sum
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: uav.kind != Kind.UAV or uav.uav is None
2. Koşula göre yol seç: candidate.kind not in (Kind.SOURCE, Kind.SENSOR, Kind.BURNED)
3. Koşula göre yol seç: candidate.carried_by is not None
4. Değeri/alanı oluştur veya güncelle: up = uav.uav
5. Değeri/alanı oluştur veya güncelle: carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
6. Değeri/alanı oluştur veya güncelle: carried = [c for c in carried if c is not None]
7. Değeri/alanı oluştur veya güncelle: have_sensor = any((c.kind == Kind.SENSOR for c in carried))
8. Değeri/alanı oluştur veya güncelle: have_source = any((c.kind in (Kind.SOURCE, Kind.BURNED) for c in carried))
9. Koşula göre yol seç: candidate.kind == Kind.SENSOR
10. Koşula göre yol seç: have_sensor
11. Değeri/alanı oluştur veya güncelle: nsrc = sum((1 for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED)))
12. Çağırana sonucu döndür: nsrc < 3

**Gerçek kaynak:**

```python
def can_attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if uav.kind != Kind.UAV or uav.uav is None:
        return False
    if candidate.kind not in (Kind.SOURCE, Kind.SENSOR, Kind.BURNED):
        return False
    if candidate.carried_by is not None:
        return False

    up = uav.uav
    carried = [find_entity_by_id(entities, cid) for cid in up.carrying_ids]
    carried = [c for c in carried if c is not None]

    have_sensor = any(c.kind == Kind.SENSOR for c in carried)
    have_source = any(c.kind in (Kind.SOURCE, Kind.BURNED) for c in carried)

    if candidate.kind == Kind.SENSOR:
        if have_source:
            return False
        if have_sensor:
            return False
        return True

    if have_sensor:
        return False

    nsrc = sum(1 for c in carried if c.kind in (Kind.SOURCE, Kind.BURNED))
    return nsrc < 3
```

### attach_to_uav — satır 34

Uygun yükü drone'a bağlar; kimlik listesi, taşıyıcı ve konumu birlikte günceller.

**Girdiler:** entities: list[Entity], uav: Entity, candidate: Entity. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; True
**Atanan yerel değerler / durum alanları:** up, candidate.carried_by, candidate.tx, candidate.ty
**Bağlandığı işlevler:** can_attach_to_uav, up.carrying_ids.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: not can_attach_to_uav(entities, uav, candidate)
2. Değeri/alanı oluştur veya güncelle: up = uav.uav
3. Koşula göre yol seç: up is None
4. Yan etki/çağrı adımını çalıştır: up.carrying_ids.append(candidate.id)
5. Değeri/alanı oluştur veya güncelle: candidate.carried_by = uav.id
6. Değeri/alanı oluştur veya güncelle: candidate.tx = uav.tx
7. Değeri/alanı oluştur veya güncelle: candidate.ty = uav.ty
8. Çağırana sonucu döndür: True

**Gerçek kaynak:**

```python
def attach_to_uav(entities: list[Entity], uav: Entity, candidate: Entity) -> bool:
    if not can_attach_to_uav(entities, uav, candidate):
        return False
    up = uav.uav
    if up is None:
        return False

    up.carrying_ids.append(candidate.id)
    candidate.carried_by = uav.id
    candidate.tx = uav.tx
    candidate.ty = uav.ty
    return True
```


## iot_sim/constants.py

Korunmuş sabitler. Yeni ekran boyutu App.layout, zaman adımı Simulation.STEP içindedir.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: import math

```python
import math
```

Satır 3: Değeri/alanı oluştur veya güncelle: SCREEN_W, SCREEN_H = (1200, 800)

```python
SCREEN_W, SCREEN_H = 1200, 800
```

Satır 4: Değeri/alanı oluştur veya güncelle: PANEL_W = 320

```python
PANEL_W = 320
```

Satır 5: Değeri/alanı oluştur veya güncelle: FPS = 60

```python
FPS = 60
```

Satır 7: Değeri/alanı oluştur veya güncelle: DEFAULT_TILE = 16

```python
DEFAULT_TILE = 16
```

Satır 8: Değeri/alanı oluştur veya güncelle: MAX_ZOOM = 4.0

```python
MAX_ZOOM = 4.0
```

Satır 9: Değeri/alanı oluştur veya güncelle: MIN_ZOOM_FLOOR = 0.15

```python
MIN_ZOOM_FLOOR = 0.15
```

Satır 11: Değeri/alanı oluştur veya güncelle: TICK_SECONDS = 1.0

```python
TICK_SECONDS = 1.0
```

Satır 13: Değeri/alanı oluştur veya güncelle: ACCURACY_BY_DIST = [100, 99, 96, 90, 82, 70, 55, 40, 28, 18, 12, 8, 5, 3, 2, 1]

```python
ACCURACY_BY_DIST = [100, 99, 96, 90, 82, 70, 55, 40, 28, 18, 12, 8, 5, 3, 2, 1]
```

Satır 15: Değeri/alanı oluştur veya güncelle: PAN_SPEED = 1.0

```python
PAN_SPEED = 1.0
```

Satır 16: Değeri/alanı oluştur veya güncelle: PAN_DRAG_THRESHOLD_PX = 4

```python
PAN_DRAG_THRESHOLD_PX = 4
```

Satır 17: Değeri/alanı oluştur veya güncelle: FIELD_STEP_PX = 6

```python
FIELD_STEP_PX = 6
```

Satır 19: Değeri/alanı oluştur veya güncelle: PAD = 20

```python
PAD = 20
```

Satır 20: Değeri/alanı oluştur veya güncelle: SECTION_GAP = 18

```python
SECTION_GAP = 18
```

Satır 22: Değeri/alanı oluştur veya güncelle: PANEL_Y_APPEAR = 370

```python
PANEL_Y_APPEAR = 370
```

Satır 23: Değeri/alanı oluştur veya güncelle: PANEL_Y_GLOBAL_SWITCH = 406

```python
PANEL_Y_GLOBAL_SWITCH = 406
```

Satır 24: Değeri/alanı oluştur veya güncelle: PANEL_Y_SELECTED_TITLE = 450

```python
PANEL_Y_SELECTED_TITLE = 450
```

Satır 25: Değeri/alanı oluştur veya güncelle: PANEL_Y_SELECTED_LABEL = 490

```python
PANEL_Y_SELECTED_LABEL = 490
```

Satır 26: Değeri/alanı oluştur veya güncelle: PANEL_SCROLL_Y0 = 520

```python
PANEL_SCROLL_Y0 = 520
```

Satır 28: Değeri/alanı oluştur veya güncelle: DRAG_THRESHOLD_PX = 6

```python
DRAG_THRESHOLD_PX = 6
```


## iot_sim/engine.py

Kimlik/konum arama, sınırlandırma ve rota için karo geometrisi sağlar. Eski doğruluk yardımcısı korunmuştur.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: import math

```python
import math
```

Satır 2: Gereken isimleri içeri al: import random

```python
import random
```

Satır 3: Gereken isimleri içeri al: from .models import *

```python
from .models import *
```

Satır 4: Gereken isimleri içeri al: from .constants import *

```python
from .constants import *
```

Satır 5: Gereken isimleri içeri al: from .constants import ACCURACY_BY_DIST

```python
from .constants import ACCURACY_BY_DIST
```

Satır 6: Gereken isimleri içeri al: from .models import Entity

```python
from .models import Entity
```

### clamp — satır 8

Sayısal değeri alt ve üst sınır arasında tutar; panel ve konum ayarlarında kullanılır.

**Girdiler:** v, lo, hi. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** max(lo, min(hi, v))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** max, min
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: max(lo, min(hi, v))

**Gerçek kaynak:**

```python
def clamp(v, lo, hi):
    return max(lo, min(hi, v))
```

### accuracy_for_dist — satır 11

Eski uzaklık tablosundan yüzde döndürür; yeni noktasal ölçüm bunu kullanmaz.

**Girdiler:** d: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** 0; ACCURACY_BY_DIST[d]
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** len
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: d < 0
2. Koşula göre yol seç: d < len(ACCURACY_BY_DIST)
3. Çağırana sonucu döndür: 0

**Gerçek kaynak:**

```python
def accuracy_for_dist(d: int) -> int:
    if d < 0:
        return 0
    if d < len(ACCURACY_BY_DIST):
        return ACCURACY_BY_DIST[d]
    return 0
```

### tile_occupied — satır 18

Taşınmayan nesneler arasında hedef karenin dolu olup olmadığını söyler.

**Girdiler:** entities: list[Entity], tx: int, ty: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** True; False
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: e ← entities
2. Çağırana sonucu döndür: False

**Gerçek kaynak:**

```python
def tile_occupied(entities: list[Entity], tx: int, ty: int) -> bool:
    for e in entities:
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return True
    return False
```

### find_entity_at — satır 26

Bir karenin seçilebilir nesnesinin listedeki indeksini bulur; taşınan yükü atlar.

**Girdiler:** entities: list[Entity], tx: int, ty: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** i; None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** enumerate
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: (i, e) ← enumerate(entities)
2. Çağırana sonucu döndür: None

**Gerçek kaynak:**

```python
def find_entity_at(entities: list[Entity], tx: int, ty: int):
    # Prefer non-carried things for selection
    for i, e in enumerate(entities):
        if e.carried_by is not None:
            continue
        if e.tx == tx and e.ty == ty:
            return i
    return None
```

### find_entity_by_id — satır 35

Kalıcı nesne kimliğini gerçek nesneye çözer; bulunamazsa None döner.

**Girdiler:** entities: list[Entity], eid: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** e; None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: e ← entities
2. Çağırana sonucu döndür: None

**Gerçek kaynak:**

```python
def find_entity_by_id(entities: list[Entity], eid: int):
    for e in entities:
        if e.id == eid:
            return e
    return None
```

### build_entity_index — satır 41

O(1) lookup için entity id -> Entity dict'i oluşturur.

**Girdiler:** entities: list[Entity]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** {e.id: e for e in entities}
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: {e.id: e for e in entities}

**Gerçek kaynak:**

```python
def build_entity_index(entities: list[Entity]) -> dict[int, Entity]:
    """O(1) lookup için entity id -> Entity dict'i oluşturur."""
    return {e.id: e for e in entities}
```

### dist — satır 45

İki konum arasındaki Öklid uzaklığını hesaplar.

**Girdiler:** a, b. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** math.hypot(a[0] - b[0], a[1] - b[1])
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** math.hypot
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: math.hypot(a[0] - b[0], a[1] - b[1])

**Gerçek kaynak:**

```python
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])
```

### bresenham_tiles — satır 49

Bir doğru boyunca geçilen tam sayı karolarını sırayla üretir; rota engel testinin temelidir.

**Girdiler:** x0: int, y0: int, x1: int, y1: int. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (x, y)
**Atanan yerel değerler / durum alanları:** dx, dy, sx, sy, err, (x, y), e2, x, y
**Bağlandığı işlevler:** abs
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: dx = abs(x1 - x0)
2. Değeri/alanı oluştur veya güncelle: dy = abs(y1 - y0)
3. Değeri/alanı oluştur veya güncelle: sx = 1 if x0 < x1 else -1
4. Değeri/alanı oluştur veya güncelle: sy = 1 if y0 < y1 else -1
5. Değeri/alanı oluştur veya güncelle: err = dx - dy
6. Değeri/alanı oluştur veya güncelle: x, y = (x0, y0)
7. Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: True

**Gerçek kaynak:**

```python
def bresenham_tiles(x0: int, y0: int, x1: int, y1: int):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
```

### route_is_valid — satır 68

Başlangıç, tüm parçalar ve LOOP dönüşünü kapsayan rota kontrolü.

**Girdiler:** route_points, obstacle_tiles, mode=RouteMode.LOOP, start=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** False; all((not any((p in obstacle_tiles for p in bresenham_tiles(*a, *b))) for a, b in zip(points, points[1:])))
**Atanan yerel değerler / durum alanları:** points
**Bağlandığı işlevler:** len, set, list, points.append, points.insert, tuple, int, round, all, any, bresenham_tiles, zip
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: len(set(route_points)) < 2
2. Değeri/alanı oluştur veya güncelle: points = list(route_points)
3. Koşula göre yol seç: mode == RouteMode.LOOP
4. Koşula göre yol seç: start is not None
5. Çağırana sonucu döndür: all((not any((p in obstacle_tiles for p in bresenham_tiles(*a, *b))) for a, b in zip(points, points[1:])))

**Gerçek kaynak:**

```python
def route_is_valid(route_points, obstacle_tiles, mode=RouteMode.LOOP, start=None) -> bool:
    """Başlangıç, tüm parçalar ve LOOP dönüşünü kapsayan rota kontrolü."""
    if len(set(route_points)) < 2:
        return False
    points = list(route_points)
    if mode == RouteMode.LOOP:
        points.append(points[0])
    if start is not None:
        points.insert(0, tuple(int(round(v)) for v in start))
    return all(not any(p in obstacle_tiles for p in bresenham_tiles(*a, *b))
               for a, b in zip(points, points[1:]))
```


## iot_sim/exporter.py

Her deney için yeni klasör ve dosyalar oluşturur; ölçüm/olay/değişiklikleri yazar.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Her deney için ayrı, üzerine yazılmayan sonuç klasörü."""
```

Satır 2: Gereken isimleri içeri al: import csv

```python
import csv
```

Satır 3: Gereken isimleri içeri al: import json

```python
import json
```

Satır 4: Gereken isimleri içeri al: import tempfile

```python
import tempfile
```

Satır 5: Gereken isimleri içeri al: from contextlib import ExitStack

```python
from contextlib import ExitStack
```

Satır 6: Gereken isimleri içeri al: from datetime import datetime

```python
from datetime import datetime
```

Satır 7: Gereken isimleri içeri al: from pathlib import Path

```python
from pathlib import Path
```

Satır 8: Gereken isimleri içeri al: from .sensors import VALUE_ATTR, position

```python
from .sensors import VALUE_ATTR, position
```

Satır 9: Gereken isimleri içeri al: from .scene import MODEL_VERSION

```python
from .scene import MODEL_VERSION
```

Satır 11: Değeri/alanı oluştur veya güncelle: ROOT = Path(__file__).resolve().parent.parent

```python
ROOT = Path(__file__).resolve().parent.parent
```

### Exporter — satır 14

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Exporter.__init__ — satır 15

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, out_dir=None, tag=None, scene=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** root, self.directory, self.stack, self.streams, self.closed, self.rows, self.csv_path, self.alarm_path, self.actions_path, self._sensor, self._alarm, self._actions, metadata
**Bağlandığı işlevler:** Path, root.mkdir, tempfile.mkdtemp, datetime.now().strftime, datetime.now, ExitStack, self._writer, self.stack.enter_context, self.actions_path.open, self.streams.append, (self.directory / 'experiment.json').write_text, json.dumps, self.stack.close
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: root = Path(out_dir) if out_dir is not None else ROOT / 'exports'
2. Yan etki/çağrı adımını çalıştır: root.mkdir(parents=True, exist_ok=True)
3. Değeri/alanı oluştur veya güncelle: self.directory = Path(tempfile.mkdtemp(prefix=datetime.now().strftime('%Y%m%d_%H%M%S_'), dir=root))
4. Değeri/alanı oluştur veya güncelle: self.stack = ExitStack()
5. Değeri/alanı oluştur veya güncelle: self.streams = []
6. Değeri/alanı oluştur veya güncelle: self.closed = False
7. Değeri/alanı oluştur veya güncelle: self.rows = 0
8. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def __init__(self, out_dir=None, tag=None, scene=None):
        root = Path(out_dir) if out_dir is not None else ROOT / "exports"
        root.mkdir(parents=True, exist_ok=True)
        self.directory = Path(tempfile.mkdtemp(prefix=datetime.now().strftime("%Y%m%d_%H%M%S_"), dir=root))
        self.stack = ExitStack()
        self.streams = []
        self.closed = False
        self.rows = 0
        try:
            self.csv_path = self.directory / "sensor_log.csv"
            self.alarm_path = self.directory / "alarm_log.csv"
            self.actions_path = self.directory / "changes.jsonl"
            self._sensor = self._writer(self.csv_path, ["t", "sensor_id", "sensor_name", "x", "y", "carried_by",
                "channel", "valid", "status", "measured", "theoretical", "battery", "threshold", "clear_threshold"])
            self._alarm = self._writer(self.alarm_path, ["t", "sensor_id", "sensor_name", "channel", "kind", "value", "details"])
            self._actions = self.stack.enter_context(self.actions_path.open("x", encoding="utf-8"))
            self.streams.append(self._actions)
            metadata = {"schema_version": 2, "model_version": MODEL_VERSION, "scene": scene,
                        "units": {"TEMP": "°C", "CO": "ppm", "CO2": "ppm", "H2": "ppm", "battery": "eğitim enerji birimi"}}
            (self.directory / "experiment.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2, allow_nan=False))
        except Exception:
            self.stack.close()
            raise
```

### Exporter._writer — satır 39

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** self, path, fields. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** writer
**Atanan yerel değerler / durum alanları:** f, writer
**Bağlandığı işlevler:** self.stack.enter_context, path.open, self.streams.append, csv.DictWriter, writer.writeheader
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: f = self.stack.enter_context(path.open('x', newline='', encoding='utf-8'))
2. Yan etki/çağrı adımını çalıştır: self.streams.append(f)
3. Değeri/alanı oluştur veya güncelle: writer = csv.DictWriter(f, fieldnames=fields)
4. Yan etki/çağrı adımını çalıştır: writer.writeheader()
5. Çağırana sonucu döndür: writer

**Gerçek kaynak:**

```python
def _writer(self, path, fields):
        f = self.stack.enter_context(path.open("x", newline="", encoding="utf-8"))
        self.streams.append(f)
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        return writer
```

### Exporter.log_sensor — satır 46

Örneğin kanal değerlerini, geçerliliğini, konumunu ve eşiklerini CSV'ye yazar.

**Girdiler:** self, sim_time, entity, entities=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s, (x, y), value, valid, self.rows
**Bağlandığı işlevler:** position, VALUE_ATTR.items, getattr, self._sensor.writerow, dict, round, int, s.theoretical.get, self.flush
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s = entity.sensor
2. Değeri/alanı oluştur veya güncelle: x, y = position(entity, entities or [entity])
3. Her öğe için işle: (channel, attr) ← VALUE_ATTR.items()
4. Değeri/alanı oluştur veya güncelle: self.rows += 1
5. Koşula göre yol seç: self.rows % 20 == 0

**Gerçek kaynak:**

```python
def log_sensor(self, sim_time, entity, entities=None):
        s = entity.sensor
        x, y = position(entity, entities or [entity])
        for channel, attr in VALUE_ATTR.items():
            value = getattr(s, attr)
            valid = s.valid and value is not None
            self._sensor.writerow(dict(t=round(sim_time, 6), sensor_id=entity.id, sensor_name=entity.name,
                x=x, y=y, carried_by=entity.carried_by, channel=channel, valid=int(valid), status=s.status,
                measured=value if valid else "", theoretical=s.theoretical.get(channel) if valid else "",
                battery=s.battery, threshold=s.thresholds[channel], clear_threshold=s.clear_thresholds[channel]))
        self.rows += 1
        if self.rows % 20 == 0:
            self.flush()
```

### Exporter.log_event — satır 60

Bir geçiş/durum olayını CSV'ye yazar ve tamponu boşaltır.

**Girdiler:** self, event. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self._alarm.writerow, self.flush
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self._alarm.writerow(event)
2. Yan etki/çağrı adımını çalıştır: self.flush()

**Gerçek kaynak:**

```python
def log_event(self, event):
        self._alarm.writerow(event)
        self.flush()
```

### Exporter.log_change — satır 64

Kullanıcı müdahalesini zamanı ve sahne düzeniyle JSONL satırı olarak kaydeder.

**Girdiler:** self, sim_time, action, scene. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self._actions.write, json.dumps, dict, round, self.flush
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self._actions.write(json.dumps(dict(t=round(sim_time, 6), action=action, scene=scene), ensure_ascii=False, allow_nan=False) + '\n')
2. Yan etki/çağrı adımını çalıştır: self.flush()

**Gerçek kaynak:**

```python
def log_change(self, sim_time, action, scene):
        self._actions.write(json.dumps(dict(t=round(sim_time, 6), action=action, scene=scene),
                                       ensure_ascii=False, allow_nan=False) + "\n")
        self.flush()
```

### Exporter.flush — satır 69

Açık dosyaların Python tamponunu işletim sistemine iletir; tek başına fiziksel disk garantisi değildir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** stream.flush
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: stream ← self.streams

**Gerçek kaynak:**

```python
def flush(self):
        for stream in self.streams:
            if not stream.closed:
                stream.flush()
```

### Exporter.close — satır 74

Kaynakları tekrar çağrılmaya dayanıklı biçimde kapatır ve çıktı konumunu döndürür.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.directory
**Atanan yerel değerler / durum alanları:** self.closed
**Bağlandığı işlevler:** self.stack.close
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: not self.closed
2. Çağırana sonucu döndür: self.directory

**Gerçek kaynak:**

```python
def close(self):
        if not self.closed:
            self.stack.close()
            self.closed = True
        return self.directory
```

### Exporter.__enter__ — satır 80

with bloğunun kullanacağı nesneyi döndürür.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: self

**Gerçek kaynak:**

```python
def __enter__(self):
        return self
```

### Exporter.__exit__ — satır 83

with bloğundan normal veya hatalı çıkışta kaynakları kapatır.

**Girdiler:** self, exc_type, exc, traceback. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self.close
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.close()

**Gerçek kaynak:**

```python
def __exit__(self, exc_type, exc, traceback):
        self.close()
```


## iot_sim/fire.py

Yanabilirlik, eşik sıcaklık ve süreye göre ağaçları kaynak yapar.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Sıcaklık ve kesintisiz maruz kalma süresine bağlı eğitim modeli."""
```

Satır 2: Gereken isimleri içeri al: from .models import Kind, SourceProps, SourceType

```python
from .models import Kind, SourceProps, SourceType
```

Satır 3: Gereken isimleri içeri al: from .sensors import field_at

```python
from .sensors import field_at
```

### spread_fire — satır 6

Önce tüm sıcaklıkları hesapla; sonra tutuşanları birlikte dönüştür.

**Girdiler:** entities, dt=2.0. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** burning
**Atanan yerel değerler / durum alanları:** burning, temperature, e.heat_seconds, e.kind, e.source, e.icon_override
**Bağlandığı işlevler:** field_at, burning.append, SourceProps
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: burning = []
2. Her öğe için işle: e ← entities
3. Her öğe için işle: e ← burning
4. Çağırana sonucu döndür: burning

**Gerçek kaynak:**

```python
def spread_fire(entities, dt=2.0):
    """Önce tüm sıcaklıkları hesapla; sonra tutuşanları birlikte dönüştür."""
    burning = []
    for e in entities:
        if e.kind != Kind.OBSTACLE or not e.flammable:
            continue
        temperature = field_at(e.tx, e.ty, entities)["TEMP"]
        e.heat_seconds = e.heat_seconds + dt if temperature >= e.ignition_temp else 0.0
        if e.heat_seconds + 1e-9 >= e.ignition_seconds:
            burning.append(e)
    for e in burning:
        e.kind = Kind.BURNED
        e.source = SourceProps(stype=SourceType.TEMP, temp_celcius=300, range_tiles=6)
        e.icon_override = "burned"
    return burning
```


## iot_sim/geom.py

Korunan çokgen sıralama ve alan yardımcıları; yeni noktadan ölçüm akışına bağlı değildir.

### Dosya düzeyindeki kod

Satır 2: Gereken isimleri içeri al: import math

```python
import math
```

Satır 3: Gereken isimleri içeri al: from typing import List, Tuple

```python
from typing import List, Tuple
```

Satır 5: Değeri/alanı oluştur veya güncelle: Point = Tuple[float, float]

```python
Point = Tuple[float, float]
```

### order_polygon_points — satır 7

Centroid'e göre açı sıralaması (CW/CCW).

**Girdiler:** points: List[Point]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** points[:]; sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
**Atanan yerel değerler / durum alanları:** cx, cy
**Bağlandığı işlevler:** len, sum, sorted, math.atan2
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: len(points) < 3
2. Değeri/alanı oluştur veya güncelle: cx = sum((p[0] for p in points)) / len(points)
3. Değeri/alanı oluştur veya güncelle: cy = sum((p[1] for p in points)) / len(points)
4. Çağırana sonucu döndür: sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))

**Gerçek kaynak:**

```python
def order_polygon_points(points: List[Point]) -> List[Point]:
    """Centroid'e göre açı sıralaması (CW/CCW)."""
    if len(points) < 3:
        return points[:]
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    return sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
```

### polygon_area — satır 15

Shoelace formula. points ordered olmalı (order_polygon_points ile sırala).

**Girdiler:** points: List[Point]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** 0.0; abs(s) * 0.5
**Atanan yerel değerler / durum alanları:** n, s, (x1, y1), (x2, y2)
**Bağlandığı işlevler:** len, range, abs
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: n = len(points)
2. Koşula göre yol seç: n < 3
3. Değeri/alanı oluştur veya güncelle: s = 0.0
4. Her öğe için işle: i ← range(n)
5. Çağırana sonucu döndür: abs(s) * 0.5

**Gerçek kaynak:**

```python
def polygon_area(points: List[Point]) -> float:
    """Shoelace formula. points ordered olmalı (order_polygon_points ile sırala)."""
    n = len(points)
    if n < 3:
        return 0.0
    s = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - y1 * x2
    return abs(s) * 0.5
```


## iot_sim/graphs.py

Sensör geçmişini kanal/birim bazında ölçüm, teori, eşik ve pil grafiğine dönüştürür.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Sınırlı geçmişten birimleri ayrı canlı kanal ve pil grafiği."""
```

Satır 2: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 3: Gereken isimleri içeri al: from .ui_widgets import TEXT, MUTED, ACCENT, BORDER

```python
from .ui_widgets import TEXT,MUTED,ACCENT,BORDER
```

### draw_graph — satır 6

Boş/kapalı örneklerde çizgiyi kes; olay anları ve eşik geçmişini çiz.

**Girdiler:** screen, rect, history, channel, font, theory=True. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** unit, label, rows, values, v, (low, high), margin, plot, (t0, t1), value, y, keys, previous, p, last, active, x, end
**Bağlandığı işlevler:** pygame.draw.rect, screen.blit, font.render, list, values.append, row[key].get, min, max, pygame.Rect, range, point, pygame.draw.line, keys.append, pygame.draw.circle, end.get_width
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, (19, 29, 41), rect, border_radius=12)
2. Değeri/alanı oluştur veya güncelle: unit = 'enerji' if channel == 'BATTERY' else '°C' if channel == 'TEMP' else 'ppm'
3. Değeri/alanı oluştur veya güncelle: label = f'{channel} • {unit}    Ölçüm / pil'
4. Koşula göre yol seç: theory and channel != 'BATTERY'
5. Yan etki/çağrı adımını çalıştır: screen.blit(font.render(label, True, TEXT), (rect.x + 14, rect.y + 10))
6. Koşula göre yol seç: not history
7. Değeri/alanı oluştur veya güncelle: rows = list(history)[-180:]
8. Değeri/alanı oluştur veya güncelle: values = []
9. Her öğe için işle: row ← rows
10. Koşula göre yol seç: not values
11. Değeri/alanı oluştur veya güncelle: low, high = (min(values), max(values))
12. Değeri/alanı oluştur veya güncelle: margin = max(1, (high - low) * 0.12)
13. Değeri/alanı oluştur veya güncelle: low, high = (low - margin, high + margin)
14. Değeri/alanı oluştur veya güncelle: plot = pygame.Rect(rect.x + 57, rect.y + 39, max(40, rect.width - 78), max(30, rect.height - 67))
15. Değeri/alanı oluştur veya güncelle: t0, t1 = (rows[0]['t'], max(rows[-1]['t'], rows[0]['t'] + 1))
16. Yerel yardımcı tanımla: point; ayrı sembol kaydı aşağıdadır.
17. Her öğe için işle: i ← range(3)
18. Değeri/alanı oluştur veya güncelle: keys = [('battery', ACCENT)] if channel == 'BATTERY' else [('measured', ACCENT), ('thresholds', (235, 182, 98))]
19. Koşula göre yol seç: theory and channel != 'BATTERY'
20. Her öğe için işle: (key, color) ← keys
21. Değeri/alanı oluştur veya güncelle: last = False
22. Her öğe için işle: row ← rows
23. Yan etki/çağrı adımını çalıştır: screen.blit(font.render(f'{t0:.1f}s', True, MUTED), (plot.left, plot.bottom + 7))
24. Değeri/alanı oluştur veya güncelle: end = font.render(f'{rows[-1]['t']:.1f}s', True, MUTED)
25. Yan etki/çağrı adımını çalıştır: screen.blit(end, (plot.right - end.get_width(), plot.bottom + 7))

**Gerçek kaynak:**

```python
def draw_graph(screen, rect, history, channel, font, theory=True):
    """Boş/kapalı örneklerde çizgiyi kes; olay anları ve eşik geçmişini çiz."""
    pygame.draw.rect(screen,(19,29,41),rect,border_radius=12)
    unit="enerji" if channel=="BATTERY" else "°C" if channel=="TEMP" else "ppm"
    label=f"{channel} • {unit}    Ölçüm / pil"
    if theory and channel!="BATTERY": label+="    Teorik + eşik"
    screen.blit(font.render(label,True,TEXT),(rect.x+14,rect.y+10))
    if not history:
        screen.blit(font.render("Başlat veya Tek adım ile ilk örneği al.",True,MUTED),(rect.x+14,rect.y+48))
        return
    rows=list(history)[-180:]
    values=[]
    for row in rows:
        if channel=="BATTERY": values.append(row["battery"])
        else:
            for key in ("measured","theoretical" if theory else "measured","thresholds"):
                v=row[key].get(channel)
                if v is not None: values.append(v)
    if not values: values=[0,1]
    low,high=min(values),max(values)
    margin=max(1,(high-low)*.12)
    low,high=low-margin,high+margin
    plot=pygame.Rect(rect.x+57,rect.y+39,max(40,rect.width-78),max(30,rect.height-67))
    t0,t1=rows[0]["t"],max(rows[-1]["t"],rows[0]["t"]+1)
    def point(t,value):
        return (round(plot.left+(t-t0)/(t1-t0)*plot.width),round(plot.bottom-(value-low)/(high-low)*plot.height))
    for i in range(3):
        value=low+(high-low)*i/2
        y=point(t0,value)[1]
        pygame.draw.line(screen,BORDER,(plot.left,y),(plot.right,y))
        screen.blit(font.render(f"{value:.0f}",True,MUTED),(rect.x+8,y-7))
    keys=[("battery",ACCENT)] if channel=="BATTERY" else [("measured",ACCENT),("thresholds",(235,182,98))]
    if theory and channel!="BATTERY": keys.append(("theoretical",(129,154,234)))
    for key,color in keys:
        previous=None
        for row in rows:
            value=row["battery"] if key=="battery" else row[key].get(channel)
            if value is None:
                previous=None
                continue
            p=point(row["t"],value)
            if previous: pygame.draw.line(screen,color,previous,p,2 if key=="measured" else 1)
            else: pygame.draw.circle(screen,color,p,2)
            previous=p
    last=False
    for row in rows:
        active=channel in row["alarms"]
        if active!=last:
            x=point(row["t"],low)[0]
            pygame.draw.line(screen,(150,71,87),(x,plot.top),(x,plot.bottom),1)
        last=active
    screen.blit(font.render(f"{t0:.1f}s",True,MUTED),(plot.left,plot.bottom+7))
    end=font.render(f"{rows[-1]['t']:.1f}s",True,MUTED)
    screen.blit(end,(plot.right-end.get_width(),plot.bottom+7))
```

### draw_graph.point — satır 30

Grafik zamanı ve değerini çizim dikdörtgeninin piksel koordinatına çevirir.

**Girdiler:** t, value. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (round(plot.left + (t - t0) / (t1 - t0) * plot.width), round(plot.bottom - (value - low) / (high - low) * plot.height))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: (round(plot.left + (t - t0) / (t1 - t0) * plot.width), round(plot.bottom - (value - low) / (high - low) * plot.height))

**Gerçek kaynak:**

```python
def point(t,value):
        return (round(plot.left+(t-t0)/(t1-t0)*plot.width),round(plot.bottom-(value-low)/(high-low)*plot.height))
```


## iot_sim/lessons.py

Altı Türkçe deneyin yönergeleri ve taze başlangıç sahnelerini üretir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Aynı şablonda altı Türkçe deney ve değiştirilebilir başlangıç sahneleri."""
```

Satır 2: Gereken isimleri içeri al: from .models import Entity, Kind, SensorProps, SensorMode, SourceProps, SourceType, GasMode, UavProps, RouteMode

```python
from .models import Entity, Kind, SensorProps, SensorMode, SourceProps, SourceType, GasMode, UavProps, RouteMode
```

Satır 3: Gereken isimleri içeri al: from .scene import to_scene

```python
from .scene import to_scene
```

Satır 5: Değeri/alanı oluştur veya güncelle: LESSONS = [dict(title='Uzaklık ve ölçüm', goal='Kaynağın etkisi ile cihaz hatasını ayır.', steps=['Başlat; Yakın ve Uzak sensörlerinin sıcaklıklarını karşılaştır.', 'Duraklat; Uzak sensörünü seç, M ile kaynağa yaklaştır …

```python
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
```

### lesson_scene — satır 39

1–6 arası hazır sahneyi her çağrıda yeni nesnelerle üret.

**Girdiler:** number. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** to_scene(entities, seed=42, lesson=number)
**Atanan yerel değerler / durum alanları:** source, entities, (source.tx, source.source.temp_celcius), s, (s.sensor.thresholds['TEMP'], s.sensor.clear_thresholds['TEMP']), source.source, source.name, drone, s.carried_by, (source.tx, source.ty), source.source.temp_celcius
**Bağlandığı işlevler:** ValueError, Entity, SourceProps, sensor, list, UavProps, to_scene
**Açık hata yolları:** ValueError('Deney numarası 1–6 olmalı.')

**İşleyiş sırası:**

1. Koşula göre yol seç: not 1 <= number <= 6
2. Yerel yardımcı tanımla: sensor; ayrı sembol kaydı aşağıdadır.
3. Değeri/alanı oluştur veya güncelle: source = Entity(3, Kind.SOURCE, 12, 12, name='Sıcaklık kaynağı', source=SourceProps(temp_celcius=180, range_tiles=12))
4. Koşula göre yol seç: number == 1
5. Çağırana sonucu döndür: to_scene(entities, seed=42, lesson=number)

**Gerçek kaynak:**

```python
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
```

### lesson_scene.sensor — satır 43

Hazır deneylerde benzer sensör nesnelerini okunur parametrelerle kuran yerel yardımcıdır.

**Girdiler:** eid, x, y, name, modes=None, **settings. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Entity(eid, Kind.SENSOR, x, y, name=name, sensor=SensorProps(modes=set(modes or [SensorMode.TEMP]), **settings))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Entity, SensorProps, set
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: Entity(eid, Kind.SENSOR, x, y, name=name, sensor=SensorProps(modes=set(modes or [SensorMode.TEMP]), **settings))

**Gerçek kaynak:**

```python
def sensor(eid, x, y, name, modes=None, **settings):
        return Entity(eid, Kind.SENSOR, x, y, name=name,
                      sensor=SensorProps(modes=set(modes or [SensorMode.TEMP]), **settings))
```


## iot_sim/models.py

Nesne ve kanal türleri ile bütün bileşenlerin paylaştığı durum alanlarını tanımlar.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: from dataclasses import dataclass, field

```python
from dataclasses import dataclass, field
```

Satır 2: Gereken isimleri içeri al: from enum import Enum

```python
from enum import Enum
```

Satır 37: Değeri/alanı oluştur veya güncelle: GAS_CRITICAL_PPM: dict[GasMode, float] = {GasMode.CO: 35.0, GasMode.CO2: 5000.0, GasMode.H2: 4000.0}

```python
GAS_CRITICAL_PPM: dict[GasMode, float] = {
    GasMode.CO:   35.0,
    GasMode.CO2:  5000.0,
    GasMode.H2:   4000.0,
}
```

Satır 43: Değeri/alanı oluştur veya güncelle: GAS_DANGER_PPM: dict[GasMode, float] = {GasMode.CO: 200.0, GasMode.CO2: 40000.0, GasMode.H2: 40000.0}

```python
GAS_DANGER_PPM: dict[GasMode, float] = {
    GasMode.CO:   200.0,
    GasMode.CO2:  40000.0,
    GasMode.H2:   40000.0,
}
```

Satır 49: Değeri/alanı oluştur veya güncelle: TEMP_CRITICAL_C = 60.0

```python
TEMP_CRITICAL_C = 60.0
```

Satır 50: Değeri/alanı oluştur veya güncelle: TEMP_DANGER_C = 100.0

```python
TEMP_DANGER_C   = 100.0
```

### Kind — satır 5

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
SENSOR = "SENSOR"
SOURCE = "SOURCE"
OBSTACLE = "OBSTACLE"
BURNED = "BURNED"
UAV = "UAV"
```

### SourceType — satır 13

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
TEMP = "TEMP"
GAS = "GAS"
```

### GasMode — satır 18

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
CO  = "CO"
CO2 = "CO2"
H2  = "H2"
```

### SensorMode — satır 24

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
TEMP = "TEMP"
CO   = "CO"
CO2  = "CO2"
H2   = "H2"
```

### RouteMode — satır 31

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** str, Enum. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
LOOP = "LOOP"
PINGPONG = "PINGPONG"
```

### SensorProps — satır 54

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
threat_active: bool = False
threat_points: list[tuple[float, float]] = field(default_factory=list)
threat_area: float = 0.0
range_tiles: int = 6
efficiency: int = 80
battery: float = 5000.0
active: bool = True
enabled: bool = True
status: str = "WAITING"
sample_interval: float = 1.0
noise_percent: float = 5.0
offsets: dict[str, float] = field(default_factory=lambda: {m.value: 0.0 for m in SensorMode})
thresholds: dict[str, float] = field(default_factory=lambda: {"TEMP": 60.0, "CO": 35.0, "CO2": 5000.0, "H2": 4000.0})
clear_thresholds: dict[str, float] = field(default_factory=lambda: {"TEMP": 55.0, "CO": 30.0, "CO2": 4500.0, "H2": 3500.0})
theoretical: dict[str, float] = field(default_factory=dict)
elapsed: float = 0.0
repeat_seconds: float = 0.0
valid: bool = False
modes: set[SensorMode] = field(default_factory=lambda: {
        SensorMode.TEMP, SensorMode.CO, SensorMode.CO2, SensorMode.H2
    })
limit: int = 40
max_limit: int = 40
last_temp: float | None = None
last_co:  float | None = None
last_co2: float | None = None
last_h2:  float | None = None
last_gas: float = 0.0
```

### SourceProps — satır 94

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
stype: SourceType = SourceType.TEMP
temp_celcius: float = 300.0
gas_modes: set[GasMode] = field(default_factory=set)
co_ppm: float = 200.0
co_range: int = 8
co2_ppm: float = 15000.0
co2_range: int = 10
h2_ppm: float = 12000.0
h2_range: int = 6
power: int = 5
range_tiles: int = 8
```

### UavProps — satır 115

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
speed: float = 3.0
route: list[tuple[int, int]] = field(default_factory=list)
route_mode: RouteMode = RouteMode.LOOP
route_dir: int = 1
route_i: int = 0
x: float = 0.0
y: float = 0.0
carrying_ids: list[int] = field(default_factory=list)
show_route: bool = True
blocked_reason: str = ""
```

### Entity — satır 129

Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
id: int
kind: Kind
tx: int
ty: int
name: str = ""
sensor: SensorProps | None = None
source: SourceProps | None = None
uav: UavProps | None = None
show_effect: bool = True
carried_by: int | None = None
icon_override: str | None = None
flammable: bool = True
ignition_temp: float = 120.0
ignition_seconds: float = 3.0
heat_seconds: float = 0.0
```

### Entity.display_name — satır 147

Kullanıcı adı varsa kimlikle birlikte, yoksa tür ve kimlikle okunur etiket üretir.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** f'{self.name} (#{self.id})'; f'{self.kind.value} #{self.id}'
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: self.name
2. Çağırana sonucu döndür: f'{self.kind.value} #{self.id}'

**Gerçek kaynak:**

```python
def display_name(self) -> str:
        if self.name:
            return f"{self.name} (#{self.id})"
        return f"{self.kind.value} #{self.id}"
```


## iot_sim/operations.py

Arayüzün ekleme, taşıma, silme, yük ve rota eylemlerine ortak giriş sağlar.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Arayüz girişinden bağımsız, kimliğe dayalı ve bütünlüğü koruyan işlemler."""
```

Satır 2: Gereken isimleri içeri al: from .models import Kind, Entity, SensorProps, SourceProps, UavProps

```python
from .models import Kind, Entity, SensorProps, SourceProps, UavProps
```

Satır 3: Gereken isimleri içeri al: from .engine import find_entity_by_id, tile_occupied, route_is_valid

```python
from .engine import find_entity_by_id, tile_occupied, route_is_valid
```

Satır 4: Gereken isimleri içeri al: from .cargo import attach_to_uav

```python
from .cargo import attach_to_uav
```

Satır 5: Gereken isimleri içeri al: from .uav import sync_cargo

```python
from .uav import sync_cargo
```

### add_entity — satır 8

Boş ve sınırlar içindeki kareye benzersiz kimlikle nesne ekle.

**Girdiler:** sim, kind, x, y. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** e
**Atanan yerel değerler / durum alanları:** e, e.sensor, e.source, e.uav, sim.next_id
**Bağlandığı işlevler:** tile_occupied, ValueError, Entity, SensorProps, SourceProps, UavProps, float, sim.entities.append
**Açık hata yolları:** ValueError('Bu kare dolu veya harita dışında.')

**İşleyiş sırası:**

1. Koşula göre yol seç: not (0 <= x < sim.width and 0 <= y < sim.height) or tile_occupied(sim.entities, x, y)
2. Değeri/alanı oluştur veya güncelle: e = Entity(sim.next_id, kind, x, y)
3. Koşula göre yol seç: kind == Kind.SENSOR
4. Yan etki/çağrı adımını çalıştır: sim.entities.append(e)
5. Değeri/alanı oluştur veya güncelle: sim.next_id += 1
6. Çağırana sonucu döndür: e

**Gerçek kaynak:**

```python
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
```

### move_entity — satır 24

Drone dahil tek nesneyi taşı; yükleri aynı işlemde eşitle.

**Girdiler:** sim, eid, x, y. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** e, others, (e.tx, e.ty), (e.uav.x, e.uav.y)
**Bağlandığı işlevler:** find_entity_by_id, ValueError, tile_occupied, float, sync_cargo
**Açık hata yolları:** ValueError("Taşınan nesneyi önce drone'dan indir."); ValueError('Hedef kare dolu veya harita dışında.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e = find_entity_by_id(sim.entities, eid)
2. Koşula göre yol seç: e is None or e.carried_by is not None
3. Değeri/alanı oluştur veya güncelle: others = [other for other in sim.entities if other.id != eid]
4. Koşula göre yol seç: not (0 <= x < sim.width and 0 <= y < sim.height) or tile_occupied(others, x, y)
5. Değeri/alanı oluştur veya güncelle: e.tx, e.ty = (x, y)
6. Koşula göre yol seç: e.uav

**Gerçek kaynak:**

```python
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
```

### release_cargo — satır 38

Tüm yükler için önce yer bul; yer yoksa hiçbir bağlantıyı değiştirme.

**Girdiler:** sim, drone, deleting=False. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** cargo, occupied, candidates, places, e.carried_by, (e.tx, e.ty)
**Bağlandığı işlevler:** find_entity_by_id, abs, range, heapq.nsmallest, len, ValueError, zip, drone.uav.carrying_ids.clear
**Açık hata yolları:** ValueError('Yükleri bırakacak boş kare yok; işlem yapılmadı.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: cargo = [find_entity_by_id(sim.entities, cid) for cid in drone.uav.carrying_ids]
2. Değeri/alanı oluştur veya güncelle: cargo = [e for e in cargo if e is not None]
3. Değeri/alanı oluştur veya güncelle: occupied = {(e.tx, e.ty) for e in sim.entities if e.carried_by is None and (not (deleting and e.id == drone.id))}
4. Değeri/alanı oluştur veya güncelle: candidates = ((abs(x - drone.tx) + abs(y - drone.ty), y, x) for y in range(sim.height) for x in range(sim.width) if (x, y) not in occupied)
5. Gereken isimleri içeri al: import heapq
6. Değeri/alanı oluştur veya güncelle: places = heapq.nsmallest(len(cargo), candidates)
7. Koşula göre yol seç: len(places) < len(cargo)
8. Her öğe için işle: (e, (_, y, x)) ← zip(cargo, places)
9. Yan etki/çağrı adımını çalıştır: drone.uav.carrying_ids.clear()

**Gerçek kaynak:**

```python
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
```

### delete_entity — satır 57

Sağ tık ve DEL aynı işlemi çağırır; geçersiz yük referansı bırakmaz.

**Girdiler:** sim, eid. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** None
**Atanan yerel değerler / durum alanları:** e, parent
**Bağlandığı işlevler:** find_entity_by_id, release_cargo, parent.uav.carrying_ids.remove, sim.entities.remove, sim.alarm.update, sim.history.pop
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e = find_entity_by_id(sim.entities, eid)
2. Koşula göre yol seç: e is None
3. Koşula göre yol seç: e.uav
4. Koşula göre yol seç: e.carried_by is not None
5. Yan etki/çağrı adımını çalıştır: sim.entities.remove(e)
6. Yan etki/çağrı adımını çalıştır: sim.alarm.update(sim.entities, sim.time)
7. Yan etki/çağrı adımını çalıştır: sim.history.pop(eid, None)

**Gerçek kaynak:**

```python
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
```

### set_route — satır 73

Rota türü ve ilk yaklaşım dahil geçerli rotayı atomik olarak kur.

**Girdiler:** sim, drone, points. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** obstacles, drone.uav.route, (drone.uav.route_i, drone.uav.route_dir), drone.uav.blocked_reason
**Bağlandığı işlevler:** any, ValueError, route_is_valid, list
**Açık hata yolları:** ValueError('Durak harita dışında.'); ValueError('En az iki farklı durak gerekli; rota engelden geçemez.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: obstacles = {(e.tx, e.ty) for e in sim.entities if e.kind == Kind.OBSTACLE}
2. Koşula göre yol seç: any((not (0 <= x < sim.width and 0 <= y < sim.height) for x, y in points))
3. Koşula göre yol seç: not route_is_valid(points, obstacles, drone.uav.route_mode, (drone.uav.x, drone.uav.y))
4. Değeri/alanı oluştur veya güncelle: drone.uav.route = list(points)
5. Değeri/alanı oluştur veya güncelle: drone.uav.route_i, drone.uav.route_dir = (0, 1)
6. Değeri/alanı oluştur veya güncelle: drone.uav.blocked_reason = ''

**Gerçek kaynak:**

```python
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
```

### attach — satır 85

Kapasite ve tür kuralını kontrol ederek yükle.

**Girdiler:** sim, drone_id, cargo_id. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** drone, cargo
**Bağlandığı işlevler:** find_entity_by_id, attach_to_uav, ValueError
**Açık hata yolları:** ValueError('Drone bir sensör veya en fazla üç kaynak taşıyabilir.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: drone = find_entity_by_id(sim.entities, drone_id)
2. Değeri/alanı oluştur veya güncelle: cargo = find_entity_by_id(sim.entities, cargo_id)
3. Koşula göre yol seç: not drone or not cargo or (not attach_to_uav(sim.entities, drone, cargo))

**Gerçek kaynak:**

```python
def attach(sim, drone_id, cargo_id):
    """Kapasite ve tür kuralını kontrol ederek yükle."""
    drone = find_entity_by_id(sim.entities, drone_id)
    cargo = find_entity_by_id(sim.entities, cargo_id)
    if not drone or not cargo or not attach_to_uav(sim.entities, drone, cargo):
        raise ValueError("Drone bir sensör veya en fazla üç kaynak taşıyabilir.")
```


## iot_sim/panel.py

Nesne, deney ve olay sekmelerini kaydırılabilir içerikle oluşturur.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Özellik, deney ve olay panelleri; eylemleri App'e veri olarak döndürür."""
```

Satır 2: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 3: Gereken isimleri içeri al: from .models import Kind, SensorMode, GasMode, SourceType

```python
from .models import Kind, SensorMode, GasMode, SourceType
```

Satır 4: Gereken isimleri içeri al: from .alarm_bridge import STATUS_LABELS

```python
from .alarm_bridge import STATUS_LABELS
```

Satır 5: Gereken isimleri içeri al: from .sensors import VALUE_ATTR

```python
from .sensors import VALUE_ATTR
```

Satır 6: Gereken isimleri içeri al: from .lessons import LESSONS

```python
from .lessons import LESSONS
```

Satır 7: Gereken isimleri içeri al: from .ui_widgets import text_block, button, TEXT, MUTED, ACCENT, PANEL, BORDER

```python
from .ui_widgets import text_block,button,TEXT,MUTED,ACCENT,PANEL,BORDER
```

### Inspector — satır 10

Yalnız panel içeriği kayar; sekmeler ve deney kontrolleri sabittir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
"""Yalnız panel içeriği kayar; sekmeler ve deney kontrolleri sabittir."""
```

### Inspector.__init__ — satır 12

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.scroll, self.bottom
**Bağlandığı işlevler:** Başka işlev çağrısı yok.
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.scroll = 0
2. Değeri/alanı oluştur veya güncelle: self.bottom = 0

**Gerçek kaynak:**

```python
def __init__(self):
        self.scroll=0
        self.bottom=0
```

### Inspector.draw — satır 16

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** self, app, rect. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** (screen, font, small), tabs, tabw, clip, old, (x, width, y), lesson, notifications, events, value, e, s, channel, step, key, u, self.bottom, self.scroll, bar, bar.y
**Bağlandığı işlevler:** pygame.draw.rect, enumerate, app.btn, pygame.Rect, screen.get_clip, screen.set_clip, heading, text, btn, list, reversed, STATUS_LABELS.get, numeric, app.sim.alarm.get_limiter_info, VALUE_ATTR.items, getattr, s.theoretical.get, mode.value.lower, len, max, min, round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: screen, font, small = (app.screen, app.font, app.small)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(screen, PANEL, rect, border_radius=12)
3. Değeri/alanı oluştur veya güncelle: tabs = [('properties', 'Nesne'), ('lesson', 'Deney'), ('log', 'Olaylar')]
4. Değeri/alanı oluştur veya güncelle: tabw = (rect.width - 24) // 3
5. Her öğe için işle: (i, (key, label)) ← enumerate(tabs)
6. Değeri/alanı oluştur veya güncelle: clip = pygame.Rect(rect.x + 10, rect.y + 52, rect.width - 20, rect.height - 62)
7. Değeri/alanı oluştur veya güncelle: old = screen.get_clip()
8. Yan etki/çağrı adımını çalıştır: screen.set_clip(clip)
9. Değeri/alanı oluştur veya güncelle: x, width, y = (clip.x + 5, clip.width - 10, clip.y - self.scroll)
10. Yerel yardımcı tanımla: text; ayrı sembol kaydı aşağıdadır.
11. Yerel yardımcı tanımla: heading; ayrı sembol kaydı aşağıdadır.
12. Yerel yardımcı tanımla: btn; ayrı sembol kaydı aşağıdadır.
13. Yerel yardımcı tanımla: numeric; ayrı sembol kaydı aşağıdadır.
14. Koşula göre yol seç: app.tab == 'lesson'
15. Değeri/alanı oluştur veya güncelle: self.bottom = max(0, y + self.scroll - clip.bottom + 16)
16. Değeri/alanı oluştur veya güncelle: self.scroll = max(0, min(self.scroll, self.bottom))
17. Yan etki/çağrı adımını çalıştır: screen.set_clip(old)
18. Koşula göre yol seç: self.bottom

**Gerçek kaynak:**

```python
def draw(self, app, rect):
        screen,font,small=app.screen,app.font,app.small
        pygame.draw.rect(screen,PANEL,rect,border_radius=12)
        tabs=[("properties","Nesne"),("lesson","Deney"),("log","Olaylar")]
        tabw=(rect.width-24)//3
        for i,(key,label) in enumerate(tabs):
            app.btn("tab_"+key,pygame.Rect(rect.x+10+i*tabw,rect.y+10,tabw-4,32),label,("tab",key),app.tab==key)
        clip=pygame.Rect(rect.x+10,rect.y+52,rect.width-20,rect.height-62)
        old=screen.get_clip()
        screen.set_clip(clip)
        x,width,y=clip.x+5,clip.width-10,clip.y-self.scroll
        def text(value,color=TEXT):
            nonlocal y
            y=text_block(screen,value,x,y,width,small,color)+7
        def heading(value):
            nonlocal y
            y=text_block(screen,value,x,y,width,font,ACCENT)+12
        def btn(key,label,action,active=False):
            nonlocal y
            r=pygame.Rect(x,y,width,32)
            app.btn(key,r,label,action,active,clip=clip)
            y+=40
        def numeric(key,label,value,action,step,low,high,hint=""):
            nonlocal y
            text(f"{label}: {value:g}")
            w=(width-8)//2
            app.btn(key+"_minus",pygame.Rect(x,y,w,28),f"− {step:g}",("adjust",action,-step,low,high),clip=clip)
            app.btn(key+"_plus",pygame.Rect(x+w+8,y,w,28),f"+ {step:g}",("adjust",action,step,low,high),clip=clip)
            y+=36
            if hint: text(hint,MUTED)
        if app.tab=="lesson":
            heading("Deney defteri")
            text("Hazır bir sahne seç. Her seçim yeni bir deney başlatır; sonuç dosyaları korunur.",MUTED)
            for i,lesson in enumerate(LESSONS,1):
                btn(f"lesson_{i}",f"{i}. {lesson['title']}",("lesson",i),app.sim.lesson==i)
            if app.sim.lesson:
                lesson=LESSONS[app.sim.lesson-1]
                heading(lesson["goal"])
                for i,step in enumerate(lesson["steps"],1): text(f"{i}. {step}")
                heading("Neden?")
                text(lesson["why"])
            text("Serbest sahne: Yeni düğmesi. Haritada seç; özellikleri değiştir; grafiği izle.",MUTED)
        elif app.tab=="log":
            heading(f"Olay geçmişi • {app.sim.alarm.total_events}")
            btn("filter_sensor",f"Sensör: {'Seçili' if app.filter_selected else 'Tümü'}",("filter_sensor",),app.filter_selected)
            btn("filter_kind",f"Tür: {app.filter_kind}",("filter_kind",))
            text("Alarm geçişleri kotadan bağımsız kaydedilir. Son 1000 olay burada; tam geçmiş sonuç dosyasında.",MUTED)
            notifications=[ev for ev in app.sim.alarm.notifications
                           if (not app.filter_selected or ev["sensor_id"]==app.selected_id)
                           and ev["kind"]=="REPEAT"]
            if notifications:
                heading("Son tekrar bildirimleri")
                for ev in list(reversed(notifications))[:5]:
                    text(f"{ev['t']:.2f}s  #{ev['sensor_id']}  {ev['channel']} • {ev['details']}",(255,188,106))
                heading("Durum geçişleri")
            events=[ev for ev in app.sim.alarm.events
                    if (not app.filter_selected or ev["sensor_id"]==app.selected_id)
                    and (app.filter_kind=="Tümü" or ev["kind"]==app.filter_kind)]
            for ev in reversed(events):
                value="" if ev["value"] is None else f" • {ev['value']:.2f}"
                text(f"{ev['t']:.2f}s  #{ev['sensor_id']}  {ev['channel']}  {ev['kind']}{value}\n{ev['details']}",
                     (255,149,151) if ev["kind"]=="ALERT" else TEXT)
            if not events: text("Filtreye uyan olay yok.",MUTED)
        else:
            e=app.selected
            if e is None:
                heading("Bir nesne seç")
                text("Üstte bir araç seçip haritaya tıklayarak ekle. Seç aracıyla mevcut nesneyi incele.")
                heading("Kısayollar")
                text("Space: başlat/duraklat\nN: tek örnekleme adımı\nM: seçiliyi taşı\nK: drone rotası\nDelete / sağ tık: sil\nCtrl+S / Ctrl+O: sahne kaydet/yükle\nTekerlek: yakınlaş\nOrta tuş sürükle: haritayı kaydır\nEsc: geçici işlemi iptal")
                text("Renkli alan, sensörün okuması değil simülatörün teorik alanıdır.",MUTED)
            else:
                heading(e.display_name)
                text(f"{e.kind.value} • ({e.tx}, {e.ty})"+(f" • Drone #{e.carried_by} üzerinde" if e.carried_by else ""),MUTED)
                btn("rename","İsmi değiştir",("rename",))
                if e.carried_by is None: btn("move","Haritada taşı (M)",("move",))
                if e.sensor:
                    s=e.sensor
                    heading(STATUS_LABELS.get(s.status,s.status))
                    btn("enabled","Sensör: "+("Açık" if s.enabled else "Kapalı"),("toggle","enabled"),s.enabled)
                    for mode in SensorMode:
                        btn("sensor_"+mode.value,mode.value+(" • ölçüyor" if mode in s.modes else " • kapalı"),("sensor_mode",mode),mode in s.modes)
                    numeric("interval","Örnek aralığı (s)",s.sample_interval,"sample_interval",.1,.1,60,"Kısa aralık: daha çok örnek, daha çok enerji.")
                    numeric("battery","Pil (eğitim birimi)",s.battery,"battery",25,0,1000000)
                    numeric("efficiency","Verimlilik (%)",s.efficiency,"efficiency",5,1,100)
                    numeric("noise","Gürültü (%)",s.noise_percent,"noise_percent",1,0,50)
                    channel=app.channel if app.channel!="BATTERY" else "TEMP"
                    heading(f"Kanal ayarı: {channel}")
                    text("Grafik kanal düğmeleriyle ayarlanacak kanalı seç.",MUTED)
                    numeric("offset","Kalibrasyon sapması",s.offsets[channel],"offsets."+channel,1 if channel=="TEMP" else 10,-100000,100000)
                    step=5 if channel in ("TEMP","CO") else 500
                    numeric("threshold","Alarm açılış eşiği",s.thresholds[channel],"thresholds."+channel,step,0,100000)
                    numeric("clear","Alarm kapanış eşiği",s.clear_thresholds[channel],"clear_thresholds."+channel,step,0,100000)
                    numeric("repeat","Tekrar bildirimi (s; 0=kapalı)",s.repeat_seconds,"repeat_seconds",1,0,300)
                    numeric("quota","60 s tekrar kotası",s.max_limit,"max_limit",5,0,200)
                    numeric("remaining","Kalan tekrar hakkı",s.limit,"limit",5,0,s.max_limit)
                    text(app.sim.alarm.get_limiter_info(e.id),MUTED)
                    if e.id in app.sim.alarm.limiter_exhausted: text("Tekrar bildirimi bastırılıyor; ölçüm ve alarm kaydı sürüyor.",(255,188,106))
                    for key,attr in VALUE_ATTR.items():
                        value=getattr(s,attr)
                        if value is not None: text(f"{key}: ölçüm {value:.2f} / teorik {s.theoretical.get(key,0):.2f}")
                elif e.source:
                    s=e.source
                    btn("source_type","Kaynak: "+s.stype.value,("source_type",))
                    if s.stype==SourceType.TEMP:
                        numeric("temperature","Kaynak sıcaklığı (°C)",s.temp_celcius,"temp_celcius",25,22,1500)
                        numeric("source_range","Yayılım yarıçapı (kare)",s.range_tiles,"range_tiles",1,1,80)
                    else:
                        if not s.gas_modes:
                            text("Yayılım için aşağıdan en az bir gaz kanalı aç.",MUTED)
                        for mode in GasMode:
                            key=mode.value.lower()
                            btn("gas_"+key,mode.value+(" • açık" if mode in s.gas_modes else " • kapalı"),("gas_mode",mode),mode in s.gas_modes)
                            if mode in s.gas_modes:
                                numeric(key+"_ppm",mode.value+" yoğunluğu (ppm)",getattr(s,key+"_ppm"),key+"_ppm",50 if key=="co" else 500,0,100000)
                                numeric(key+"_range",mode.value+" yarıçapı",getattr(s,key+"_range"),key+"_range",1,1,80)
                    numeric("visibility","Görsel görünürlük",s.power,"power",1,1,10,"Görsel ayar ölçümü değiştirmez.")
                    btn("effect","Kaynak görseli: "+("Açık" if e.show_effect else "Kapalı"),("entity_toggle","show_effect"),e.show_effect)
                elif e.uav:
                    u=e.uav
                    numeric("speed","Hız (kare/s)",u.speed,"speed",.5,1,10)
                    btn("route","Rota çiz / bitir (K)",("route",))
                    btn("route_mode","Rota: "+u.route_mode.value,("route_mode",))
                    btn("route_clear","Rotayı temizle",("route_clear",))
                    btn("route_visible","Rota görünümü",("toggle","show_route"),u.show_route)
                    text(f"{len(u.route)} durak • {len(u.carrying_ids)} yük",MUTED)
                    if u.blocked_reason: text(u.blocked_reason,(255,188,106))
                    btn("attach","Haritadan yük seç",("attach",))
                    btn("release","Tüm yükleri indir",("release",))
                    for cid in u.carrying_ids: btn(f"cargo_{cid}",f"Yük #{cid} özellikleri",("select",cid))
                else:
                    btn("flammable","Yanabilir: "+("Evet" if e.flammable else "Hayır"),("entity_toggle","flammable"),e.flammable)
                    numeric("ignition","Tutuşma sıcaklığı (°C)",e.ignition_temp,"ignition_temp",10,25,1500)
                    numeric("exposure","Gerekli maruz kalma (s)",e.ignition_seconds,"ignition_seconds",.5,.1,300)
                    text(f"Eşik üstünde geçen süre: {e.heat_seconds:.2f}s")
                btn("delete","Nesneyi sil",("delete",))
                text("Ölçüm ve yangın kuralları eğitim amaçlıdır. Değişiklikler sonuç klasörüne kaydedilir.",MUTED)
        self.bottom=max(0,y+self.scroll-clip.bottom+16)
        self.scroll=max(0,min(self.scroll,self.bottom))
        screen.set_clip(old)
        if self.bottom:
            bar=pygame.Rect(rect.right-7,clip.top,3,max(20,clip.height*clip.height/(clip.height+self.bottom)))
            bar.y+=round((clip.height-bar.height)*self.scroll/self.bottom)
            pygame.draw.rect(screen,ACCENT,bar,border_radius=2)
```

### Inspector.draw.text — satır 27

Panelin sıradaki metnini sararak çizer ve dikey yerleşim imlecini ilerletir.

**Girdiler:** value, color=TEXT. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** y
**Bağlandığı işlevler:** text_block
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: y = text_block(screen, value, x, y, width, small, color) + 7

**Gerçek kaynak:**

```python
def text(value,color=TEXT):
            nonlocal y
            y=text_block(screen,value,x,y,width,small,color)+7
```

### Inspector.draw.heading — satır 30

Panel bölüm başlığını çizer ve sonraki satırın konumunu ayarlar.

**Girdiler:** value. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** y
**Bağlandığı işlevler:** text_block
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: y = text_block(screen, value, x, y, width, font, ACCENT) + 12

**Gerçek kaynak:**

```python
def heading(value):
            nonlocal y
            y=text_block(screen,value,x,y,width,font,ACCENT)+12
```

### Inspector.draw.btn — satır 33

Butonu çizip eylemini aynı tıklama alanıyla kaydeder; panel kırpmasını uygular.

**Girdiler:** key, label, action, active=False. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** r, y
**Bağlandığı işlevler:** pygame.Rect, app.btn
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: r = pygame.Rect(x, y, width, 32)
2. Yan etki/çağrı adımını çalıştır: app.btn(key, r, label, action, active, clip=clip)
3. Değeri/alanı oluştur veya güncelle: y += 40

**Gerçek kaynak:**

```python
def btn(key,label,action,active=False):
            nonlocal y
            r=pygame.Rect(x,y,width,32)
            app.btn(key,r,label,action,active,clip=clip)
            y+=40
```

### Inspector.draw.numeric — satır 38

Sayısal değer, azalt/artır eylemleri ve kısa açıklamasını ortak yerleşimle üretir.

**Girdiler:** key, label, value, action, step, low, high, hint=''. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** w, y
**Bağlandığı işlevler:** text, app.btn, pygame.Rect
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: text(f'{label}: {value:g}')
2. Değeri/alanı oluştur veya güncelle: w = (width - 8) // 2
3. Yan etki/çağrı adımını çalıştır: app.btn(key + '_minus', pygame.Rect(x, y, w, 28), f'− {step:g}', ('adjust', action, -step, low, high), clip=clip)
4. Yan etki/çağrı adımını çalıştır: app.btn(key + '_plus', pygame.Rect(x + w + 8, y, w, 28), f'+ {step:g}', ('adjust', action, step, low, high), clip=clip)
5. Değeri/alanı oluştur veya güncelle: y += 36
6. Koşula göre yol seç: hint

**Gerçek kaynak:**

```python
def numeric(key,label,value,action,step,low,high,hint=""):
            nonlocal y
            text(f"{label}: {value:g}")
            w=(width-8)//2
            app.btn(key+"_minus",pygame.Rect(x,y,w,28),f"− {step:g}",("adjust",action,-step,low,high),clip=clip)
            app.btn(key+"_plus",pygame.Rect(x+w+8,y,w,28),f"+ {step:g}",("adjust",action,step,low,high),clip=clip)
            y+=36
            if hint: text(hint,MUTED)
```


## iot_sim/render.py

Harita, kaynak yarıçapı, teorik katman, nesne ve rota çizimidir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Yeniden boyutlandırılabilir harita; gerçek ölçüm ile teorik katman ayrıdır."""
```

Satır 2: Gereken isimleri içeri al: import math

```python
import math
```

Satır 3: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 4: Gereken isimleri içeri al: from .models import Kind, SourceType, RouteMode

```python
from .models import Kind, SourceType, RouteMode
```

Satır 5: Gereken isimleri içeri al: from .sensors import field_at, position

```python
from .sensors import field_at, position
```

Satır 6: Gereken isimleri içeri al: from .viz import EffectCache

```python
from .viz import EffectCache
```

Satır 8: Değeri/alanı oluştur veya güncelle: COLORS = {Kind.SENSOR: (91, 211, 194), Kind.SOURCE: (255, 184, 96), Kind.UAV: (119, 163, 255), Kind.OBSTACLE: (103, 154, 109), Kind.BURNED: (244, 114, 96)}

```python
COLORS = {Kind.SENSOR:(91,211,194), Kind.SOURCE:(255,184,96),
          Kind.UAV:(119,163,255), Kind.OBSTACLE:(103,154,109), Kind.BURNED:(244,114,96)}
```

Satır 10: Değeri/alanı oluştur veya güncelle: FIELD_CACHE = EffectCache()

```python
FIELD_CACHE = EffectCache()
```

Satır 12: Değeri/alanı oluştur veya güncelle: GAS_COLORS = {'CO': (244, 114, 114), 'CO2': (106, 215, 161), 'H2': (117, 170, 255)}

```python
GAS_COLORS = {"CO":(244,114,114),"CO2":(106,215,161),"H2":(117,170,255)}
```

### draw_world — satır 15

Görünür karoları çiz; alan örnekleri en fazla 35×25 hücredir.

**Girdiler:** screen, cam, sim, selected_id, icons, font, layer='TEMP', show_field=False, route_preview=None, show_grid=True. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** viewport, previous, tile, (wx0, wy0), (wx1, wy1), key, visual, (px, py), (sx, sy), source, ranges, (sx, _), (_, sy), points, radius, color, icon_key, icon, image, rect, label
**Bağlandığı işlevler:** screen.get_clip, screen.set_clip, screen.fill, cam.screen_to_world, int, screen.blit, FIELD_CACHE.get, pygame.Surface, position, cam.world_to_screen, getattr, m.value.lower, pygame.draw.circle, max, round, range, math.floor, min, math.ceil, pygame.draw.line, len, pygame.draw.lines, viewport.inflate(60, 60).collidepoint, viewport.inflate, icons.get, pygame.transform.smoothscale, pygame.Rect, pygame.draw.rect, font.render, label.get_width
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: viewport = cam.viewport
2. Değeri/alanı oluştur veya güncelle: previous = screen.get_clip()
3. Yan etki/çağrı adımını çalıştır: screen.set_clip(viewport)
4. Yan etki/çağrı adımını çalıştır: screen.fill((18, 26, 35), viewport)
5. Değeri/alanı oluştur veya güncelle: tile = 24 * cam.zoom
6. Değeri/alanı oluştur veya güncelle: wx0, wy0 = cam.screen_to_world(viewport.topleft)
7. Değeri/alanı oluştur veya güncelle: wx1, wy1 = cam.screen_to_world(viewport.bottomright)
8. Koşula göre yol seç: show_field and sim.entities
9. Değeri/alanı oluştur veya güncelle: visual = pygame.Surface(viewport.size, pygame.SRCALPHA)
10. Her öğe için işle: e ← sim.entities
11. Yan etki/çağrı adımını çalıştır: screen.blit(visual, viewport.topleft)
12. Koşula göre yol seç: show_grid
13. Her öğe için işle: e ← sim.entities
14. Koşula göre yol seç: route_preview
15. Her öğe için işle: e ← sim.entities
16. Yan etki/çağrı adımını çalıştır: screen.set_clip(previous)

**Gerçek kaynak:**

```python
def draw_world(screen, cam, sim, selected_id, icons, font, layer="TEMP", show_field=False, route_preview=None, show_grid=True):
    """Görünür karoları çiz; alan örnekleri en fazla 35×25 hücredir."""
    viewport = cam.viewport
    previous = screen.get_clip()
    screen.set_clip(viewport)
    screen.fill((18,26,35), viewport)
    tile = 24 * cam.zoom
    wx0, wy0 = cam.screen_to_world(viewport.topleft)
    wx1, wy1 = cam.screen_to_world(viewport.bottomright)
    if show_field and sim.entities:
        key=(sim.cache_token, sim.revision, int(sim.time*2), viewport.size, cam.x, cam.y, cam.zoom, layer)
        def build_overlay():
            cell = max(28, math.ceil(max(viewport.width/35, viewport.height/25)))
            overlay = pygame.Surface(viewport.size, pygame.SRCALPHA)
            for sy in range(0, viewport.height, cell):
                for sx in range(0, viewport.width, cell):
                    wx, wy = cam.screen_to_world((viewport.x+sx+cell/2, viewport.y+sy+cell/2))
                    if not (0 <= wx < sim.width and 0 <= wy < sim.height):
                        continue
                    values = field_at(wx-.5, wy-.5, sim.entities)
                    base, scale = (22,200) if layer=="TEMP" else (0, {"CO":200,"CO2":15000,"H2":12000}[layer])
                    alpha = round(min(135,max(0,(values[layer]-base)/scale*135)))
                    color = (255,160,80) if layer=="TEMP" else GAS_COLORS[layer]
                    pygame.draw.rect(overlay, (*color,alpha), (sx,sy,cell,cell))
            return overlay
        screen.blit(FIELD_CACHE.get(key, build_overlay), viewport.topleft)
    visual = pygame.Surface(viewport.size, pygame.SRCALPHA)
    for e in sim.entities:
        if e.source and e.show_effect:
            px,py=position(e,sim.entities)
            sx,sy=cam.world_to_screen(px+.5,py+.5)
            source=e.source
            ranges=[(source.range_tiles,(255,184,96))] if source.stype==SourceType.TEMP else [
                (getattr(source,m.value.lower()+"_range"),GAS_COLORS[m.value]) for m in source.gas_modes]
            for radius,color in ranges:
                pygame.draw.circle(visual,(*color,20+source.power*10),
                    (sx-viewport.x,sy-viewport.y),max(1,round(radius*tile)),1)
    screen.blit(visual,viewport.topleft)
    if show_grid:
        for x in range(max(0,math.floor(wx0)),min(sim.width,math.ceil(wx1))+1):
            sx,_=cam.world_to_screen(x,0)
            pygame.draw.line(screen,(31,43,55),(sx,viewport.top),(sx,viewport.bottom))
        for y in range(max(0,math.floor(wy0)),min(sim.height,math.ceil(wy1))+1):
            _,sy=cam.world_to_screen(0,y)
            pygame.draw.line(screen,(31,43,55),(viewport.left,sy),(viewport.right,sy))
    for e in sim.entities:
        if e.uav and e.uav.show_route and e.uav.route:
            points=[cam.world_to_screen(x+.5,y+.5) for x,y in e.uav.route]
            if len(points)>1:
                pygame.draw.lines(screen,(83,126,185),e.uav.route_mode==RouteMode.LOOP,points,2)
            for p in points: pygame.draw.circle(screen,(130,172,240),p,4)
    if route_preview:
        points=[cam.world_to_screen(x+.5,y+.5) for x,y in route_preview]
        if len(points)>1: pygame.draw.lines(screen,(255,215,119),False,points,3)
        for p in points: pygame.draw.circle(screen,(255,215,119),p,5)
    for e in sim.entities:
        if e.carried_by is not None:
            continue
        px,py=position(e,sim.entities)
        sx,sy=cam.world_to_screen(px+.5,py+.5)
        radius=max(5,min(25,round(tile*.35)))
        if not viewport.inflate(60,60).collidepoint(sx,sy):
            continue
        color=COLORS[e.kind]
        if e.kind==Kind.OBSTACLE and not e.flammable: color=(131,147,165)
        pygame.draw.circle(screen,color,(sx,sy),radius)
        icon_key="drone" if e.uav else "sensor" if e.sensor else "burned" if e.kind==Kind.BURNED else "obstacle" if e.kind==Kind.OBSTACLE else "source_gas" if e.source.stype==SourceType.GAS else "source_temp"
        icon=icons.get(icon_key)
        if icon:
            # En fazla altı ikon × mevcut tek ölçek; ara kopya cache büyütmez.
            image=pygame.transform.smoothscale(icon,(radius*2,radius*2))
            screen.blit(image,(sx-radius,sy-radius))
        if selected_id==e.id: pygame.draw.circle(screen,(234,243,255),(sx,sy),radius+5,2)
        if e.id in sim.alarm.active_alerts: pygame.draw.circle(screen,(255,101,114),(sx,sy),radius+9,2)
        if e.uav and e.uav.carrying_ids:
            pygame.draw.circle(screen,(91,211,194),(sx+radius,sy+radius),5)
        if e.kind==Kind.OBSTACLE and e.heat_seconds:
            rect=pygame.Rect(sx-radius,sy+radius+7,radius*2,4)
            pygame.draw.rect(screen,(80,60,50),rect)
            pygame.draw.rect(screen,(255,180,90),(rect.x,rect.y,rect.width*min(1,e.heat_seconds/e.ignition_seconds),4))
        label=font.render(e.name or f"#{e.id}",True,(196,211,226))
        screen.blit(label,(sx-label.get_width()/2,sy-radius-20))
    screen.set_clip(previous)
```

### draw_world.build_overlay — satır 26

Yalnız görünür alanda teorik kanal değerini örnekleyip renkli yüzey üretir.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** overlay
**Atanan yerel değerler / durum alanları:** cell, overlay, (wx, wy), values, (base, scale), alpha, color
**Bağlandığı işlevler:** max, math.ceil, pygame.Surface, range, cam.screen_to_world, field_at, round, min, pygame.draw.rect
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: cell = max(28, math.ceil(max(viewport.width / 35, viewport.height / 25)))
2. Değeri/alanı oluştur veya güncelle: overlay = pygame.Surface(viewport.size, pygame.SRCALPHA)
3. Her öğe için işle: sy ← range(0, viewport.height, cell)
4. Çağırana sonucu döndür: overlay

**Gerçek kaynak:**

```python
def build_overlay():
            cell = max(28, math.ceil(max(viewport.width/35, viewport.height/25)))
            overlay = pygame.Surface(viewport.size, pygame.SRCALPHA)
            for sy in range(0, viewport.height, cell):
                for sx in range(0, viewport.width, cell):
                    wx, wy = cam.screen_to_world((viewport.x+sx+cell/2, viewport.y+sy+cell/2))
                    if not (0 <= wx < sim.width and 0 <= wy < sim.height):
                        continue
                    values = field_at(wx-.5, wy-.5, sim.entities)
                    base, scale = (22,200) if layer=="TEMP" else (0, {"CO":200,"CO2":15000,"H2":12000}[layer])
                    alpha = round(min(135,max(0,(values[layer]-base)/scale*135)))
                    color = (255,160,80) if layer=="TEMP" else GAS_COLORS[layer]
                    pygame.draw.rect(overlay, (*color,alpha), (sx,sy,cell,cell))
            return overlay
```


## iot_sim/scene.py

Başlangıç sahnesinin sürümlü JSON biçimi, doğrulaması ve atomik yazımıdır.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Sürümlü başlangıç sahnesi; tam doğrulama sonrası nesne üretimi."""
```

Satır 2: Gereken isimleri içeri al: import json

```python
import json
```

Satır 3: Gereken isimleri içeri al: import math

```python
import math
```

Satır 4: Gereken isimleri içeri al: import os

```python
import os
```

Satır 5: Gereken isimleri içeri al: import tempfile

```python
import tempfile
```

Satır 6: Gereken isimleri içeri al: from dataclasses import asdict

```python
from dataclasses import asdict
```

Satır 7: Gereken isimleri içeri al: from pathlib import Path

```python
from pathlib import Path
```

Satır 8: Gereken isimleri içeri al: from .models import Entity, Kind, SensorProps, SourceProps, SourceType, SensorMode, GasMode, UavProps, RouteMode

```python
from .models import Entity, Kind, SensorProps, SourceProps, SourceType, SensorMode, GasMode, UavProps, RouteMode
```

Satır 10: Değeri/alanı oluştur veya güncelle: SCHEMA_VERSION = 1

```python
SCHEMA_VERSION = 1
```

Satır 11: Değeri/alanı oluştur veya güncelle: MODEL_VERSION = 'education-2.0'

```python
MODEL_VERSION = "education-2.0"
```

Satır 12: Değeri/alanı oluştur veya güncelle: CHANNELS = ('TEMP', 'CO', 'CO2', 'H2')

```python
CHANNELS = ("TEMP", "CO", "CO2", "H2")
```

Satır 13: Değeri/alanı oluştur veya güncelle: SENSOR_FIELDS = ('range_tiles', 'efficiency', 'battery', 'enabled', 'sample_interval', 'noise_percent', 'offsets', 'thresholds', 'clear_thresholds', 'modes', 'limit', 'max_limit', 'repeat_seconds')

```python
SENSOR_FIELDS = ("range_tiles", "efficiency", "battery", "enabled", "sample_interval", "noise_percent",
                 "offsets", "thresholds", "clear_thresholds", "modes", "limit", "max_limit", "repeat_seconds")
```

Satır 15: Değeri/alanı oluştur veya güncelle: SOURCE_FIELDS = tuple(SourceProps.__dataclass_fields__)

```python
SOURCE_FIELDS = tuple(SourceProps.__dataclass_fields__)
```

### encode — satır 18

Enum, küme ve koordinatları standart JSON türlerine çevir.

**Girdiler:** value. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** {k: encode(v) for k, v in value.items()}; [encode(v) for v in items]; value.value if hasattr(value, 'value') else value
**Atanan yerel değerler / durum alanları:** items
**Bağlandığı işlevler:** isinstance, encode, value.items, sorted, hasattr
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: isinstance(value, dict)
2. Koşula göre yol seç: isinstance(value, (set, list, tuple))
3. Çağırana sonucu döndür: value.value if hasattr(value, 'value') else value

**Gerçek kaynak:**

```python
def encode(value):
    """Enum, küme ve koordinatları standart JSON türlerine çevir."""
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (set, list, tuple)):
        items = sorted(value, key=str) if isinstance(value, set) else value
        return [encode(v) for v in items]
    return value.value if hasattr(value, "value") else value
```

### to_scene — satır 28

Canlı okumaları dışarıda bırakıp mevcut düzeni yeni başlangıç olarak kodla.

**Girdiler:** entities, seed=42, width=200, height=200, lesson=0. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** dict(schema_version=SCHEMA_VERSION, model_version=MODEL_VERSION, seed=seed, width=width, height=height, lesson=lesson, entities=items)
**Atanan yerel değerler / durum alanları:** items, row, row['sensor'], row['source'], row['uav']
**Bağlandığı işlevler:** getattr, asdict, items.append, encode, dict
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: items = []
2. Her öğe için işle: e ← entities
3. Çağırana sonucu döndür: dict(schema_version=SCHEMA_VERSION, model_version=MODEL_VERSION, seed=seed, width=width, height=height, lesson=lesson, entities=items)

**Gerçek kaynak:**

```python
def to_scene(entities, seed=42, width=200, height=200, lesson=0):
    """Canlı okumaları dışarıda bırakıp mevcut düzeni yeni başlangıç olarak kodla."""
    items = []
    for e in entities:
        row = {k: getattr(e, k) for k in ("id", "kind", "tx", "ty", "name", "show_effect", "carried_by",
                                          "icon_override", "flammable", "ignition_temp", "ignition_seconds")}
        if e.sensor:
            row["sensor"] = {k: getattr(e.sensor, k) for k in SENSOR_FIELDS}
        if e.source:
            row["source"] = asdict(e.source)
        if e.uav:
            row["uav"] = {k: getattr(e.uav, k) for k in ("speed", "route", "route_mode", "carrying_ids", "show_route")}
        items.append(encode(row))
    return dict(schema_version=SCHEMA_VERSION, model_version=MODEL_VERSION, seed=seed,
                width=width, height=height, lesson=lesson, entities=items)
```

### number — satır 45

Boolean/NaN/sonsuz dahil bozuk sayıları reddet.

**Girdiler:** value, low, high, label, integer=False. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** value
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** type, math.isfinite, ValueError
**Açık hata yolları:** ValueError(f'{label}: {low}–{high} aralığında sayı gerekli.'); ValueError(f'{label}: tam sayı gerekli.')

**İşleyiş sırası:**

1. Koşula göre yol seç: type(value) not in (int, float) or not math.isfinite(value) or (not low <= value <= high)
2. Koşula göre yol seç: integer and type(value) is not int
3. Çağırana sonucu döndür: value

**Gerçek kaynak:**

```python
def number(value, low, high, label, integer=False):
    """Boolean/NaN/sonsuz dahil bozuk sayıları reddet."""
    if type(value) not in (int, float) or not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f"{label}: {low}–{high} aralığında sayı gerekli.")
    if integer and type(value) is not int:
        raise ValueError(f"{label}: tam sayı gerekli.")
    return value
```

### boolean — satır 54

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** value, label. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** value
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** type, ValueError
**Açık hata yolları:** ValueError(f'{label}: doğru/yanlış değeri gerekli.')

**İşleyiş sırası:**

1. Koşula göre yol seç: type(value) is not bool
2. Çağırana sonucu döndür: value

**Gerçek kaynak:**

```python
def boolean(value, label):
    if type(value) is not bool:
        raise ValueError(f"{label}: doğru/yanlış değeri gerekli.")
    return value
```

### object_fields — satır 60

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** value, allowed, label. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** value
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** isinstance, set, ValueError
**Açık hata yolları:** ValueError(f'{label}: bilinmeyen alan veya bozuk nesne.')

**İşleyiş sırası:**

1. Koşula göre yol seç: not isinstance(value, dict) or set(value) - set(allowed)
2. Çağırana sonucu döndür: value

**Gerçek kaynak:**

```python
def object_fields(value, allowed, label):
    if not isinstance(value, dict) or set(value) - set(allowed):
        raise ValueError(f"{label}: bilinmeyen alan veya bozuk nesne.")
    return value
```

### parse_scene — satır 66

Bütün yapı ve çapraz referanslar geçerliyse yeni nesne listesi döndür.

**Girdiler:** data. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (entities, seed, width, height, lesson)
**Atanan yerel değerler / durum alanları:** width, height, seed, lesson, rows, (entities, ids, occupied), eid, kind, x, y, name, e, e.show_effect, e.flammable, e.ignition_temp, e.ignition_seconds, e.carried_by, icon, e.icon_override, expected, p, s, bounds, s.enabled, modes, s.modes, values, e.sensor, s.stype, s.gas_modes, s.temp_celcius, e.source, u, u.speed, u.route_mode, route, u.route, u.carrying_ids, u.show_route, e.uav, index, parent, children
**Bağlandığı işlevler:** object_fields, type, ValueError, number, data.get, isinstance, len, set, ids.add, Kind, row.get, Entity, boolean, occupied.add, SensorProps, bounds.items, setattr, p.get, getattr, abs, round, list, SensorMode, values.items, any, SourceProps, SourceType, GasMode, UavProps, float, RouteMode, u.route.append, entities.append, index.get
**Açık hata yolları:** ValueError('Desteklenmeyen sahne/model sürümü.'); ValueError('Sahne en fazla 500 nesne içerebilir.'); ValueError('Tekrarlanan nesne kimliği.'); ValueError('İsim en fazla 80 karakter olmalı.'); ValueError('Bağımsız nesneler aynı karede olamaz.'); ValueError('Bilinmeyen ikon.'); ValueError('Nesne türü ile özellikleri uyuşmuyor.'); ValueError('Örnekleme aralığı 0,05 saniyenin katı olmalı.'); ValueError('Kalan bildirim hakkı maksimumu aşamaz.'); ValueError('Ölçüm kanalları tekrarsız liste olmalı.'); ValueError('Her kanalın ayarı gerekli.'); ValueError('Alarm kapanış eşiği açılış eşiğini aşamaz.'); ValueError('Gaz kanalları tekrarsız liste olmalı.'); ValueError('Rota en fazla 500 durak içerebilir.'); ValueError('Rota noktası [x,y] olmalı.'); ValueError('Rota en az iki farklı durak içermeli.'); ValueError('Yük listesi geçersiz.'); ValueError('Tekrarlanan yük.'); ValueError('Taşıyıcı bağlantısı/konumu geçersiz.'); ValueError('Drone yük bağlantısı geçersiz.'); ValueError('Sensör yalnız taşınabilir.'); ValueError('Eksik veya bozuk sahne alanı.')

**İşleyiş sırası:**

1. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def parse_scene(data):
    """Bütün yapı ve çapraz referanslar geçerliyse yeni nesne listesi döndür."""
    try:
        object_fields(data, ("schema_version", "model_version", "seed", "width", "height", "lesson", "entities"), "Sahne")
        if type(data["schema_version"]) is not int or data["schema_version"] != SCHEMA_VERSION or data["model_version"] != MODEL_VERSION:
            raise ValueError("Desteklenmeyen sahne/model sürümü.")
        width = number(data["width"], 2, 200, "Genişlik", True)
        height = number(data["height"], 2, 200, "Yükseklik", True)
        seed = number(data["seed"], 0, 2**32 - 1, "Tohum", True)
        lesson = number(data.get("lesson", 0), 0, 6, "Deney", True)
        rows = data["entities"]
        if not isinstance(rows, list) or len(rows) > 500:
            raise ValueError("Sahne en fazla 500 nesne içerebilir.")
        entities, ids, occupied = [], set(), set()
        for row in rows:
            object_fields(row, ("id", "kind", "tx", "ty", "name", "show_effect", "carried_by", "icon_override",
                                "flammable", "ignition_temp", "ignition_seconds", "sensor", "source", "uav"), "Nesne")
            eid = number(row["id"], 1, 10**9, "Kimlik", True)
            if eid in ids:
                raise ValueError("Tekrarlanan nesne kimliği.")
            ids.add(eid)
            kind = Kind(row["kind"])
            x = number(row["tx"], 0, width - 1, "X", True)
            y = number(row["ty"], 0, height - 1, "Y", True)
            name = row.get("name", "")
            if not isinstance(name, str) or len(name) > 80:
                raise ValueError("İsim en fazla 80 karakter olmalı.")
            e = Entity(eid, kind, x, y, name=name)
            e.show_effect = boolean(row.get("show_effect", True), "Görünürlük")
            e.flammable = boolean(row.get("flammable", True), "Yanabilirlik")
            e.ignition_temp = number(row.get("ignition_temp", 120), 25, 1500, "Tutuşma sıcaklığı")
            e.ignition_seconds = number(row.get("ignition_seconds", 3), .1, 300, "Tutuşma süresi")
            e.carried_by = row.get("carried_by")
            if e.carried_by is not None:
                number(e.carried_by, 1, 10**9, "Taşıyıcı kimliği", True)
            elif kind != Kind.UAV and (x, y) in occupied:
                raise ValueError("Bağımsız nesneler aynı karede olamaz.")
            elif kind != Kind.UAV:
                occupied.add((x, y))
            icon = row.get("icon_override")
            if icon not in (None, "burned"):
                raise ValueError("Bilinmeyen ikon.")
            e.icon_override = icon
            expected = "sensor" if kind == Kind.SENSOR else "uav" if kind == Kind.UAV else "source" if kind in (Kind.SOURCE, Kind.BURNED) else None
            for key in ("sensor", "source", "uav"):
                if (key in row) != (key == expected):
                    raise ValueError("Nesne türü ile özellikleri uyuşmuyor.")
            if kind == Kind.SENSOR:
                p = object_fields(row["sensor"], SENSOR_FIELDS, "Sensör")
                s = SensorProps()
                bounds = {"range_tiles": (1, 50, True), "efficiency": (1, 100, True), "battery": (0, 1000000, False),
                          "sample_interval": (.1, 60, False), "noise_percent": (0, 50, False),
                          "limit": (0, 200, True), "max_limit": (0, 200, True), "repeat_seconds": (0, 300, False)}
                for key, (low, high, integer) in bounds.items():
                    setattr(s, key, number(p.get(key, getattr(s, key)), low, high, key, integer))
                if abs(s.sample_interval / .05 - round(s.sample_interval / .05)) > 1e-6:
                    raise ValueError("Örnekleme aralığı 0,05 saniyenin katı olmalı.")
                if s.limit > s.max_limit:
                    raise ValueError("Kalan bildirim hakkı maksimumu aşamaz.")
                s.enabled = boolean(p.get("enabled", True), "Sensör açık")
                modes = p.get("modes", list(CHANNELS))
                if not isinstance(modes, list) or len(modes) != len(set(modes)):
                    raise ValueError("Ölçüm kanalları tekrarsız liste olmalı.")
                s.modes = {SensorMode(m) for m in modes}
                for key in ("offsets", "thresholds", "clear_thresholds"):
                    values = p.get(key, getattr(s, key))
                    if not isinstance(values, dict) or set(values) != set(CHANNELS):
                        raise ValueError("Her kanalın ayarı gerekli.")
                    setattr(s, key, {k: number(v, -100000 if key == "offsets" else 0, 100000, key) for k, v in values.items()})
                if any(s.clear_thresholds[k] > s.thresholds[k] for k in CHANNELS):
                    raise ValueError("Alarm kapanış eşiği açılış eşiğini aşamaz.")
                e.sensor = s
            elif expected == "source":
                p = object_fields(row["source"], SOURCE_FIELDS, "Kaynak")
                s = SourceProps()
                s.stype = SourceType(p.get("stype", "TEMP"))
                modes = p.get("gas_modes", [])
                if not isinstance(modes, list) or len(modes) != len(set(modes)):
                    raise ValueError("Gaz kanalları tekrarsız liste olmalı.")
                s.gas_modes = {GasMode(m) for m in modes}
                for key in ("range_tiles", "co_range", "co2_range", "h2_range", "power"):
                    setattr(s, key, number(p.get(key, getattr(s, key)), 1, 10 if key == "power" else 80, key, True))
                s.temp_celcius = number(p.get("temp_celcius", 300), 22, 1500, "Sıcaklık")
                for key in ("co_ppm", "co2_ppm", "h2_ppm"):
                    setattr(s, key, number(p.get(key, getattr(s, key)), 0, 100000, key))
                e.source = s
            elif kind == Kind.UAV:
                p = object_fields(row["uav"], ("speed", "route", "route_mode", "carrying_ids", "show_route"), "Drone")
                u = UavProps(x=float(x), y=float(y))
                u.speed = number(p.get("speed", 3), 1, 10, "Hız")
                u.route_mode = RouteMode(p.get("route_mode", "LOOP"))
                route = p.get("route", [])
                if not isinstance(route, list) or len(route) > 500:
                    raise ValueError("Rota en fazla 500 durak içerebilir.")
                u.route = []
                for point in route:
                    if not isinstance(point, list) or len(point) != 2:
                        raise ValueError("Rota noktası [x,y] olmalı.")
                    u.route.append((number(point[0], 0, width-1, "Durak X", True), number(point[1], 0, height-1, "Durak Y", True)))
                if u.route and len(set(u.route)) < 2:
                    raise ValueError("Rota en az iki farklı durak içermeli.")
                u.carrying_ids = p.get("carrying_ids", [])
                if not isinstance(u.carrying_ids, list) or len(u.carrying_ids) > 3:
                    raise ValueError("Yük listesi geçersiz.")
                for cid in u.carrying_ids:
                    number(cid, 1, 10**9, "Yük kimliği", True)
                if len(set(u.carrying_ids)) != len(u.carrying_ids):
                    raise ValueError("Tekrarlanan yük.")
                u.show_route = boolean(p.get("show_route", True), "Rota görünürlüğü")
                e.uav = u
            entities.append(e)
        index = {e.id: e for e in entities}
        for e in entities:
            if e.carried_by is not None:
                parent = index.get(e.carried_by)
                if not parent or not parent.uav or e.id not in parent.uav.carrying_ids or (e.tx, e.ty) != (parent.tx, parent.ty):
                    raise ValueError("Taşıyıcı bağlantısı/konumu geçersiz.")
            if e.uav:
                children = [index.get(cid) for cid in e.uav.carrying_ids]
                if any(c is None or c.carried_by != e.id or c.kind not in (Kind.SENSOR, Kind.SOURCE, Kind.BURNED) for c in children):
                    raise ValueError("Drone yük bağlantısı geçersiz.")
                if any(c.sensor for c in children) and len(children) != 1:
                    raise ValueError("Sensör yalnız taşınabilir.")
        return entities, seed, width, height, lesson
    except (KeyError, TypeError, OverflowError) as exc:
        raise ValueError("Eksik veya bozuk sahne alanı.") from exc
```

### load_scene — satır 194

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** path. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** data
**Atanan yerel değerler / durum alanları:** path, data
**Bağlandığı işlevler:** Path, path.stat, ValueError, json.loads, path.read_text, parse_scene
**Açık hata yolları:** ValueError('Sahne dosyası 2 MB sınırını aşıyor.')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: path = Path(path)
2. Koşula göre yol seç: path.stat().st_size > 2000000
3. Değeri/alanı oluştur veya güncelle: data = json.loads(path.read_text(encoding='utf-8'))
4. Yan etki/çağrı adımını çalıştır: parse_scene(data)
5. Çağırana sonucu döndür: data

**Gerçek kaynak:**

```python
def load_scene(path):
    path = Path(path)
    if path.stat().st_size > 2_000_000:
        raise ValueError("Sahne dosyası 2 MB sınırını aşıyor.")
    data = json.loads(path.read_text(encoding="utf-8"))
    parse_scene(data)
    return data
```

### save_scene — satır 203

Önce doğrula; yarım dosya bırakmadan atomik değiştir.

**Girdiler:** path, data. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** path, temporary
**Bağlandığı işlevler:** parse_scene, Path, path.parent.mkdir, tempfile.NamedTemporaryFile, json.dump, f.flush, os.fsync, f.fileno, os.replace, Path(temporary).exists, Path(temporary).unlink
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: parse_scene(data)
2. Değeri/alanı oluştur veya güncelle: path = Path(path)
3. Yan etki/çağrı adımını çalıştır: path.parent.mkdir(parents=True, exist_ok=True)
4. Değeri/alanı oluştur veya güncelle: temporary = None
5. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

**Gerçek kaynak:**

```python
def save_scene(path, data):
    """Önce doğrula; yarım dosya bırakmadan atomik değiştir."""
    parse_scene(data)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as f:
            temporary = f.name
            json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and Path(temporary).exists():
            Path(temporary).unlink()
```


## iot_sim/sensors.py

Teorik ortam, noktasal cihaz ölçümü, sapma ve enerji tüketimini hesaplar.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Noktasal alan, cihaz hatası ve örnek başına enerji: ekran bağımsız model."""
```

Satır 2: Gereken isimleri içeri al: import math

```python
import math
```

Satır 3: Gereken isimleri içeri al: import random

```python
import random
```

Satır 4: Gereken isimleri içeri al: from .models import Entity, Kind, SourceType, SensorMode

```python
from .models import Entity, Kind, SourceType, SensorMode
```

Satır 6: Değeri/alanı oluştur veya güncelle: AMBIENT_TEMP_C = 22.0

```python
AMBIENT_TEMP_C = 22.0
```

Satır 7: Değeri/alanı oluştur veya güncelle: VALUE_ATTR = {'TEMP': 'last_temp', 'CO': 'last_co', 'CO2': 'last_co2', 'H2': 'last_h2'}

```python
VALUE_ATTR = {"TEMP": "last_temp", "CO": "last_co", "CO2": "last_co2", "H2": "last_h2"}
```

### position — satır 10

Taşınan cihaz ve kaynak için drone'un kesintisiz konumunu kullan.

**Girdiler:** entity: Entity, entities: list[Entity]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (target.uav.x, target.uav.y) if target.uav else (target.tx, target.ty)
**Atanan yerel değerler / durum alanları:** target
**Bağlandığı işlevler:** next
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: target = entity
2. Koşula göre yol seç: entity.carried_by is not None
3. Çağırana sonucu döndür: (target.uav.x, target.uav.y) if target.uav else (target.tx, target.ty)

**Gerçek kaynak:**

```python
def position(entity: Entity, entities: list[Entity]) -> tuple[float, float]:
    """Taşınan cihaz ve kaynak için drone'un kesintisiz konumunu kullan."""
    target = entity
    if entity.carried_by is not None:
        target = next((e for e in entities if e.id == entity.carried_by), entity)
    return (target.uav.x, target.uav.y) if target.uav else (target.tx, target.ty)
```

### field_at — satır 18

Kaynakların katkısını topla; duvar/rüzgâr ve zamanla difüzyon modeli yok.

**Girdiler:** x: float, y: float, entities: list[Entity]. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** result
**Atanan yerel değerler / durum alanları:** result, s, (px, py), distance, attenuation, result['TEMP'], key, result[mode.value]
**Bağlandığı işlevler:** position, math.hypot, max, mode.value.lower, getattr
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: result = {'TEMP': AMBIENT_TEMP_C, 'CO': 0.0, 'CO2': 0.0, 'H2': 0.0}
2. Her öğe için işle: e ← entities
3. Çağırana sonucu döndür: result

**Gerçek kaynak:**

```python
def field_at(x: float, y: float, entities: list[Entity]) -> dict[str, float]:
    """Kaynakların katkısını topla; duvar/rüzgâr ve zamanla difüzyon modeli yok."""
    result = {"TEMP": AMBIENT_TEMP_C, "CO": 0.0, "CO2": 0.0, "H2": 0.0}
    for e in entities:
        s = e.source
        if s is None or e.kind not in (Kind.SOURCE, Kind.BURNED):
            continue
        px, py = position(e, entities)
        distance = math.hypot(x - px, y - py)
        if s.stype == SourceType.TEMP:
            attenuation = max(0.0, 1 - distance / max(1, s.range_tiles)) ** 1.5
            result["TEMP"] += (s.temp_celcius - AMBIENT_TEMP_C) * attenuation
        else:
            for mode in s.gas_modes:
                key = mode.value.lower()
                attenuation = max(0.0, 1 - distance / max(1, getattr(s, key + "_range"))) ** 1.3
                result[mode.value] += getattr(s, key + "_ppm") * attenuation
    return result
```

### invalidate — satır 38

Veri yokluğunu sıfır ölçümden ayır; eski okumaları temizle.

**Girdiler:** sensor, status: str. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sensor.status, sensor.active, sensor.valid, sensor.theoretical, sensor.last_gas
**Bağlandığı işlevler:** VALUE_ATTR.values, setattr
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sensor.status = status
2. Değeri/alanı oluştur veya güncelle: sensor.active = sensor.valid = False
3. Değeri/alanı oluştur veya güncelle: sensor.theoretical = {}
4. Her öğe için işle: attr ← VALUE_ATTR.values()
5. Değeri/alanı oluştur veya güncelle: sensor.last_gas = 0.0

**Gerçek kaynak:**

```python
def invalidate(sensor, status: str):
    """Veri yokluğunu sıfır ölçümden ayır; eski okumaları temizle."""
    sensor.status = status
    sensor.active = sensor.valid = False
    sensor.theoretical = {}
    for attr in VALUE_ATTR.values():
        setattr(sensor, attr, None)
    sensor.last_gas = 0.0
```

### simulate_tick — satır 48

Enerjiyi ilerlet; zamanı gelen sensörleri örnekle ve değişenleri döndür.

**Girdiler:** entities: list[Entity], dt_seconds: float, rng=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** changed
**Atanan yerel değerler / durum alanları:** rng, changed, s, unavailable, (s.status, s.elapsed), s.active, s.battery, s.elapsed, energy, s.theoretical, value, truth, s.last_gas, s.valid
**Bağlandığı işlevler:** sorted, invalidate, changed.append, max, len, field_at, position, rng.uniform, setattr, sum, getattr
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: rng = rng or random
2. Değeri/alanı oluştur veya güncelle: changed = []
3. Her öğe için işle: e ← sorted(entities, key=lambda item: item.id)
4. Çağırana sonucu döndür: changed

**Gerçek kaynak:**

```python
def simulate_tick(entities: list[Entity], dt_seconds: float, rng=None) -> list[Entity]:
    """Enerjiyi ilerlet; zamanı gelen sensörleri örnekle ve değişenleri döndür."""
    rng = rng or random
    changed = []
    for e in sorted(entities, key=lambda item: item.id):
        s = e.sensor
        if e.kind != Kind.SENSOR or s is None:
            continue
        unavailable = "OFF" if not s.enabled or not s.modes else "EMPTY" if s.battery <= 0 else None
        if unavailable:
            if s.status != unavailable or s.valid:
                invalidate(s, unavailable)
                changed.append(e)
            continue
        if not s.active:
            s.status, s.elapsed = "WAITING", 0.0
        s.active = True
        s.battery = max(0.0, s.battery - 0.02 * dt_seconds)
        s.elapsed += dt_seconds
        if s.battery <= 0:
            invalidate(s, "EMPTY")
            changed.append(e)
            continue
        if s.elapsed + 1e-9 < s.sample_interval:
            continue
        s.elapsed = max(0.0, s.elapsed - s.sample_interval)
        energy = 0.6 * len(s.modes) * 100 / max(1, s.efficiency)
        s.battery = max(0.0, s.battery - energy)
        if s.battery <= 0:
            invalidate(s, "EMPTY")
        else:
            s.theoretical = field_at(*position(e, entities), entities)
            for mode in SensorMode:
                value = None
                if mode in s.modes:
                    truth = s.theoretical[mode.value]
                    value = truth * (1 + rng.uniform(-s.noise_percent, s.noise_percent) / 100) + s.offsets[mode.value]
                    if mode != SensorMode.TEMP:
                        value = max(0.0, value)
                setattr(s, VALUE_ATTR[mode.value], value)
            s.last_gas = sum(getattr(s, a) or 0 for a in ("last_co", "last_co2", "last_h2"))
            s.valid = True
        changed.append(e)
    return changed
```


## iot_sim/simulation.py

Ekrandan bağımsız deney saati, güncelleme sırası, RNG ve sınırlı geçmişin sahibidir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Sabit zaman adımıyla, Pygame olmadan çalıştırılabilen deney."""
```

Satır 2: Gereken isimleri içeri al: from collections import defaultdict, deque

```python
from collections import defaultdict, deque
```

Satır 3: Gereken isimleri içeri al: from copy import deepcopy

```python
from copy import deepcopy
```

Satır 4: Gereken isimleri içeri al: import random

```python
import random
```

Satır 5: Gereken isimleri içeri al: from .alarm_bridge import AlarmBridge

```python
from .alarm_bridge import AlarmBridge
```

Satır 6: Gereken isimleri içeri al: from .sensors import simulate_tick, VALUE_ATTR

```python
from .sensors import simulate_tick, VALUE_ATTR
```

Satır 7: Gereken isimleri içeri al: from .fire import spread_fire

```python
from .fire import spread_fire
```

Satır 8: Gereken isimleri içeri al: from .uav import update_uavs

```python
from .uav import update_uavs
```

Satır 9: Gereken isimleri içeri al: from .scene import to_scene, parse_scene

```python
from .scene import to_scene, parse_scene
```

Satır 11: Değeri/alanı oluştur veya güncelle: STEP = 0.05

```python
STEP = 0.05
```

### Simulation — satır 14

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### Simulation.__init__ — satır 15

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, scene=None. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** scene, (self.entities, self.seed, self.width, self.height, self.lesson), self.baseline, self.rng, self.steps, self.pending, self.revision, self.cache_token, self.next_id, self.history, self.exporter, self.alarm
**Bağlandığı işlevler:** to_scene, parse_scene, deepcopy, random.Random, object, max, defaultdict, deque, AlarmBridge, self.alarm.update
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: scene is None
2. Değeri/alanı oluştur veya güncelle: self.entities, self.seed, self.width, self.height, self.lesson = parse_scene(scene)
3. Değeri/alanı oluştur veya güncelle: self.baseline = deepcopy(scene)
4. Değeri/alanı oluştur veya güncelle: self.rng = random.Random(self.seed)
5. Değeri/alanı oluştur veya güncelle: self.steps = 0
6. Değeri/alanı oluştur veya güncelle: self.pending = 0.0
7. Değeri/alanı oluştur veya güncelle: self.revision = 0
8. Değeri/alanı oluştur veya güncelle: self.cache_token = object()
9. Değeri/alanı oluştur veya güncelle: self.next_id = max((e.id for e in self.entities), default=0) + 1
10. Değeri/alanı oluştur veya güncelle: self.history = defaultdict(lambda: deque(maxlen=600))
11. Değeri/alanı oluştur veya güncelle: self.exporter = None
12. Değeri/alanı oluştur veya güncelle: self.alarm = AlarmBridge(on_event=self._event)
13. Yan etki/çağrı adımını çalıştır: self.alarm.update(self.entities, 0)

**Gerçek kaynak:**

```python
def __init__(self, scene=None):
        if scene is None:
            scene = to_scene([])
        self.entities, self.seed, self.width, self.height, self.lesson = parse_scene(scene)
        self.baseline = deepcopy(scene)
        self.rng = random.Random(self.seed)
        self.steps = 0
        self.pending = 0.0
        self.revision = 0
        self.cache_token = object()
        self.next_id = max((e.id for e in self.entities), default=0) + 1
        self.history = defaultdict(lambda: deque(maxlen=600))
        self.exporter = None
        self.alarm = AlarmBridge(on_event=self._event)
        self.alarm.update(self.entities, 0)
```

### Simulation.time — satır 32

Tam adım sayısını adım süresiyle çarparak simülasyon saniyesini sunar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** round(self.steps * STEP, 6)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: round(self.steps * STEP, 6)

**Gerçek kaynak:**

```python
def time(self):
        return round(self.steps * STEP, 6)
```

### Simulation.snapshot — satır 35

Mevcut düzeni canlı geçmişten ayrılmış başlangıç sahnesi olarak kodlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** to_scene(self.entities, self.seed, self.width, self.height, self.lesson)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** to_scene
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: to_scene(self.entities, self.seed, self.width, self.height, self.lesson)

**Gerçek kaynak:**

```python
def snapshot(self):
        return to_scene(self.entities, self.seed, self.width, self.height, self.lesson)
```

### Simulation._event — satır 38

Model olayını açık sonuç oturumuna aktarır; exporter yoksa dosyaya yazmaz.

**Girdiler:** self, event. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self.exporter.log_event
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: self.exporter

**Gerçek kaynak:**

```python
def _event(self, event):
        if self.exporter:
            self.exporter.log_event(event)
```

### Simulation.start_recording — satır 42

Exporter'ı modele bağlar ve kayıttan önce oluşmuş ilk durum olaylarını aktarır.

**Girdiler:** self, exporter. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.exporter
**Bağlandığı işlevler:** exporter.log_event
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.exporter = exporter
2. Her öğe için işle: event ← self.alarm.events

**Gerçek kaynak:**

```python
def start_recording(self, exporter):
        self.exporter = exporter
        for event in self.alarm.events:
            exporter.log_event(event)
```

### Simulation.advance — satır 47

Süre biriktir; hareket, enerji ve yangını aynı sabit sırada yürüt.

**Girdiler:** self, seconds. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** count
**Atanan yerel değerler / durum alanları:** self.pending, count, burning, self.steps, changed, s
**Bağlandığı işlevler:** ValueError, int, max, range, update_uavs, spread_fire, simulate_tick, self.alarm.update, self.history[e.id].append, dict, getattr, VALUE_ATTR.items, list, self.alarm.flags.get, set, self.exporter.log_sensor, self.alarm._emit
**Açık hata yolları:** ValueError('İlerleme süresi 0–3600 saniye olmalı.')

**İşleyiş sırası:**

1. Koşula göre yol seç: not 0 <= seconds <= 3600
2. Değeri/alanı oluştur veya güncelle: self.pending += seconds
3. Değeri/alanı oluştur veya güncelle: count = int((self.pending + 1e-09) / STEP)
4. Değeri/alanı oluştur veya güncelle: self.pending = max(0.0, self.pending - count * STEP)
5. Her öğe için işle: _ ← range(count)
6. Çağırana sonucu döndür: count

**Gerçek kaynak:**

```python
def advance(self, seconds):
        """Süre biriktir; hareket, enerji ve yangını aynı sabit sırada yürüt."""
        if not 0 <= seconds <= 3600:
            raise ValueError("İlerleme süresi 0–3600 saniye olmalı.")
        self.pending += seconds
        count = int((self.pending + 1e-9) / STEP)
        self.pending = max(0.0, self.pending - count * STEP)
        for _ in range(count):
            update_uavs(self.entities, STEP, self.width, self.height)
            burning = spread_fire(self.entities, STEP)
            self.steps += 1
            changed = simulate_tick(self.entities, STEP, self.rng)
            if changed:
                self.alarm.update(self.entities, self.time)
                for e in changed:
                    s = e.sensor
                    self.history[e.id].append(dict(t=self.time, measured={k: getattr(s, attr) for k, attr in VALUE_ATTR.items()},
                        theoretical=dict(s.theoretical), battery=s.battery, status=s.status,
                        thresholds=dict(s.thresholds), alarms=list(self.alarm.flags.get(e.id, set()))))
                    if self.exporter:
                        self.exporter.log_sensor(self.time, e, self.entities)
            for e in burning:
                self.alarm._emit(e, "TEMP", "FIRE", e.source.temp_celcius, "Tutuşma sıcaklığı ve süresi sağlandı")
        return count
```

### Simulation.reset — satır 72

Başlangıç sahnesi ve RNG aynı olacak şekilde yeni deney üret.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Simulation(deepcopy(self.baseline))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Simulation, deepcopy
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: Simulation(deepcopy(self.baseline))

**Gerçek kaynak:**

```python
def reset(self):
        """Başlangıç sahnesi ve RNG aynı olacak şekilde yeni deney üret."""
        return Simulation(deepcopy(self.baseline))
```


## iot_sim/uav.py

LOOP/PINGPONG hareketini, engelde durmayı ve yük eşitlemesini uygular.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Sonlu rota takibi ve tüm durumlarda yük konumu eşitleme."""
```

Satır 2: Gereken isimleri içeri al: import math

```python
import math
```

Satır 3: Gereken isimleri içeri al: from .models import Kind, RouteMode

```python
from .models import Kind, RouteMode
```

Satır 4: Gereken isimleri içeri al: from .engine import clamp, route_is_valid, find_entity_by_id, bresenham_tiles

```python
from .engine import clamp, route_is_valid, find_entity_by_id, bresenham_tiles
```

### sync_cargo — satır 7

Rotasız/duraklatılmış araçta da yük koordinatlarını eşitle.

**Girdiler:** entities, drone. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** cargo, (cargo.tx, cargo.ty)
**Bağlandığı işlevler:** find_entity_by_id
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: cid ← drone.uav.carrying_ids

**Gerçek kaynak:**

```python
def sync_cargo(entities, drone):
    """Rotasız/duraklatılmış araçta da yük koordinatlarını eşitle."""
    for cid in drone.uav.carrying_ids:
        cargo = find_entity_by_id(entities, cid)
        if cargo:
            cargo.tx, cargo.ty = drone.tx, drone.ty
```

### update_uavs — satır 15

Geçerli rotada süre kadar ilerle; kapalı yolu aşmadan dur.

**Girdiler:** entities, dt, map_w, map_h. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** obstacles, up, up.blocked_reason, target, remaining, zero_hops, up.route_i, (tx, ty), (dx, dy), distance, nxt, up.route_dir, step, up.x, up.y, (up.x, up.y), (e.tx, e.ty)
**Bağlandığı işlevler:** int, clamp, len, route_is_valid, any, bresenham_tiles, max, math.hypot, min, round, sync_cargo
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: obstacles = {(e.tx, e.ty) for e in entities if e.kind == Kind.OBSTACLE}
2. Her öğe için işle: e ← entities

**Gerçek kaynak:**

```python
def update_uavs(entities, dt, map_w, map_h):
    """Geçerli rotada süre kadar ilerle; kapalı yolu aşmadan dur."""
    obstacles = {(e.tx, e.ty) for e in entities if e.kind == Kind.OBSTACLE}
    for e in entities:
        up = e.uav
        if e.kind != Kind.UAV or up is None:
            continue
        up.blocked_reason = ""
        if up.route:
            target = int(clamp(up.route_i, 0, len(up.route) - 1))
            if not route_is_valid(up.route, obstacles, up.route_mode):
                up.blocked_reason = "Rota geçersiz: iki farklı durak ve açık yol gerekli."
            elif any(p in obstacles for p in bresenham_tiles(e.tx, e.ty, *up.route[target])):
                up.blocked_reason = "Sıradaki durağa giden yol kapalı."
            if not up.blocked_reason:
                remaining = max(0, dt) * clamp(up.speed, 1, 10)
                zero_hops = 0
                while remaining > 1e-9:
                    up.route_i = int(clamp(up.route_i, 0, len(up.route) - 1))
                    tx, ty = up.route[up.route_i]
                    dx, dy = tx - up.x, ty - up.y
                    distance = math.hypot(dx, dy)
                    if distance < 1e-9:
                        zero_hops += 1
                        if zero_hops > len(up.route) * 2:
                            up.blocked_reason = "Rotada ilerlenemiyor."
                            break
                        nxt = up.route_i + up.route_dir
                        if up.route_mode == RouteMode.LOOP:
                            nxt %= len(up.route)
                        elif not 0 <= nxt < len(up.route):
                            up.route_dir *= -1
                            nxt = up.route_i + up.route_dir
                        up.route_i = nxt
                        continue
                    zero_hops = 0
                    step = min(remaining, distance)
                    up.x += dx / distance * step
                    up.y += dy / distance * step
                    remaining -= step
        up.x, up.y = clamp(up.x, 0, map_w - 1), clamp(up.y, 0, map_h - 1)
        e.tx, e.ty = int(round(up.x)), int(round(up.y))
        sync_cargo(entities, e)
```


## iot_sim/ui_widgets.py

Satır sarma, metin ve buton çizimi için ortak bileşenlerdir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Metin sarma ve kimlikli butonlar; çizimle tıklama alanı aynı kayıttadır."""
```

Satır 2: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 4: Değeri/alanı oluştur veya güncelle: BG = (12, 19, 28)

```python
BG=(12,19,28)
```

Satır 5: Değeri/alanı oluştur veya güncelle: PANEL = (23, 33, 46)

```python
PANEL=(23,33,46)
```

Satır 6: Değeri/alanı oluştur veya güncelle: TEXT = (224, 234, 244)

```python
TEXT=(224,234,244)
```

Satır 7: Değeri/alanı oluştur veya güncelle: MUTED = (147, 166, 184)

```python
MUTED=(147,166,184)
```

Satır 8: Değeri/alanı oluştur veya güncelle: ACCENT = (91, 211, 194)

```python
ACCENT=(91,211,194)
```

Satır 9: Değeri/alanı oluştur veya güncelle: BORDER = (47, 64, 81)

```python
BORDER=(47,64,81)
```

### wrap_text — satır 12

Uzun sözcük dahil metni piksel genişliğine göre satırla.

**Girdiler:** text, font, width. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** lines
**Atanan yerel değerler / durum alanları:** lines, line, candidate
**Bağlandığı işlevler:** str(text).split, str, paragraph.split, f'{line} {word}'.strip, font.size, lines.append
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: lines = []
2. Her öğe için işle: paragraph ← str(text).split('\n')
3. Çağırana sonucu döndür: lines

**Gerçek kaynak:**

```python
def wrap_text(text, font, width):
    """Uzun sözcük dahil metni piksel genişliğine göre satırla."""
    lines=[]
    for paragraph in str(text).split("\n"):
        line=""
        for word in paragraph.split():
            candidate=f"{line} {word}".strip()
            if font.size(candidate)[0]<=width:
                line=candidate
                continue
            if line:
                lines.append(line)
                line=""
            for char in word:
                if font.size(line+char)[0]>width and line:
                    lines.append(line)
                    line=""
                line+=char
        lines.append(line)
    return lines
```

### text_block — satır 34

Satırları çiz ve sonraki boş y koordinatını döndür.

**Girdiler:** surface, text, x, y, width, font, color=TEXT, gap=4. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** y
**Atanan yerel değerler / durum alanları:** y
**Bağlandığı işlevler:** wrap_text, max, surface.blit, font.render, font.get_height
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: line ← wrap_text(text, font, max(10, width))
2. Çağırana sonucu döndür: y

**Gerçek kaynak:**

```python
def text_block(surface, text, x, y, width, font, color=TEXT, gap=4):
    """Satırları çiz ve sonraki boş y koordinatını döndür."""
    for line in wrap_text(text,font,max(10,width)):
        surface.blit(font.render(line,True,color),(x,y))
        y+=font.get_height()+gap
    return y
```

### button — satır 42

Etkin/seçili durumu çiz; etiket dar alanda küçültülür.

**Girdiler:** surface, rect, label, font, active=False, enabled=True. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** color, chosen, image
**Bağlandığı işlevler:** pygame.draw.rect, chosen.size, chosen.get_height, pygame.font.SysFont, chosen.render, surface.blit, image.get_width, image.get_height
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(surface, (35, 75, 77) if active else PANEL, rect, border_radius=8)
2. Yan etki/çağrı adımını çalıştır: pygame.draw.rect(surface, ACCENT if active else BORDER, rect, 1, border_radius=8)
3. Değeri/alanı oluştur veya güncelle: color = TEXT if enabled else MUTED
4. Değeri/alanı oluştur veya güncelle: chosen = font
5. Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: chosen.size(label)[0] > rect.width - 12 and chosen.get_height() > 13
6. Değeri/alanı oluştur veya güncelle: image = chosen.render(label, True, color)
7. Yan etki/çağrı adımını çalıştır: surface.blit(image, (rect.centerx - image.get_width() / 2, rect.centery - image.get_height() / 2))

**Gerçek kaynak:**

```python
def button(surface, rect, label, font, active=False, enabled=True):
    """Etkin/seçili durumu çiz; etiket dar alanda küçültülür."""
    pygame.draw.rect(surface,(35,75,77) if active else PANEL,rect,border_radius=8)
    pygame.draw.rect(surface,ACCENT if active else BORDER,rect,1,border_radius=8)
    color=TEXT if enabled else MUTED
    chosen=font
    while chosen.size(label)[0]>rect.width-12 and chosen.get_height()>13:
        chosen=pygame.font.SysFont("DejaVu Sans",chosen.get_height()-3)
    image=chosen.render(label,True,color)
    surface.blit(image,(rect.centerx-image.get_width()/2,rect.centery-image.get_height()/2))
```


## iot_sim/viz.py

Yüzeyler için bellekle sınırlı LRU önbelleği ve görsel yardımcı içerir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Pencere boyutunu aşmayan, ortak anahtarlı ve sınırlı görsel önbellek."""
```

Satır 2: Gereken isimleri içeri al: from collections import OrderedDict

```python
from collections import OrderedDict
```

Satır 3: Gereken isimleri içeri al: import pygame

```python
import pygame
```

### EffectCache — satır 6

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** Doğrudan object; özel üst sınıf yok. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### EffectCache.__init__ — satır 7

Sınıf örneğinin alanlarını ve birlikte çalışacağı yardımcı nesneleri başlatır.

**Girdiler:** self, limit_bytes=16 * 1024 * 1024. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.limit, self.bytes, self.items
**Bağlandığı işlevler:** OrderedDict
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.limit = limit_bytes
2. Değeri/alanı oluştur veya güncelle: self.bytes = 0
3. Değeri/alanı oluştur veya güncelle: self.items = OrderedDict()

**Gerçek kaynak:**

```python
def __init__(self, limit_bytes=16*1024*1024):
        self.limit = limit_bytes
        self.bytes = 0
        self.items = OrderedDict()
```

### EffectCache.get — satır 12

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** self, key, factory. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** self.items[key]; surface
**Atanan yerel değerler / durum alanları:** surface, size, (_, old), self.bytes, self.items[key]
**Bağlandığı işlevler:** self.items.move_to_end, factory, surface.get_pitch, surface.get_height, self.items.popitem, old.get_pitch, old.get_height
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: key in self.items
2. Değeri/alanı oluştur veya güncelle: surface = factory()
3. Değeri/alanı oluştur veya güncelle: size = surface.get_pitch() * surface.get_height()
4. Koşula göre yol seç: size <= self.limit
5. Çağırana sonucu döndür: surface

**Gerçek kaynak:**

```python
def get(self, key, factory):
        if key in self.items:
            self.items.move_to_end(key)
            return self.items[key]
        surface = factory()
        size = surface.get_pitch() * surface.get_height()
        if size <= self.limit:
            while self.items and self.bytes + size > self.limit:
                _, old = self.items.popitem(last=False)
                self.bytes -= old.get_pitch() * old.get_height()
            self.items[key] = surface
            self.bytes += size
        return surface
```

### field_overlay — satır 27

Görünür alanda çiz; menzil büyüse de tam dünya boyutunda yüzey üretme.

**Girdiler:** cache, size, sources. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** surface
**Atanan yerel değerler / durum alanları:** surface
**Bağlandığı işlevler:** pygame.Surface, pygame.draw.circle, int, max, round
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: surface = pygame.Surface(size, pygame.SRCALPHA)
2. Her öğe için işle: (cx, cy, radius, color, alpha) ← sources
3. Çağırana sonucu döndür: surface

**Gerçek kaynak:**

```python
def field_overlay(cache, size, sources):
    """Görünür alanda çiz; menzil büyüse de tam dünya boyutunda yüzey üretme."""
    surface = pygame.Surface(size, pygame.SRCALPHA)
    for cx, cy, radius, color, alpha in sources:
        # Yalnız pencere boyutundaki hedefe çizim; dev ara sprite yok.
        for fraction in (1, .8, .6, .4, .2):
            pygame.draw.circle(surface, (*color, int(alpha*(1-fraction*.7))),
                               (cx, cy), max(1, round(radius*fraction)))
    return surface
```


## main.py

Güncel komut satırı girişidir; iot_sim.app.main işlevine aktarır.

### Dosya düzeyindeki kod

Satır 1: Gereken isimleri içeri al: from iot_sim.app import main

```python
from iot_sim.app import main
```

Satır 3: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__ == "__main__":
    main()
```


## tests/test_simulation.py

Model, alarm, enerji, rota, yük, sahne, kayıt ve deterministik zaman regresyonları.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Başlangıç davranışları değil, onaylı kuralları doğrulayan regresyonlar."""
```

Satır 2: Gereken isimleri içeri al: import copy

```python
import copy
```

Satır 3: Gereken isimleri içeri al: import csv

```python
import csv
```

Satır 4: Gereken isimleri içeri al: import json

```python
import json
```

Satır 5: Gereken isimleri içeri al: import math

```python
import math
```

Satır 6: Gereken isimleri içeri al: from pathlib import Path

```python
from pathlib import Path
```

Satır 7: Gereken isimleri içeri al: import tempfile

```python
import tempfile
```

Satır 8: Gereken isimleri içeri al: import unittest

```python
import unittest
```

Satır 9: Gereken isimleri içeri al: from iot_sim.models import *

```python
from iot_sim.models import *
```

Satır 10: Gereken isimleri içeri al: from iot_sim.simulation import Simulation

```python
from iot_sim.simulation import Simulation
```

Satır 11: Gereken isimleri içeri al: from iot_sim.scene import to_scene, parse_scene, load_scene, save_scene

```python
from iot_sim.scene import to_scene, parse_scene, load_scene, save_scene
```

Satır 12: Gereken isimleri içeri al: from iot_sim.lessons import lesson_scene

```python
from iot_sim.lessons import lesson_scene
```

Satır 13: Gereken isimleri içeri al: from iot_sim.sensors import field_at, simulate_tick, invalidate

```python
from iot_sim.sensors import field_at, simulate_tick, invalidate
```

Satır 14: Gereken isimleri içeri al: from iot_sim.alarm_bridge import AlarmBridge

```python
from iot_sim.alarm_bridge import AlarmBridge
```

Satır 15: Gereken isimleri içeri al: from iot_sim.engine import route_is_valid

```python
from iot_sim.engine import route_is_valid
```

Satır 16: Gereken isimleri içeri al: from iot_sim.uav import update_uavs

```python
from iot_sim.uav import update_uavs
```

Satır 17: Gereken isimleri içeri al: from iot_sim import operations

```python
from iot_sim import operations
```

Satır 18: Gereken isimleri içeri al: from iot_sim.exporter import Exporter

```python
from iot_sim.exporter import Exporter
```

Satır 19: Gereken isimleri içeri al: from iot_sim.fire import spread_fire

```python
from iot_sim.fire import spread_fire
```

Satır 295: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__=="__main__":
    unittest.main()
```

### MeasurementTests — satır 22

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** unittest.TestCase. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### MeasurementTests.test_point_measurement_has_no_distance_cutoff — satır 23

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s, src, before, s.sensor.range_tiles, src.source.power
**Bağlandığı işlevler:** Entity, SensorProps, SourceProps, simulate_tick, self.assertAlmostEqual, field_at, self.assertGreater, self.assertEqual
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s = Entity(1, Kind.SENSOR, 0, 0, sensor=SensorProps(noise_percent=0, range_tiles=1))
2. Değeri/alanı oluştur veya güncelle: src = Entity(2, Kind.SOURCE, 16, 0, source=SourceProps(range_tiles=80))
3. Yan etki/çağrı adımını çalıştır: simulate_tick([s, src], 1)
4. Yan etki/çağrı adımını çalıştır: self.assertAlmostEqual(s.sensor.last_temp, field_at(0, 0, [src])['TEMP'])
5. Yan etki/çağrı adımını çalıştır: self.assertGreater(s.sensor.last_temp, 22)
6. Değeri/alanı oluştur veya güncelle: before = s.sensor.last_temp
7. Değeri/alanı oluştur veya güncelle: s.sensor.range_tiles = 50
8. Değeri/alanı oluştur veya güncelle: src.source.power = 10
9. Yan etki/çağrı adımını çalıştır: simulate_tick([s, src], 1)
10. Yan etki/çağrı adımını çalıştır: self.assertEqual(before, s.sensor.last_temp)

**Gerçek kaynak:**

```python
def test_point_measurement_has_no_distance_cutoff(self):
        s=Entity(1,Kind.SENSOR,0,0,sensor=SensorProps(noise_percent=0,range_tiles=1))
        src=Entity(2,Kind.SOURCE,16,0,source=SourceProps(range_tiles=80))
        simulate_tick([s,src],1)
        self.assertAlmostEqual(s.sensor.last_temp,field_at(0,0,[src])["TEMP"])
        self.assertGreater(s.sensor.last_temp,22)
        before=s.sensor.last_temp
        s.sensor.range_tiles=50
        src.source.power=10
        simulate_tick([s,src],1)
        self.assertEqual(before,s.sensor.last_temp)
```

### MeasurementTests.test_channels_and_calibration — satır 35

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** e, e.sensor.offsets['TEMP']
**Bağlandığı işlevler:** Entity, SensorProps, simulate_tick, self.assertEqual, self.assertIsNone
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e = Entity(1, Kind.SENSOR, 0, 0, sensor=SensorProps(noise_percent=0, modes={SensorMode.TEMP}))
2. Değeri/alanı oluştur veya güncelle: e.sensor.offsets['TEMP'] = 7
3. Yan etki/çağrı adımını çalıştır: simulate_tick([e], 1)
4. Yan etki/çağrı adımını çalıştır: self.assertEqual(e.sensor.last_temp, 29)
5. Yan etki/çağrı adımını çalıştır: self.assertIsNone(e.sensor.last_co)

**Gerçek kaynak:**

```python
def test_channels_and_calibration(self):
        e=Entity(1,Kind.SENSOR,0,0,sensor=SensorProps(noise_percent=0,modes={SensorMode.TEMP}))
        e.sensor.offsets["TEMP"]=7
        simulate_tick([e],1)
        self.assertEqual(e.sensor.last_temp,29)
        self.assertIsNone(e.sensor.last_co)
```

### MeasurementTests.test_energy_frequency_and_channels — satır 42

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** results, s, sim
**Bağlandığı işlevler:** set, SensorProps, Simulation, to_scene, Entity, sim.advance, results.append, self.assertGreater
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: results = []
2. Her öğe için işle: (channels, interval) ← [({SensorMode.TEMP}, 1), (set(SensorMode), 1), ({SensorMode.TEMP}, 0.5)]
3. Yan etki/çağrı adımını çalıştır: self.assertGreater(results[0], results[1])
4. Yan etki/çağrı adımını çalıştır: self.assertGreater(results[0], results[2])

**Gerçek kaynak:**

```python
def test_energy_frequency_and_channels(self):
        results=[]
        for channels,interval in [({SensorMode.TEMP},1), (set(SensorMode),1), ({SensorMode.TEMP},.5)]:
            s=SensorProps(modes=channels,sample_interval=interval)
            sim=Simulation(to_scene([Entity(1,Kind.SENSOR,1,1,sensor=s)]))
            sim.advance(10)
            results.append(sim.entities[0].sensor.battery)
        self.assertGreater(results[0],results[1])
        self.assertGreater(results[0],results[2])
```

### MeasurementTests.test_empty_and_off_are_not_zero_normal — satır 52

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim, s
**Bağlandığı işlevler:** SensorProps, set, Simulation, to_scene, Entity, sim.advance, self.assertEqual, self.assertIsNone, self.assertFalse
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: (props, state) ← [(SensorProps(battery=0), 'EMPTY'), (SensorProps(enabled=False), 'OFF'), (SensorProps(modes=set()), 'OFF')]

**Gerçek kaynak:**

```python
def test_empty_and_off_are_not_zero_normal(self):
        for props,state in [(SensorProps(battery=0),"EMPTY"),(SensorProps(enabled=False),"OFF"),(SensorProps(modes=set()),"OFF")]:
            sim=Simulation(to_scene([Entity(1,Kind.SENSOR,1,1,sensor=props)]))
            sim.advance(1)
            s=sim.entities[0].sensor
            self.assertEqual(s.status,state)
            self.assertIsNone(s.last_temp)
            self.assertFalse(s.valid)
```

### MeasurementTests.test_carried_sensor_is_logged_and_alerts — satır 61

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim
**Bağlandığı işlevler:** Simulation, lesson_scene, sim.advance, self.assertGreater, len, self.assertIn
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sim = Simulation(lesson_scene(5))
2. Yan etki/çağrı adımını çalıştır: sim.advance(4)
3. Yan etki/çağrı adımını çalıştır: self.assertGreater(len(sim.history[2]), 0)
4. Yan etki/çağrı adımını çalıştır: self.assertIn(2, sim.alarm.active_alerts)
5. Yan etki/çağrı adımını çalıştır: self.assertGreater(sim.entities[1].sensor.last_temp, 60)

**Gerçek kaynak:**

```python
def test_carried_sensor_is_logged_and_alerts(self):
        sim=Simulation(lesson_scene(5))
        sim.advance(4)
        self.assertGreater(len(sim.history[2]),0)
        self.assertIn(2,sim.alarm.active_alerts)
        self.assertGreater(sim.entities[1].sensor.last_temp,60)
```

### AlarmTests — satır 69

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** unittest.TestCase. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### AlarmTests.make — satır 70

Alarm testi için tek kanal ve ölçüm değerine sahip bağımsız sensör kurar.

**Girdiler:** self, channel, value, limit=40. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Entity(1, Kind.SENSOR, 0, 0, sensor=s)
**Atanan yerel değerler / durum alanları:** s
**Bağlandığı işlevler:** SensorProps, SensorMode, setattr, Entity
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s = SensorProps(modes={SensorMode(channel)}, valid=True, limit=limit, max_limit=40)
2. Yan etki/çağrı adımını çalıştır: setattr(s, {'TEMP': 'last_temp', 'CO': 'last_co', 'CO2': 'last_co2', 'H2': 'last_h2'}[channel], value)
3. Çağırana sonucu döndür: Entity(1, Kind.SENSOR, 0, 0, sensor=s)

**Gerçek kaynak:**

```python
def make(self,channel,value,limit=40):
        s=SensorProps(modes={SensorMode(channel)},valid=True,limit=limit,max_limit=40)
        setattr(s,{"TEMP":"last_temp","CO":"last_co","CO2":"last_co2","H2":"last_h2"}[channel],value)
        return Entity(1,Kind.SENSOR,0,0,sensor=s)
```

### AlarmTests.test_all_threshold_boundaries_agree — satır 75

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** thresholds, e, b
**Bağlandığı işlevler:** thresholds.items, self.subTest, self.make, AlarmBridge, b.update, self.assertEqual, any
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: thresholds = {'TEMP': 60, 'CO': 35, 'CO2': 5000, 'H2': 4000}
2. Her öğe için işle: (channel, threshold) ← thresholds.items()

**Gerçek kaynak:**

```python
def test_all_threshold_boundaries_agree(self):
        thresholds={"TEMP":60,"CO":35,"CO2":5000,"H2":4000}
        for channel,threshold in thresholds.items():
            for value,alarm in [(threshold-.01,False),(threshold,True),(threshold+.01,True)]:
                with self.subTest(channel=channel,value=value):
                    e=self.make(channel,value)
                    b=AlarmBridge()
                    b.update([e],0)
                    self.assertEqual(e.sensor.status=="ALERT",alarm)
                    self.assertEqual(any(ev["kind"]=="ALERT" for ev in b.events),alarm)
```

### AlarmTests.test_hysteresis_and_transition_only — satır 86

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** e, b, n, e.sensor.last_temp
**Bağlandığı işlevler:** self.make, AlarmBridge, b.update, self.assertEqual, sum
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e = self.make('TEMP', 60)
2. Değeri/alanı oluştur veya güncelle: b = AlarmBridge()
3. Yan etki/çağrı adımını çalıştır: b.update([e], 0)
4. Değeri/alanı oluştur veya güncelle: n = b.total_events
5. Değeri/alanı oluştur veya güncelle: e.sensor.last_temp = 57
6. Yan etki/çağrı adımını çalıştır: b.update([e], 1)
7. Yan etki/çağrı adımını çalıştır: self.assertEqual(n, b.total_events)
8. Yan etki/çağrı adımını çalıştır: self.assertEqual(e.sensor.status, 'ALERT')
9. Değeri/alanı oluştur veya güncelle: e.sensor.last_temp = 54.9
10. Yan etki/çağrı adımını çalıştır: b.update([e], 2)
11. Yan etki/çağrı adımını çalıştır: self.assertEqual(e.sensor.status, 'NORMAL')
12. Yan etki/çağrı adımını çalıştır: self.assertEqual(sum((ev['kind'] == 'CALM' for ev in b.events)), 1)

**Gerçek kaynak:**

```python
def test_hysteresis_and_transition_only(self):
        e=self.make("TEMP",60)
        b=AlarmBridge()
        b.update([e],0)
        n=b.total_events
        e.sensor.last_temp=57
        b.update([e],1)
        self.assertEqual(n,b.total_events)
        self.assertEqual(e.sensor.status,"ALERT")
        e.sensor.last_temp=54.9
        b.update([e],2)
        self.assertEqual(e.sensor.status,"NORMAL")
        self.assertEqual(sum(ev["kind"]=="CALM" for ev in b.events),1)
```

### AlarmTests.test_zero_repeat_quota_preserves_measurements_events — satır 100

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** e, e.sensor.repeat_seconds, b, e.sensor.last_temp
**Bağlandığı işlevler:** self.make, AlarmBridge, b.update, self.assertEqual, len, self.assertTrue, any
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e = self.make('TEMP', 70, limit=0)
2. Değeri/alanı oluştur veya güncelle: e.sensor.repeat_seconds = 1
3. Değeri/alanı oluştur veya güncelle: b = AlarmBridge()
4. Yan etki/çağrı adımını çalıştır: b.update([e], 0)
5. Yan etki/çağrı adımını çalıştır: b.update([e], 1)
6. Yan etki/çağrı adımını çalıştır: self.assertEqual(e.sensor.limit, 0)
7. Yan etki/çağrı adımını çalıştır: self.assertEqual(e.sensor.status, 'ALERT')
8. Yan etki/çağrı adımını çalıştır: self.assertEqual(len(b.notifications), 1)
9. Değeri/alanı oluştur veya güncelle: e.sensor.last_temp = 40
10. Yan etki/çağrı adımını çalıştır: b.update([e], 2)
11. Yan etki/çağrı adımını çalıştır: self.assertTrue(any((ev['kind'] == 'CALM' for ev in b.events)))
12. Yan etki/çağrı adımını çalıştır: b.update([e], 60)
13. Yan etki/çağrı adımını çalıştır: self.assertEqual(e.sensor.limit, 40)

**Gerçek kaynak:**

```python
def test_zero_repeat_quota_preserves_measurements_events(self):
        e=self.make("TEMP",70,limit=0)
        e.sensor.repeat_seconds=1
        b=AlarmBridge()
        b.update([e],0)
        b.update([e],1)
        self.assertEqual(e.sensor.limit,0)
        self.assertEqual(e.sensor.status,"ALERT")
        self.assertEqual(len(b.notifications),1)  # ilk geçiş sınırlanmaz
        e.sensor.last_temp=40
        b.update([e],2)
        self.assertTrue(any(ev["kind"]=="CALM" for ev in b.events))
        b.update([e],60)
        self.assertEqual(e.sensor.limit,40)
```

### AlarmTests.test_removed_sensor_state_is_pruned — satır 115

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** e, b
**Bağlandığı işlevler:** self.make, AlarmBridge, b.update, self.assertEqual, self.assertFalse
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: e = self.make('TEMP', 80)
2. Değeri/alanı oluştur veya güncelle: b = AlarmBridge()
3. Yan etki/çağrı adımını çalıştır: b.update([e], 0)
4. Yan etki/çağrı adımını çalıştır: b.update([], 1)
5. Yan etki/çağrı adımını çalıştır: self.assertEqual(b.alert_count, 0)
6. Yan etki/çağrı adımını çalıştır: self.assertFalse(b.slots)

**Gerçek kaynak:**

```python
def test_removed_sensor_state_is_pruned(self):
        e=self.make("TEMP",80)
        b=AlarmBridge()
        b.update([e],0)
        b.update([],1)
        self.assertEqual(b.alert_count,0)
        self.assertFalse(b.slots)
```

### DroneTests — satır 124

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** unittest.TestCase. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### DroneTests.sim — satır 125

Drone testleri için hazır hareketli ölçüm sahnesinden yeni simülasyon kurar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Simulation(lesson_scene(5))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** Simulation, lesson_scene
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: Simulation(lesson_scene(5))

**Gerçek kaynak:**

```python
def sim(self):
        return Simulation(lesson_scene(5))
```

### DroneTests.test_degenerate_route_returns — satır 128

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** u
**Bağlandığı işlevler:** Entity, UavProps, update_uavs, self.assertTrue
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: mode ← RouteMode

**Gerçek kaynak:**

```python
def test_degenerate_route_returns(self):
        for mode in RouteMode:
            u=Entity(1,Kind.UAV,2,2,uav=UavProps(x=2,y=2,route=[(2,2),(2,2)],route_mode=mode))
            update_uavs([u],.05,200,200)
            self.assertTrue(u.uav.blocked_reason)
```

### DroneTests.test_loop_closure_and_approach — satır 134

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim, old
**Bağlandığı işlevler:** self.assertFalse, route_is_valid, self.sim, sim.entities.append, Entity, self.assertRaises, operations.set_route, sim.advance, self.assertEqual, self.assertTrue
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.assertFalse(route_is_valid([(2, 2), (2, 4), (4, 4)], {(3, 3)}))
2. Değeri/alanı oluştur veya güncelle: sim = self.sim()
3. Yan etki/çağrı adımını çalıştır: sim.entities.append(Entity(9, Kind.OBSTACLE, 8, 12))
4. Kaynak yaşam süresini with bloğuyla sınırla: self.assertRaises(ValueError)
5. Değeri/alanı oluştur veya güncelle: old = (sim.entities[0].uav.x, sim.entities[0].uav.y)
6. Yan etki/çağrı adımını çalıştır: sim.advance(1)
7. Yan etki/çağrı adımını çalıştır: self.assertEqual(old, (sim.entities[0].uav.x, sim.entities[0].uav.y))
8. Yan etki/çağrı adımını çalıştır: self.assertTrue(sim.entities[0].uav.blocked_reason)

**Gerçek kaynak:**

```python
def test_loop_closure_and_approach(self):
        self.assertFalse(route_is_valid([(2,2),(2,4),(4,4)],{(3,3)}))
        sim=self.sim()
        sim.entities.append(Entity(9,Kind.OBSTACLE,8,12))
        with self.assertRaises(ValueError):
            operations.set_route(sim,sim.entities[0],[(9,12),(12,12)])
        old=(sim.entities[0].uav.x,sim.entities[0].uav.y)
        sim.advance(1)
        self.assertEqual(old,(sim.entities[0].uav.x,sim.entities[0].uav.y))
        self.assertTrue(sim.entities[0].uav.blocked_reason)
```

### DroneTests.test_move_and_delete_keep_cargo_consistent — satır 145

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim, (drone, sensor), drone.uav.route
**Bağlandığı işlevler:** self.sim, operations.move_entity, self.assertEqual, operations.delete_entity, self.assertIsNone, self.assertNotEqual, parse_scene, sim.snapshot
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sim = self.sim()
2. Değeri/alanı oluştur veya güncelle: drone, sensor = sim.entities[:2]
3. Değeri/alanı oluştur veya güncelle: drone.uav.route = []
4. Yan etki/çağrı adımını çalıştır: operations.move_entity(sim, drone.id, 2, 2)
5. Yan etki/çağrı adımını çalıştır: self.assertEqual((sensor.tx, sensor.ty), (2, 2))
6. Yan etki/çağrı adımını çalıştır: operations.delete_entity(sim, drone.id)
7. Yan etki/çağrı adımını çalıştır: self.assertIsNone(sensor.carried_by)
8. Yan etki/çağrı adımını çalıştır: self.assertNotEqual((sensor.tx, sensor.ty), (sim.entities[-1].tx, sim.entities[-1].ty))
9. Yan etki/çağrı adımını çalıştır: parse_scene(sim.snapshot())

**Gerçek kaynak:**

```python
def test_move_and_delete_keep_cargo_consistent(self):
        sim=self.sim()
        drone,sensor=sim.entities[:2]
        drone.uav.route=[]
        operations.move_entity(sim,drone.id,2,2)
        self.assertEqual((sensor.tx,sensor.ty),(2,2))
        operations.delete_entity(sim,drone.id)
        self.assertIsNone(sensor.carried_by)
        self.assertNotEqual((sensor.tx,sensor.ty),(sim.entities[-1].tx,sim.entities[-1].ty))
        parse_scene(sim.snapshot())
```

### DroneTests.test_release_is_atomic_when_full — satır 156

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** s, u, entities, sim, before
**Bağlandığı işlevler:** Entity, SensorProps, UavProps, enumerate, Simulation, to_scene, sim.snapshot, self.assertRaises, operations.release_cargo, self.assertEqual
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: s = Entity(2, Kind.SENSOR, 0, 0, sensor=SensorProps(), carried_by=1)
2. Değeri/alanı oluştur veya güncelle: u = Entity(1, Kind.UAV, 0, 0, uav=UavProps(x=0, y=0, carrying_ids=[2]))
3. Değeri/alanı oluştur veya güncelle: entities = [u, s] + [Entity(3 + i, Kind.OBSTACLE, x, y) for i, (x, y) in enumerate([(0, 1), (1, 0), (1, 1)])]
4. Değeri/alanı oluştur veya güncelle: sim = Simulation(to_scene(entities, width=2, height=2))
5. Değeri/alanı oluştur veya güncelle: before = sim.snapshot()
6. Kaynak yaşam süresini with bloğuyla sınırla: self.assertRaises(ValueError)
7. Yan etki/çağrı adımını çalıştır: self.assertEqual(before, sim.snapshot())

**Gerçek kaynak:**

```python
def test_release_is_atomic_when_full(self):
        s=Entity(2,Kind.SENSOR,0,0,sensor=SensorProps(),carried_by=1)
        u=Entity(1,Kind.UAV,0,0,uav=UavProps(x=0,y=0,carrying_ids=[2]))
        entities=[u,s]+[Entity(3+i,Kind.OBSTACLE,x,y) for i,(x,y) in enumerate([(0,1),(1,0),(1,1)])]
        sim=Simulation(to_scene(entities,width=2,height=2))
        before=sim.snapshot()
        with self.assertRaises(ValueError): operations.release_cargo(sim,sim.entities[0])
        self.assertEqual(before,sim.snapshot())
```

### DroneTests.test_capacity_and_mixed_load — satır 165

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim, drone, s, source
**Bağlandığı işlevler:** Simulation, to_scene, operations.add_entity, operations.attach, self.assertRaises
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sim = Simulation(to_scene([]))
2. Değeri/alanı oluştur veya güncelle: drone = operations.add_entity(sim, Kind.UAV, 0, 0)
3. Değeri/alanı oluştur veya güncelle: s = operations.add_entity(sim, Kind.SENSOR, 1, 0)
4. Değeri/alanı oluştur veya güncelle: source = operations.add_entity(sim, Kind.SOURCE, 2, 0)
5. Yan etki/çağrı adımını çalıştır: operations.attach(sim, drone.id, s.id)
6. Kaynak yaşam süresini with bloğuyla sınırla: self.assertRaises(ValueError)

**Gerçek kaynak:**

```python
def test_capacity_and_mixed_load(self):
        sim=Simulation(to_scene([]))
        drone=operations.add_entity(sim,Kind.UAV,0,0)
        s=operations.add_entity(sim,Kind.SENSOR,1,0)
        source=operations.add_entity(sim,Kind.SOURCE,2,0)
        operations.attach(sim,drone.id,s.id)
        with self.assertRaises(ValueError): operations.attach(sim,drone.id,source.id)
```

### TimeAndSceneTests — satır 174

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** unittest.TestCase. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### TimeAndSceneTests.test_lessons_demonstrate_promised_relationships — satır 175

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** distance, noisy, noisy.entities[0].sensor.noise_percent, baseline, noisy.entities[0].sensor.offsets['TEMP'], battery, gas, gas.entities[0].sensor.noise_percent, co, moving, fire
**Bağlandığı işlevler:** Simulation, lesson_scene, distance.advance, self.assertGreater, noisy.advance, self.assertAlmostEqual, battery.advance, self.assertEqual, gas.advance, gas.entities[1].source.gas_modes.add, moving.advance, len, fire.advance
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: distance = Simulation(lesson_scene(1))
2. Yan etki/çağrı adımını çalıştır: distance.advance(1)
3. Yan etki/çağrı adımını çalıştır: self.assertGreater(distance.entities[0].sensor.last_temp, distance.entities[1].sensor.last_temp)
4. Değeri/alanı oluştur veya güncelle: noisy = Simulation(lesson_scene(2))
5. Değeri/alanı oluştur veya güncelle: noisy.entities[0].sensor.noise_percent = 0
6. Yan etki/çağrı adımını çalıştır: noisy.advance(1)
7. Değeri/alanı oluştur veya güncelle: baseline = noisy.entities[0].sensor.last_temp
8. Değeri/alanı oluştur veya güncelle: noisy.entities[0].sensor.offsets['TEMP'] = 10
9. Yan etki/çağrı adımını çalıştır: noisy.advance(1)
10. Yan etki/çağrı adımını çalıştır: self.assertAlmostEqual(noisy.entities[0].sensor.last_temp, baseline + 10)
11. Değeri/alanı oluştur veya güncelle: battery = Simulation(lesson_scene(3))
12. Yan etki/çağrı adımını çalıştır: battery.advance(10)
13. Yan etki/çağrı adımını çalıştır: self.assertEqual(battery.entities[1].sensor.status, 'EMPTY')
14. Yan etki/çağrı adımını çalıştır: self.assertEqual(battery.entities[0].sensor.status, 'NORMAL')
15. Değeri/alanı oluştur veya güncelle: gas = Simulation(lesson_scene(4))
16. Değeri/alanı oluştur veya güncelle: gas.entities[0].sensor.noise_percent = 0
17. Yan etki/çağrı adımını çalıştır: gas.advance(1)
18. Değeri/alanı oluştur veya güncelle: co = gas.entities[0].sensor.last_co
19. Yan etki/çağrı adımını çalıştır: self.assertEqual(gas.entities[0].sensor.last_co2, 0)
20. Yan etki/çağrı adımını çalıştır: gas.entities[1].source.gas_modes.add(GasMode.CO2)
21. Yan etki/çağrı adımını çalıştır: gas.advance(1)
22. Yan etki/çağrı adımını çalıştır: self.assertEqual(gas.entities[0].sensor.last_co, co)
23. Yan etki/çağrı adımını çalıştır: self.assertGreater(gas.entities[0].sensor.last_co2, 0)
24. Değeri/alanı oluştur veya güncelle: moving = Simulation(lesson_scene(5))
25. Yan etki/çağrı adımını çalıştır: moving.advance(6)
26. Yan etki/çağrı adımını çalıştır: self.assertGreater(len({r['measured']['TEMP'] for r in moving.history[2]}), 1)
27. Değeri/alanı oluştur veya güncelle: fire = Simulation(lesson_scene(6))
28. Yan etki/çağrı adımını çalıştır: fire.advance(4)
29. Yan etki/çağrı adımını çalıştır: self.assertEqual(fire.entities[1].kind, Kind.BURNED)
30. Yan etki/çağrı adımını çalıştır: self.assertEqual(fire.entities[2].kind, Kind.OBSTACLE)

**Gerçek kaynak:**

```python
def test_lessons_demonstrate_promised_relationships(self):
        distance=Simulation(lesson_scene(1));distance.advance(1)
        self.assertGreater(distance.entities[0].sensor.last_temp,distance.entities[1].sensor.last_temp)
        noisy=Simulation(lesson_scene(2))
        noisy.entities[0].sensor.noise_percent=0
        noisy.advance(1)
        baseline=noisy.entities[0].sensor.last_temp
        noisy.entities[0].sensor.offsets["TEMP"]=10
        noisy.advance(1)
        self.assertAlmostEqual(noisy.entities[0].sensor.last_temp,baseline+10)
        battery=Simulation(lesson_scene(3));battery.advance(10)
        self.assertEqual(battery.entities[1].sensor.status,"EMPTY")
        self.assertEqual(battery.entities[0].sensor.status,"NORMAL")
        gas=Simulation(lesson_scene(4));gas.entities[0].sensor.noise_percent=0;gas.advance(1)
        co=gas.entities[0].sensor.last_co
        self.assertEqual(gas.entities[0].sensor.last_co2,0)
        gas.entities[1].source.gas_modes.add(GasMode.CO2);gas.advance(1)
        self.assertEqual(gas.entities[0].sensor.last_co,co)
        self.assertGreater(gas.entities[0].sensor.last_co2,0)
        moving=Simulation(lesson_scene(5));moving.advance(6)
        self.assertGreater(len({r["measured"]["TEMP"] for r in moving.history[2]}),1)
        fire=Simulation(lesson_scene(6));fire.advance(4)
        self.assertEqual(fire.entities[1].kind,Kind.BURNED)
        self.assertEqual(fire.entities[2].kind,Kind.OBSTACLE)
```

### TimeAndSceneTests.test_scene_can_capture_drone_crossing_ground_sensor — satır 200

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** drone, sensor, scene
**Bağlandığı işlevler:** Entity, UavProps, SensorProps, to_scene, parse_scene
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: drone = Entity(1, Kind.UAV, 2, 2, uav=UavProps(x=2, y=2))
2. Değeri/alanı oluştur veya güncelle: sensor = Entity(2, Kind.SENSOR, 2, 2, sensor=SensorProps())
3. Değeri/alanı oluştur veya güncelle: scene = to_scene([drone, sensor])
4. Yan etki/çağrı adımını çalıştır: parse_scene(scene)

**Gerçek kaynak:**

```python
def test_scene_can_capture_drone_crossing_ground_sensor(self):
        drone=Entity(1,Kind.UAV,2,2,uav=UavProps(x=2,y=2))
        sensor=Entity(2,Kind.SENSOR,2,2,sensor=SensorProps())
        scene=to_scene([drone,sensor])
        parse_scene(scene)
```

### TimeAndSceneTests.test_frame_partition_and_seed_reproduce_all_history — satır 206

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** (a, b), c
**Bağlandığı işlevler:** Simulation, lesson_scene, a.advance, range, b.advance, self.assertEqual, list, a.reset, c.advance
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: a, b = (Simulation(lesson_scene(2)), Simulation(lesson_scene(2)))
2. Yan etki/çağrı adımını çalıştır: a.advance(10)
3. Her öğe için işle: _ ← range(400)
4. Yan etki/çağrı adımını çalıştır: self.assertEqual(a.time, b.time)
5. Yan etki/çağrı adımını çalıştır: self.assertEqual(list(a.history[1]), list(b.history[1]))
6. Yan etki/çağrı adımını çalıştır: self.assertEqual(list(a.alarm.events), list(b.alarm.events))
7. Değeri/alanı oluştur veya güncelle: c = a.reset()
8. Yan etki/çağrı adımını çalıştır: c.advance(10)
9. Yan etki/çağrı adımını çalıştır: self.assertEqual(list(a.history[1]), list(c.history[1]))

**Gerçek kaynak:**

```python
def test_frame_partition_and_seed_reproduce_all_history(self):
        a,b=Simulation(lesson_scene(2)),Simulation(lesson_scene(2))
        a.advance(10)
        for _ in range(400): b.advance(.025)
        self.assertEqual(a.time,b.time)
        self.assertEqual(list(a.history[1]),list(b.history[1]))
        self.assertEqual(list(a.alarm.events),list(b.alarm.events))
        c=a.reset();c.advance(10)
        self.assertEqual(list(a.history[1]),list(c.history[1]))
```

### TimeAndSceneTests.test_all_lessons_roundtrip — satır 216

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** scene, path, sim
**Bağlandığı işlevler:** tempfile.TemporaryDirectory, range, lesson_scene, Path, save_scene, Simulation, load_scene, self.assertEqual, sim.snapshot, sim.advance
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Kaynak yaşam süresini with bloğuyla sınırla: tempfile.TemporaryDirectory()

**Gerçek kaynak:**

```python
def test_all_lessons_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            for n in range(1,7):
                scene=lesson_scene(n)
                path=Path(tmp)/f"{n}.json"
                save_scene(path,scene)
                sim=Simulation(load_scene(path))
                self.assertEqual(scene,sim.snapshot())
                sim.advance(10)
```

### TimeAndSceneTests.test_reject_corrupt_scene_without_mutation — satır 226

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim, before, changes, data
**Bağlandığı işlevler:** Simulation, lesson_scene, sim.snapshot, d.update, float, d['entities'].append, copy.deepcopy, d['entities'][0]['sensor'].update, d['entities'][0].update, d['entities'][0]['sensor']['clear_thresholds'].update, change, self.assertRaises, parse_scene, self.assertEqual
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sim = Simulation(lesson_scene(1))
2. Değeri/alanı oluştur veya güncelle: before = sim.snapshot()
3. Değeri/alanı oluştur veya güncelle: changes = [lambda d: d.update(schema_version=999), lambda d: d.update(seed=float('nan')), lambda d: d['entities'].append(copy.deepcopy(d['entities'][0])), lambda d: d['entities'][0]['sensor'].update(sample_interval=0), l…
4. Her öğe için işle: change ← changes

**Gerçek kaynak:**

```python
def test_reject_corrupt_scene_without_mutation(self):
        sim=Simulation(lesson_scene(1));before=sim.snapshot()
        changes=[lambda d:d.update(schema_version=999), lambda d:d.update(seed=float("nan")),
                 lambda d:d["entities"].append(copy.deepcopy(d["entities"][0])),
                 lambda d:d["entities"][0]["sensor"].update(sample_interval=0),
                 lambda d:d["entities"][0].update(carried_by=987),
                 lambda d:d["entities"][0]["sensor"]["clear_thresholds"].update(TEMP=900),
                 lambda d:d["entities"][0].update(tx=-1)]
        for change in changes:
            data=copy.deepcopy(before);change(data)
            with self.assertRaises(ValueError): parse_scene(data)
            self.assertEqual(sim.snapshot(),before)
```

### TimeAndSceneTests.test_speed_and_interval_partition — satır 239

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** references, sim
**Bağlandığı işlevler:** Simulation, lesson_scene, range, round, sim.advance, references.append, list, self.assertTrue, all
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: references = []
2. Her öğe için işle: speed ← (0.25, 1, 2, 5)
3. Yan etki/çağrı adımını çalıştır: self.assertTrue(all((item == references[0] for item in references)))

**Gerçek kaynak:**

```python
def test_speed_and_interval_partition(self):
        references=[]
        for speed in (.25,1,2,5):
            sim=Simulation(lesson_scene(5))
            for _ in range(round(4/(.01*speed))): sim.advance(.01*speed)
            references.append((sim.time,list(sim.history[2])))
        self.assertTrue(all(item==references[0] for item in references))
```

### ExportAndFireTests — satır 248

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** unittest.TestCase. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### ExportAndFireTests.test_unique_sessions_complete_data_and_metadata — satır 249

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** scene, sim, rows
**Bağlandığı işlevler:** tempfile.TemporaryDirectory, lesson_scene, Exporter, self.assertNotEqual, Simulation, sim.start_recording, sim.advance, a.log_change, sim.snapshot, a.csv_path.open, list, csv.DictReader, self.assertEqual, len, self.assertTrue, all, json.loads, (a.directory / 'experiment.json').read_text, a.actions_path.read_text().splitlines, a.actions_path.read_text
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Kaynak yaşam süresini with bloğuyla sınırla: tempfile.TemporaryDirectory()

**Gerçek kaynak:**

```python
def test_unique_sessions_complete_data_and_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            scene=lesson_scene(5)
            with Exporter(tmp,tag="same",scene=scene) as a, Exporter(tmp,tag="same",scene=scene) as b:
                self.assertNotEqual(a.directory,b.directory)
                sim=Simulation(scene);sim.start_recording(a);sim.advance(2)
                a.log_change(sim.time,"test",sim.snapshot())
            with a.csv_path.open() as f:
                rows=list(csv.DictReader(f))
            self.assertEqual(len(rows),8)
            self.assertTrue(all(r["carried_by"]=="1" for r in rows))
            self.assertEqual(json.loads((a.directory/"experiment.json").read_text())["scene"],scene)
            self.assertEqual(len(a.actions_path.read_text().splitlines()),1)
            self.assertTrue(a.closed)
```

### ExportAndFireTests.test_invalid_measurements_are_blank — satır 264

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim, rows
**Bağlandığı işlevler:** tempfile.TemporaryDirectory, Simulation, to_scene, Entity, SensorProps, Exporter, sim.snapshot, sim.start_recording, sim.advance, exporter.csv_path.open, list, csv.DictReader, self.assertTrue, all
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Kaynak yaşam süresini with bloğuyla sınırla: tempfile.TemporaryDirectory()

**Gerçek kaynak:**

```python
def test_invalid_measurements_are_blank(self):
        with tempfile.TemporaryDirectory() as tmp:
            sim=Simulation(to_scene([Entity(1,Kind.SENSOR,1,1,sensor=SensorProps(battery=0))]))
            with Exporter(tmp,scene=sim.snapshot()) as exporter:
                sim.start_recording(exporter);sim.advance(1)
            with exporter.csv_path.open() as f:
                rows=list(csv.DictReader(f))
            self.assertTrue(all(r["measured"]=="" and r["valid"]=="0" and r["status"]=="EMPTY" for r in rows))
```

### ExportAndFireTests.test_exception_closes_files — satır 273

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** exporter
**Bağlandığı işlevler:** tempfile.TemporaryDirectory, self.assertRaises, Exporter, RuntimeError, self.assertTrue
**Açık hata yolları:** RuntimeError('deneme')

**İşleyiş sırası:**

1. Kaynak yaşam süresini with bloğuyla sınırla: tempfile.TemporaryDirectory()

**Gerçek kaynak:**

```python
def test_exception_closes_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            exporter=None
            with self.assertRaises(RuntimeError):
                with Exporter(tmp) as exporter: raise RuntimeError("deneme")
            self.assertTrue(exporter.closed)
```

### ExportAndFireTests.test_ignition_needs_heat_time_and_flammability — satır 280

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim
**Bağlandığı işlevler:** Simulation, lesson_scene, sim.advance, self.assertEqual
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sim = Simulation(lesson_scene(6))
2. Yan etki/çağrı adımını çalıştır: sim.advance(2.95)
3. Yan etki/çağrı adımını çalıştır: self.assertEqual(sim.entities[1].kind, Kind.OBSTACLE)
4. Yan etki/çağrı adımını çalıştır: sim.advance(0.05)
5. Yan etki/çağrı adımını çalıştır: self.assertEqual(sim.entities[1].kind, Kind.BURNED)
6. Yan etki/çağrı adımını çalıştır: self.assertEqual(sim.entities[2].kind, Kind.OBSTACLE)

**Gerçek kaynak:**

```python
def test_ignition_needs_heat_time_and_flammability(self):
        sim=Simulation(lesson_scene(6))
        sim.advance(2.95)
        self.assertEqual(sim.entities[1].kind,Kind.OBSTACLE)
        sim.advance(.05)
        self.assertEqual(sim.entities[1].kind,Kind.BURNED)
        self.assertEqual(sim.entities[2].kind,Kind.OBSTACLE)
```

### ExportAndFireTests.test_cool_source_does_not_ignite — satır 288

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sim, sim.entities[0].source.temp_celcius
**Bağlandığı işlevler:** Simulation, lesson_scene, sim.advance, self.assertTrue, all
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: sim = Simulation(lesson_scene(6))
2. Değeri/alanı oluştur veya güncelle: sim.entities[0].source.temp_celcius = 50
3. Yan etki/çağrı adımını çalıştır: sim.advance(10)
4. Yan etki/çağrı adımını çalıştır: self.assertTrue(all((e.kind == Kind.OBSTACLE for e in sim.entities[1:3])))

**Gerçek kaynak:**

```python
def test_cool_source_does_not_ignite(self):
        sim=Simulation(lesson_scene(6))
        sim.entities[0].source.temp_celcius=50
        sim.advance(10)
        self.assertTrue(all(e.kind==Kind.OBSTACLE for e in sim.entities[1:3]))
```


## tests/test_ui.py

Pygame çizimi ve gerçek olay işleyicisini kontrollü girişlerle sınar.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Pygame'in gerçek çizim ve olay işleyicisini kontrollü SDL girdileriyle sınar."""
```

Satır 2: Gereken isimleri içeri al: import os

```python
import os
```

Satır 3: Gereken isimleri içeri al: import tempfile

```python
import tempfile
```

Satır 4: Gereken isimleri içeri al: import unittest

```python
import unittest
```

Satır 5: Gereken isimleri içeri al: from pathlib import Path

```python
from pathlib import Path
```

Satır 6: Gereken isimleri içeri al: from unittest.mock import patch

```python
from unittest.mock import patch
```

Satır 7: Yan etki/çağrı adımını çalıştır: os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')

```python
os.environ.setdefault("SDL_VIDEODRIVER","dummy")
```

Satır 8: Yan etki/çağrı adımını çalıştır: os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')

```python
os.environ.setdefault("SDL_AUDIODRIVER","dummy")
```

Satır 9: Yan etki/çağrı adımını çalıştır: os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')

```python
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT","1")
```

Satır 10: Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.

```python
try:
    import pygame
except ImportError:
    raise unittest.SkipTest("Grafik testleri için requirements.txt kurulmalı.")
```

Satır 14: Gereken isimleri içeri al: from iot_sim.app import App

```python
from iot_sim.app import App
```

Satır 15: Gereken isimleri içeri al: from iot_sim.lessons import lesson_scene

```python
from iot_sim.lessons import lesson_scene
```

Satır 16: Gereken isimleri içeri al: from iot_sim.scene import to_scene, parse_scene

```python
from iot_sim.scene import to_scene,parse_scene
```

Satır 17: Gereken isimleri içeri al: from iot_sim.models import *

```python
from iot_sim.models import *
```

Satır 194: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__=="__main__":
    unittest.main()
```

### UITests — satır 20

İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.

**Sınıf ilişkisi:** unittest.TestCase. Alanlar nesnenin durumudur; yöntemler aşağıda ayrı kayıtlıdır.

**Alanlar ve sınıf düzeyindeki bloklar:**

```python
# Alanlar __init__ içinde atanır.
```

### UITests.setUp — satır 21

Her test için bağımsız geçici çıktı alanı ve uygulama örneği hazırlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.tmp, self.app, self.app.toast
**Bağlandığı işlevler:** tempfile.TemporaryDirectory, App, self.app.draw
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.tmp = tempfile.TemporaryDirectory()
2. Değeri/alanı oluştur veya güncelle: self.app = App(out_dir=self.tmp.name, size=(1024, 720))
3. Değeri/alanı oluştur veya güncelle: self.app.toast = ''
4. Yan etki/çağrı adımını çalıştır: self.app.draw()

**Gerçek kaynak:**

```python
def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.app=App(out_dir=self.tmp.name,size=(1024,720))
        self.app.toast=""
        self.app.draw()
```

### UITests.tearDown — satır 27

Test kaynaklarını kapatır; geçici sonuç alanını temizler.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self.app.close_recording, pygame.quit, self.tmp.cleanup
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.app.close_recording()
2. Yan etki/çağrı adımını çalıştır: pygame.quit()
3. Yan etki/çağrı adımını çalıştır: self.tmp.cleanup()

**Gerçek kaynak:**

```python
def tearDown(self):
        self.app.close_recording()
        pygame.quit()
        self.tmp.cleanup()
```

### UITests.click — satır 32

Kimlikli butonu görünür hale getirip gerçek olay işleyicisine tıklama yollar.

**Girdiler:** self, key. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.app.inspector.scroll, (rect, _), pos
**Bağlandığı işlevler:** range, self.app.draw, min, self.assertIn, self.app.process_event, pygame.event.Event
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: _ ← range(25)
2. Yan etki/çağrı adımını çalıştır: self.assertIn(key, self.app.buttons)
3. Değeri/alanı oluştur veya güncelle: rect, _ = self.app.buttons[key]
4. Değeri/alanı oluştur veya güncelle: pos = rect.center
5. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=pos))
6. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=pos))

**Gerçek kaynak:**

```python
def click(self,key):
        for _ in range(25):
            self.app.draw()
            if key in self.app.buttons: break
            self.app.inspector.scroll=min(self.app.inspector.bottom,self.app.inspector.scroll+200)
        self.assertIn(key,self.app.buttons)
        rect,_=self.app.buttons[key]
        pos=rect.center
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=1,pos=pos))
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP,button=1,pos=pos))
```

### UITests.mapclick — satır 43

Dünya koordinatını piksele çevirip harita fare olayını üretir.

**Girdiler:** self, x, y, button=1. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** pos
**Bağlandığı işlevler:** self.app.draw, self.app.cam.world_to_screen, self.app.process_event, pygame.event.Event
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.app.draw()
2. Değeri/alanı oluştur veya güncelle: pos = self.app.cam.world_to_screen(x + 0.5, y + 0.5)
3. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=button, pos=pos))
4. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP, button=button, pos=pos))

**Gerçek kaynak:**

```python
def mapclick(self,x,y,button=1):
        self.app.draw()
        pos=self.app.cam.world_to_screen(x+.5,y+.5)
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=button,pos=pos))
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP,button=button,pos=pos))
```

### UITests.key — satır 49

Gerçek olay işleyicisine kontrollü tuş olayı yollar.

**Girdiler:** self, key. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** self.app.process_event, pygame.event.Event
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.KEYDOWN, key=key, unicode='', mod=0))

**Gerçek kaynak:**

```python
def key(self,key):
        self.app.process_event(pygame.event.Event(pygame.KEYDOWN,key=key,unicode="",mod=0))
```

### UITests.test_all_lessons_graphs_and_resizing — satır 52

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** range, self.app.action, self.click, str, self.assertEqual, self.app.sim.advance, self.app.draw, self.app.process_event, pygame.event.Event, self.assertTrue, self.app.screen.get_rect().contains, self.app.screen.get_rect
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: n ← range(1, 7)

**Gerçek kaynak:**

```python
def test_all_lessons_graphs_and_resizing(self):
        for n in range(1,7):
            self.app.action(("tab","lesson"))
            self.click("lesson_"+str(n))
            self.assertEqual(self.app.sim.lesson,n)
            self.click("step")
            self.app.sim.advance(9)
            for channel in ("TEMP","CO","CO2","H2","BATTERY"):
                self.click("channel_"+channel)
                self.app.draw()
            self.app.process_event(pygame.event.Event(pygame.VIDEORESIZE,w=1280,h=800))
            self.app.draw()
            self.assertTrue(self.app.screen.get_rect().contains(self.app.panel_rect))
            self.assertTrue(self.app.screen.get_rect().contains(self.app.graph_rect))
```

### UITests.test_editor_and_actual_event_coordinates — satır 67

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** sensor, self.app.input_text
**Bağlandığı işlevler:** self.click, self.mapclick, self.assertEqual, len, self.key, self.assertFalse
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.click('new')
2. Yan etki/çağrı adımını çalıştır: self.click('tool_sensor')
3. Yan etki/çağrı adımını çalıştır: self.mapclick(100, 100)
4. Yan etki/çağrı adımını çalıştır: self.assertEqual(len(self.app.sim.entities), 1)
5. Değeri/alanı oluştur veya güncelle: sensor = self.app.selected
6. Yan etki/çağrı adımını çalıştır: self.assertEqual((sensor.tx, sensor.ty), (100, 100))
7. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_m)
8. Yan etki/çağrı adımını çalıştır: self.mapclick(101, 101)
9. Yan etki/çağrı adımını çalıştır: self.assertEqual((sensor.tx, sensor.ty), (101, 101))
10. Yan etki/çağrı adımını çalıştır: self.click('rename')
11. Değeri/alanı oluştur veya güncelle: self.app.input_text = 'Öğretici sensör'
12. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_RETURN)
13. Yan etki/çağrı adımını çalıştır: self.assertEqual(sensor.name, 'Öğretici sensör')
14. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_DELETE)
15. Yan etki/çağrı adımını çalıştır: self.assertFalse(self.app.sim.entities)

**Gerçek kaynak:**

```python
def test_editor_and_actual_event_coordinates(self):
        self.click("new")
        self.click("tool_sensor")
        self.mapclick(100,100)
        self.assertEqual(len(self.app.sim.entities),1)
        sensor=self.app.selected
        self.assertEqual((sensor.tx,sensor.ty),(100,100))
        self.key(pygame.K_m)
        self.mapclick(101,101)
        self.assertEqual((sensor.tx,sensor.ty),(101,101))
        self.click("rename")
        self.app.input_text="Öğretici sensör"
        self.key(pygame.K_RETURN)
        self.assertEqual(sensor.name,"Öğretici sensör")
        self.key(pygame.K_DELETE)
        self.assertFalse(self.app.sim.entities)
```

### UITests.test_right_click_and_del_both_release — satır 84

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** drone, self.app.selected_id, sensor
**Bağlandığı işlevler:** self.app.replace_sim, lesson_scene, self.key, self.mapclick, next, self.assertIsNone, parse_scene, self.app.sim.snapshot
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: key_delete ← (False, True)

**Gerçek kaynak:**

```python
def test_right_click_and_del_both_release(self):
        for key_delete in (False,True):
            self.app.replace_sim(lesson_scene(5))
            drone=self.app.sim.entities[0]
            if key_delete:
                self.app.selected_id=drone.id
                self.key(pygame.K_DELETE)
            else:
                self.mapclick(drone.tx,drone.ty,3)
            sensor=next(e for e in self.app.sim.entities if e.sensor)
            self.assertIsNone(sensor.carried_by)
            self.assertIsNone(next((e for e in self.app.sim.entities if e.uav),None))
            parse_scene(self.app.sim.snapshot())
```

### UITests.test_drag_drop_sensor_to_drone_panel — satır 98

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** scene, self.app.selected_id, pos
**Bağlandığı işlevler:** to_scene, Entity, UavProps, SensorProps, self.app.replace_sim, self.app.draw, self.app.cam.world_to_screen, self.app.process_event, pygame.event.Event, self.assertEqual
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: scene = to_scene([Entity(1, Kind.UAV, 10, 10, uav=UavProps(x=10, y=10)), Entity(2, Kind.SENSOR, 12, 10, sensor=SensorProps())])
2. Yan etki/çağrı adımını çalıştır: self.app.replace_sim(scene)
3. Değeri/alanı oluştur veya güncelle: self.app.selected_id = 1
4. Yan etki/çağrı adımını çalıştır: self.app.draw()
5. Değeri/alanı oluştur veya güncelle: pos = self.app.cam.world_to_screen(12.5, 10.5)
6. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=pos))
7. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.MOUSEMOTION, pos=self.app.panel_rect.center, rel=(50, 0), buttons=(1, 0, 0)))
8. Yan etki/çağrı adımını çalıştır: self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP, button=1, pos=self.app.panel_rect.center))
9. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.sim.entities[1].carried_by, 1)
10. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.sim.entities[0].uav.carrying_ids, [2])

**Gerçek kaynak:**

```python
def test_drag_drop_sensor_to_drone_panel(self):
        scene=to_scene([Entity(1,Kind.UAV,10,10,uav=UavProps(x=10,y=10)),
                        Entity(2,Kind.SENSOR,12,10,sensor=SensorProps())])
        self.app.replace_sim(scene)
        self.app.selected_id=1
        self.app.draw()
        pos=self.app.cam.world_to_screen(12.5,10.5)
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=1,pos=pos))
        self.app.process_event(pygame.event.Event(pygame.MOUSEMOTION,pos=self.app.panel_rect.center,rel=(50,0),buttons=(1,0,0)))
        self.app.process_event(pygame.event.Event(pygame.MOUSEBUTTONUP,button=1,pos=self.app.panel_rect.center))
        self.assertEqual(self.app.sim.entities[1].carried_by,1)
        self.assertEqual(self.app.sim.entities[0].uav.carrying_ids,[2])
```

### UITests.test_route_keyboard_and_cancel — satır 111

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.app.selected_id
**Bağlandığı işlevler:** self.app.replace_sim, lesson_scene, self.key, self.mapclick, self.assertEqual, len
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.app.replace_sim(lesson_scene(5))
2. Değeri/alanı oluştur veya güncelle: self.app.selected_id = 1
3. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_k)
4. Yan etki/çağrı adımını çalıştır: self.mapclick(7, 10)
5. Yan etki/çağrı adımını çalıştır: self.mapclick(9, 10)
6. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_k)
7. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.sim.entities[0].uav.route, [(7, 10), (9, 10)])
8. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_k)
9. Yan etki/çağrı adımını çalıştır: self.mapclick(7, 10)
10. Yan etki/çağrı adımını çalıştır: self.mapclick(7, 10)
11. Yan etki/çağrı adımını çalıştır: self.assertEqual(len(self.app.route_points), 1)
12. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_ESCAPE)
13. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.sim.entities[0].uav.route, [(7, 10), (9, 10)])

**Gerçek kaynak:**

```python
def test_route_keyboard_and_cancel(self):
        self.app.replace_sim(lesson_scene(5))
        self.app.selected_id=1
        self.key(pygame.K_k)
        self.mapclick(7,10)
        self.mapclick(9,10)
        self.key(pygame.K_k)
        self.assertEqual(self.app.sim.entities[0].uav.route,[(7,10),(9,10)])
        self.key(pygame.K_k)
        self.mapclick(7,10)
        self.mapclick(7,10)
        self.assertEqual(len(self.app.route_points),1)
        self.key(pygame.K_ESCAPE)
        self.assertEqual(self.app.sim.entities[0].uav.route,[(7,10),(9,10)])
```

### UITests.test_save_load_seed_invalid_load_preserves_scene — satır 126

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** path, self.app.input_text, before
**Bağlandığı işlevler:** Path, self.click, str, self.key, self.assertTrue, path.exists, self.app.sim.snapshot, self.assertEqual, path.write_text
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: path = Path(self.tmp.name) / 'sahne.json'
2. Yan etki/çağrı adımını çalıştır: self.click('save')
3. Değeri/alanı oluştur veya güncelle: self.app.input_text = str(path)
4. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_RETURN)
5. Yan etki/çağrı adımını çalıştır: self.assertTrue(path.exists())
6. Değeri/alanı oluştur veya güncelle: before = self.app.sim.snapshot()
7. Yan etki/çağrı adımını çalıştır: self.click('new')
8. Yan etki/çağrı adımını çalıştır: self.click('load')
9. Değeri/alanı oluştur veya güncelle: self.app.input_text = str(path)
10. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_RETURN)
11. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.sim.snapshot(), before)
12. Yan etki/çağrı adımını çalıştır: path.write_text('{"schema_version": 999}')
13. Yan etki/çağrı adımını çalıştır: self.click('load')
14. Değeri/alanı oluştur veya güncelle: self.app.input_text = str(path)
15. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_RETURN)
16. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.sim.snapshot(), before)
17. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_ESCAPE)
18. Yan etki/çağrı adımını çalıştır: self.click('seed')
19. Değeri/alanı oluştur veya güncelle: self.app.input_text = '123'
20. Yan etki/çağrı adımını çalıştır: self.key(pygame.K_RETURN)
21. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.sim.seed, 123)

**Gerçek kaynak:**

```python
def test_save_load_seed_invalid_load_preserves_scene(self):
        path=Path(self.tmp.name)/"sahne.json"
        self.click("save")
        self.app.input_text=str(path)
        self.key(pygame.K_RETURN)
        self.assertTrue(path.exists())
        before=self.app.sim.snapshot()
        self.click("new")
        self.click("load")
        self.app.input_text=str(path)
        self.key(pygame.K_RETURN)
        self.assertEqual(self.app.sim.snapshot(),before)
        path.write_text('{"schema_version": 999}')
        self.click("load")
        self.app.input_text=str(path)
        self.key(pygame.K_RETURN)
        self.assertEqual(self.app.sim.snapshot(),before)
        self.key(pygame.K_ESCAPE)
        self.click("seed")
        self.app.input_text="123"
        self.key(pygame.K_RETURN)
        self.assertEqual(self.app.sim.seed,123)
```

### UITests.test_panel_controls_and_filters — satır 149

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.app.selected_id, self.app.tab, before
**Bağlandığı işlevler:** self.click, self.assertGreater, self.assertEqual, self.assertTrue, self.app.draw
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: self.app.selected_id = 1
2. Değeri/alanı oluştur veya güncelle: self.app.tab = 'properties'
3. Değeri/alanı oluştur veya güncelle: before = self.app.selected.sensor.battery
4. Yan etki/çağrı adımını çalıştır: self.click('battery_plus')
5. Yan etki/çağrı adımını çalıştır: self.assertGreater(self.app.selected.sensor.battery, before)
6. Yan etki/çağrı adımını çalıştır: self.click('noise_plus')
7. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.selected.sensor.noise_percent, 1)
8. Yan etki/çağrı adımını çalıştır: self.click('step')
9. Yan etki/çağrı adımını çalıştır: self.click('tab_log')
10. Yan etki/çağrı adımını çalıştır: self.click('filter_sensor')
11. Yan etki/çağrı adımını çalıştır: self.click('filter_kind')
12. Yan etki/çağrı adımını çalıştır: self.assertTrue(self.app.filter_selected)
13. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.filter_kind, 'ALERT')
14. Yan etki/çağrı adımını çalıştır: self.app.draw()

**Gerçek kaynak:**

```python
def test_panel_controls_and_filters(self):
        self.app.selected_id=1
        self.app.tab="properties"
        before=self.app.selected.sensor.battery
        self.click("battery_plus")
        self.assertGreater(self.app.selected.sensor.battery,before)
        self.click("noise_plus")
        self.assertEqual(self.app.selected.sensor.noise_percent,1)
        self.click("step")
        self.click("tab_log")
        self.click("filter_sensor")
        self.click("filter_kind")
        self.assertTrue(self.app.filter_selected)
        self.assertEqual(self.app.filter_kind,"ALERT")
        self.app.draw()
```

### UITests.test_source_fire_and_alarm_controls — satır 165

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** self.app.selected_id, self.app.tab, before, self.app.inspector.scroll
**Bağlandığı işlevler:** self.app.replace_sim, lesson_scene, self.click, self.assertIn, self.assertGreater, self.assertEqual, self.assertLessEqual, self.assertFalse
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.app.replace_sim(lesson_scene(4))
2. Değeri/alanı oluştur veya güncelle: self.app.selected_id = 3
3. Değeri/alanı oluştur veya güncelle: self.app.tab = 'properties'
4. Yan etki/çağrı adımını çalıştır: self.click('gas_co2')
5. Yan etki/çağrı adımını çalıştır: self.assertIn(GasMode.CO2, self.app.selected.source.gas_modes)
6. Değeri/alanı oluştur veya güncelle: before = self.app.selected.source.co2_ppm
7. Yan etki/çağrı adımını çalıştır: self.click('co2_ppm_plus')
8. Yan etki/çağrı adımını çalıştır: self.assertGreater(self.app.selected.source.co2_ppm, before)
9. Değeri/alanı oluştur veya güncelle: self.app.selected_id = 1
10. Değeri/alanı oluştur veya güncelle: self.app.inspector.scroll = 0
11. Yan etki/çağrı adımını çalıştır: self.click('channel_CO2')
12. Yan etki/çağrı adımını çalıştır: self.click('threshold_minus')
13. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.selected.sensor.thresholds['CO2'], 4500)
14. Yan etki/çağrı adımını çalıştır: self.click('clear_plus')
15. Yan etki/çağrı adımını çalıştır: self.assertLessEqual(self.app.selected.sensor.clear_thresholds['CO2'], 4500)
16. Yan etki/çağrı adımını çalıştır: self.app.replace_sim(lesson_scene(6))
17. Değeri/alanı oluştur veya güncelle: self.app.selected_id = 1
18. Değeri/alanı oluştur veya güncelle: self.app.tab = 'properties'
19. Yan etki/çağrı adımını çalıştır: self.click('flammable')
20. Yan etki/çağrı adımını çalıştır: self.assertFalse(self.app.selected.flammable)
21. Yan etki/çağrı adımını çalıştır: self.click('ignition_plus')
22. Yan etki/çağrı adımını çalıştır: self.assertEqual(self.app.selected.ignition_temp, 130)

**Gerçek kaynak:**

```python
def test_source_fire_and_alarm_controls(self):
        self.app.replace_sim(lesson_scene(4))
        self.app.selected_id=3;self.app.tab="properties"
        self.click("gas_co2")
        self.assertIn(GasMode.CO2,self.app.selected.source.gas_modes)
        before=self.app.selected.source.co2_ppm
        self.click("co2_ppm_plus")
        self.assertGreater(self.app.selected.source.co2_ppm,before)
        self.app.selected_id=1;self.app.inspector.scroll=0
        self.click("channel_CO2")
        self.click("threshold_minus")
        self.assertEqual(self.app.selected.sensor.thresholds["CO2"],4500)
        self.click("clear_plus")
        self.assertLessEqual(self.app.selected.sensor.clear_thresholds["CO2"],4500)
        self.app.replace_sim(lesson_scene(6))
        self.app.selected_id=1;self.app.tab="properties"
        self.click("flammable")
        self.assertFalse(self.app.selected.flammable)
        self.click("ignition_plus")
        self.assertEqual(self.app.selected.ignition_temp,130)
```

### UITests.test_exception_path_closes_exporter — satır 186

Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.

**Girdiler:** self. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** exporter
**Bağlandığı işlevler:** self.app.action, patch.object, RuntimeError, self.assertRaises, self.app.run, self.assertTrue
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: self.app.action(('play',))
2. Değeri/alanı oluştur veya güncelle: exporter = self.app.exporter
3. Kaynak yaşam süresini with bloğuyla sınırla: patch.object(self.app.sim, 'advance', side_effect=RuntimeError('injected'))
4. Yan etki/çağrı adımını çalıştır: self.assertTrue(exporter.closed)

**Gerçek kaynak:**

```python
def test_exception_path_closes_exporter(self):
        self.app.action(("play",))
        exporter=self.app.exporter
        with patch.object(self.app.sim,"advance",side_effect=RuntimeError("injected")):
            with self.assertRaises(RuntimeError): self.app.run(max_frames=2)
        self.assertTrue(exporter.closed)
```


## tools/build_guide.py

Bu ekin envanterini, kod kesitlerini ve kaynak hash manifestini üretir/kontrol eder.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""Bütün dosyalar ve Python sembolleri için kaynakla eşleşen Türkçe eki üret."""
```

Satır 2: Gereken isimleri içeri al: import argparse

```python
import argparse
```

Satır 3: Gereken isimleri içeri al: import ast

```python
import ast
```

Satır 4: Gereken isimleri içeri al: import hashlib

```python
import hashlib
```

Satır 5: Gereken isimleri içeri al: import json

```python
import json
```

Satır 6: Gereken isimleri içeri al: from pathlib import Path

```python
from pathlib import Path
```

Satır 7: Gereken isimleri içeri al: from urllib.parse import quote

```python
from urllib.parse import quote
```

Satır 9: Değeri/alanı oluştur veya güncelle: ROOT = Path(__file__).resolve().parents[1]

```python
ROOT=Path(__file__).resolve().parents[1]
```

Satır 10: Değeri/alanı oluştur veya güncelle: OUTPUT = ROOT / 'docs' / 'KOD_REHBERI.md'

```python
OUTPUT=ROOT/"docs"/"KOD_REHBERI.md"
```

Satır 11: Değeri/alanı oluştur veya güncelle: MANIFEST = ROOT / 'docs' / 'kod_kapsami.json'

```python
MANIFEST=ROOT/"docs"/"kod_kapsami.json"
```

Satır 12: Değeri/alanı oluştur veya güncelle: EXCLUDE = {'.git', '.venv', 'venv', 'env', '__pycache__', 'exports', 'scenes', '.pytest_cache'}

```python
EXCLUDE={".git",".venv","venv","env","__pycache__","exports","scenes",".pytest_cache"}
```

Satır 13: Değeri/alanı oluştur veya güncelle: ROLES = {'main.py': 'Güncel komut satırı girişidir; iot_sim.app.main işlevine aktarır.', 'CALCULATOR.py': 'Bağımsız nesne yönelimli sensör/olay dersi. Güncel uygulama yalnız RateLimiter sınıfını kullanır.', 'iot_sim/mode…

```python
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
```

Satır 57: Değeri/alanı oluştur veya güncelle: PURPOSES = {'clamp': 'Sayısal değeri alt ve üst sınır arasında tutar; panel ve konum ayarlarında kullanılır.', 'accuracy_for_dist': 'Eski uzaklık tablosundan yüzde döndürür; yeni noktasal ölçüm bunu kullanmaz.', 'tile_oc…

```python
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
```

Satır 313: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__=="__main__":
    main()
```

### source_files — satır 134

Çalışma verilerini hariç tut; gizli eski yedek Python'u kapsa.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** sorted((p for p in ROOT.rglob('*') if p.is_file() and (not any((part in EXCLUDE for part in p.relative_to(ROOT).parts))) and (p.suffix not in ('.pyc', '.pyo'))))
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** sorted, ROOT.rglob, p.is_file, any, p.relative_to
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Çağırana sonucu döndür: sorted((p for p in ROOT.rglob('*') if p.is_file() and (not any((part in EXCLUDE for part in p.relative_to(ROOT).parts))) and (p.suffix not in ('.pyc', '.pyo'))))

**Gerçek kaynak:**

```python
def source_files():
    """Çalışma verilerini hariç tut; gizli eski yedek Python'u kapsa."""
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and not any(part in EXCLUDE for part in p.relative_to(ROOT).parts)
                  and p.suffix not in (".pyc",".pyo"))
```

### role — satır 141

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** path. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** ROLES[rel]; 'Korunan eski/alternatif sürümün özgün ikonudur; yeni assets ile tümü aynı değildir.' if path.suffix == '.png' else 'Korunan eski tek dosyalı simülasyon/yedek. Yeni giriş noktası bu kodu çalıştırmaz; güncel davranış test…; f'{path.stem} nesne türünün özgün PNG ikonu; assets yükleyicisi ve harita çizimi tarafından kullanılır.'; 'Proje yardımcı/belgeleme dosyası; içerik ve bağlı kullanım kaynak dosyasında görülebilir.'
**Atanan yerel değerler / durum alanları:** rel
**Bağlandığı işlevler:** path.relative_to(ROOT).as_posix, path.relative_to, rel.startswith
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: rel = path.relative_to(ROOT).as_posix()
2. Koşula göre yol seç: rel in ROLES
3. Koşula göre yol seç: rel.startswith('IoT PyGame/')
4. Koşula göre yol seç: path.suffix == '.png'
5. Çağırana sonucu döndür: 'Proje yardımcı/belgeleme dosyası; içerik ve bağlı kullanım kaynak dosyasında görülebilir.'

**Gerçek kaynak:**

```python
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
```

### symbols — satır 153

İç işlevleri ve property getter/setterlarını ayrı kaynak konumuyla dolaş.

**Girdiler:** node, parents=(). self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** (qualified, child); symbols(child, (*parents, child.name)); symbols(child, parents)
**Atanan yerel değerler / durum alanları:** qualified
**Bağlandığı işlevler:** ast.iter_child_nodes, isinstance, '.'.join, symbols
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Her öğe için işle: child ← ast.iter_child_nodes(node)

**Gerçek kaynak:**

```python
def symbols(node, parents=()):
    """İç işlevleri ve property getter/setterlarını ayrı kaynak konumuyla dolaş."""
    for child in ast.iter_child_nodes(node):
        if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            qualified=".".join((*parents,child.name))
            yield qualified,child
            yield from symbols(child,(*parents,child.name))
        else:
            yield from symbols(child,parents)
```

### local_nodes — satır 164

Bir işlevin kendi gövdesini dolaş; iç işlevin etkilerini ona yükleme.

**Girdiler:** node. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** node; local_nodes(child)
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** ast.iter_child_nodes, isinstance, local_nodes
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Yan etki/çağrı adımını çalıştır: (yield node)
2. Her öğe için işle: child ← ast.iter_child_nodes(node)

**Gerçek kaynak:**

```python
def local_nodes(node):
    """Bir işlevin kendi gövdesini dolaş; iç işlevin etkilerini ona yükleme."""
    yield node
    for child in ast.iter_child_nodes(node):
        if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and child is not node:
            continue
        yield from local_nodes(child)
```

### short — satır 173

Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.

**Girdiler:** node, limit=220. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** text if len(text) <= limit else text[:limit] + '…'
**Atanan yerel değerler / durum alanları:** text
**Bağlandığı işlevler:** ast.unparse(node).replace, ast.unparse, len
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: text = ast.unparse(node).replace('\n', ' ')
2. Çağırana sonucu döndür: text if len(text) <= limit else text[:limit] + '…'

**Gerçek kaynak:**

```python
def short(node,limit=220):
    text=ast.unparse(node).replace("\n"," ")
    return text if len(text)<=limit else text[:limit]+"…"
```

### purpose — satır 178

Kaynak docstring'ini öncele; ortak yöntemlerin öğretici anlamını tamamla.

**Girdiler:** node. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** ' '.join(doc.split()); PURPOSES[name]; 'Birlikte değişen durum alanlarını veri sınıfında toplar; her örnek kendi değerlerini taşır. Alan varsayılanları aşağıdaki kodda açıklanır.'; 'İlgili durum ve davranışları tek sınıf altında toplar. Alanlar, üst sınıflar ve her yöntemin giriş/çıkışı aşağıda ayrı gösterilir.'; 'Adında belirtilen kullanıcı/model davranışını bağımsız başlangıçla çalıştırır; aşağıdaki assert ifadeleri beklenen sonucu ve hata sınırını tanımlar.'; 'Panelden gelen değişimi ilgili özelliğe uygular; varsa clamp/min/max ile değer sınırını korur. Bu eski/yerel eylemin hangi alanı değiştirdiği atamalar bölümünde gösterilir.'; 'İlgili görünüm/mod seçimini tersine çevirir veya seçili kümeye ekler/çıkarır; yeniden çizimde yeni durum görünür.'; 'Veriyi Pygame çizim komutlarıyla ekrana aktarır; koordinatlar, renkler ve koşullu görünürlük aşağıdaki akışta belirlenir.'; 'Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.'
**Atanan yerel değerler / durum alanları:** doc, name
**Bağlandığı işlevler:** ast.get_docstring, ' '.join, doc.split, isinstance, any, name.startswith
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: doc = ast.get_docstring(node)
2. Koşula göre yol seç: doc
3. Değeri/alanı oluştur veya güncelle: name = node.name
4. Koşula göre yol seç: name in PURPOSES
5. Koşula göre yol seç: isinstance(node, ast.ClassDef)
6. Koşula göre yol seç: name.startswith('test_')
7. Koşula göre yol seç: name.startswith('set_')
8. Koşula göre yol seç: 'toggle' in name
9. Koşula göre yol seç: name.startswith('draw_')
10. Çağırana sonucu döndür: 'Bu yerel yardımcı kendisini içeren akışın bir adımını yerine getirir; girdileri, çağırdığı parçalar, değişen alanlar ve dönüş/hata yolları aşağıda kaynakla birlikte gösterilir.'

**Gerçek kaynak:**

```python
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
```

### step_description — satır 201

Gövdenin üst düzey adımlarını gerçek ifadeler üzerinden açıkla.

**Girdiler:** stmt. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** 'Değeri/alanı oluştur veya güncelle: ' + short(stmt); 'Koşula göre yol seç: ' + short(stmt.test); 'Her öğe için işle: ' + short(stmt.target) + ' ← ' + short(stmt.iter); 'Koşul sürdükçe yinele; gövdedeki ilerleme/çıkışa dikkat et: ' + short(stmt.test); 'Çağırana sonucu döndür: ' + (short(stmt.value) if stmt.value else 'None'); 'Geçersiz durumu hata olarak bildir: ' + short(stmt.exc); 'Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.'; 'Kaynak yaşam süresini with bloğuyla sınırla: ' + ', '.join((short(i.context_expr) for i in stmt.items)); 'Yerel yardımcı tanımla: ' + stmt.name + '; ayrı sembol kaydı aşağıdadır.'; 'Yan etki/çağrı adımını çalıştır: ' + short(stmt.value); 'Gereken isimleri içeri al: ' + short(stmt); 'Döngü akışını değiştir: ' + short(stmt); 'Beklenen sonucu doğrula: ' + short(stmt.test); None
**Atanan yerel değerler / durum alanları:** Doğrudan atama yok.
**Bağlandığı işlevler:** isinstance, short, ', '.join
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Koşula göre yol seç: isinstance(stmt, (ast.Assign, ast.AnnAssign, ast.AugAssign))
2. Koşula göre yol seç: isinstance(stmt, ast.If)
3. Koşula göre yol seç: isinstance(stmt, (ast.For, ast.AsyncFor))
4. Koşula göre yol seç: isinstance(stmt, ast.While)
5. Koşula göre yol seç: isinstance(stmt, ast.Return)
6. Koşula göre yol seç: isinstance(stmt, ast.Raise)
7. Koşula göre yol seç: isinstance(stmt, ast.Try)
8. Koşula göre yol seç: isinstance(stmt, (ast.With, ast.AsyncWith))
9. Koşula göre yol seç: isinstance(stmt, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef))
10. Koşula göre yol seç: isinstance(stmt, ast.Expr) and (not isinstance(stmt.value, ast.Constant))
11. Koşula göre yol seç: isinstance(stmt, (ast.Import, ast.ImportFrom))
12. Koşula göre yol seç: isinstance(stmt, (ast.Break, ast.Continue))
13. Koşula göre yol seç: isinstance(stmt, ast.Assert)
14. Çağırana sonucu döndür: None

**Gerçek kaynak:**

```python
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
```

### render — satır 232

Dosya haritası, bütün semboller ve tam kod kesitlerini deterministik üret.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** ('\n'.join((line.rstrip() for line in '\n'.join(lines).splitlines())).rstrip() + '\n', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
**Atanan yerel değerler / durum alanları:** paths, lines, manifest, rel, source, tree, manifest['sources'][rel], segment, entry, bases, body, code, args, own, returns, yields, raises, targets, calls, descriptions
**Bağlandığı işlevler:** source_files, paths.append, paths.sort, path.relative_to(ROOT).as_posix, path.relative_to, lines.append, quote, role, path.exists, path.read_text, ast.parse, hashlib.sha256(source.encode()).hexdigest, hashlib.sha256, source.encode, isinstance, ast.get_source_segment, step_description, symbols, type, manifest['symbols'].append, purpose, ', '.join, short, '\n'.join, ast.unparse, list, local_nodes, targets.extend, targets.append, dict.fromkeys, '; '.join, lines.extend, enumerate, len, '\n'.join((line.rstrip() for line in '\n'.join(lines).splitlines())).rstrip, line.rstrip, '\n'.join(lines).splitlines, json.dumps
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: paths = source_files()
2. Her öğe için işle: future ← (OUTPUT, MANIFEST)
3. Yan etki/çağrı adımını çalıştır: paths.sort()
4. Değeri/alanı oluştur veya güncelle: lines = ['# Kaynakla eşleşen dosya, sınıf ve fonksiyon rehberi', '', '[Ana öğretici rehbere dön](../PROJE_REHBERI.md). Bu ek tools/build_guide.py ile üretilir.', 'Kaynak kesitleri gerçek dosyalardan alınır; gösterimde ya…
5. Değeri/alanı oluştur veya güncelle: manifest = {'sources': {}, 'symbols': []}
6. Her öğe için işle: path ← paths
7. Her öğe için işle: path ← paths
8. Değeri/alanı oluştur veya güncelle: lines += ['', '## Yenileme ve kapsam kontrolü', '', f'Bu üretimde {len(manifest['sources'])} Python dosyası ve {len(manifest['symbols'])} sınıf/fonksiyon konumu kapsanır.', 'Kaynak değişince python -B tools/build_guide.p…
9. Çağırana sonucu döndür: ('\n'.join((line.rstrip() for line in '\n'.join(lines).splitlines())).rstrip() + '\n', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

**Gerçek kaynak:**

```python
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
```

### main — satır 297

Komut seçeneklerini/başlangıç nesnelerini kurup programın ana akışını başlatır.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** parser, args, (content, manifest)
**Bağlandığı işlevler:** argparse.ArgumentParser, parser.add_argument, parser.parse_args, render, OUTPUT.exists, MANIFEST.exists, OUTPUT.read_text, MANIFEST.read_text, SystemExit, print, OUTPUT.parent.mkdir, OUTPUT.write_text, MANIFEST.write_text
**Açık hata yolları:** SystemExit('Kaynak rehberi güncel değil: python -B tools/build_guide.py')

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: parser = argparse.ArgumentParser()
2. Yan etki/çağrı adımını çalıştır: parser.add_argument('--check', action='store_true')
3. Değeri/alanı oluştur veya güncelle: args = parser.parse_args()
4. Değeri/alanı oluştur veya güncelle: content, manifest = render()
5. Koşula göre yol seç: args.check

**Gerçek kaynak:**

```python
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
```


## tools/verify_runtime.py

Altı sahne ekranı, X11/SDL sürücü bilgisi ve eğitim ölçeğinde performans üretir.

### Dosya düzeyindeki kod

Satır 1: Modül açıklaması / sabit tanım.

```python
"""SDL pencere denemesi, altı ekran ve sınırlı eğitim sahnesi performansı."""
```

Satır 2: Gereken isimleri içeri al: import argparse

```python
import argparse
```

Satır 3: Gereken isimleri içeri al: import hashlib

```python
import hashlib
```

Satır 4: Gereken isimleri içeri al: import json

```python
import json
```

Satır 5: Gereken isimleri içeri al: import os

```python
import os
```

Satır 6: Gereken isimleri içeri al: import platform

```python
import platform
```

Satır 7: Gereken isimleri içeri al: import resource

```python
import resource
```

Satır 8: Gereken isimleri içeri al: import statistics

```python
import statistics
```

Satır 9: Gereken isimleri içeri al: import sys

```python
import sys
```

Satır 10: Gereken isimleri içeri al: import time

```python
import time
```

Satır 11: Gereken isimleri içeri al: from pathlib import Path

```python
from pathlib import Path
```

Satır 12: Değeri/alanı oluştur veya güncelle: ROOT = Path(__file__).resolve().parents[1]

```python
ROOT=Path(__file__).resolve().parents[1]
```

Satır 13: Yan etki/çağrı adımını çalıştır: sys.path.insert(0, str(ROOT))

```python
sys.path.insert(0,str(ROOT))
```

Satır 14: Yan etki/çağrı adımını çalıştır: os.environ.setdefault('SDL_AUDIODRIVER', 'dummy')

```python
os.environ.setdefault("SDL_AUDIODRIVER","dummy")
```

Satır 15: Yan etki/çağrı adımını çalıştır: os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')

```python
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT","1")
```

Satır 16: Gereken isimleri içeri al: import pygame

```python
import pygame
```

Satır 17: Gereken isimleri içeri al: from iot_sim.app import App

```python
from iot_sim.app import App
```

Satır 18: Gereken isimleri içeri al: from iot_sim.models import *

```python
from iot_sim.models import *
```

Satır 19: Gereken isimleri içeri al: from iot_sim.scene import to_scene

```python
from iot_sim.scene import to_scene
```

Satır 20: Gereken isimleri içeri al: from iot_sim.lessons import lesson_scene

```python
from iot_sim.lessons import lesson_scene
```

Satır 21: Gereken isimleri içeri al: from iot_sim.render import FIELD_CACHE

```python
from iot_sim.render import FIELD_CACHE
```

Satır 98: Koşula göre yol seç: __name__ == '__main__'

```python
if __name__=="__main__":
    main()
```

### benchmark_scene — satır 24

30 sensör, 10 kaynak, 3 drone; öğretici ölçekte tekrarlanabilir yük.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** to_scene(entities)
**Atanan yerel değerler / durum alanları:** entities, x
**Bağlandığı işlevler:** range, entities.append, Entity, SensorProps, SourceProps, UavProps, to_scene
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: entities = []
2. Her öğe için işle: i ← range(30)
3. Her öğe için işle: i ← range(10)
4. Her öğe için işle: i ← range(3)
5. Çağırana sonucu döndür: to_scene(entities)

**Gerçek kaynak:**

```python
def benchmark_scene():
    """30 sensör, 10 kaynak, 3 drone; öğretici ölçekte tekrarlanabilir yük."""
    entities=[]
    for i in range(30):
        entities.append(Entity(i+1,Kind.SENSOR,5+2*(i%10),6+2*(i//10),
                               sensor=SensorProps(),name=f"S{i+1}"))
    for i in range(10):
        entities.append(Entity(31+i,Kind.SOURCE,5+2*i,18,source=SourceProps()))
    for i in range(3):
        x=5+6*i
        entities.append(Entity(41+i,Kind.UAV,x,22,
            uav=UavProps(x=x,y=22,route=[(x,22),(x,26)])))
    return to_scene(entities)
```

### main — satır 39

Komut seçeneklerini/başlangıç nesnelerini kurup programın ana akışını başlatır.

**Girdiler:** Parametre yok. self varsa üzerinde işlem yapılan örnektir.
**Çıktı:** Açık return yok: None. Etki atama, çizim, dosya veya çağrılan işlem üzerinden oluşur.
**Atanan yerel değerler / durum alanları:** parser, args, app, app.toast, report, report['source_sha256'], captures, app.tab, app.show_field, path, report['lessons'], durations, start, report['benchmark'], e.source.range_tiles, app.sim.revision, app.cam.zoom, report['maximum_radius'], report['peak_rss_mib']
**Bağlandığı işlevler:** argparse.ArgumentParser, parser.add_argument, parser.parse_args, args.output.mkdir, App, platform.python_version, platform.platform, pygame.display.get_driver, p.relative_to(ROOT).as_posix, p.relative_to, hashlib.sha256(p.read_bytes()).hexdigest, hashlib.sha256, p.read_bytes, sorted, ROOT.glob, Path(__file__).resolve, Path, range, app.replace_sim, lesson_scene, app.begin_recording, app.sim.advance, app.draw, pygame.image.save, captures.append, dict, sum, len, app.sim.history.values, benchmark_scene, app.focus_scene, time.perf_counter, pygame.event.pump, durations.append, statistics.median, int, max, resource.getrusage, app.close_recording, pygame.quit, (args.output / 'runtime.json').write_text, json.dumps, print
**Açık hata yolları:** Bu gövdede açık raise yok; çağrılan işlevlerden hata gelebilir.

**İşleyiş sırası:**

1. Değeri/alanı oluştur veya güncelle: parser = argparse.ArgumentParser()
2. Yan etki/çağrı adımını çalıştır: parser.add_argument('--output', type=Path, required=True)
3. Değeri/alanı oluştur veya güncelle: args = parser.parse_args()
4. Yan etki/çağrı adımını çalıştır: args.output.mkdir(parents=True, exist_ok=True)
5. Değeri/alanı oluştur veya güncelle: app = App(out_dir=args.output / 'exports', size=(1280, 800))
6. Değeri/alanı oluştur veya güncelle: app.toast = ''
7. Değeri/alanı oluştur veya güncelle: report = {'python': platform.python_version(), 'pygame': pygame.version.ver, 'platform': platform.platform(), 'display_driver': pygame.display.get_driver(), 'interactive_human_test': False}
8. Değeri/alanı oluştur veya güncelle: report['source_sha256'] = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted([*ROOT.glob('iot_sim/*.py'), ROOT / 'CALCULATOR.py', ROOT / 'main.py', Path(__file__).resolve()])}
9. Başarısız olabilecek işi çalıştır; except yollarında hatayı ele al, finally varsa her çıkışta temizle.
10. Yan etki/çağrı adımını çalıştır: (args.output / 'runtime.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
11. Yan etki/çağrı adımını çalıştır: print(json.dumps(report, ensure_ascii=False, indent=2))

**Gerçek kaynak:**

```python
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    app=App(out_dir=args.output/"exports",size=(1280,800))
    app.toast=""
    report={"python":platform.python_version(),"pygame":pygame.version.ver,"platform":platform.platform(),
            "display_driver":pygame.display.get_driver(),"interactive_human_test":False}
    report["source_sha256"]={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in sorted([*ROOT.glob("iot_sim/*.py"),ROOT/"CALCULATOR.py",ROOT/"main.py",Path(__file__).resolve()])}
    try:
        captures=[]
        for number in range(1,7):
            app.replace_sim(lesson_scene(number))
            app.tab="lesson"
            app.begin_recording()
            app.sim.advance(10)
            app.show_field=True
            app.toast=""
            app.draw()
            path=args.output/f"deney-{number}.png"
            pygame.image.save(app.screen,path)
            captures.append(dict(lesson=number,seconds=app.sim.time,events=app.sim.alarm.total_events,
                                 samples=sum(len(h) for h in app.sim.history.values()),image=path.name))
        report["lessons"]=captures
        app.replace_sim(benchmark_scene())
        app.tab="properties"
        app.show_field=True
        app.focus_scene()
        durations=[]
        for _ in range(150):
            start=time.perf_counter()
            app.sim.advance(1/30)
            app.draw()
            pygame.event.pump()
            durations.append((time.perf_counter()-start)*1000)
        report["benchmark"]={"sensors":30,"sources":10,"drones":3,"frames":150,
            "includes_model_and_drawing":True,"theoretical_layer":True,
            "median_ms":statistics.median(durations),"p95_ms":sorted(durations)[int(len(durations)*.95)],
            "max_ms":max(durations),"cache_bytes":FIELD_CACHE.bytes,"cache_limit_bytes":FIELD_CACHE.limit}
        for e in app.sim.entities:
            if e.source: e.source.range_tiles=80
        app.sim.revision+=1
        app.cam.zoom=3.5
        start=time.perf_counter()
        app.draw()
        report["maximum_radius"]={"source_range":80,"zoom":3.5,"frame_ms":(time.perf_counter()-start)*1000,
                                 "cache_bytes":FIELD_CACHE.bytes}
        assert FIELD_CACHE.bytes<=FIELD_CACHE.limit
        report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
        pygame.image.save(app.screen,args.output/"kalabalik-sahne.png")
    finally:
        app.close_recording()
        pygame.quit()
    (args.output/"runtime.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))
```


## Yenileme ve kapsam kontrolü

Bu üretimde 32 Python dosyası ve 340 sınıf/fonksiyon konumu kapsanır.
Kaynak değişince python -B tools/build_guide.py çalıştır; ardından --check ile aynı kaynak kesitlerinin ve hashlerin korunduğunu doğrula.
