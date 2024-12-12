class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak(self):
        print(f'hewan {self.nama} ini memakan {self.makanan} ini juga hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}')  

# C1 = Animal('buaya', 'daging', 'amphibi', 'bertelur')  
# C1.cetak()       



