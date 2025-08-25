import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import requests

# 🚨 Telegram Bot Configuration
API_TOKEN = '7819363215:AAHVxsS2k2L7glSPKt3g023_Nex0Y8pdCGI'  # Replace with your bot token
CHAT_ID = '7915582627'  # Replace with your chat ID

# 🚨 Function to send a Telegram text alert
def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Telegram text alert sent!")
        else:
            print("❌ Failed to send text alert:", response.text)
    except Exception as e:
        print("⚠️ Exception while sending text alert:", e)

# 🚨 Function to send a Telegram photo alert
def send_telegram_photo(image_path, caption="🚨 Accident Detected!"):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendPhoto"
    try:
        with open(image_path, 'rb') as photo:
            files = {'photo': photo}
            data = {'chat_id': CHAT_ID, 'caption': caption}
            response = requests.post(url, files=files, data=data)
            if response.status_code == 200:
                print("📸 Telegram photo alert sent!")
            else:
                print("❌ Failed to send photo:", response.text)
    except Exception as e:
        print("⚠️ Exception while sending photo alert:", e)

# Load YOLO model
model = YOLO('best.pt')

# Optional: track mouse position
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# Load video
cap = cv2.VideoCapture('cr.mp4')

# Load class names
with open("coco1.txt", "r") as my_file:
    class_list = my_file.read().split("\n")

count = 0
alert_sent = False
cooldown_frames = 0
cooldown_limit = 90  # Frames to wait before sending next alert

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    accident_detected = False

    for index, row in px.iterrows():
        x1, y1, x2, y2 = map(int, row[:4])
        d = int(row[5])
        c = class_list[d]

        if 'Accident' in c:
            accident_detected = True
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)
        else:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)

    # 🚨 Accident Alert Logic with Image
    if accident_detected:
        if not alert_sent:
            cv2.imwrite("accident.jpg", frame)
            send_telegram_photo("accident.jpg", "🚨 Accident Detected! Please take action.")
            alert_sent = True
            cooldown_frames = 0
        else:
            cooldown_frames += 1
            if cooldown_frames >= cooldown_limit:
                cv2.imwrite("accident.jpg", frame)
                send_telegram_photo("accident.jpg", "🚨 Accident Still Detected! Please act now.")
                cooldown_frames = 0
    else:
        alert_sent = False  # Reset if no accident in current frame

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

