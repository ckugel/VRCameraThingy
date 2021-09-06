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
            y = 50
            yOffset = 30
            stringer = scraper()
            frame = cv2.putText(frame, str(scraper()[0]), (50, y), cv2.FONT_HERSHEY_SIMPLEX,
                                0.75, (255, 0, 255), 2, cv2.LINE_AA)
            frame = cv2.putText(frame, str(scraper()[1]), (50, y + yOffset), cv2.FONT_HERSHEY_SIMPLEX,
                                0.75, (255, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Camera', frame)
        cv2.imshow('Camera2', frame)

        cv2.moveWindow('Camera', 0, 0)
        cv2.moveWindow('Camera2', 765, 0)

    cap.release()
    cv2.destroyAllWindows()

def scraper():
    # importing requests and json
    import requests
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Minneapolis"
    API_KEY = "a4607507018ae05d3610c90156b45ecd"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # weather report
        report = data['weather']

        return 'Temperature: ' + str(int((int(temperature) - 273.15) / 5 * 9 + 32)), 'Weather Report: ' + report[0]['description']
    else:
        # showing the error message
        print("Error in the HTTP request")


# TODO: remove this
if __name__ == '__main__':
    app()
