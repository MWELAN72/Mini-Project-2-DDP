from datetime import datetime

akun = {
    "admin": {
        "password": "mario72",
        "role": "admin"
    },
    "user": {
        "password": "mario72",
        "role": "user"
    }
}

data_game = []


def login():
    while True:
        print("\n=== LOGIN ===")

        username = input("Username: ")
        password = input("Password: ")

        if username in akun and akun[username]["password"] == password:
            print("Login berhasil!")
            print("Role:", akun[username]["role"])
            return akun[username]["role"]

        else:
            print("Username atau password salah. Silakan coba lagi.")

def tambah_data():
    print("\n=== TAMBAH DATA GAME ===")

    nama = input("Nama game: ")
    platform = input("Platform: ")
    tanggal = input("Tanggal rilis (DD-MM-YYYY): ")

    if nama == "" or platform == "" or tanggal == "":
        print("Data tidak boleh kosong.")
        return

    try:
        datetime.strptime(tanggal, "%d-%m-%Y")

        data = {
            "nama": nama,
            "platform": platform,
            "tanggal": tanggal
        }

        data_game.append(data)

        print("Data game berhasil ditambahkan.")

    except ValueError:
        print("Format tanggal tidak valid.")
        print("Gunakan format DD-MM-YYYY.")

def lihat_data():
    print("\n=== DATA GAME ===")

    if len(data_game) == 0:
        print("Belum ada data game.")
    else:
        for i, data in enumerate(data_game, start=1):
            print(
                i,
                ". Nama:", data["nama"],
                "| Platform:", data["platform"],
                "| Tanggal:", data["tanggal"]
            )

def ubah_data():
    print("\n=== UBAH DATA GAME ===")

    if len(data_game) == 0:
        print("Belum ada data game.")
        return

    lihat_data()

    try:
        nomor = int(input("Masukkan nomor data yang ingin diubah: "))

        if nomor >= 1 and nomor <= len(data_game):

            nama_baru = input("Nama game baru: ")
            platform_baru = input("Platform baru: ")
            tanggal_baru = input("Tanggal rilis baru (DD-MM-YYYY): ")

            if nama_baru == "" or platform_baru == "" or tanggal_baru == "":
                print("Data tidak boleh kosong.")
                return

            try:
                datetime.strptime(tanggal_baru, "%d-%m-%Y")

                data_game[nomor - 1] = {
                    "nama": nama_baru,
                    "platform": platform_baru,
                    "tanggal": tanggal_baru
                }

                print("Data game berhasil diubah.")

            except ValueError:
                print("Format tanggal tidak valid.")
                print("Gunakan format DD-MM-YYYY.")

        else:
            print("Data tidak ditemukan.")

    except ValueError:
        print("Nomor data harus berupa angka.")


def hapus_data():
    print("\n=== HAPUS DATA GAME ===")

    if len(data_game) == 0:
        print("Belum ada data game.")
        return

    lihat_data()

    try:
        nomor = int(input("Masukkan nomor data yang ingin dihapus: "))

        if nomor >= 1 and nomor <= len(data_game):
            data_game.pop(nomor - 1)
            print("Data game berhasil dihapus.")

        else:
            print("Data tidak ditemukan.")

    except ValueError:
        print("Nomor data harus berupa angka.")


while True:

    role = login()

    if role == "admin":

        while True:
            print("\n=== SISTEM PENDATAAN JADWAL RILIS GAME ===")
            print("1. Tambah Data Game")
            print("2. Lihat Data Game")
            print("3. Ubah Data Game")
            print("4. Hapus Data Game")
            print("5. Logout")

            pilihan = input("Pilih menu (1-5): ")

            if pilihan == "1":
                tambah_data()

            elif pilihan == "2":
                lihat_data()

            elif pilihan == "3":
                ubah_data()

            elif pilihan == "4":
                hapus_data()

            elif pilihan == "5":
                print("Logout berhasil.")
                break

            else:
                print("Menu tidak tersedia. Silakan pilih 1-5.")

    elif role == "user":

        while True:
            print("\n=== MENU USER ===")
            print("1. Lihat Data Game")
            print("2. Logout")

            pilihan = input("Pilih menu (1-2): ")

            if pilihan == "1":
                lihat_data()

            elif pilihan == "2":
                print("Logout berhasil.")
                break

            else:
                print("Menu tidak tersedia. Silakan pilih 1-2.")