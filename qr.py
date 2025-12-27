import cv2

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Kameraa ei löytynyt")
        return

    detector = cv2.QRCodeDetector()

    print("📷 QR-lukija käynnissä (paina q lopettaaksesi)")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Kamerakuvaa ei saatu")
            break

        data, bbox, _ = detector.detectAndDecode(frame)

        if data:
            print("✅ QR-koodi luettu:", data)

            if bbox is not None:
                for i in range(len(bbox)):
                    p1 = tuple(bbox[i][0])
                    p2 = tuple(bbox[(i + 1) % len(bbox)][0])
                    cv2.line(frame, p1, p2, (0, 255, 0), 2)

        cv2.imshow("QR Reader", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
