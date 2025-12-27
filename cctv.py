import cv2
import os
import time

def main():
    # 0 tarkoittaa ensimmäistä USB-kameraa
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kameraa ei löytynyt!")
        return

    # Luo kansio kuville, jos sitä ei ole
    os.makedirs("kuvat", exist_ok=True)
    frame_count = 0
    last_saved_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kuvaa ei voitu lukea")
            break

        # Näytetään videokehys
        cv2.imshow("USB Kamera", frame)

        # Tallenna kuva 10 sekunnin välein
        current_time = time.time()
        if current_time - last_saved_time >= 10:
            filename = f"kuvat/kuva_{frame_count:04d}.png"
            cv2.imwrite(filename, frame)
            print(f"Tallennettu {filename}")
            frame_count += 1
            last_saved_time = current_time

        # Lopeta, kun painetaan 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
