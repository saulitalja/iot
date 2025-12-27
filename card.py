from smartcard.System import readers
from smartcard.Exceptions import NoCardException
import time

def main():
    r = readers()
    if not r:
        print("❌ Kortinlukijaa ei löydy")
        return

    reader = r[0]
    print(f"✅ Käytetään lukijaa: {reader}")

    connection = reader.createConnection()

    print("🔄 Odotetaan korttia... (Ctrl+C lopettaa)")
    while True:
        try:
            connection.connect()
            atr = connection.getATR()
            print("🎉 Kortti havaittu!")
            print("📇 ATR:", " ".join(f"{b:02X}" for b in atr))
            break
        except NoCardException:
            time.sleep(0.5)

if __name__ == "__main__":
    main()
