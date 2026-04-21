# 🖐️ Gesture Control System

🚀 A real-time gesture-based system that allows users to control their computer using hand movements.

🔗 **Live Demo Website:**
https://srichethanapolaki.github.io/gesture-control-system/

---

## 🎯 Features

* ☝️ Cursor movement using index finger
* ✌️ Click using two-finger gesture
* 🤟 Scroll up/down using multi-finger gestures
* 👍 Volume control using finger distance
*  Exit using custom gesture

---

## 🧠 Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

## ⚙️ How It Works

The system captures real-time video using the webcam.
MediaPipe detects 21 hand landmarks and identifies finger positions.

Based on gesture combinations:

* Cursor movement
* Clicking
* Scrolling
* Volume control

are executed using PyAutoGUI.

---

## 💻 Installation

1. Clone the repository:

```
git clone https://github.com/srichethanapolaki/gesture-control-system.git
```

2. Install dependencies:

```
pip install opencv-python mediapipe pyautogui
```

3. Run the project:

```
python hand_test.py
```

---

## 🖐️ Gesture Controls

| Gesture          | Action         |
| ---------------- | -------------- |
| ☝️ Index finger  | Move cursor    |
| ✌️ Two fingers   | Click          |
| 🤟 Three fingers | Scroll Down    |
| 🖖 Four fingers  | Scroll Up      |
| 👍 + ☝️          | Volume control |
|  Ring + Pinky  | Exit           |

---

## 🎥 Demo

👉 Check the working demo on the website:
https://srichethanapolaki.github.io/gesture-control-system/

---

## 💡 Future Improvements

* Gesture customization
* Multi-hand support
* AI-based gesture classification
* Improved UI feedback

---

## 👩‍💻 Author

**Polaki Srichethana**

---

⭐ If you like this project, give it a star!
