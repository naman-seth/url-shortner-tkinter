import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("Url shortner")
root.geometry('300x150')

def shorten():
    shortener = pyshorteners.Shortener()
    shortUrl=shortener.tinyurl.short(longurl_entry.get())  #to get longurl
    shorturl_entry.insert(0,shortUrl)
# components
longurl_Label = tkinter.Label(root,text="Enter long url")
longurl_entry = tkinter.Entry(root)
shorturl_Label = tkinter.Label(root,text="Enter short url")
shorturl_entry = tkinter.Entry(root)
shortButton = tkinter.Button(root,text='Shorten',command=shorten)

#pack(geometry manager) to display components on application
longurl_Label.pack()
longurl_entry.pack()
shorturl_Label.pack()
shorturl_entry.pack()
shortButton.pack()

root.mainloop()