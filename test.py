from ultralytics import YOLO

model = YOLO("models/fall_det_1.pt")

print(model.names)