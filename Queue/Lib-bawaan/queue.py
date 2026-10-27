from collections import deque

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