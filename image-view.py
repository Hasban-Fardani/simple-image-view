#!/usr/bin/python3
import os, getpass
from tkinter import Tk, Label, Button
from PIL import ImageTk, Image

window = Tk()
window.title("simple image view")


username = getpass.getuser()
path = f"/home/{username}/Downloads"
all_file = os.listdir(path)
all_image = []
for i in all_file:    
    if ".png" in i or ".jpg" in i or ".jpeg" in i:
        img = ImageTk.PhotoImage(Image.open(path + "/" + i))
        all_image.append(img)
    else:
        pass


path = f"/home/{username}/Pictures"
all_file = os.listdir(path)
for i in all_file:    
    if ".png" in i or ".jpg" in i or ".jpeg" in i:
        img = ImageTk.PhotoImage(Image.open(path + "/" + i))
        all_image.append(img)
    else:
        pass


index = 0
label = Label(image=all_image[index])
label.grid(row=0, column=0, columnspan=3)


def gantiGambar(operasi,number): 
    global label
    global index
    global tombol_kembali
    global tombol_selanjutnya
    label.grid_forget()
    label = Label(image=all_image[number])
    label.grid(row=0, column=0, columnspan=3)
    if operasi == ">>":
        index = index + 1 if index != len(all_image)-1 else 0
    elif operasi == "<<":
        index = index - 1 if index != 0 else -1
    tombol_kembali = Button(window, text="<<", command=lambda: gantiGambar("<<", index))
    tombol_selanjutnya = Button(window, text=">>", command=lambda: gantiGambar(">>", index))
    tombol_keluar = Button(window, text="Exit Program", command=window.quit)
    tombol_kembali.grid(row=1, column=0)
    tombol_selanjutnya.grid(row=1, column=2)
    tombol_keluar.grid(row=1, column=1)


selanjutnya = index + 1 if index != len(all_image) else 0
sebelumnya = index - 1 if index != 0 else -1
tombol_kembali = Button(window, text="<<", command=lambda: gantiGambar("<<",sebelumnya))
tombol_selanjutnya = Button(window, text=">>", command=lambda: gantiGambar(">>",selanjutnya))
tombol_keluar = Button(window, text="Exit Program", command=window.quit)

tombol_kembali.grid(row=1, column=0)
tombol_selanjutnya.grid(row=1, column=2)
tombol_keluar.grid(row=1, column=1)

window.mainloop()
