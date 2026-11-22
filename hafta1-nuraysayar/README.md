# Hafta 1 - B Grubu Görüntü İşleme Alıştırmaları

## 1. Alıştırma: Canny Kenar Tespiti ve Parametre Gözlemleri
* **Eşik Değerleri (`Canny`):** `30, 100` gibi düşük eşik değerlerinde meyve dokuları ve gölgeler dahil çok fazla ince detay (gürültü) kenar olarak algılandı. `200, 300` gibi yüksek eşik değerlerinde ise yalnızca en belirgin dış sınırlar kaldı. En dengeli sonuç `100, 200` aralığında elde edildi.
* **Bulanıklaştırma (`GaussianBlur`):** Çekirdek boyutu `(5, 5)` iken gürültüler temizlenip net kenarlar korundu. Çekirdek boyutu `(51, 51)` yapıldığında görüntü aşırı yumuşadığı için gradyan geçişleri sıfırlandı ve kenar tespiti çıktısı tamamen siyah oldu.

## 2. Alıştırma: Canlı Kamera Kenar Tespiti
* `cv2.VideoCapture(0)` ve `while` döngüsü kullanılarak kameradan alınan kareler gerçek zamanlı olarak gri tonlamaya çevrildi, bulanıklaştırıldı ve canlı Canny kenar tespiti uygulandı.

## 3. Alıştırma: HSV Renk Maskeleme
* Görüntü BGR uzayından HSV uzayına dönüştürüldü. Kırmızı renk için çift aralık (`0-10` ve `170-180`) tanımlanarak kırmızı nesneleri beyaz (`255`), geri kalan tüm bölgeleri siyah (`0`) yapan ikili maske (`kirmizi_maske.jpg`) üretildi.
