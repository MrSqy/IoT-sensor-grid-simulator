# IoT Grid Simulator

Pygame tabanlı, gerçek zamanlı bir IoT sensör ağı simülasyonu. Sıcaklık ve gaz kaynaklarını haritaya yerleştirin, sensörlerle izleyin, drone'larla taşıyın ve alarm sistemini canlı takip edin.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Özellikler

### Simülasyon Ortamı
- **200×200 tile grid** harita, zoom ve pan desteği
- Gerçek zamanlı fizik: sıcaklık yayılımı (°C), gaz difüzyonu (ppm)
- Yangın yayılım modeli (engeller tutuşabilir)
- ±%5 ölçüm gürültüsü ile gerçekçi sensör davranışı

### Sensör Sistemi
- **4 bağımsız ölçüm modu**: TEMP, CO, CO2, H2
- Çoklu mod seçimi — sadece aktif modlar ölçüm yapar ve limiter hakkı tüketir
- Gerçek dünya eşik değerleri (CO: 35 ppm OSHA TWA, CO2: 5000 ppm, H2: 4000 ppm, Sıcaklık: 60°C)
- Pil tüketim modeli, verimlilik ayarı, menzil kontrolü
- Sensör bazlı rate limiter (limit / max_limit panelden ayarlanabilir)

### Kaynak Sistemi
- **Sıcaklık kaynakları**: Merkez sıcaklık (°C) ayarlanabilir, mesafeyle üstel düşüş
- **Gaz kaynakları**: CO, CO2, H2 modları bağımsız açılıp kapatılabilir
  - Her gaz için ayrı konsantrasyon (ppm) ve menzil (tile) ayarı
  - Mod seçilmezse yayılım sıfır
  - Gaz tipine göre farklı efekt renkleri (CO: kırmızı, CO2: yeşil, H2: mavi)

### Alarm Sistemi (CALCULATOR Entegrasyonu)
- `CALCULATOR.py` modülü ile olay değerlendirme motoru
- Her sensöre özel `RateLimiter` — bağımsız işlem hakkı yönetimi
- `EventEngine` ile ALERT/CALM durumu belirleme (eşik değeri yapılandırılabilir)
- Limiter hakkı bitince: haritada sarı yanıp sönen çerçeve, panelde uyarı, log'a kayıt

### Drone (İHA) Sistemi
- Waypoint tabanlı rota düzenleme (LOOP / PINGPONG modu)
- Sensör ve kaynak taşıma (sürükle-bırak)
- Hız ayarı, rota görselleştirme

### Kullanıcı Arayüzü
- Sağ panel: nesne özellikleri, ölçüm değerleri, alarm durumu
- **Log butonu** (harita sağ üst): tüm sensör/kaynak/drone özeti ve olay logu
- **İsim değiştirme**: her nesneye özel isim verilebilir (uygulama içi input)
- **Taşıma modu** (M tuşu): nesneleri haritada yeniden konumlandırma
- Toast mesajları, rota düzenleme banner'ı

### Veri Dışa Aktarma
- `sensor_log_*.csv`: Tüm sensör ölçümleri (°C, ppm, pil, modlar, limit)
- `alarm_log_*.csv`: Alarm olayları (zaman, sensör, tip, detay)
- `threat_polygons_*.jsonl`: Tehdit bölgesi poligon verileri

## Kurulum

```bash
git clone https://github.com/MrSqy/IoT-Grid-Simulator.git
cd IoT-Grid-Simulator

python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

## Çalıştırma

```bash
python3 main.py
```

## Kontroller

| Tuş / İşlem | Açıklama |
|---|---|
| **Sol tık** | Seç / Araç seçiliyken yerleştir |
| **Sağ tık** | Haritadan sil |
| **DEL / Backspace** | Seçili nesneyi sil |
| **Space** | Simülasyon başlat/durdur |
| **G** | Izgara göster/gizle |
| **M** | Seçili nesneyi taşıma modu |
| **K** | İHA rota düzenleme (İHA seçiliyken) |
| **ESC** | Seçimi/modu iptal |
| **Ctrl + Wheel** | Zoom |
| **Wheel** | Dikey kaydırma |
| **Shift + Wheel** | Yatay kaydırma |

## Proje Yapısı

```
IoT/
├── main.py                 # Giriş noktası
├── CALCULATOR.py           # Olay değerlendirme motoru (EventEngine, RateLimiter, vb.)
├── requirements.txt
├── assets/                 # Sensör, kaynak, drone ikonları (PNG)
├── exports/                # Otomatik oluşturulan CSV/JSONL dosyaları
└── iot_sim/                # Ana simülasyon paketi
    ├── __init__.py
    ├── app.py              # Ana döngü, event handling, çizim
    ├── models.py           # Veri modelleri (Entity, SensorProps, SourceProps, vb.)
    ├── sensors.py          # Fizik motoru: sıcaklık/gaz ölçüm hesabı
    ├── alarm_bridge.py     # CALCULATOR ↔ Sim köprüsü
    ├── panel.py            # Sağ panel UI (build + draw)
    ├── render.py           # Harita çizimi, efektler, göstergeler
    ├── engine.py           # Yardımcı fonksiyonlar (accuracy, bresenham, vb.)
    ├── constants.py        # Sabitler (ekran boyutu, accuracy tablosu, vb.)
    ├── camera.py           # Kamera (zoom, pan, screen↔world dönüşümü)
    ├── cargo.py            # Drone yük taşıma mantığı
    ├── uav.py              # Drone hareket ve rota takibi
    ├── fire.py             # Yangın yayılım modeli
    ├── exporter.py         # CSV/JSONL veri dışa aktarma
    ├── viz.py              # Görsel efektler (gauss field, dashed circle)
    ├── ui_widgets.py       # Panel UI bileşenleri (buton, switch, vb.)
    ├── assets.py           # İkon yükleme ve önbellekleme
    └── geom.py             # Geometri yardımcıları (polygon area, vb.)
```

## Gerçek Dünya Eşik Değerleri

| Parametre | Alarm Eşiği | Tehlike Seviyesi | Kaynak |
|---|---|---|---|
| Sıcaklık | 60°C | 100°C | Yanık riski / kaynar su |
| CO | 35 ppm | 200 ppm | OSHA 8-saat TWA |
| CO₂ | 5,000 ppm | 40,000 ppm | OSHA 8-saat TWA |
| H₂ | 4,000 ppm | 40,000 ppm | %10 LEL (alt patlama limiti) |

## Ekran Görüntüleri

> Proje çalıştırıldıktan sonra ekran görüntülerini `screenshots/` klasörüne ekleyebilirsiniz.

## Katkı ve Kredi

Bu proje **Baran Bey** tarafından tasarlanmış ve geliştirilmiştir. Projenin fikri, konsepti, simülasyon mimarisi ve tüm tasarım kararları kendisine aittir.

Kod yazım sürecinde **Anthropic Claude Opus 4.6** yapay zeka modelinden teknik destek alınmıştır. AI desteği kod implementasyonu, hata düzeltme ve optimizasyon önerileri ile sınırlıdır; projenin fikri mülkiyeti ve yaratıcı yönü tamamen geliştiriciye aittir.

## 📜 Lisans

[MIT](LICENSE) — `2026 Baran Demir B.`
