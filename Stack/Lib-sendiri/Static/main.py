from stack_paket import StackPaket

data_paket = [
    {"resi": "PKT001", "nama": "Andi Galon",
     "tujuan": "Jakarta"},
    {"resi": "PKT002", "nama": "Budi Tambal Ban",
     "tujuan": "Bandung"},
    {"resi": "PKT003", "nama": "Cecep Alat Tulis",
     "tujuan": "Surabaya"},
    {"resi": "PKT004", "nama": "Dodi Kompor Gas",
     "tujuan": "Yogyakarta"},
    {"resi": "PKT005", "nama": "Eko Agen BRI",
     "tujuan": "Semarang"},
    {"resi": "PKT006", "nama": "Fajar Bengkel",
     "tujuan": "Malang"},
    {"resi": "PKT007", "nama": "Gilang Las",
     "tujuan": "Tangerang"},
    {"resi": "PKT008", "nama": "Surya Toko Bangunan",
     "tujuan": "Bekasi"},
    {"resi": "PKT009", "nama": "Indra Sedot WC",
     "tujuan": "Depok"},
    {"resi": "PKT010", "nama": "Joko Solo King",
     "tujuan": "Bogor"}
]

stack = StackPaket(10)

for paket in data_paket[:3]:
    stack.push(paket)

stack.display()

print("\nMelihat paket teratas:")
stack.peek()

print("\nMengeluarkan paket:")
stack.pop()

print("\nStack setelah pop:")
stack.display()
