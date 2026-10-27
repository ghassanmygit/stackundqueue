class StackPaket: 
    
    #nentuin kapasitas stack
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.top = -1
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.kapasitas - 1
    
    def push(self, paket):
        if self.is_full():
            print("Stack Penuh!")
        else:
            self.top += 1 #masukin data dengan push()
            self.data[self.top] = paket
            print("Paket berhasil ditambahkan!")
            
    def pop(self):
        if self.is_empty():
            print("Stack Kosong!")
        else:
            paket = self.data[self.top] #ngeluarin paket dengan pop()
            self.data[self.top] = None
            self.top -= 1
            print("Paket dikeluarkan:", paket["resi"]) 

    #lihat paket dengan peek()
    def peek(self):
        if self.is_empty():
            print("Stack Kosong!")
        else:
            print("Paket teratas:",
                self.data[self.top]["resi"])
    
    #nampilkan isi Stack dengan display()        
    def display(self):
        if self.is_empty():
            print("Stack kosong!")
        else:
            print("\nIsi Stack (atas ke bawah):")
            for i in range(self.top, -1, -1): 
                paket = self.data[i]
                print(
                    paket["resi"], "-",
                    paket["nama"], "-",
                    paket["tujuan"]
                )