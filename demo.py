import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()  # Tracker seçimi
tracking_active = False  # Takip durumu

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Takip aktifse güncelle
    if tracking_active:
        success, bbox = tracker.update(frame)
        if success:
            x, y, w, h = [int(v) for v in bbox]
            # Dikdörtgen çiz
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Bilgi metni
            cv2.putText(frame, "TAKIP AKTIF", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow("Nesne Takip Sistemi", frame)

    # Klavye kontrolleri
    key = cv2.waitKey(1)
    if key == ord('s'):
        # Fareyle dikdörtgen seçimi
        bbox = cv2.selectROI("Nesne Takip Sistemi", frame, False)
        if bbox != (0, 0, 0, 0):  # Geçerli seçim kontrolü
            tracker.init(frame, bbox)
            tracking_active = True
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
