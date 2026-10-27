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

kapasitas = 3
queue = []

# Memasukkan paket ke Queue 
for paket in data_paket:
    if len(queue) == kapasitas:
        print("Queue Penuh! Gagal enqueue:", paket["resi"])
    else:
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
    paket = queue.pop(0)
    print("Paket dikeluarkan:", paket["resi"])

print("\n=== QUEUE SETELAH DEQUEUE ===")
for paket in queue:
    print(paket["resi"], "-", paket["nama"],
          "-", paket["tujuan"])
