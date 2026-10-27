# Data dummy
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

# Membuat Stack
stack = []

# Memasukkan 3 paket ke Stack
for paket in data_paket[:3]:
    stack.append(paket)

# Menampilkan isi Stack
print("=== ISI STACK ===")
for paket in reversed(stack):
    print(paket["resi"], "-", paket["nama"],
          "-", paket["tujuan"])

# Melihat paket teratas
print("\n=== PAKET TERATAS ===")
if stack:
    print(stack[-1]["resi"])

# Mengeluarkan paket teratas
print("\n=== POP ===")
if stack:
    paket = stack.pop()
    print("Paket dikeluarkan:", paket["resi"])

# Menampilkan Stack setelah pop
print("\n=== STACK SETELAH POP ===")
for paket in reversed(stack):
    print(paket["resi"], "-", paket["nama"],
          "-", paket["tujuan"])
