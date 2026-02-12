import pymem
import pymem.process

class Memory:
    def __init__(self):
        try:
            self.pm = pymem.Pymem("cs2.exe")
            print("[+] CS2 Bulundu!")
            self.client_base = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
            print(f"[+] Client.dll Adresi: {hex(self.client_base)}")
        except Exception as e:
            print("[-] CS2 Bulunamadı! Oyunu açtın mı?")
            exit()

    def read_ptr(self, address):
        try:
            return self.pm.read_longlong(address)
        except: return 0

    def read_int(self, address):
        try:
            return self.pm.read_int(address)
        except: return 0

    def read_float(self, address):
        try:
            return self.pm.read_float(address)
        except: return 0.0

    def read_vec3(self, address):
        try:
            x = self.pm.read_float(address)
            y = self.pm.read_float(address + 4)
            z = self.pm.read_float(address + 8)
            return x, y, z
        except: return 0.0, 0.0, 0.0