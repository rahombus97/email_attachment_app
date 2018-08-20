from tkinter import Tk, Label, Entry, mainloop
from email_attachment import EmailAttachmentGUI

if __name__ == "__main__":
    root = Tk()
    gui = EmailAttachmentGUI(root)
    root.mainloop()