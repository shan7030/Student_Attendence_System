# main.py

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2



class CreateAccountWindow(Screen):
    namee = kivy.properties.ObjectProperty(None)
    email = kivy.properties.ObjectProperty(None)
    password = kivy.properties.ObjectProperty(None)
    

    def submit(self):
        if self.namee.text != "" and self.email.text != "" :
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def addQRCode(self):
        print("[INFO] starting video stream...")
        vs = VideoStream(src=0).start()
        #vs = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)
# loop over the frames from the video stream
        while True:
	# grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame, width=400)

            # find the barcodes in the frame and decode each of the barcodes
            barcodes = pyzbar.decode(frame)

            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                # draw the barcode data and barcode type on the image
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.cv2.putText(frame, text, (x, y - 10),
                    cv2.cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # if the barcode text is currently not in our CSV file, write
                # the timestamp + barcode to disk and update the set
                print(barcodeData)
                self.email.text=barcodeData
                
                break
            # show the output frame
            cv2.cv2.imshow("Barcode Scanner", frame)
            key = cv2.cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
            if self.email.text!="":
                break                
        

# close the output CSV file do a bit of cleanup

        print("[INFO] cleaning up...")
        cv2.cv2.destroyAllWindows()
        vs.stop()
        return 

        

class LoginWindow(Screen):
    email = kivy.properties.ObjectProperty(None)
    password = kivy.properties.ObjectProperty(None)

    def loginBtn(self):
        if self.email.text=="admin" and self.password.text=="admin" :
            MainWindow.current="admin"
            self.reset()
            sm.current = "main"
        elif db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

    def UploadQRCode(self):
        print("[INFO] starting video stream...")
        vs = VideoStream(src=0).start()
        #vs = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)
# loop over the frames from the video stream
        while True:
	# grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame, width=400)

            # find the barcodes in the frame and decode each of the barcodes
            barcodes = pyzbar.decode(frame)

            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                # draw the barcode data and barcode type on the image
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.cv2.putText(frame, text, (x, y - 10),
                    cv2.cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # if the barcode text is currently not in our CSV file, write
                # the timestamp + barcode to disk and update the set
                print(barcodeData)
                self.email.text=barcodeData
                
                break
            # show the output frame
            cv2.cv2.imshow("Barcode Scanner", frame)
            key = cv2.cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
            if self.email.text!="":
                break                
        

# close the output CSV file do a bit of cleanup

        print("[INFO] cleaning up...")
        cv2.cv2.destroyAllWindows()
        vs.stop()
        return 
    
class AdminWindow(Screen):
    n = kivy.properties.ObjectProperty(None)
    created = kivy.properties.ObjectProperty(None)
    email = kivy.properties.ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        self.n.text = "Name: ADMINISTRATOR"
        self.email.text = "ID No.: ADMIN" 
        self.created.text = "Absent/Present Today: ADMIN" 
    
    def updateAttendence(self):
        print("[INFO] starting video stream...")
        vs = VideoStream("Device 004").start()
        #vs = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)
# loop over the frames from the video stream
        while True:
	# grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame, width=400)

            # find the barcodes in the frame and decode each of the barcodes
            barcodes = pyzbar.decode(frame)

            # loop over the detected barcodes
            for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                # draw the barcode data and barcode type on the image
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.cv2.putText(frame, text, (x, y - 10),
                    cv2.cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # if the barcode text is currently not in our CSV file, write
                # the timestamp + barcode to disk and update the set
                print(barcodeData)
                print(barcodeData)
                print(barcodeData)
                self.created.text="Updated Successfully attendence of :"+barcodeData
                db.update(barcodeData)
                break
            # show the output frame
            cv2.cv2.imshow("Barcode Scanner", frame)
            key = cv2.cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
            if self.created.text!="Absent/Present Today: ADMIN":
                break                
        

# close the output CSV file do a bit of cleanup

        print("[INFO] cleaning up...")
        cv2.cv2.destroyAllWindows()
        vs.stop()
        return



class MainWindow(Screen):
    
    n = kivy.properties.ObjectProperty(None)
    created = kivy.properties.ObjectProperty(None)
    email = kivy.properties.ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        db.load()
        if self.current!="admin" :
            password, name, created = db.get_user(self.current)
            self.n.text = "Name: " + name
            self.email.text = "Student Id no.: " + self.current
            self.created.text = "Present/Absent: " + created
        else :
            sm.current="admin"

class ShowWindow(Screen):
    n = kivy.properties.ObjectProperty(None)
    
    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        db.load()
        self.n.text="Whole Data"
        self.n.text=db.retstring()

class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),AdminWindow(name="admin"),ShowWindow(name="showatt")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
