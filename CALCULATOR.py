import datetime
import time
from enum import Enum

class Logger: # Klasik logger sınıfı

    def __init__(self):
        self._records = [] # Kayıt edilecek mesajların bulunacağı liste

    def Clog(self, msg: str) -> None: # Mesajı ekrana basan fonksiyon
        print(f"{msg}")
    
    def Mlog(self, msg: str) -> None: # Mesajı kayıtlara yazan fonksiyon
        if len(self._records) >= 100:
            self._records = self._records[1:] # 101 adet kayıt sonrasında eski kayıtlar silinir
        self._records.append(msg)
    
    def get_records(self) -> list: # Kayıtları döndüren fonksiyon
        return list(self._records)


class RateLimiter:

    def __init__(self, n: int):
    
        if not isinstance(n, int):
            raise TypeError("İşlem hakkı için yanlış veri tipi girildi")

        self.max_remaining = n # İşlem hakkı sayısının sıfırlanacağı sabit değeri tutan değişken
        self.remaining = n # İşlem hakkı sayısının tutulacağı değişken
        self.window_seconds = 60 # İşlem hakkı sayısının sıfırlanması için geçmesi gereken süreyi tutan değişken
        self.setTime = datetime.datetime.now() # İşlem hakkı sayısının atandığı ilk süreyi tutan değişken
        self.delta = 0 # İşlem hakkı sayısının sıfırlanmasına kalan süreyi tutan değişken

    @property
    def remaining(self) -> int: # Gizli işlem hakkı sayısını döndüren fonksiyon protokolü 
        return self._remaining

    @remaining.setter
    def remaining(self, n: int) -> None: # Gizli işlem hakkı sayısını ayarlayan fonksiyon protokolü
        if not isinstance(n, int):
            raise TypeError("İşlem hakkı için yanlış veri tipi girildi")
        if n < 0:
            raise ValueError("İşlem hakkı negatif olamaz")
        self._remaining = n

    def allow(self) -> bool: # İşlem hakkı var mı yok mu test eder
        currentTime = datetime.datetime.now() 
        self.delta = (currentTime - self.setTime).total_seconds()

        if self.delta >= self.window_seconds:
            self.remaining = self.max_remaining
            self.setTime = currentTime
        if self.remaining <= 0:
            return False
        self.remaining -= 1
        return True

    def __call__(self) -> bool: # Nesne çağrılırsa yapılacak fonksiyonu işaret eder
        return self.allow()


class EventType(str, Enum): # Olay tipi için ayarlanan bir sınıf
    CALM = "CALM"
    ALERT = "ALERT"


class SensorKind(str, Enum): # Olay adı için ayarlanan bir sınıf
    GAS = "GAS"
    TEMP = "TEMP"


class Event:

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


class Sensor:

    def __init__(self, raw: float, name: str, kind: SensorKind, min_deger = 0,max_deger = 100): 
        # temp için 0-100, gas için 0-100 o yüzden direkt değerler girildi. 
        # Farklı olmaları durumunda sensör tanımlama kısmında değerler verilebilir.
        if not isinstance(kind, SensorKind): 
            raise TypeError("Hatalı alarm ismi girildi")
        self.kind = kind
        self._min_deger = min_deger
        self._max_deger = max_deger
        self.name = name # Sensörün adını (kodunu) tutan değişken
        self.raw = raw # Sensörün ham (işlenmemiş) değerini tutan değişken


    @property 
    def raw(self) -> float: # Gizli ham değeri döndüren fonksiyon
        return self._raw 

    @raw.setter 
    def raw(self, x: float) -> None:
        if not (isinstance(x, float) or isinstance(x, int)):
            raise TypeError("Hatalı ham değer tipi girildi")
        if not self._min_deger <= x <= self._max_deger: 
            raise ValueError("Ölçülen ham değer için hatalı değer girildi")
        self._raw = float(x) # Gizli ham değeri ayarlayan fonksiyon protokolü

    @property 
    def name(self) -> str:
        return self._name # Gizli sensör ismini döndüren fonksiyon protokolü

    @name.setter
    def name(self, name: str) -> None: # Gizli sensör ismini ayarlayan fonksiyon protokolü
        if not isinstance(name,str):
            raise TypeError("İsim str olmalı")
        self._name = name
    
    @property
    def kind(self) -> SensorKind:
        return self._kind
    
    @kind.setter
    def kind(self,kind) -> None:
        if not isinstance(kind, SensorKind):
            raise TypeError("Tür tanımsız")
        self._kind = kind

    def __repr__(self) -> str: # Sensör tanımı
        return f"Sensör adı : {self._name}, ölçülen son ham değeri : {self._raw}, min-max aralığı : {self._min_deger}-{self._max_deger}"


class CalibratedSensor(Sensor):

    def __init__(self, sensor: Sensor, offset: float, min_deger = -20, max_deger = 20):
        self._max_deger = max_deger
        self._min_deger = min_deger
        self.sensor = sensor # Kalibre edilecek sensörü tutan değişken
        self.offset = offset # İşlenmemiş değeri işlemek için gereken sapma değerini tutan değişken

    @property
    def name(self) -> str: # Gizli sensör ismini döndüren fonksiyon protokolü
        return self.sensor.name

    @name.setter
    def name(self, name: str) -> None: # Gizli sensör ismini ayarlayan fonksiyon protokolü
        self.sensor.name = name

    @property
    def raw(self) -> float: # Gizli ham veriyi döndüren fonksiyon protokolü
        return self.sensor.raw

    @raw.setter
    def raw(self, x: float) -> None: # Gizli ham veriyi ayarlayan fonksiyon protokolü
        self.sensor.raw = x

    @property 
    def offset(self) -> float: # Gizli sapma değerini döndüren fonksiyon protokolü
        return self._offset

    @offset.setter
    def offset(self, x: float) -> None: # Gizli sapma değerini ayarlayan fonksiyon protokolü
        if not isinstance(x, (int, float)):
            raise TypeError("Offset sayısal olmalı")
        if not self._min_deger <= x <= self._max_deger:
            raise ValueError("Hatalı sapma değeri girildi")
        self._offset = x

    @property 
    def value(self) -> float: # Gizli işlenmiş değeri hesaplayıp döndüren fonksiyon protokolü
        return self.raw + self.offset

    @property
    def kind(self) -> SensorKind:
        return self.sensor.kind

    def __repr__(self) -> str:
        return (f"Sensör adı : {self.name}, ölçülen son işlenmiş değeri : {self.value}, "f"offset : {self.offset}, raw : {self.raw}, offset_aralığı : {self._min_deger}-{self._max_deger}")



class ConsoleNotifier:

    def notify(self, event: Event) -> None: # Alarm durumunu detaylarıyla ekrana bastırır
        Etype = event.Etype.value # Alert durumu
        Ekind = event.Ekind.value # Sensör tipini tutar
        Sname = event.detected_from # Sensör adını tutar
        Evalue = event.Evalue # Sensörün işlenmiş değeri
        Etimestamp = event.Ets # Sensörün ölçüm tarihi

        print(f"DİKKAT ! {Etype} tipli {Ekind} olayı {Sname} kodlu sensör tarafından ölçüldü. {Etimestamp} tarihli ölçülen veri: {Evalue}")


class InMemoryStage:
    def __init__(self):
        self._events = [] # Olayların kaydedileceği depolama birimi

    @property
    def events(self) -> list: # Gizli depolama birimini döndüren fonksiyon protokolü
        return list(self._events)

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

        self._events.append(eventD) # Olaylar sözlük halinde depolama biriminde tutulur


class EventEngine:
    def __init__(self, Csensors: list[Sensor], logger: Logger, storage: InMemoryStage, notifier: ConsoleNotifier, limiter: RateLimiter, threshold: float = 80.0):
        self.Csensors = Csensors # Sensör listesi
        self.logger = logger # Logger nesnesi
        self.storage = storage # InMemoryStage nesnesi
        self.notifier = notifier # ConsoleNotifier nesnesi
        self.limiter = limiter # RateLimiter nesnesi
        self.threshold = threshold # Alarm eşik değeri (varsayılan 80, dışarıdan ayarlanabilir)
        self._limiter_log_cooldown_s = 5 # İşlem hakkı sayısının bitiminin tekrar etmesi için geçmesi gereken süreyi tutan değişken
        self._last_limiter_log_ts = None # İşlem hakkı sayısının bitiminin basıldığı en son tarihi tutan değişken

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