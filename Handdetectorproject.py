import cv2
from cvzone.HandTrackingModule import HandDetector
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import pyautogui
import time

# access to Web cam and recognizing hands
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

#the function that will detect hands and open the webcam untill you stop it.
while True:

    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        HandType = hand['type']
        bbox = hand['bbox']
        centerpoint= hand['center']

        print(centerpoint[0])
        time.sleep(0.1)
        if centerpoint [0]>450:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            time.sleep(0.55)

        if centerpoint [0]<100:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(0.55)




    cv2.imshow('Video', img)
    cv2.waitKey(1)