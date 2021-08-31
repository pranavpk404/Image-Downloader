import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
from pyautogui import press, write
from time import sleep


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
        press('win')
        write('powershell')
        sleep(2)
        press('enter')
        sleep(5)
        path = self.place_entry.text()
        write('cd \"' + path + "\"")
        press('enter')
        link = self.link_entry.text()
        write('image-scraper  ' + link)
        press('enter')
        write('Remove-Item (Get-PSReadlineOption).HistorySavePath')
        press('enter')
        write('exit')
        sleep(5)
        press('enter')

    def default(self):
        self.place_entry.setText("E:\\")

    def browse(self):
        download_directory = QFileDialog.getExistingDirectory()
        self.place_entry.setText(download_directory)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    app.exec_()
