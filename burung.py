from animals import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}') 

# Object pertama
print('--- objek pertama ---')
beo = Burung('burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'kamu jeleqqq')        
beo.cetak_burung()


      
# Object kedua
print('\n--- objek kedua ---')
merpati = Burung('Burung merpati', 'biji-bijian', 'udara', 'bertelur', 'putih', 'cuakkss')
merpati.cetak_burung()