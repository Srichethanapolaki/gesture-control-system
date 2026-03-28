import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Setup
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

prev_x, prev_y = 0, 0
smooth = 6
last_click = 0
last_vol = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)
            lm = hand.landmark

            # -------- FINGER DETECTION --------
            fingers = []
            tip_ids = [4,8,12,16,20]

            fingers.append(1 if lm[4].x > lm[3].x else 0)

            for i in range(1,5):
                fingers.append(1 if lm[tip_ids[i]].y < lm[tip_ids[i]-2].y else 0)

            # Finger tips
            x1, y1 = int(lm[8].x * w), int(lm[8].y * h)
            x2, y2 = int(lm[12].x * w), int(lm[12].y * h)
            x_thumb, y_thumb = int(lm[4].x * w), int(lm[4].y * h)

            # -------- EXIT --------
            if fingers == [0,0,0,1,1]:
                print("Exit")
                cap.release()
                cv2.destroyAllWindows()
                exit()

            # -------- MOVE --------
            if fingers == [0,1,0,0,0]:
                sx, sy = screen_w * lm[8].x, screen_h * lm[8].y
                cx = prev_x + (sx - prev_x)/smooth
                cy = prev_y + (sy - prev_y)/smooth
                pyautogui.moveTo(cx, cy)
                prev_x, prev_y = cx, cy

            # -------- CLICK --------
            if fingers == [0,1,1,0,0]:
                dist = math.hypot(x2-x1, y2-y1)
                if dist < 30 and time.time() - last_click > 0.4:
                    pyautogui.click()
                    last_click = time.time()

            # -------- SCROLL DOWN --------
            if fingers == [0,1,1,1,0]:
                pyautogui.scroll(-40)

            # -------- SCROLL UP --------
            if fingers == [0,1,1,1,1]:
                pyautogui.scroll(40)

            # -------- VOLUME --------
            if fingers == [1,1,0,0,0]:
                if time.time() - last_vol > 0.5:
                    dist_vol = math.hypot(x_thumb-x1, y_thumb-y1)

                    if dist_vol < 40:
                        pyautogui.press("volumeup")
                    elif dist_vol > 120:
                        pyautogui.press("volumedown")

                    last_vol = time.time()

            # -------- DISPLAY --------
            cv2.putText(img, f"{fingers}", (10,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()