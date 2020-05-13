from tkinter import*

from tkinter import ttk

font_style = Tk()
font_style.title("Font")
font_style.geometry('400x400')

#font family
jlabel1 = Label(font_style,text = 'font family')
jlabel1.grid(row=0,column = 1)
font_tuple = font.families()
font_family = StringVar()
font_box = ttk.Combobox(font_style, textvariable = font_family,state = 'readonly')
font_box["values"] = font_tuple
#font_box.current(font_family.index("Ariel"))
font_box.grid(row = 0,column = 3)

# font size
jlabel2=Label(font_style,text = 'font size')
jlabel2.grid(row = 1,column = 1)
font_size = IntVar()
size = ttk.Combobox(font_style,textvariable = font_size,state = 'readonly')
size["values"]=tuple(range(2,100,2))
size.current("2")
size.grid(row =  1, column = 3)

font_now = "ariel"
font_size_now = 2

def change_font(fapp):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font = (font_now,font_size_now))

def change_size(fapp):
    global font_size_now
    font_size_now = font_size.get()
    text_editor.configure(font = (font_size_now,font_now))

font_box.bind("<<ComboboxSelected>>",change_font)
size.bind("<<ComboboxSelected>>",change_size)





font_style.mainloop()