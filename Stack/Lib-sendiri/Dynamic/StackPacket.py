class StackPaket:

    #stack dinamis: tidak ada kapasitas, list tumbuh otomatis
    def __init__(self):
        self.data = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, paket):
        self.data.append(paket) #masukin data dengan push()
        self.top += 1
        print("Paket berhasil ditambahkan!")

    def pop(self):
        if self.is_empty():
            print("Stack Kosong!")
        else:
            paket = self.data.pop() #ngeluarin paket dengan pop()
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
