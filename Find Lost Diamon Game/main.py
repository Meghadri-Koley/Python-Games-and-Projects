# Data (Matriks 5x5/List of List/Nested List)
boardGame = [
    ["x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x"],
    ["x", "x", "x", "x", "x"],
    ["O", "x", "x", "x", "x"]
    ]

## Variable Penampung Dari Operasi List Comprehension
# Target Manipulasi
steps = []

# Hasil Manipulasi
stepsComprehension = []

# Pure Function For Clear Terminal
def clear():
    import os
    return os.system('cls')

## 01 - UI Function
# Welcome Screen Made By 366
def welcome_screen():
    clear()
    print("""
      _ _    F I N D   T H E   L O S T    _      
   __| (_) __ _ _ __ ___   ___  _ __   __| |___  
  / _` | |/ _` | '_ ` _ \ / _ \| '_ \ / _` / __| 
 | (_| | | (_| | | | | | | (_) | | | | (_| \__ \ 
  \__,_|_|\__,_|_| |_| |_|\___/|_| |_|\__,_|___/ 
                                                 
    """) 
    print("# Selamat Datang Di Game Harta Karun")
    print()
    print("1. Play Game")
    print("2. Aturan Main")
    print("3. Exit")
    print()

    scanInputHome = input("Masukkan Pilihan : ")
    if scanInputHome == "1":
        clear()
        play_game()
    elif scanInputHome == "2":
        clear()
        aturan_main()
    elif scanInputHome == "3":
        clear()
        exit()
    else:
        welcome_screen()

# Play Game Function
def play_game():
    print("# Clue")
    print()
    print("Berlian Berada Di Index (0, 0)")
    print()

    scanPlayGame = input("Tekan 'y' Untuk Melanjutkan Atau 'b' Untuk Kembali Ke Menu Utama : ")
    if scanPlayGame == "y":
        clear()
        level_satu()
    elif scanPlayGame == "b":
        welcome_screen()
    else:
        clear()
        play_game()

# Level One
def level_satu():
    validasiIndexingItem = hof_find_index(boardGame, "O")
    if validasiIndexingItem == (0, 0):
        clear()
        print("# Congratulations")
        print()
        boardGame[0][0] = "💎"
        mapBoardGame = list(map(str, boardGame ))
        print('\n'.join(mapBoardGame))
        print()
        print("🎉 Selamat, Anda Telah Berhasil Menemukan Berlian Yang Hilang")
        mapStepsComprehension = list(map(str, stepsComprehension))
        print("👣 Riwayat Step :" + "".join(mapStepsComprehension))
        print()
        print("1. Kembali Ke Menu Utama")
        print("2. Exit")
        print()
        scanCongratulation = input("Masukkan Pilihan : ")
        if scanCongratulation == "1":
            reset_list()
            welcome_screen()
        elif scanCongratulation == "2":
            clear()
            exit()
        else:
            clear()
            # index ke (0, 0) diganti kembali menjadi 'O' agar percabangan di atas terpenuhi
            boardGame[0][0] = "O"
            level_satu()
    else:
        print("# Level 1")
        print()
        mapBoardGame = list(map(str, boardGame ))
        print('\n'.join(mapBoardGame))
        print()
        print("1. Cek Posisi")
        print("2. Senggol Kanan")
        print("3. Senggol Atas")
        print("4. Senggol Diagonal")
        print("5. Nyerah")
        print("6. Exit")
        print()
        
        scanInputLevelSatu = input("Masukkan Pilihan : ")
        if scanInputLevelSatu == "1":
            # HOF Implementation as Module 2 Intructions
            searchIndexingItem = hof_find_index(boardGame, "O")
            print()
            print("📍 Posisi 'O' Sedang Berada Di Index :", searchIndexingItem)
            print()
            level_satu()
        elif scanInputLevelSatu == "2":
            steps.append("Senggol Kanan")
            # List Comprehension
            stepsComprehension[:] = [" -> " + x for x in steps]
            shift_right()
            print()
            level_satu()
        elif scanInputLevelSatu == "3":
            steps.append("Senggol Atas")
            # List Comprehension
            stepsComprehension[:] = [" -> " + x for x in steps]
            shift_up()
            print()
            level_satu()
        elif scanInputLevelSatu == "4":
            steps.append("Senggol Diagonal")
            # List Comprehension
            stepsComprehension[:] = [" -> " + x for x in steps]
            shift_diagonal()
            print()
            level_satu()
        elif scanInputLevelSatu == "5":
            reset_list()
            welcome_screen()
        elif scanInputLevelSatu == "6":
            clear()
            exit()
        else:
            clear()
            level_satu()

# Aturan Main
def aturan_main():
    print("# Petunjuk Sebelum Bermain")
    print()
    # Map Implementation
    # Membuat Variable Dengan Tipe Data List (Hasil Dari Mapping List 'boardGame')
    mapBoardGame = list(map(str, boardGame ))
    print('\n'.join(mapBoardGame)) 
    print()
    print("Gambar di atas adalah papan permainan yang akan kamu mainkan. Kamu hanya bisa")
    print("menggerakkan bidak (O) secara horizontal (ke kanan), secara vertical (ke atas)")
    print("dan secara diagonal ke (atas kanan).Temukan harta karun dan menangkan gamenya.")
    print("Selamat bermain, semoga jackpot 🔥")
    print()
    print("NB : Bermainlah Dengan Senang, Tanpa Paksaan Dan Jangan Lupa Makan")
    print()
    print("1. Menu Utama")
    print("2. Exit")
    print()
    scanAturanMain = input("Masukkan Pilihan : ")
    if scanAturanMain == "1":
        welcome_screen()
    elif scanAturanMain == "2":
        clear()
        exit()
    else:
        clear()
        aturan_main()

## 02 - Independent Function
# HOF To Find Index (Global Function)
def hof_find_index(list, item):
    # Enumerate() menambahkan penghitung ke setiap item dari objek yang dapat diubah dan mengembalikan objek enumerate sebagai string keluaran.
    # Enumerate() dilengkapi dengan penghitung atau indeks otomatis untuk setiap item.
    for i, sub in enumerate(list):
        if item in sub:
            indexFound = (i, sub.index(item))
            return indexFound

# Senggol Kanan
def shift_right():
    print()
    # HOF Implementation
    searchSenggolKananItem = hof_find_index(boardGame, "O")
    print("➡️  Elemen 'O' Telah Berhasil Di Senggol Kanan")

    indexOne = searchSenggolKananItem[0]
    indexTwo = searchSenggolKananItem[1]

    senggolKanan = indexTwo - 4

    # Core
    boardGame[indexOne][indexTwo] = "x"
    boardGame[indexOne][senggolKanan] = "O"

# Senggol Atas
def shift_up():
    print()
    # HOF Implementation
    searchSenggolAtasItem = hof_find_index(boardGame, "O")
    print("⬆️  Elemen 'O' Telah Berhasil Di Senggol Atas")

    indexOne = searchSenggolAtasItem[0]
    indexTwo = searchSenggolAtasItem[1]

    senggolAtas = indexOne - 1

    # Core
    boardGame[indexOne][indexTwo] = "x"
    boardGame[senggolAtas][indexTwo] = "O"

# Senggol Diagonal
def shift_diagonal():
    print()
    # HOF Implementation
    searchSenggolDiagonalItem = hof_find_index(boardGame, "O")
    print("↗️  Elemen 'O' Telah Berhasil Di Senggol Diagonal")

    indexOne = searchSenggolDiagonalItem[0]
    indexTwo = searchSenggolDiagonalItem[1]

    senggolDiagonalOne = indexOne - 1
    senggolDiagonalTwo = indexTwo - 4

    # Core
    boardGame[indexOne][indexTwo] = "x"
    boardGame[senggolDiagonalOne][senggolDiagonalTwo] = "O"

# Reset List
def reset_list():
    defaultList = [
        ["x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x"],
        ["O", "x", "x", "x", "x"]
        ]
    boardGame[:] = defaultList

# Main Code
welcome_screen()