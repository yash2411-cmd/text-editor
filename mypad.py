from tkinter import *
# from tkinter import font
# from tkinter.font import BOLD
from tkinter import messagebox as tmsg
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import pyttsx3 
# from gtts import gTTS
# zoom in and out functionalities: 
def fullscreen():
    root.geometry("1920x1080")
def zoomin():
    Font[1]=Font[1]+2
    textEditor.config(font=Font)
def zoomout():
    Font[1]=Font[1]-2
    textEditor.config(font=Font)

# to make the text speak :
def talk():
    engine= pyttsx3.init()
    engine.say(textEditor.get(1.0,END))
    engine.runAndWait()
# to open new file:
def newFile():
    global file
    root.title("untitled -Notepad")
    file= None
    textEditor.delete(1.0,END)

# to open a existing file:
def openFile():
    global file
    file= askopenfilename(defaultextension=".txt",filetypes= [("All Files","*.*"),
    ("Text Documents","*.txt")])
    if file == "":
        file= None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textEditor.delete(1.0,END)
        f= open(file,"r")
        textEditor.insert(1.0,f.read())
        f.close()

# to save the file :
def saveFile():
    global file
    if file == None:
        file= asksaveasfilename(initialfile=" untitled",defaultextension=".txt",filetypes= [("All Files","*.*"),
    ("Text Documents","*.txt")])
        if file== "":
            file= None
        else:
            f= open(file,"w")
            f.write(textEditor.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ "- Notepad")
            print("file saved")
    else:
            f= open(file,"w")
            f.write(textEditor.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
            print("file saved")
# exit the Text_editor: 
def quitapp():
    b= tmsg.askyesno("warning","are you sure want to exit")
    if(b):
        root.destroy()
# to cut the selected text on the screen :
def cut():
    textEditor.event_generate(("<<Cut>>"))

# to copy the selected text on the screen :
def copy():
    textEditor.event_generate(("<<Copy>>"))

# to paste the selected text on the screen :
def paste():
    textEditor.event_generate(("<<Paste>>"))

# to print about the Text_editor :
def about():
    a=tmsg.showinfo("About","this is a simple text editor designed by Yash")
def myfunc():
    pass
#function for working with the binded keys :
def c1(event):
    copy()
def x1(event):
    cut()
def p1(event):
    paste()
def q1(event):
    quitapp()
def zi(event):
    zoomin()
def zo(event):
    zoomout()

# main OUTLET of the program :
root=Tk()
root.wm_iconbitmap('text editor/myicon.ico')
root.title("Notepad")
root.geometry("620x420")
root.maxsize(1920,1080)
root.minsize(620,420)

# text area for the input text and scroll bar setup : 
Font=["times",20]   
scrollbar= Scrollbar(root)
textEditor = Text(root,yscrollcommand=scrollbar.set,font=Font)
textEditor.pack(expand =True,fill=BOTH)
file= None
scrollbar.pack(fill=Y,side=RIGHT)
scrollbar.config(command=textEditor.yview)

#packing keys 
root.bind_all('<Control-Key-C>', c1)
root.bind_all('<Control-Key-plus>', zi)
root.bind_all('<Control-Key-minus>', zo)
root.bind_all('<Control-Key-X>', x1)
root.bind_all('<Control-Key-V>', p1)
root.bind_all('<Control-Key-Escape>', q1)

# creating the dropdown box for each menu element :
mymenu= Menu(root)
#file menu starts :
filemenu= Menu(mymenu,tearoff=0)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Speak",command=talk)
filemenu.add_command(label="Exit",command=quitapp)
mymenu.add_cascade(label="File",menu=filemenu)
root.config(menu=mymenu)

#edit menu starts :
editmenu= Menu(mymenu,tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_separator()
editmenu.add_command(label="Paste",command=paste)
mymenu.add_cascade(label="Edit",menu=editmenu)
root.config(menu=mymenu)

# view meanu starts : 
viewmenu= Menu(mymenu,tearoff=0)
zoom= Menu(viewmenu,tearoff=0)
zoom.add_command(label="Zoom In",command=zoomin)
zoom.add_command(label="Zoom Out",command=zoomout)
viewmenu.add_command(label="FullScreen",command=fullscreen)
root.config(menu=mymenu)
mymenu.add_cascade(label="View",menu=viewmenu)
viewmenu.add_cascade(label="Zoom",menu=zoom) 
# help menu starts : 
helpmenu= Menu(mymenu,tearoff=0)
helpmenu.add_command(label="About PyPad",command=about)
mymenu.add_cascade(label="Help",menu=helpmenu)
root.config(menu=mymenu)


root.mainloop() # packed the all code in the main of the editor......