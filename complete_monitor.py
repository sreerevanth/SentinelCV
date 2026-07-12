import cv2
import cvzone
import math
from ultralytics import YOLO
from datetime import datetime
import requests
import time
# ---------------- TELEGRAM ---------------- #
BOT_TOKEN = "your bot token "
CHAT_ID = "xxxxxxchat id"
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
# ---------------- INIT ---------------- #
cap = cv2.VideoCapture(0)  # CAMERA
model = YOLO("yolov8s.pt")
logs = []
MAX_LOGS = 5
status = "NORMAL"
confidence_display = 0
fall_counter = 0
triggered = False
last_sent_time = 0
# ---------------- LOG FUNCTION ---------------- #
def add_log(message):
    time_str = datetime.now().strftime("%H:%M:%S")
    logs.append(f"[{time_str}] {message}")
    if len(logs) > MAX_LOGS:
        logs.pop(0)
# ---------------- MAIN LOOP ---------------- #
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (980, 740))
    results = model(frame, stream=True, verbose=False)

    fall_detected = False
    for info in results:
        for box in info.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width = x2 - x1
            height = y2 - y1
            conf = int(box.conf[0] * 100)
            cls = int(box.cls[0])
            label = model.names[cls]
            if label == "person" and conf > 70:
                cvzone.cornerRect(frame, [x1, y1, width, height], l=20, rt=2)
                cvzone.putTextRect(frame, f"{label} {conf}%", [x1, y1 - 10])
                # 🔥 FALL LOGIC
                if width > height * 1.5:
                    fall_detected = True
                    confidence_display = conf
    # ---------------- STABILITY FILTER ---------------- #
    if fall_detected:
        fall_counter += 1
    else:
        fall_counter = 0
        triggered = False
    # ---------------- ALERT ---------------- #
    if fall_counter >= 5 and not triggered:
        triggered = True
        status = "FALL DETECTED"
        add_log("Fall detected!")
        if time.time() - last_sent_time > 20:
            msg = f"🚨 FALL DETECTED!\nTime: {datetime.now().strftime('%H:%M:%S')}"
            # 📸 SAVE IMAGE
            image_path = "fall_capture.jpg"
            cv2.imwrite(image_path, frame)
            # 📱 SEND BOTH
            send_alert(msg)
            send_image(image_path)
            add_log("Alert + image sent")
            last_sent_time = time.time()
    elif fall_counter == 0:
        status = "NORMAL"
    # STATUS
    if status == "FALL DETECTED":
        cvzone.putTextRect(frame, status, [50, 80], scale=3, thickness=3)
    else:
        cvzone.putTextRect(frame, status, [50, 80], scale=2, thickness=2)
    # CONFIDENCE
    cvzone.putTextRect(
        frame,
        f"Confidence: {confidence_display}%",
        [50, 140],
        scale=2,
        thickness=2,
    )
    # LOG PANEL
    y_offset = 200
    cvzone.putTextRect(frame, "EVENT LOGS:", [50, y_offset], scale=2)
    for i, log in enumerate(logs):
        cvzone.putTextRect(
            frame,
            log,
            [50, y_offset + 40 + (i * 35)],
            scale=1,
        )
    cv2.imshow("AI Monitor (FINAL SYSTEM)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()