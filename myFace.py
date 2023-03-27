import os, random
from time import sleep
def videoEffect(mark, filter):
    import cv2
    RES = 600 , 300
    main_capture = cv2.VideoCapture(mark)
    background_capture = cv2.VideoCapture(filter)
    subtractor = cv2.createBackgroundSubtractorKNN()

    while True:
        try:
            frame = main_capture.read()[1]
            frame = cv2.resize(frame, RES, interpolation = cv2.INTER_AREA)

            bg_frame = background_capture.read()[1]
            bg_frame = cv2.resize(bg_frame, RES, interpolation = cv2.INTER_AREA)

            mask = subtractor.apply(frame, 1)
            bitwise = cv2.bitwise_and(bg_frame, bg_frame, mask=mask)

            cv2.imshow('', bitwise)

            if cv2.waitKey(1) == 27:
                # pass
                return 0
        except:
            return 0
    return 0
os.system('start python le_START_LEARNING.py -b True')
videoShow = [
    ['video/mustang43.mp4', 'video/matrix43.mp4'], ['video/benc37.mp4', 'video/matrix37.mp4']
]
ready = 1
while True:
    thisOne = random.choice(videoShow)
    ready = videoEffect(thisOne[0], thisOne[1])
    if ready != 0:
        sleep(100)