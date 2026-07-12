import cv2
import cvzone
import math
from ultralytics import YOLO
from datetime import datetime
import requests
import time
# ---------------- TELEGRAM ---------------- #
BOT_TOKEN = "8205081054:AAFSeIgntU8TfW8jl03WsbZ_HhTh3kGY93o"
CHAT_ID = "7135291777"
def send_alert(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
        print("✅ MESSAGE SENT")
    except Exception as e:
        print("❌ MESSAGE ERROR:", e)
def send_image(image_path):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open(image_path, "rb") as img:
            requests.post(
                url,
                data={"chat_id": CHAT_ID},
                files={"photo": img}
            )

        print("📸 IMAGE SENT")
    except Exception as e:
        print("❌ IMAGE ERROR:", e)
# ---------------- VIDEO ---------------- #
VIDEO_PATH = "fall_video.mp4"
cap = cv2.VideoCapture(VIDEO_PATH)
model = YOLO("yolov8s.pt")
fall_counter = 0
triggered = False
last_sent_time = 0
logs = []
def add_log(msg):
    time_str = datetime.now().strftime("%H:%M:%S")
    logs.append(f"[{time_str}] {msg}")
    if len(logs) > 5:
        logs.pop(0)
# ---------------- LOOP ---------------- #
while True:
    ret, frame = cap.read()
    # 🔁 loop video smoothly
    if not ret:
        cap.release()
        cap = cv2.VideoCapture(VIDEO_PATH)
        fall_counter = 0
        triggered = False
        continue
    frame = cv2.resize(frame, (1000, 700))
    results = model(frame, stream=True, verbose=False)
    fall_detected = False
    confidence = 0
    for info in results:
        for box in info.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width = x2 - x1
            height = y2 - y1
            conf = int(box.conf[0] * 100)
            cls = int(box.cls[0])
            label = model.names[cls]
            if label == "person" and conf > 70:
                cvzone.cornerRect(frame, [x1, y1, width, height])
                cvzone.putTextRect(frame, f"{conf}%", [x1, y1 - 10])
                if width > height * 1.5:
                    fall_detected = True
                    confidence = conf
    # ---------------- STABILITY ---------------- #
    if fall_detected:
        fall_counter += 1
    else:
        fall_counter = 0
        triggered = False
    # ---------------- ALERT ---------------- #
    if fall_counter >= 6 and not triggered:
        triggered = True
        add_log("Fall detected!")
        if time.time() - last_sent_time > 20:
            msg = f"🚨 FALL DETECTED! IN CAM INPUT : 1  : \nTime: {datetime.now().strftime('%H:%M:%S')}"
            # 📸 SAVE IMAGE
            image_path = "fall_capture.jpg"
            cv2.imwrite(image_path, frame)
            # 📱 SEND BOTH
            send_alert(msg)
            send_image(image_path)
            add_log("Alert + image sent")
            last_sent_time = time.time()
    # ---------------- UI ---------------- #
    if triggered:
        cvzone.putTextRect(frame, "FALL DETECTED!", [50, 80], scale=3, thickness=3)
    else:
        cvzone.putTextRect(frame, "NORMAL", [50, 80], scale=2, thickness=2)
    cvzone.putTextRect(
        frame,
        f"Confidence: {confidence}%",
        [50, 140],
        scale=2,
        thickness=2,
    )
    cvzone.putTextRect(frame, "EVENT LOGS", [50, 200], scale=2)
    for i, log in enumerate(logs):
        cvzone.putTextRect(frame, log, [50, 240 + i * 35], scale=1)
    cv2.imshow("AI Fall Detection (VIDEO + IMAGE ALERT)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()