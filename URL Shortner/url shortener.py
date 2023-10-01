import pyshorteners
from tkinter import *

def shorten_url():
    url = entry1.get()
    if url:
        s = pyshorteners.Shortener().tinyurl.short(url)
        entry2.delete(0, END)  # Clear any previous result
        entry2.insert(END, s)
    else:
        entry2.delete(0, END)
        entry2.insert(END, "Please enter a URL")

win = Tk()
win.geometry("400x270")
win.title("URL Shortener")
win.configure(bg="green")

Label(win, text="Enter Your URL Link", font="impact 17 bold", bg="black", fg="white").pack(fill="x")

entry1 = Entry(win, font="10", bd=3, width=40)
entry1.pack(pady=10)

Button(win, text="Shorten", font="impact 12 bold", bg="blue", fg="white", width=14, command=shorten_url).pack()

entry2 = Entry(win, font="impact 16 bold", bg="green", width=24, bd=0)
entry2.pack(pady=10)

win.mainloop()
