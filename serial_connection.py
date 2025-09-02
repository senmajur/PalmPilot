import cv2
import mediapipe as mp
import serial
import time
import math

Arduino = serial.Serial('/dev/cu.usbmodem11101', 9600, timeout=0.1)

wCam, hCam = 1240, 720
cam = cv2.VideoCapture(1)
cam.set(3, wCam)
cam.set(4, hCam)

class mpHands:
    def __init__(self, mode=False, modelComplexity=1, maxHands=2, TrackCon=0.5, DetectCon=0.5):
        self.mode = mode
        self.modelComplexity = modelComplexity
        self.maxHands = maxHands
        self.TrackCon = TrackCon
        self.DetCon = DetectCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity,
                                        self.TrackCon, self.DetCon)
        self.mpDraw = mp.solutions.drawing_utils

    def Marks(self, frame):
        myHands = []
        handsType = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks:
            for hand in results.multi_handedness:
                handType = hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    h, w, c = frame.shape
                    myHand.append((int(landMark.x * w), int(landMark.y * h)))
                myHands.append(myHand)
        return myHands, handsType

    def getGesture(self, hand):
        fingers = []
        if hand:
            # Thumb
            if hand[4][0] > hand[3][0]:
                fingers.append(1)  # Thumb is open
            else:
                fingers.append(0)  # Thumb is closed

            # Other four fingers
            for i in range(8, 21, 4):
                if hand[i][1] < hand[i-2][1]:
                    fingers.append(1)  # Finger is open
                else:
                    fingers.append(0)  # Finger is closed
        return fingers

findHands = mpHands(maxHands=2)

while True:
    ret, frames = cam.read()
    if not ret:
        print("Failed to capture image")
        continue

    frame = cv2.flip(frames, 1)
    handData, handType = findHands.Marks(frame)

    command = 'NO_HAND\n'
    if handData:
        for hand in handData:
            fingers = findHands.getGesture(hand)
            if sum(fingers) == 5:  # All fingers are open
                command = 'FORWARD\n'
            elif sum(fingers) == 0:  # All fingers are closed
                command = 'STOP\n'
            elif fingers == [0, 0, 1, 0, 0]:  # Middle finger only
                command = 'BACKWARD\n'
            elif fingers == [0, 1, 0, 0, 0]:  # Pointer finger up
                command = 'TURN_RIGHT\n'
            elif fingers == [0, 1, 1, 0, 0]:  # Pointer and middle finger up
                command = 'TURN_LEFT\n'

    Arduino.write(command.encode())

    cv2.imshow('my WEBcam', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
