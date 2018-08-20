# PaperClip

![PaperClip](https://www.ha-mtl.org/supplies/wp-content/uploads/2015/07/paperclips-small.jpg)

This application was created for my grandmother to use to help her with sending attachments with emails. I decided to name it PaperClip due to the common image of a paper clip being used to attach things to emails.
She has never been able to quite get it after walking her through the process. So I decided to utilize some of my programming skills to help her out a bit.
I created a simple GUI utilizing the python module for her to send emails through, Tkinter: https://wiki.python.org/moin/TkInter

![PaperClip GUI](https://i.imgur.com/PB7ggJB.png)

## Getting Started

You can run this application via running it directly through your Termainl or Commnad Prompt.

```
python3 <directory path of repo on local machine>/email_attachment_main.py
```
or

I created a Bash script to be used on Windows and Mac machines to execute right from a desktop icon

## Windows
```
[Desktop Entry]
Name=PaperClip
Comment=Runs GUI for PaperClip
Exec=<path to email_attachment_main.py>
Terminal=false
Type=Application
```

## Mac
```
!/bin/sh
python3 /Users/Rahombus97/Documents/dev/tk_email_attachment/email_attachment_main.py
```

### Prerequisites

Tkinter: https://wiki.python.org/moin/TkInter

### Installing and Running

Pull down the repo and change into the directory to run email_attachment_main.py

```
cd email_attachment_app/src
python3 email_attachment_main.py
```



