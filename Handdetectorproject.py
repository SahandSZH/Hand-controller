import cv2
from cvzone.HandTrackingModule import HandDetector
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import pyautogui
import time

# access to Webcam and recognizing hands
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

        fingers= detector.fingersUp(hand)
        #print(fingers)
        #print(centerpoint[0])
        #print(HandType)
        time.sleep(0.1)
        length, info, img = detector.findDistance(lmList[4][:2], lmList[8][:2], img)
        a = length
        print(a)
        if HandType== 'Right' and a> 100:
            pyautogui.scroll(50)
        if HandType== 'Right' and a<60 :
            pyautogui.scroll(-50)
        if HandType== 'Left' and a> 100:
            pyautogui.hotkey('ctrl', '+')
        if HandType== 'Left' and 10<a<60 :
            pyautogui.hotkey('ctrl', '-')
        if centerpoint [0]>450 and fingers == [1,1,1,1,1]:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            time.sleep(0.55)

        if centerpoint [0]<100 and fingers == [1,1,1,1,1]:
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(0.55)
        if HandType== 'Left' and fingers == [0,1,1,0,0]:
            pyautogui.press('volumeup')
        if HandType== 'Left' and fingers == [0,1,0,0,0]:
            pyautogui.press('volumedown')


    cv2.imshow('Video', img)
    cv2.waitKey(1)