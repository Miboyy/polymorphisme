class Helm:
    def __init__(self, ukuran):
        self.ukuran = ukuran
    
    def deskripsi(self):
        print(f"Ini adalah helm dengan ukuran standar {self.ukuran}")

class KacaHelm(Helm):
    def deskripsi(self):
        print(f"Ini adalah helm khusus dengan ukuran {self.ukuran}")

class HelmMotor(Helm):
    def deskripsi(self):
        print(f"Ini adalah helm motor dengan ukuran {self.ukuran}")

# Contoh polymorphisme
def tampilkan_deskripsi(helm):
    helm.deskripsi()

# Penggunaan
helm_standar = Helm(58)
helm_kaca = KacaHelm(60)
helm_motor = HelmMotor(62)

tampilkan_deskripsi(helm_standar)
tampilkan_deskripsi(helm_kaca)
tampilkan_deskripsi(helm_motor)