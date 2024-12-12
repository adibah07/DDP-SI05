from animals import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ikan
        self.ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'ini adalah jenis ikan {self.ikan} dan ikan ini berwarna {self.warna}')

print('--- objek pertama ---')
nemo = ikan('ikan nemo','plankton', 'air', 'bertelur', 'putih oren', 'air laut')
nemo.cetak_ikan()

print('\n--- objek kedua ---')
hiu = ikan('ikan hiu','ikan kecil dan invertebrata', 'air', 'bertelur dan beranak', 'biru abu', 'air laut')
hiu.cetak_ikan()