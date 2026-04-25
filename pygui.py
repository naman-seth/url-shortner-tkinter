import tkinter
import pyshorteners

root = tkinter.Tk()
root.title("Url shortner")
root.geometry('300x150') #default window size

def shorten():
    shortener = pyshorteners.Shortener()
    oriurl = longurl_entry.get()
    if oriurl.startswith("https://"):
        shortUrl=shortener.tinyurl.short(oriurl)  #to get longurl
    else:
        shortUrl=shortener.tinyurl.short('https://'+oriurl)
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