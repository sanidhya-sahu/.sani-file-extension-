import os
cmd="pip install decodesani"
os.system(cmd)
from decodesani import *
from tkinter import *
from tkinter import filedialog as fd
root = Tk()
root.geometry("500x500")
def select_file():
    filetypes = (
        ('sani files', '*.sani'),
        ('All files', '*.*')
    )
    global filename
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    print(filename)
select_file()
with open(f"{filename}", "r") as f:
    r = f.read()
    print(r)
o = deco(r)
o.decosani()
print(o)
bot = Label(text=o, bg="cyan", fg="black", padx="20", pady="20", font="comicsans 10 bold",
            borderwidth=5, relief="groove",wraplength=450)
# important pack option
bot.pack(side="top", fill=X)
# root.wm_iconbitmap('favicon.ico')
root.mainloop()
