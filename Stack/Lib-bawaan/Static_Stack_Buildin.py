data_paket = [
    {"resi": "PKT001", "nama": "Andi Saputra", "tujuan": "Jakarta"},
    {"resi": "PKT002", "nama": "Budi Santoso", "tujuan": "Bandung"},
    {"resi": "PKT003", "nama": "Citra Lestari", "tujuan": "Surabaya"},
    {"resi": "PKT004", "nama": "Dinda Permata", "tujuan": "Yogyakarta"},
    {"resi": "PKT005", "nama": "Eko Pratama", "tujuan": "Semarang"},
    {"resi": "PKT006", "nama": "Fajar Ramadhan", "tujuan": "Malang"},
    {"resi": "PKT007", "nama": "Gita Maharani", "tujuan": "Tangerang"},
    {"resi": "PKT008", "nama": "Hendra Wijaya", "tujuan": "Bekasi"},
    {"resi": "PKT009", "nama": "Intan Safitri", "tujuan": "Depok"},
    {"resi": "PKT010", "nama": "Joko Firmansyah", "tujuan": "Bogor"}
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