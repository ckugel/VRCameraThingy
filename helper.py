import cv2
import numpy as np

all_camera_idx_available = []

for camera_idx in range(10):
    try:
        cap = cv2.VideoCapture(camera_idx)
        if cap.isOpened():
            print(f'Camera index available: {camera_idx}')
            all_camera_idx_available.append(camera_idx)
            cap.release()
    except:
        print(camera_idx)