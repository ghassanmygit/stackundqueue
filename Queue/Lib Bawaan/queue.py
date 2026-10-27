from collections import deque

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

queue = deque()

for paket in data_paket:
    queue.append(paket)
    print("Paket berhasil ditambahkan:", paket["resi"])

print("\n=== ISI QUEUE ===")
for paket in queue:
    print(paket["resi"], "-", paket["nama"],
          "-", paket["tujuan"])

print("\n=== PAKET TERDEPAN ===")
if queue:
    print(queue[0]["resi"])

print("\n=== DEQUEUE ===")
if queue:
    paket = queue.popleft()
    print("Paket dikeluarkan:", paket["resi"])

print("\n=== QUEUE SETELAH DEQUEUE ===")
for paket in queue:
    print(paket["resi"], "-", paket["nama"],
          "-", paket["tujuan"])