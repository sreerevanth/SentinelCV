‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ **SentinelCV**
>
                                         Turning everyday cameras into intelligent safety systems.



#                                                               DETECTION PROOF


<img width="800" height="411" alt="ezgif com-video-to-gif-converter (1) (1)" src="https://github.com/user-attachments/assets/bef30fa0-f14f-4c89-b8f4-83f0d6dbe07c" />

#
#
#
#




#                                                            TELEGRAM ALERT PROOF
<img width="728" height="854" alt="image" src="https://github.com/user-attachments/assets/51d8fc38-3661-461d-abbf-aa72e042e330" />


**SentinelCV** is a real-time computer vision platform that transforms any CCTV, IP camera, webcam, or video stream into an AI-powered safety monitor.

It starts with its first module — **real-time fall detection** — and is built to grow into a full modular vision-intelligence platform covering industrial safety, surveillance, healthcare, and smart infrastructure.

---

## ✨ Features

- 🚶 Real-time human fall detection
- 📹 Works with CCTV, RTSP streams, USB webcams, and recorded video files
- ⚡ YOLOv8-powered detection pipeline
- 🔔 Instant Telegram alerts the moment a fall is detected
- 🖥️ Lightweight, real-time inference
- 🔧 Built to extend — fall detection is module one, not the whole product

---

## 🎯 Use Cases

| Elderly Care | Hospitals | Smart Homes |
|---|---|---|
| **Warehouses** | **Factories** | **Construction Sites** |
| **Assisted Living** | **Public Surveillance** | |

---

## 🏗️ How It Works

```
Camera Feed (CCTV / RTSP / Webcam / Video File)
        │
        ▼
  Frame Capture
        │
        ▼
  YOLOv8 Detection
        │
        ▼
  Fall Analysis
        │
        ▼
  Alert Engine
        │
        ├── Telegram Notification
        ├── Dashboard (Planned)
        └── Logging
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/sreerevanth/SentinelCV.git
cd SentinelCV
```

Install the core dependencies (OpenCV, Ultralytics, NumPy, python-telegram-bot):

```bash
pip install opencv-python ultralytics numpy python-telegram-bot
```

Run the monitor:

```bash
python complete_monitor.py
```

> 📌 Set up your Telegram bot token and chat ID first — see `telegram bot details` in this repo for the setup steps used by `notification_alert_test.py`.

---

## 📂 Project Structure

```
SentinelCV/
├── complete_monitor.py         # Main fall detection + monitoring pipeline
├── video_test.py                # Run detection against a video file
├── test.py                      # Detection pipeline testing
├── download_dataset.py          # Fetch/prepare training data
├── notification_alert_test.py   # Telegram alert integration test
├── telegram bot details         # Telegram bot setup notes
└── .gitignore
```

*(A `requirements.txt`, trained model weights, and a proper `src/` layout are on the way — see [Roadmap](#-roadmap).)*

---

## 🧠 Tech Stack

- **Python**
- **OpenCV** — video capture & frame processing
- **Ultralytics YOLOv8** — object/pose detection
- **NumPy**
- **Telegram Bot API** — real-time alerting

---

## 🛣️ Roadmap

- [x] Real-time fall detection
- [ ] `requirements.txt` + packaged CLI entry point
- [ ] Fire & smoke detection
- [ ] PPE (personal protective equipment) detection
- [ ] Violence detection
- [ ] Weapon detection
- [ ] Intrusion detection
- [ ] Crowd analytics
- [ ] Web dashboard
- [ ] Multi-camera support
- [ ] Edge deployment (Jetson / Raspberry Pi)

---

## 🤝 Contributing

Contributions are welcome! Please open an issue before submitting major changes so we can align on direction first.

---

## 📄 License

MIT License

---

<p align="center"><i>SentinelCV — the first module of a bigger vision intelligence platform.</i></p>
