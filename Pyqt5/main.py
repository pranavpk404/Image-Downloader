import webbrowser
from time import sleep

import pyautogui as pa
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.actionwallpapercave.triggered.connect(self.wallpapercave)
        self.actionwallpaperhd.triggered.connect(self.wallpaperhd)
        self.actionWallpaperalphacoders.triggered.connect(self.wallpaperalphacoders)
        self.actionwallpapersupercars.triggered.connect(self.wallpapersupercars)
        self.browse_button.clicked.connect(self.browse)
        self.download_button.clicked.connect(self.download)
        self.default_button.clicked.connect(self.default)

    @staticmethod
    def wallpapercave():
        webbrowser.open("https://wallpapercave.com/")

    @staticmethod
    def wallpaperhd():
        webbrowser.open("https://www.hdwallpapers.in/")

    @staticmethod
    def wallpaperalphacoders():
        webbrowser.open("https://wall.alphacoders.com/")

    @staticmethod
    def wallpapersupercars():
        webbrowser.open("https://www.wsupercars.com/")

    def download(self):
        pa.press('win')
        pa.write('powershell')
        sleep(2)
        pa.press('enter')
        sleep(5)
        path = self.place_entry.text()
        pa.write('cd \"' + path + "\"")
        pa.press('enter')
        link = self.link_entry.text()
        pa.write('image-scraper  ' + link)
        pa.press('enter')
        pa.write('Remove-Item (Get-PSReadlineOption).HistorySavePath')
        pa.press('enter')
        pa.write('exit')
        sleep(5)
        pa.press('enter')

    def default(self):
        self.place_entry.setText("E:\\")

    def browse(self):
        download_directory = QFileDialog.getExistingDirectory()
        self.place_entry.setText(download_directory)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    app.exec_()
