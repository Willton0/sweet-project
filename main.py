import tkinter as tk
import win32gui, win32con, win32api
from menu import SweetMenuUI
from memory import Memory # Senin önceki memory dosyan
from offsets import Offsets

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry("1920x1080+0+0")
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "black")
        self.root.configure(bg="black")

        # Menü UI Sınıfını Başlat
        self.menu_ui = SweetMenuUI(self.root)
        self.menu_acik = True

        self.update_loop()

    def set_click_through(self, enabled):
        hwnd = win32gui.FindWindow(None, "SWEET_Candy_Overlay")
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        if enabled:
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
        else:
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style & ~win32con.WS_EX_TRANSPARENT)

    def update_loop(self):
        # INSERT Tuşuna Basılma Kontrolü
        if win32api.GetAsyncKeyState(win32con.VK_INSERT) & 1:
            self.menu_acik = not self.menu_acik
            self.set_click_through(not self.menu_acik)

        if self.menu_acik:
            self.menu_ui.render()
        else:
            self.menu_ui.canvas.delete("all")
            # Burada ESP çizim fonksiyonlarını çağıracağız (Gelecek ders)

        self.root.after(10, self.update_loop)

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()