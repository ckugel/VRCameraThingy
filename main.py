import threading

import cv2

myBool = False


def toggleBool():
    global myBool
    myBool = not myBool


height = 1
width = 1

def updateVals():
    global height, width
    a = input("new height: ")
    b = input("new width: ")
    height = a
    width = b

def app():
    #thread1 = threading.Thread(target=updateVals)
    #thread1.start()
    cap = cv2.VideoCapture(1)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=1.185, fy=1.65, interpolation=cv2.INTER_AREA)

        c = cv2.waitKey(1)
        if c == 27:
            break

        elif c == 32:
            toggleBool()

        if myBool:
            frame = cv2.putText(frame, 'THIS IS A TEST', (25, 1150), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (255, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Camera', frame)
        cv2.imshow('Camera2', frame)

        cv2.moveWindow('Camera', 0, 0)
        cv2.moveWindow('Camera2', 765, 0)

    cap.release()
    cv2.destroyAllWindows()


# TODO: remove this
if __name__ == '__main__':
    app()
