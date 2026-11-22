import cv2
import numpy as np

# 1) Görüntüyü oku ve BGR'den HSV renk uzayına çevir
img = cv2.imread('test.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2) Kırmızı renk için alt ve üst HSV sınırlarını belirle
# HSV renk uzayında kırmızı 0-10 ve 170-180 aralıklarında yer alır
alt_kirmizi1 = np.array([0, 120, 70])
ust_kirmizi1 = np.array([10, 255, 255])

alt_kirmizi2 = np.array([170, 120, 70])
ust_kirmizi2 = np.array([180, 255, 255])

# 3) Kırmızı bölgeleri beyaz (255), geri kalanı siyah (0) yapan maskeyi üret
maske1 = cv2.inRange(hsv, alt_kirmizi1, ust_kirmizi1)
maske2 = cv2.inRange(hsv, alt_kirmizi2, ust_kirmizi2)
kirmizi_maske = cv2.bitwise_or(maske1, maske2)

# 4) Maskeyi kaydet ve ekranda göster
cv2.imwrite('kirmizi_maske.jpg', kirmizi_maske)

cv2.imshow('Orijinal Goruntu', img)
cv2.imshow('Kirmizi Maske (Siyah-Beyaz)', kirmizi_maske)

cv2.waitKey(0)
cv2.destroyAllWindows()