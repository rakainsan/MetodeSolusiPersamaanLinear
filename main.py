from metode_numerik import solve_using_inverse, solve_using_lu, solve_using_crout, input_matrix, input_vector

def main():
    print("Muhammad Raka Insan M.")
    print("21120122130040")
    print("Metode Numerik C")

    print("\nSilakan Pilih Metode Penyelesaian:")
    print("1. Metode Matriks Balikan")
    print("2. Metode Dekomposisi LU Gauss")
    print("3. Metode Dekomposisi Crout")
    choice = int(input("Masukkan Pilihan Anda (1/2/3): "))

    if choice not in [1, 2, 3]:
        print("Pilihan tidak valid.")
        return

    while True:
        print("\nMasukkan Ukuran Matriks A:")
        n = int(input())
        print("Masukkan Isi Matriks A:")
        A = input_matrix(n)
        print("Masukkan Isi Vektor b:")
        b = input_vector(n)

        if choice == 1:
            x = solve_using_inverse(A, b)
            method = "Metode Matriks Balikan"
        elif choice == 2:
            x = solve_using_lu(A, b)
            method = "Metode Dekomposisi LU Gauss"
        elif choice == 3:
            x = solve_using_crout(A, b)
            method = "Metode Dekomposisi Crout"

        print(f"\nSolusi Menggunakan {method}:")
        for i in range(len(x)):
            print(f"x_{i+1} = {x[i]}")

        repeat = input("\nApakah Anda ingin melakukan operasi lagi? (y/n): ")
        if repeat.lower() != 'y':
            break

        change_method = input("Apakah Anda ingin mengubah metode penyelesaian? (y/n): ")
        if change_method.lower() == 'y':
            print("\nSilakan Pilih Metode Penyelesaian:")
            print("1. Metode Matriks Balikan")
            print("2. Metode Dekomposisi LU Gauss")
            print("3. Metode Dekomposisi Crout")
            choice = int(input("Masukkan Pilihan Anda (1/2/3): "))

            if choice not in [1, 2, 3]:
                print("Pilihan tidak valid.")
                return

if __name__ == "__main__":
    main()
