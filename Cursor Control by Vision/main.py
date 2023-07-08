# Title: Cursor Control by Vision.
# Description: A very simple project in Computer-Vision that uses locations of eyes to drag the mouse cursor and click stuff.
# Author: Huzbi.
# Date Created: 09/07/2023.

import cv2
import mediapipe
import pyautogui

camera = cv2.VideoCapture(0)
face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame, = camera.read()
    frame = cv2.flip(frame, 1) # flip the camera vertically to match the alignment properly
  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
  
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for element_id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if element_id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)

        left_eye = [landmarks[145], landmarks[159]]
        for landmark in left_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            # print(f"Y Position of Left eye: {left_eye[0].y}, {left_eye[1].y}")
            # print(f"Difference between Y positions of left eye: {left_eye[0].y-left_eye[1].y}")
        if (left_eye[0].y-left_eye[1].y) < 0.02:
            print("click")
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
