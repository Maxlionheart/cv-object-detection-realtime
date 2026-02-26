Laptop AI Object Detection (YOLOv8)
This project demonstrates real-time object detection using Ultralytics YOLOv8 and OpenCV.

The system captures live webcam frames and performs neural network inference to detect and label objects in real time.

## 🚀 Current Features
- Real-time webcam object detection
- Bounding box visualization
- Clean virtual environment setup
- Git version control integration

🧠 Learning Context
This project is part of my practical learning journey alongside CS50AI (Harvard’s Introduction to Artificial Intelligence).

While this version uses a pretrained YOLO model, future updates will focus on:

-Understanding model architecture and inference flow
-Modifying detection logic
-Experimenting with filtering specific classes
-Connecting computer vision concepts to AI theory
-Exploring robotics integration in future iterations

##🛠️ Technologies Used
-Python
-Ultralytics YOLOv8
-OpenCV
-Git & GitHub

##📌 Future Improvements
-Add class filtering (e.g., detect only persons)
-Display confidence scores
-Save output video
-Raspberry Pi deployment
-Connect detection output to decision-making logic


## How to Run

1. Clone the repository:
git clone https://github.com/yourusername/cv-object-detection-realtime.git

2. Create a virtual environment:
python -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Install dependencies:
pip install -r requirements.txt

4. Run:
python detect_webcam.py
