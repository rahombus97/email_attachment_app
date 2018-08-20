from tkinter import Tk, Label, Entry, Button, mainloop, filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import re

class EmailAttachmentGUI:

    SMTP_SERVER = "SMTP Sever name goes here"
    FROM_EMAIL_ADDRESS = "From email address goes here"
    EMAIL_PASSWORD = "Email password goes here"

    def __init__(self, master):
        self.email = ""
        self.subject = ""
        self.photo_path = ""

        self.master = master
        master.title("Send an email with an attachment here!")

        self.title_label = Label(master, text="Email Attachment Sender", font=("Helvetica", 24))

        self.email_label = Label(master, text="Email to send to:")
        self.email_entry = Entry(master, validate="key")
        self.email_warning = Label(master, text="The email address wasn't correct", fg="red")

        self.subject_label = Label(master, text="Enter the subject of the email: ")
        self.subject_entry = Entry(master, validate="key")
        
        self.photo_label = Label(master, text="Photo to send: ")
        self.upload_button = Button(master, text="Pick a photo", command=self.upload)

        self.submit_button = Button(master, text="Send email", command=self.submit)

        #LAYOUT

        self.title_label.grid(row=0, column=1)

        self.email_label.grid(row=1, column=0)
        self.subject_label.grid(row=2, column=0)
        self.photo_label.grid(row=3, column=0)

        self.email_entry.grid(row=1, column=1)
        self.subject_entry.grid(row=2, column=1)
        self.upload_button.grid(row=3, column=1)

        self.submit_button.grid(row=3, column=2)

    def validate_email(self, email):
        if len(email) > 7 and re.match("[^@]+@[^@]+\.[^@]+", email) != None:
            return True
        return False

    def upload(self):
        self.photo_path = filedialog.askopenfilename()
        print(self.photo_path)

    def send_email(self, to_email_address, subject, photo_path):
        #Create the message
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = FROM_EMAIL_ADDRESS
        msg["To"] = to_email_address
        msg.preamble = "Here's your picture!"

        #Attach the photo to the email via the file path given
        with open(photo_path, "rb") as fp:
            img = MIMEImage(fp.read())
        msg.attach(img)

        #Send the email via localhost
        server = smtplib.SMTP_SSL(SMTP_SERVER, 465)
        server.ehlo()
        server.login(FROM_EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

    def submit(self):
        #Get data from entries in Tk
        self.email = self.email_entry.get()
        self.subject = self.subject_entry.get()
        if self.validate_email(self.email):
            self.email_warning.grid_forget()
            self.send_email(self.email, self.subject, self.photo_path)
            print("Submitted")
        else:
            self.email_warning.grid(row=1, column=2)
            print("Not Submitted")
