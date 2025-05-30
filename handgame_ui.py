import tkinter as tk
from tkinter import PhotoImage
import threading
import webbrowser
import cv2
import mediapipe as mp
import pyautogui
import time
from PIL import Image, ImageTk

# === Gesture Controller Class ===
class IndexFingerSwipeTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(min_detection_confidence=0.7, max_num_hands=1)
        self.last_pos = None
        self.swipe_threshold_x = 0.05
        self.swipe_threshold_y = 0.05
        self.cooldown = 0.5
        self.last_trigger = time.time()

    def detect_gesture(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        gesture = None
        hand_landmarks = None

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            index_tip = hand_landmarks.landmark[8]
            current_pos = (index_tip.x, index_tip.y)

            if self.last_pos:
                dx = current_pos[0] - self.last_pos[0]
                dy = current_pos[1] - self.last_pos[1]

                if abs(dx) > self.swipe_threshold_x and abs(dx) > abs(dy):
                    gesture = "left" if dx > 0 else "right"
                elif abs(dy) > self.swipe_threshold_y and abs(dy) > abs(dx):
                    gesture = "down" if dy > 0 else "up"

            self.last_pos = current_pos
        else:
            self.last_pos = None

        return gesture, hand_landmarks

def trigger_key(gesture, tracker):
    now = time.time()
    if gesture and (now - tracker.last_trigger > tracker.cooldown):
        print(f"[Gesture Detected] {gesture.upper()}")
        # Uncomment below if you want to test pyautogui on desktop apps (Not recommended for browsers)
        # pyautogui.press(gesture)
        tracker.last_trigger = now

# === Gesture Cam Function ===
def gesture_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    tracker = IndexFingerSwipeTracker()
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame")
            break

        gesture, landmarks = tracker.detect_gesture(frame)

        if landmarks:
            mp_drawing.draw_landmarks(
                frame, landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)
            )

        if gesture:
            cv2.putText(frame, gesture.upper(), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            trigger_key(gesture, tracker)

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to quit
            print("ESC pressed. Exiting gesture detection.")
            break

    cap.release()
    cv2.destroyAllWindows()

# === Game Window Function ===
def launch_game():
    print("Opening Subway Surfers game in browser...")
    webbrowser.open("https://poki.com/en/g/subway-surfers")
    t = threading.Thread(target=gesture_camera)
    t.daemon = True  # Close thread when main app exits
    t.start()
    print("Started gesture detection thread.")

# === Tkinter UI ===
root = tk.Tk()
root.title("Subway Surfer Gesture Game")
root.geometry("800x500")
root.resizable(False, False)

# 🖼️ Background image setup (make sure background.jpeg exists)
try:
    bg_img = Image.open("background.jpeg")
    bg_img = bg_img.resize((800, 500))
    bg_img = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print("Warning: Could not load background image:", e)

# 🎮 Title
title = tk.Label(root, text="Gesture Controlled Subway Surfer", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#ff1493")
title.pack(pady=20)

# 🔘 Start Button
start_btn = tk.Button(root, text="Start Game", font=("Helvetica", 16), bg="#28a745", fg="white", command=launch_game)
start_btn.place(x=300, y=250, width=200, height=50)

# ❌ Exit Button
exit_btn = tk.Button(root, text="Exit", font=("Helvetica", 16), bg="#dc3545", fg="white", command=root.destroy)
exit_btn.place(x=300, y=320, width=200, height=50)

root.mainloop()
