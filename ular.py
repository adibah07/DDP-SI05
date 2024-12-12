from animals import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup,berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.jenis = jenis_ular

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini adalah warna {self.warna} dan ini jenis ular {self.jenis}')

print('--- objek pertama ---')
sawah = ular('ular sawah', 'serangga', 'darat', 'bertelur', 'hijau', 'melilit')   
sawah.cetak_ular() 

print('\n--- objek kedua ---')
cobra = ular('ular cobra', 'tikus', 'darat', 'bertelur', 'hitam bercampur coklat dan abu', 'berbisa')   
cobra.cetak_ular()
