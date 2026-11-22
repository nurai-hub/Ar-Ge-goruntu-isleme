import cv2

# Bilgisayarın kamerasını aç (Eğer video dosyası kullanacaksan 0 yerine 'video.mp4' yaz)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera veya video açılamadı.")
    exit()

while True:
    # 1) Kameradan tek bir kare (frame) oku
    ret, frame = cap.read()
    
    # Görüntü okunamazsa veya video bittiyse döngüden çık
    if not ret:
        print("Görüntü akışı sonlandı.")
        break

    # 2) Kareyi gri tonlamaya çevir ve gürültüyü azalt
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3) Canlı kare üzerinde Canny kenar tespiti uygula
    edges = cv2.Canny(blur, 100, 200)

    # 4) Hem orijinal görüntüyü hem kenar tespitini ekranda göster
    cv2.imshow('Orijinal Kamera', frame)
    cv2.imshow('Canli Kenar Tespiti', edges)

    # 5) Klavyeden 'q' tuşuna basıldığında döngüyü kır ve çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()