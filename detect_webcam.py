import cv2
from ultralytics import YOLO
print("Script started")
def main():
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam. Try changing VideoCapture(0) to (1).")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model(frame, verbose=False)
        annotated = results[0].plot()

        cv2.imshow("Laptop Object Detection (press q to quit)", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()