from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.colorchooser import *
import time
from tkinter import ttk
import tkinter.font as font


from saveF import *
import Tools
import os
fapp = Tk()
fapp.title("notepad")
fapp.geometry("800x600")
tool_bar = Label(fapp)
tool_bar.pack(side = TOP, fill = X)
#text editor
text_editor = Text(fapp,width = 800,height = 600 ,bg = 'gray',fg = 'white')
scroll_bar = Scrollbar(text_editor)
scroll_bar.pack(side = RIGHT,fill = Y)
text_editor.pack(fill = BOTH , expand = TRUE)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

def newfile():
    new = fapp
    new.title("untitled")

    file = None
    text_editor.delete(1.0,END)


def openfile():
   global file

   file =askopenfilename(defaultextension=".txt",filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
   if file=="":
       file=None

   else:
       fapp.title(os.path.basename(file)+" - notepad")
       text_editor.delete(1.0,END)
       f = open(file,'r')
       text_editor.insert(1.0,f.read())
       f.close()




def savef():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'untitled.txt',defaultextension = '.txt',filetypes = [("All files","*.*"),("Text Documents","*.txt")])

        if file=="":
            file = None

        else :
            f = open(file,'w')
            f.write(text_editor.get(1.0,END))
            f.close()

            fapp.title(os.path.basename(file)+"-notepad")
            print("file saved")

    else :
        f = open(file, 'w')
        f.write(text_editor.get(1.0, END))
        f.close()
def saveAs():
    global file
    file = asksaveasfilename(initialfile='untitled.txt', defaultextension='.txt',
                             filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        f = open(file, 'w')
        f.write(text_editor.get(1.0, END))
        f.close()

        fapp.title(os.path.basename(file) + "-notepad")
        print("file saved")

def exit():
    fapp.destroy()

def fontstar():
    top = Toplevel(fapp)
    top .geometry("300x300")
    top.title("Fonts")
    top.resizable(False,False)
    jlabel = Label(top,width = 10,height = 3 , text = 'Font-style')
    font_tuple = font.families()
    font_variable = StringVar()
    font_box = ttk.Combobox(top,textvariable = font_variable,state = 'readonly')
    font_box["values"]=font_tuple
    font_box.current(font_tuple.index('Arial'))
    font_box.grid(row=0, column=1, padx=5, pady=5)
    #font_box.current(font_tuple.index("Ariel"))
    jlabel.grid(row = 0,column = 0)

    #size
    jlabel1 = Label(top,text = 'font-size',width = 10,height = 3).grid(row = 2,column = 0)
    font_var = IntVar()
    font_size = ttk.Combobox(top,textvariable = font_var,state = 'readonly')
    font_size["values"] = tuple(range(2,100,2))
    font_size.current(8)
    font_size.grid(row = 2,column = 1,padx = 5,pady = 5)

    font_now = "Arial"
    fontsize = "16"
    def change_font(fapp):
       global font_now

       font_now = font_variable.get()
       text_editor.configure(font = (font_now,fontsize))


    def change_fontsize(fapp):
       global fontsize

       fontsize = font_var.get()
       text_editor.configure(font = (font_now,fontsize))

    font_box.bind("<<ComboboxSelected>>",change_font)
    font_size.bind("<<ComboboxSelected>>",change_fontsize)
    print(font.Font(font = text_editor["font"]).actual())
    def _bold():
        text_get = font.Font(font = text_editor["font"])
        if text_get.actual()["weight"]== 'normal':
            text_editor.configure(font=(font_now,fontsize,'bold'))
        if text_get.actual()["weight"]== 'bold':
            text_editor.configure(font = (font_now,fontsize,'normal'))
    def _italic():
        text_get = font.Font(font = text_editor["font"])
        if text_get.actual()["slant"]=='roman':
            text_editor.configure(font=(font_now,fontsize,'italic'))
        if text_get.actual()["slant"]=='italic':
            text_editor.configure(font = (font_now,fontsize,'roman'))


    button_bold = Button(top,text = "Bold",font = "Arial 10 bold",width = 10,command = _bold).grid(row = 5,column =0 , padx = 5,pady =5)
    button_italic = Button(top, text="italic", font="Arial 10 bold italic" , width = 10,command = _italic).grid(row=5, column=1, padx=5, pady=5)




def findword():
    import findwords
def _undo():
    text_editor.event_generate("<<Undo>>")
def cut():
    text_editor.event_generate("<<Cut>>")
def copy():
    text_editor.event_generate("<<Copy>>")
def paste():
    text_editor.event_generate("<<Paste>>")

def about():
    showinfo(title="about",message="created by abhishek kumar")


status_bar = ttk.Label(fapp,text = 'status bar')
status_bar.pack(side=BOTTOM)

word_change = False

def change_word(event = None):
    global word_change

    if text_editor.edit_modified():
        word_change = TRUE
        word = len(text_editor.get(1.0,"end-1c").split())
        character = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bar.configure(text = (character   ,   word))
    text_editor.edit_modified(False)
def statusbar():
    text_editor.bind("<<Modified>>",change_word)

def date_time():
    localtime = time.asctime(time.localtime(time.time()))
    print("print " + localtime)
    showinfo(title='date&time',message=localtime)



menu = Menu(fapp)
fapp.config(menu=menu)
#fileMenu
filemenu = Menu(menu,tearoff = False)
menu.add_cascade(label = 'file',menu = filemenu)
filemenu.add_command(label = 'New',accelerator = 'ctrl+N',command = newfile)
filemenu.add_command(label = 'open ',accelerator = 'ctrl+O',command = openfile)
filemenu.add_command(label = 'save',accelerator = 'ctrl+S',command = savef)
filemenu.add_command(label = 'save as',command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = 'page setup')
filemenu.add_command(label ='print ',accelerator = 'ctrl+P')
filemenu.add_separator()
filemenu.add_command(label = 'exit',command = exit)
#edit
edit =Menu(fapp,tearoff= False)
menu.add_cascade(label = 'Edit',menu = edit)
edit.add_command(label = 'undo ',accelerator = 'ctrl+Z',command = _undo)
edit.add_separator()
edit.add_command(label = 'Cut ',accelerator = 'ctrl+X',command = cut)
edit.add_command(label = 'Copy ',accelerator = 'ctrl+C',command = copy)
edit.add_command(label = 'Paste ',accelerator = 'ctrl+V',command = paste)
edit.add_command(label = 'Delete',accelerator = 'del')
edit.add_separator()
edit.add_command(label = 'Find ',accelerator = 'ctrl+F',command = findword)
edit.add_command(label = 'Find Next ',accelerator = 'F3')
edit.add_command(label = 'Replace',accelerator = 'ctrl+H')
edit.add_command(label = 'Goto  ',accelerator = 'ctrl+G')
edit.add_separator()
edit.add_command(label = 'select All',accelerator = 'ctrl+A')
edit.add_command(label = 'Time/Date',command = date_time)
#view
view = Menu(fapp,tearoff = False)
menu.add_cascade(label = 'View',menu = view)

view.add_command(label = 'Zoom')
view.add_command(label = 'status bar',command = statusbar )
#format
format = Menu(fapp,tearoff=False)
menu.add_cascade(label = 'Format',menu = format)
format.add_command(label = 'word wrap')
format.add_command(label = 'font...',command = fontstar)
#Help
helpmenu = Menu(fapp,tearoff = False)
menu.add_cascade(label = 'Help',menu = helpmenu)
helpmenu.add_command(label = 'view help')
helpmenu.add_command(label = 'about',command = about)

fapp.mainloop()

