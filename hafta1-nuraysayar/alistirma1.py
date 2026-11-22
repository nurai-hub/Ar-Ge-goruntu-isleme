import cv2

# 1) Görüntüyü oku ve boyutunu yazdır (Klasörde 'test.jpg' adında bir fotoğraf olmalı)
img = cv2.imread('test.jpg')
print('Boyut (yukseklik, genislik, kanal):', img.shape)

# 2) Gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3) Bulanıklaştır (gürültüyü azaltır)
blur = cv2.GaussianBlur(gray, (21, 21), 0)

# 4) Kenarları bul (alt ve üst eşik değerleri: 100 ve 200)
edges = cv2.Canny(blur, 30, 100)
    
# 5) Sonucu kaydet ve ekranda göster
cv2.imwrite('sonuc_30_100.jpg', edges)
cv2.imshow('Kenarlar', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()