# Data dummy
data_paket = [
    {"resi": "PKT001", "nama": "Andi Saputra",
     "tujuan": "Jakarta"},
    {"resi": "PKT002", "nama": "Budi Santoso",
     "tujuan": "Bandung"},
    {"resi": "PKT003", "nama": "Citra Lestari",
     "tujuan": "Surabaya"},
    {"resi": "PKT004", "nama": "Dinda Permata",
     "tujuan": "Yogyakarta"},
    {"resi": "PKT005", "nama": "Eko Pratama",
     "tujuan": "Semarang"},
    {"resi": "PKT006", "nama": "Fajar Ramadhan",
     "tujuan": "Malang"},
    {"resi": "PKT007", "nama": "Gita Maharani",
     "tujuan": "Tangerang"},
    {"resi": "PKT008", "nama": "Hendra Wijaya",
     "tujuan": "Bekasi"},
    {"resi": "PKT009", "nama": "Intan Safitri",
     "tujuan": "Depok"},
    {"resi": "PKT010", "nama": "Joko Firmansyah",
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
