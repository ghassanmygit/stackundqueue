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


KAPASITAS = 3


stack = [None] * KAPASITAS


top = -1


def push(paket):
    global top

    if top == KAPASITAS - 1:
        print("Stack penuh! Paket tidak bisa ditambahkan.")
        return

    top += 1
    stack[top] = paket
    print("Paket masuk:", paket["resi"])

def peek():
    if top == -1:
        print("Stack kosong!")
    else:
        print("Paket teratas:", stack[top]["resi"])

def pop():
    global top

    if top == -1:
        print("Stack kosong! Tidak ada paket untuk dikeluarkan.")
        return

    paket = stack[top]
    stack[top] = None
    top -= 1

    print("Paket dikeluarkan:", paket["resi"])



def tampilkan_stack():
    print("=== ISI STACK ===")

    if top == -1:
        print("Stack kosong!")
        return

    for i in range(top, -1, -1):
        paket = stack[i]
        print(
            paket["resi"], "-",
            paket["nama"], "-",
            paket["tujuan"]
        )



print("=== PUSH ===")
for paket in data_paket[:3]:
    push(paket)


print()
tampilkan_stack()


print("\n=== PEEK ===")
peek()


print("\n=== UJI KAPASITAS ===")
push(data_paket[3])


print("\n=== POP ===")
pop()


print()
tampilkan_stack()