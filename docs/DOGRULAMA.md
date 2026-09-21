# Doğrulama — 21 Eylül 2026

Bu rapor `education-2.0` uygulamasının yerel teslim kontrolüdür. İnceleme başlangıcındaki hatalar ve denemeler `UYGULAMA_PLANI.md` içinde tarihsel olarak korunmuştur. Aşağıdaki test ve X11 çalışma sonuçları ek sağlamlaştırma sonrasında yenilendi; önceki ölçümler planın bölüm 8–9 kayıtlarında korunur.

## Ortam ve kurulabilirlik

- Linux x86_64, Python 3.12.3, Pygame 2.6.1.
- `/tmp/iot-education-20260921-env` altında yeni sanal ortam kuruldu; Pygame PyPI'den indirildi ve burada çalıştırıldı.
- Projede ayrıca `.venv/` oluşturuldu; sabit requirements dosyasından kurulum yapıldı. Paket uyumluluk kontrolü geçti.
- Sınırlandırılmış ortamda ilk denemeler kullanıcı UV cache'inin salt okunur olması ve DNS/X11 erişimi nedeniyle çalışmadı. Ayrı /tmp cache ve izinli indirme/Xvfb çalıştırmalarıyla bunlar çözüldü. Başarısız ilk denemeler başarılı kurulum/arayüz kanıtı sayılmadı.

## Davranış ve arayüz testleri

```bash
SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy .venv/bin/python -B -m unittest discover -s tests -v
xvfb-run -a env SDL_VIDEODRIVER=x11 SDL_AUDIODRIVER=dummy .venv/bin/python -B -m unittest discover -s tests -v
```

**44 test geçti**: 31 model/dosya testi ve 13 Pygame arayüz testi. Son X11 çalıştırması 4,264 saniyede tamamlandı. Grafik testleri atlanmadı.

Kapsam:

- Her kanal için alarm eşiği altı/eşit/üstü; histerezis ve yalnız geçiş kaydı.
- Kota 0 iken alarmın/kaydın devam etmesi; simülasyon saatinde yenileme.
- OFF/EMPTY durumunda boş ölçüm; taşınan cihazın ölçüm ve alarmı.
- Örnekleme sıklığı/kanal sayısıyla pil; teorik değer ve kalibrasyon.
- Aynı tohumla tekrar, farklı kare bölünmeleri ve 0,25×/1×/2×/5× hızda eşdeğer sonuç.
- Tekrarlı duraklarda dönüş, LOOP kapanışı, başlangıç yaklaşımı ve sonradan engel.
- Yük kapasitesi, ortak sağ tık/DEL silmesi, M ile taşıma, sürükle-bırak ve yer yokken atomik indirme.
- Sahne kaydet/yükle; bozuk sahne, NaN, kimlik/referans hataları ve eski sahnenin korunması.
- Ayrı çıktı oturumları, metadata, geçersiz ölçümlerin boş alanları ve hata halinde dosya kapatma.
- Altı deneyin vaat ettiği gözlenebilir ilişkiler: yakınlık, kalibrasyon, pil, bağımsız gaz, hareketli ölçüm ve tutuşma.
- Arayüzde araç ekleme, yeniden adlandırma, dosya/tohum kutuları, rota/iptal, filtreler, kaynak/yangın/eşik kontrolleri, grafik kanalları ve 1024×720 / 1280×800 çizimi.

Ek incelemedeki dokuz regresyon düzeltmelerden önce başarısız çalışarak sorunları yeniden üretti. Yangın zaman damgası, örneklemeden bağımsız tekrar bildirimi, kapatma anının CSV/grafik kaydı, düzenleme sırasında duraklatma, sahne değişiminde yarım girişlerin temizlenmesi, nesne/kimlik/rota sınırı ve büyük sahne kaydında dosya korunması düzeltildi. Ayrıca 500 duraklı geçerli rota taslağının tamamlanması sınandı.

Testler kaynak davranışını düzeltmek yerine hatayı gizleyecek beklentilerle değiştirilmedi. İncelemede kanıtlanan sorunların yeni davranışı doğrudan sınanıyor.

## Gerçek uygulama döngüsü ve görsel kontrol

```bash
xvfb-run -a env SDL_VIDEODRIVER=x11 SDL_AUDIODRIVER=dummy \
  .venv/bin/python -B tools/verify_runtime.py --output /tmp/iot-post-review-runtime
```

Pygame `x11` sürücüsüyle Xvfb üzerinde gerçek pencere/çizim yolu çalıştı. Altı deneyin her biri **10 simülasyon saniyesi** yürütüldü; ölçümler, olaylar ve sonuç dosyaları üretildi. Bu sürelerin insanın 10 saniye boyunca fare kullanması anlamına gelmediğine dikkat et.

| Deney | Sensör örneği / durum kaydı | Olay |
|---|---:|---:|
| 1 Uzaklık | 20 | 6 |
| 2 Gürültü/kalibrasyon | 10 | 3 |
| 3 Pil | 18 | 5 |
| 4 Gazlar | 10 | 3 |
| 5 Drone | 10 | 3 |
| 6 Yangın | 10 | 4 |

Üçüncü deneyde dört kanallı cihazın pili erken bittiği için geçerli örnekler durur; EMPTY geçişi kaydedilir. Sensör CSV her örnek/durum kaydı için dört kanal satırı üretir.

Arayüz görüntülerinde panel başlıklarının, uzun deney açıklamalarının, grafiklerin ve alarm bilgisinin görünümü incelendi. Uzun panel içeriği kendi kaydırma alanında; üst deney kontrolleri sabit. Belgeleme görüntüsü [burada](screenshots/deney-atolyesi.png).

**İnsan tarafından masaüstünde elle kullanım yapılmadı.** Fare/klavye işlemleri gerçek App.process_event yoluna kontrollü olaylar verilerek doğrulandı. Bu kanıt dokunmatik ekran, farklı pencere yöneticisi veya erişilebilirlik kullanımının yerine geçmez.

## Performans

1280×800 pencere, teorik katman açık; 30 sensör, 10 kaynak, 3 drone; 150 kare. Süreler model ilerletme ve ekran çizimini birlikte içerir:

| Ölçüm | Sonuç |
|---|---:|
| Ortanca kare süresi | 23,79 ms |
| Yüzde 95 kare süresi | 35,67 ms |
| En yavaş kare | 46,95 ms |
| Efekt önbelleği | 16.202.880 bayt |
| Önbellek üst sınırı | 16.777.216 bayt (16 MiB) |
| Sürecin tepe RSS belleği | 184,91 MiB |
| Kaynak yarıçapı 80, zoom 3,5 uç ayarında kare | 15,87 ms |

Kaynak yarıçapı büyüdüğünde dev kaynak bitmap'i üretilmedi; önbellek sınırda kaldı. Rapor belirli makine ve X11/Xvfb ortamına aittir; sürekli 60 FPS veya tüm makinelerde aynı kapasite iddiası değildir. 150 karelik ölçüm uzun süreli dayanıklılık testi sayılmaz.

[Ham runtime raporu](runtime.json) ölçülen kaynakların SHA-256 değerlerini de içerir. Rapor dosyası son kaynaklarla karşılaştırıldı.

## Komut satırı ve dokümantasyon

- İlk teslimde yeni sanal ortamla `main.py --lesson 5 --seconds 12 --out-dir /tmp/iot-education-cli-check` çalıştı; 12 simülasyon saniyesi ve ayrı sonuç klasörü üretildi. Son düzeltmelerden sonra proje dışındaki `/tmp` klasöründen mutlak giriş yoluyla `--lesson 2 --seconds 2 --out-dir /tmp/iot-post-review-cli` tekrar çalıştı; 2 simülasyon saniyesi, 3 olay ve ayrı çıktı oturumu doğrulandı.
- Proje dışındaki `/tmp` çalışma klasöründen mutlak giriş yolu hem üç karelik pencere koşusuyla hem iki simülasyon saniyelik CLI deneyiyle kontrol edildi; ikonlar ve varsayılan çıktı yolu proje köküne göre çözülür.
- `tools/build_guide.py --check` geçti: 32 Python dosyası, 354 sınıf/fonksiyon tanımı ve dosya düzeyindeki kod blokları kaynakla eşleşiyor. Bütün 32 dosya AST ile sözdizimi kontrolünden geçti. Ana rehberdeki ölçüm formülü alıntısı da gerçek kaynakla karşılaştırıldı.
- README, ana rehber, kaynak eki, plan ve bu rapordaki **75 yerel bağlantının** hedefleri doğrulandı; kırık bağlantı bulunmadı. Runtime raporundaki 27 kaynak hash değeri güncel dosyalarla eşleşti. `git diff --check` geçti.
- Eski `IoT PyGame/` kaynak/ikonları, özgün `assets/` ve lisans dahil **15 dosyanın** SHA-256 değeri inceleme başlangıcındaki envanterle aynı; içerikleri korundu.

## Doğrulanmayan veya kapsam dışı noktalar

- Windows/macOS canlı çalışma ve insanın masaüstünde elle kullanım testi.
- Gerçek sensör/drone donanımı, MQTT, ağ/servis entegrasyonu.
- Bilimsel yayılım modeli, gerçek pil kalibrasyonu, iş güvenliği veya mevzuat eşikleri.
- Uzun süreli dayanıklılık ve tüm nesne/zoom kombinasyonlarında performans.
- Eski iki alternatif uygulamanın çalışma doğruluğu; yalnız korunma, envanter ve sözdizimi kapsamı vardır.
- Sahne kaydı canlı oturumu aynı RNG ara durumuyla devam ettirmez. Otomatik eylem tekrar oynatma ve geriye sarma yoktur.

İlk uygulama ve commit tesliminden sonra kullanıcı ek geliştirme ve push talep etti. Düzeltmeler testleriyle birlikte iki committe kaydedildi; dokümantasyon ve bu X11 raporu son kaynaklara göre yenilendi. Son SDL dummy koşusu 44 testi 2,254 saniyede, X11 koşusu 4,264 saniyede tamamladı. Push hedefi origin/main; mevcut geçmiş korunur.
