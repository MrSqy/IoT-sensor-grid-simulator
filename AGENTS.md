# IoT-sensor-grid-simulator — çalışma talimatları

Python/Pygame tabanlı sensör, alarm ve araç davranışı simülasyonu.

## Çalışma sınırı ve ilk adım

- Bu dosya bu reponun kökü ve alt klasörleri için başlangıç talimatıdır. Alt klasörde ek bir `AGENTS.md` varsa ilgili dosyada onu da oku. Üst klasördeki talimatların yeni göreve otomatik taşındığını varsayma.
- Türkçe, sade ve öğretici anlat. Kavramları ihtiyaç doğdukça örneklerle açıkla; başlangıçta uzun bir terim listesi verme.
- Başlarken çalışma klasörünü, dalı, `git status` çıktısını ve uzak adresleri doğrula. Kullanıcının mevcut değişikliklerini koru; temizlik gerekçesiyle reset/clean, veri silme veya geçmişi yeniden yazma yapma.
- Aşağıdaki proje notları 21 Eylül 2026 tarihli başlangıç envanteridir. Ayrıntılı analiz, güncel test sonucu veya eksiksiz mimari belgesi değildir; kaynakla tekrar doğrula.
- Bu görevin kapsamı bu repodur. Kendiliğinden başka repolara geçme veya yeni görev açma. Kullanıcının bu görevde verdiği açık kapsam ve önceki kabul edilmiş kararları esas al.

## Önce inceleme ve ortak karar

- Varsayılan ilk aşama inceleme ve öneridir. README, kaynaklar, bağımlılık/yapılandırmalar, mevcut rehber ve varsa `UYGULAMA_PLANI.md` dosyasını oku. Uygulama talimatı henüz verilmediyse ürün kodu, test veya yapılandırma değişikliği başlatma.
- Projenin amacını, kullanıcı akışını, giriş noktalarını, mimarisini ve verinin hangi bileşenlerden geçtiğini açıkla. Eksik özellik, hata, test boşluğu, debug çıktısı, geçici kod ve bağımlılık konularını incele. Gerekli olduğunda commit geçmişini oku; test/debug commitlerini sırf adından dolayı silme veya geçmişi düzenleme.
- Mevcut kontrolleri çalıştırmadan önce betiklerin yan etkilerini incele. Güvenli kontrolleri yapabilirsin; kaynakları değiştiren otomatik düzeltmeler, gerçek veri üzerinde işlemler veya dış sistemlere yazma bu salt okunur aşamaya dahil değildir.
- Kullanıcıya **projeyi anladığın şekliyle açıklama + öncelikli tavsiye listesi** sun. Her bulguda mümkünse dosya/satır, tekrar üretme adımı, etki, çözüm yönü ve doğrulama yöntemi ver.
- Kanıtlanmış hata, statik inceleme şüphesi, ürün önerisi ve henüz doğrulanmamış davranışı açıkça ayır. Testin geçmesi yalnızca kapsadığı davranışı kanıtlar. Çalıştırmadığın kontrolü başarılı gösterme.
- Kullanıcıyla hangi önerilerin uygulanacağını konuş. Mevcut onayı tekrar isteme; yeni veya genişleyen kapsamı kendiliğinden uygulama.

## Astra planı, Sol uygulaması

- Kullanıcının seçtiği iş paylaşımı: Astra inceleme ve dokümanları hazırlar; Sol, kullanıcı uygulamayı başlattığında kararlaştırılmış değişiklikleri uygular. Bu not kendi başına model ayarı değiştirme veya başka görev başlatma yetkisi vermez.
- İnceleme/planlama görevinin kalıcı çıktısını repo kökündeki tek `UYGULAMA_PLANI.md` dosyasında tut. Mevcut planı önce oku; kullanıcı kararlarını kaybetmeden güncelle. Kullanıcı yalnızca rapor/plan istediyse orada bırak.
- Planda incelenen dal/commit ve tarihi, mevcut sistemi, bulguların kanıtlarını, kabul edilmiş istekleri, henüz öneri olan işleri, açık kararları, etkilenen dosyaları, uygulama sırasını, kabul koşullarını, test senaryolarını ve önerilen commit ayrımını yaz. Önerilen tasarımı mevcut davranış gibi sunma.
- Planın varlığı uygulama izni değildir. Yeni görev farklı dal/worktree açtıysa plan ve yerel dokümanların gerçekten mevcut olduğunu doğrula; eksik bilgiyi tahminle doldurma.
- Uygulama başlatıldığında kararlaştırılan işleri küçük, anlamlı adımlarla yap ve ilgili testlerle doğrula. Test düzeltmesi hatayı örtmemeli; beklenen davranışı kanıtlamalı.
- Commit ve push yalnızca kullanıcının talimatı bunları kapsıyorsa yapılır. Bu `AGENTS.md` dosyasının hazırlanmış olması commit/push onayı değildir. Yetki varsa yeni onay döngüleri yaratmadan kapsamı tamamla.
- Teslimde değişen davranışı, çalıştırılan kontrolleri, sonuçlarını ve doğrulanamayan noktaları açıkça bildir.

## İş sonunda ayrıntılı Türkçe proje rehberi

- Son kodla eşleşen kapsamlı bir öğretici rehber hazırla. Uygun mevcut rehberi güncelle; yoksa `PROJE_REHBERI.md` oluştur. README üzerinden erişilebilir kıl.
- Okuyucunun projeyi ve teknolojileri hiç bilmediğini varsay. Terimleri ilk kullanımlarında sade açıklama ve somut örnekle öğret; okuyucuyu yalnızca sözlüğe gönderme.
- Amaç, kullanıcı akışları, kurulum, çalıştırma, mimari, veri akışı ve bileşen ilişkilerini anlat.
- Projeye ait **her dosya ve klasörün** amacını, içeriğini, kim tarafından kullanıldığını ve diğer dosyalarla bağını haritala. Yapılandırma, bağımlılık, test, otomasyon ve yardımcı betikleri de kapsa. Dış bağımlılıklar ve üretilen dosyalar için rol, elde etme ve güncelleme yöntemini belirt.
- Projeye ait **tüm fonksiyonları, sınıfları ve dosya düzeyindeki kod bloklarını** açıkla: girdiler, çıktılar, durum değişiklikleri, olaylar, hata yolları ve algoritmalar. Öğrenmek için gerekli yerlerde gerçek kod üzerinden adım adım ve satır satır anlat.
- Baştan sona örnek senaryolarla bir eylemin hangi dosya ve fonksiyonlardan geçtiğini göster. Gerektiğinde şema ve küçük örnekler kullan. Kod içermeyen depolarda kapsamı gerçek içerikle eşleştir; var olmayan kod veya kurulum anlatma.
- Testlerin neyi doğruladığını, nasıl çalıştırıldığını, hata ayıklamayı, bilinen sınırlamaları ve güvenli geliştirme adımlarını açıkla. Otomatik/statik kontrol ile gerçek arayüz/donanım doğrulamasını ayır.
- Teslimden önce rehberin dosya kapsamını, komutlarını, bağlantılarını ve kod alıntılarını güncel kaynakla karşılaştır. Sonraki değişikliklerde de rehberi güncel tut.

## Bu repoya özel başlangıç notları

- Başlangıç haritası: `main.py`, `iot_sim/app.py`, `iot_sim/`, `requirements.txt`, `CALCULATOR.py` ve `assets/`.
- `IoT PyGame/` adlı eski/alternatif kaynak klasörünün rolünü incele; güncel giriş noktasıyla karıştırma veya kendiliğinden silme.
- Sensör güncellemesi, alarm geçişleri, araç hareketi, taşıma ve dışa aktarım akışlarını incele. Kare hızından bağımsız zaman hesabı, eşikler, koordinatlar ve tekrar üretilebilirlik araştırma başlıklarıdır.
- CSV/log çıktılarının nereye yazıldığını belirle; denemelerde kullanıcı sonuçlarını ezme.
- Ekranda çalışan simülasyon ile gerçek sensör/donanım ve bilimsel model doğrulamasını ayır. README açıklamaları fiziksel doğruluğu tek başına kanıtlamaz.
- Hazırlıkta tanımlı test klasörü görülmedi. Mevcut altyapıyı doğruladıktan sonra otomatik ve elle kontrol edilecek davranışları öner.

### Rehber başlangıcı

Mevcut README'yi incele; kapsamlı ayrı rehber yoksa uygulama sonunda `PROJE_REHBERI.md` oluştur.
