import cv2
from ultralytics import YOLO

# Load YOLOv8 Nano (fastest) pretrained model
model = YOLO("yolov8n.pt")  # Requires network download on first run

# Choose video source:
# 0 -> default USB webcam
# Or replace with ESP32-CAM stream URL like "http://192.168.4.1:81/stream"
video_source = 0
cap = cv2.VideoCapture(video_source)
if not cap.isOpened():
    print("Error: Cannot open video source")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame read failed — exiting")
        break

    # Run inference
    results = model(frame)

    # Draw results
    annotated_frame = results[0].plot()

    # Display
    cv2.imshow("YOLO Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
