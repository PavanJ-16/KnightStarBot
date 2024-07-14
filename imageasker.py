import cv2
import google.generativeai as genai
import PIL.Image
import os
import pyttsx3
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
engine=pyttsx3.init()
def speakText(command):
    engine.say(command)
    engine.runAndWait()
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            img_ = cv2.resize(gray,(28,28))
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
 
genai.configure(api_key="APIKEY")
img = PIL.Image.open('saved_img.jpg')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
print("what do you want to ask")
speakText("what do you want to ask")
query=input()
response = model.generate_content([query, img])
print(response.text)
speakText(response.text)
