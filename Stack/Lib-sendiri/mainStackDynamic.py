from StackPacket import StackPaket

data_paket = [
    {"resi": "PKT001", "nama": "Andi Galon",
     "tujuan": "Jakarta"},
    {"resi": "PKT002", "nama": "Budi Tambal Ban",
     "tujuan": "Bandung"},
    {"resi": "PKT003", "nama": "Cecep Alat Tulis",
     "tujuan": "Surabaya"},
    {"resi": "PKT004", "nama": "Dodi Kompor Gas",
     "tujuan": "Yogyakarta"}
]

stack = StackPaket()

for paket in data_paket:
    stack.push(paket)

stack.display()

print("\nMelihat paket teratas:")
stack.peek()

print("\nMengeluarkan paket:")
stack.pop()

print("\nStack setelah pop:")
stack.display()
