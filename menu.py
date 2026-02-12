import tkinter as tk
import os

class SweetMenuUI:
    def __init__(self, root):
        self.root = root
        
        # Renk Paleti
        self.PEMBE_SEKER = "#ff69b4"
        self.BEYAZ_TEMA = "#ffffff"
        self.GRI_YAZI = "#444444"
        
        # Durum Değişkenleri
        self.aktif_kategori = "ESP"
        self.menu_x, self.menu_y = 450, 250
        self.menu_gen, self.menu_yuk = 700, 500
        self.drag_data = {"x": 0, "y": 0}
        self.hover_x = False

        self.canvas = tk.Canvas(root, width=1920, height=1080, bg="black", highlightthickness=0)
        self.canvas.pack()

        # Bindings
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Motion>", self.on_mouse_move)

    def on_mouse_move(self, event):
        mx, my = event.x, event.y
        # X butonu hover (üstüne gelince) kontrolü
        if self.menu_x + self.menu_gen - 40 <= mx <= self.menu_x + self.menu_gen and \
           self.menu_y <= my <= self.menu_y + 40:
            self.hover_x = True
        else:
            self.hover_x = False

    def on_click(self, event):
        mx, my = event.x, event.y
        # Kapatma (X)
        if self.menu_x + self.menu_gen - 40 <= mx <= self.menu_x + self.menu_gen and \
           self.menu_y <= my <= self.menu_y + 40:
            os._exit(0)

        # Sürükleme kontrolü
        if self.menu_x <= mx <= self.menu_x + self.menu_gen - 45 and self.menu_y <= my <= self.menu_y + 40:
            self.drag_data["x"] = mx - self.menu_x
            self.drag_data["y"] = my - self.menu_y
        
        # Kategoriler (Senin istediğin 65 birimlik geniş aralıklar)
        kategoriler = ["ESP", "AIMBOT", "MISC", "SKINS", "SETTINGS"]
        for i, kat in enumerate(kategoriler):
            y_bas = self.menu_y + 125 + (i * 65) 
            if self.menu_x <= mx <= self.menu_x + 160 and y_bas <= my <= y_bas + 40:
                self.aktif_kategori = kat

    def on_drag(self, event):
        mx, my = event.x, event.y
        if self.drag_data["x"] != 0:
            self.menu_x = mx - self.drag_data["x"]
            self.menu_y = my - self.drag_data["y"]

    def render(self):
        self.canvas.delete("all")
        x, y, w, h = self.menu_x, self.menu_y, self.menu_gen, self.menu_yuk

        # Ana Arka Plan
        self.canvas.create_rectangle(x, y, x+w, y+h, fill=self.BEYAZ_TEMA, outline=self.PEMBE_SEKER, width=2)
        
        # X BUTONU (Fixlendi: Pembe, hover olunca kırmızı)
        bg_x = "red" if self.hover_x else self.BEYAZ_TEMA
        fg_x = "white" if self.hover_x else self.PEMBE_SEKER
        self.canvas.create_rectangle(x+w-39, y+1, x+w-1, y+39, fill=bg_x, outline="")
        self.canvas.create_text(x+w-20, y+20, text="X", fill=fg_x, font=("Arial", 12, "bold"))

        # SOL PANEL & ŞEKERLİ LOGO
        self.canvas.create_rectangle(x, y, x+160, y+h, fill="#fff5f8", outline=self.PEMBE_SEKER)
        self.canvas.create_text(x+80, y+40, text="🍭", font=("Arial", 18)) # ŞEKER GERİ GELDİ!
        self.canvas.create_text(x+80, y+65, text="SWEET", fill=self.PEMBE_SEKER, font=("Impact", 28, "bold"))

        # KATEGORİLER
        kategoriler = ["ESP", "AIMBOT", "MISC", "SKINS", "SETTINGS"]
        for i, kat in enumerate(kategoriler):
            y_pos = y + 125 + (i * 65)
            if self.aktif_kategori == kat:
                self.canvas.create_rectangle(x+10, y_pos, x+150, y_pos+40, fill=self.PEMBE_SEKER, outline="")
                self.canvas.create_text(x+80, y_pos+20, text=kat, fill="white", font=("Verdana", 9, "bold"))
            else:
                self.canvas.create_text(x+80, y_pos+20, text=kat, fill=self.GRI_YAZI, font=("Verdana", 9))

        # ALT BİLGİ
        self.canvas.create_text(x+175, y+h-25, text="🍬 Created by Willton", fill="#aaa", anchor="nw", font=("Arial", 7))
        self.canvas.create_text(x+w-25, y+h-25, text="v2.0.0-Candy", fill="#aaa", anchor="ne", font=("Arial", 7))