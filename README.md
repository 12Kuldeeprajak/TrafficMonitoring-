🚦 Accident Detection & Alert System (YOLOv8 + Telegram Bot).
This project uses YOLOv8 (You Only Look Once) for real-time accident detection in traffic footage.
Whenever an accident is detected, the system automatically sends a Telegram alert with an image snapshot of the detected accident.
🔥 Features

✅ Real-time accident detection from video (mp4) or live camera feed.

✅ Sends Telegram text and photo alerts when an accident is detected.

✅ Uses YOLOv8 custom-trained model (best.pt).

✅ Automatic cooldown system to prevent spamming alerts.

✅ Easy to configure with your Telegram Bot Token & Chat ID.
🛠️ Tech Stack

Python 3.8+

OpenCV
 – For video processing

YOLOv8 (Ultralytics)
 – Object detection

cvzone
 – Easy annotation

Pandas
 – Data handling

Telegram Bot API
 – For alerts

📂 Folder Structure
TrafficMonitoring-/
│── main1.py                # Main accident detection + Telegram alert code
│── best.pt                # YOLOv8 trained model
│── cr.mp4                 # Sample input video
│── coco1.txt              # Class labels
│── yolov8_object_detection_on_custom_dataset.ipynb  # Training notebook
│── requirements.txt       # Python dependencies
│── README.md              # Documentation

▶️ Usage

1.Edit main.py
Replace your Telegram Bot Token and Chat ID in the code:

API_TOKEN = 'your_bot_token_here'
CHAT_ID = 'your_chat_id_here'


2.Run the script
python main.py

3.Output
Accident detected → 🚨 Alert sent to Telegram with image snapshot.

Accident cleared → Detection resets and waits for next accident.

📸 Example Alert

When an accident is detected:

🚨 Accident Detected! Please take action.
📸 <img width="452" height="689" alt="image" src="https://github.com/user-attachments/assets/5769c778-3951-4690-88ff-5c6fd6651f3b" />


🚀 Future Improvements

 Integrate with live CCTV streams.

 Add GPS location in Telegram alert.

 Deploy on edge devices (Raspberry Pi, Jetson Nano).

 Improve accuracy with more training data.

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

📜 License

This project is licensed under the MIT License.
