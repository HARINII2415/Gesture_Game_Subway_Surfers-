# 🎮 Gesture Controlled Subway Surfer Game

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green?logo=opencv&logoColor=white)](https://opencv.org/)
[![Mediapipe](https://img.shields.io/badge/Mediapipe-0.8.10-blueviolet)](https://google.github.io/mediapipe/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.53-orange)](https://pyautogui.readthedocs.io/en/latest/)


---

## 🚀 Project Overview

This project lets you **control the Subway Surfer web game** using your **hand gestures** captured through your webcam!  
By detecting your **index finger swipe direction (left, right, up, down)** with **MediaPipe Hands** and **OpenCV**, the program sends keyboard inputs to control the game.

> *Note:* Due to browser security, simulated key presses may not work directly on the game page, but the gesture detection works perfectly, showing real-time feedback.

---

## 🛠️ Features

- Real-time hand tracking with **MediaPipe Hands**  
- Index finger swipe gesture detection (left, right, up, down)  
- Gesture visualization on webcam feed using OpenCV  
- Python GUI using Tkinter for easy game launching  
- Opens Subway Surfer game in the browser automatically  
- Modular and well-documented code for easy understanding

---
📦 Requirements
Python 3.8+

OpenCV (opencv-python)

Mediapipe (mediapipe)

PyAutoGUI (pyautogui)

Pillow (Pillow)

🧩 Code Structure
plaintext
Copy
Edit

💡 How It Works (Short)
The program captures webcam frames continuously.

MediaPipe detects your hand and tracks the tip of the index finger.

Changes in index finger position detect swipe directions.

Detected gestures are printed in the console and trigger simulated keyboard arrow presses (if enabled).

The Tkinter GUI lets you open the Subway Surfers game easily.

🤝 Contributions
Feel free to contribute! Fork, create issues or PRs, and help improve this project.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📫 Contact
Created by Harini A
Email: harinii2415@gmail.com
LinkedIn: https://www.linkedin.com/in/harini-a-9a014925a/

Happy Gaming & Coding! 🚀🎮





   
