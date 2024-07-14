import serial.tools.list_ports
import pyttsx3
import requests 
from collections import deque
import pywhatkit
import google.generativeai as genai
import cv2
import numpy as np
engine=pyttsx3.init()
def setValues(x):
   print("")
def speakText(command):
    engine.say(command)
    engine.runAndWait()
print("Hello I am your smart assistant Knight Star")
speakText("Hello I am your smart assistant Knight Star")
print("I have two voices tell me which version do you prefer")
speakText("I have two voices tell me which version do you prefer")
print("This is my first voice for this press 1")
speakText("This is my first voice for this press 1")
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
print("and this is my second voice for this press 2")
speakText("and this is my second voice for this press 2")
a=input()
if(a=='1'):
    engine.setProperty('voice', voices[0].id)
elif(a=='2'):
    engine.setProperty('voice', voices[1].id)
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portlist=[]
for onePort in ports:
    portlist.append(str(onePort))
    print(onePort)
val=int(input())
for x in range(0,len(portlist)):
    if portlist[x].startswith("COM"+str(val)):
        portvar="COM"+str(val)
serialInst.baudrate= 9600
serialInst.port=portvar
serialInst.open()
while True:
    speakText("please tell me your command")
    command = input()
    if "forward" in command:
        print(" moving forward")
        dir='F'
        serialInst.write(dir.encode('utf-8'))
        speakText("Moving forward")
    elif "stop" in command:
            print("Stopping")
            dir='S'
            serialInst.write(dir.encode('utf-8'))
            speakText("Stoping")
    elif "right" in command:
            print("moving right")
            dir='R'
            serialInst.write(dir.encode('utf-8'))
            speakText("moving right")
    elif "left"  in command:
            print("moving left")
            dir='L'
            serialInst.write(dir.encode('utf-8'))
            speakText("moving left")
    elif "back" in command:
            print(" moving back")
            dir='B'
            serialInst.write(dir.encode('utf-8'))
            speakText("Moving back")
    elif "Love" in command:
            print("AWWWW thank you i love you too")
            dir='4'
            serialInst.write(dir.encode('utf-8'))
            speakText("AWWWW thank you i love you too")
    elif "time" in command:
        import datetime
        hour = str(datetime.datetime.now().hour)+" hours"+str(datetime.datetime.now().minute)+" minutes"+str(datetime.datetime.now().second)+" seconds"
        print("The time now is   "+hour)
        speakText("The time now is"+hour)
    elif "query" in command:
        API_KEY="key"
        genai.configure(api_key=API_KEY)
        model=genai.GenerativeModel('gemini-pro') 
        chat = model.start_chat(history=[])
        while (True):
            print("hey what can i do for you")
            speakText("hey what can i do for you")
            ques=input()
            if "exit" in ques:
                exit()
            res=chat.send_message(ques)
            print(f"Bot : {res.text}")
            speakText("Bot : {res.text}")
    elif "music" in command:
        print("Please tell me wich song to play")
        speakText("Please tell me wich song to play")
        song=input()
        pywhatkit.playonyt(song)
    elif "camera" in command:
        cv2.namedWindow("Color detectors")
        cv2.createTrackbar("Upper Hue", "Color detectors", 30, 180, setValues)
        cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255, setValues)
        cv2.createTrackbar("Upper Value", "Color detectors", 255, 255, setValues)
        cv2.createTrackbar("Lower Hue", "Color detectors", 15, 180, setValues)
        cv2.createTrackbar("Lower Saturation", "Color detectors", 100, 255, setValues)
        cv2.createTrackbar("Lower Value", "Color detectors", 100, 255, setValues)
        bpoints = [deque(maxlen=1024)]
        gpoints = [deque(maxlen=1024)]
        rpoints = [deque(maxlen=1024)]
        ypoints = [deque(maxlen=1024)]
        blue_index = 0
        green_index = 0
        red_index = 0
        yellow_index = 0
        kernel = np.ones((5,5),np.uint8)
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
        colorIndex = 0
        paintWindow = np.zeros((471,636,3)) + 255
        paintWindow = cv2.rectangle(paintWindow, (40,1), (140,65), (0,0,0), 2)
        paintWindow = cv2.rectangle(paintWindow, (160,1), (255,65), colors[0], -1)
        paintWindow = cv2.rectangle(paintWindow, (275,1), (370,65), colors[1], -1)
        paintWindow = cv2.rectangle(paintWindow, (390,1), (485,65), colors[2], -1)
        paintWindow = cv2.rectangle(paintWindow, (505,1), (600,65), colors[3], -1)
        cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
        cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
            u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
            u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
            l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
            l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
            l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
            Upper_hsv = np.array([u_hue,u_saturation,u_value])
            Lower_hsv = np.array([l_hue,l_saturation,l_value])
            frame = cv2.rectangle(frame, (40,1), (140,65), (122,122,122), -1)
            frame = cv2.rectangle(frame, (160,1), (255,65), colors[0], -1)
            frame = cv2.rectangle(frame, (275,1), (370,65), colors[1], -1)
            frame = cv2.rectangle(frame, (390,1), (485,65), colors[2], -1)
            frame = cv2.rectangle(frame, (505,1), (600,65), colors[3], -1)
            cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
            Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
            Mask = cv2.erode(Mask, kernel, iterations=1)
            Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
            Mask = cv2.dilate(Mask, kernel, iterations=1)
            cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            center = None
            if len(cnts) > 0:
                cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                M = cv2.moments(cnt)
                center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
                if center[1] <= 65:
                    if 40 <= center[0] <= 140: # Clear Button
                        bpoints = [deque(maxlen=512)]
                        gpoints = [deque(maxlen=512)]
                        rpoints = [deque(maxlen=512)]
                        ypoints = [deque(maxlen=512)]
                        blue_index = 0
                        green_index = 0
                        red_index = 0
                        yellow_index = 0
                        paintWindow[67:,:,:] = 255
                    elif 160 <= center[0] <= 255:
                        colorIndex = 0 
                    elif 275 <= center[0] <= 370:
                        colorIndex = 1 
                    elif 390 <= center[0] <= 485:
                        colorIndex = 2 
                    elif 505 <= center[0] <= 600:
                        colorIndex = 3 
                else :
                    if colorIndex == 0:
                        bpoints[blue_index].appendleft(center)
                    elif colorIndex == 1:
                        gpoints[green_index].appendleft(center)
                    elif colorIndex == 2:
                        rpoints[red_index].appendleft(center)
                    elif colorIndex == 3:
                        ypoints[yellow_index].appendleft(center)
            else:
                bpoints.append(deque(maxlen=512))
                blue_index += 1
                gpoints.append(deque(maxlen=512))
                green_index += 1
                rpoints.append(deque(maxlen=512))
                red_index += 1
                ypoints.append(deque(maxlen=512))
                yellow_index += 1 
            points = [bpoints, gpoints, rpoints, ypoints]
            for i in range(len(points)):
                for j in range(len(points[i])):
                    for k in range(1, len(points[i][j])):
                        if points[i][j][k - 1] is None or points[i][j][k] is None:
                            continue
                        cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                        cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)
            cv2.imshow("Tracking", frame)
            cv2.imshow("Paint", paintWindow)
            if cv2.waitKey(1) & 0xFF == ord("q"):
               break
        cap.release()
        cv2.destroyAllWindows()
    elif "weather" in command:
        api_key = "00b7bb8bc26151ed56b82b8299344a0d"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        print("pls tell me the City name ")
        speakText("pls tell me the City name ")
        city_name=input()
        speakText("Ok weather of city "+ city_name)
        print("Ok weather of city"+ city_name)
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url) 
        x = response.json() 
        if x["cod"] != "404": 
            y = x["main"] 
            current_temperature = y["temp"] 
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"] 
            z = x["weather"] 
            weather_description = z[0]["description"] 
            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
            speakText(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
        else: 
            print("City not found")
            speakText(" City Not Found ")
    elif "lights" in command:
            print("tell me the colour")
            speakText("tell me the colour")
            col=input()
            if "red" in col:
                requests.get(API)
            elif "green" in col:
               requests.get(API)
            elif "red" in col:
               requests.get(API)
            elif "off" in col:
                requests.get(API)
    elif "down" in command:
        print("Shutting Down")
        speakText("Shutting Down")
        exit()
