#!/usr/bin/python
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

eFROM = "kd2egt@gmail.com"
eTO = "joshua.a.simons@gmail.com"
s = smtplib.SMTP('smtp.gmail.com', 587)
#server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Python Email Test'
    msg['From'] = eFROM
    msg['To'] = eTO

    text = MIMEText("This is a test of Emailing and image with Python.  If the image is attached, it worked!")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(eFROM, "ybihbernfcvynzju")
    s.sendmail(eFROM, eTO, msg.as_string())
    s.quit()


SendMail("happy.jpg")