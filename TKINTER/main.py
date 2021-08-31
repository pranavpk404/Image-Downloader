import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
from time import sleep
from tkinter import *
from tkinter import filedialog

import pyautogui as pa
from ttkthemes import ThemedStyle

root = tk.Tk()
style = ThemedStyle(root)
style.set_theme("clearlooks")
root.geometry("700x120")
mainmenu = Menu(root)
root.iconbitmap('icon.ico')
root.title("image downloader")


def wallpapercave():
    webbrowser.open("https://wallpapercave.com/")


def wallpaperhd():
    webbrowser.open("https://www.hdwallpapers.in/")


def wallpaperalphacoders():
    webbrowser.open("https://wall.alphacoders.com/")


def wallpapersupercars():
    webbrowser.open("https://www.wsupercars.com/")


try:

    def Fast_download():
        pa.press('win')
        pa.write('powershell')
        sleep(2)
        pa.press('enter')
        sleep(5)
        pathh = path.get()
        pa.write('cd \"' + pathh + "\"")
        pa.press('enter')
        linkk = link.get()
        pa.write('image-scraper  ' + linkk)
        pa.press('enter')
        pa.write('Remove-Item (Get-PSReadlineOption).HistorySavePath')
        pa.press('enter')
        pa.write('exit')
        sleep(5)
        pa.press('enter')


    def widgets():
        ttk.Label(root, text="link from you want to download images:").grid(row=1, column=0, pady=5, padx=5)
        ttk.Entry(root, width=55, textvariable=link).grid(row=1, column=1, pady=5, padx=5, columnspan=2)
        ttk.Label(root, text="Destination :").grid(row=2, column=0, pady=5, padx=5)
        ttk.Entry(root, width=40, textvariable=path).grid(row=2, column=1, pady=5, padx=5)

        ttk.Button(root, text="Download", command=Fast_download).grid()
        ttk.Button(root, text="Browse", command=Browse).grid(row=2, column=2, pady=1, padx=1)
        ttk.Button(root, text="Default Place", command=default).grid(row=3, column=2)

        m1 = Menu(mainmenu, tearoff=0)

        m1.add_command(label="Wallpaper Cave", command=wallpapercave)
        m1.add_command(label="Wallpaper HD", command=wallpaperhd)
        m1.add_command(label="Wallpaper Alpha coders", command=wallpaperalphacoders)
        m1.add_command(label="Wallpaper Wesupercars", command=wallpapersupercars)

        root.config(menu=mainmenu)
        mainmenu.add_cascade(label='Website', menu=m1)


    def default():
        path.set("E:\\")


    def Browse():
        download_directory = filedialog.askdirectory()
        path.set(download_directory)


    path = StringVar()
    link = StringVar()
    widgets()
    root.mainloop()

except Exception as e:
    print(e)
