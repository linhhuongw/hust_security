def shift_char(char, key):
    if "a" <= char <= "z":
        base = ord("a")
        return chr((ord(char) - base + key) % 26 + base)

    if "A" <= char <= "Z":
        base = ord("A")
        return chr((ord(char) - base + key) % 26 + base)

    return char


def encrypt(message, key):
    return "".join(shift_char(char, key) for char in message)


def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


def read_key():
    while True:
        value = input("Nhap khoa k: ").strip()
        try:
            return int(value)
        except ValueError:
            print("Khoa k phai la so nguyen. Vui long nhap lai.")


def main():
    while True:
        print("\n=== He mat ma Caesar ===")
        print("1. Ma hoa")
        print("2. Giai ma")
        print("0. Thoat")

        choice = input("Chon chuc nang: ").strip()

        if choice == "0":
            print("Da thoat chuong trinh.")
            break

        if choice not in {"1", "2"}:
            print("Lua chon khong hop le.")
            continue

        message = input("Nhap thong diep: ")
        key = read_key()

        if choice == "1":
            print("Ban ma:", encrypt(message, key))
        else:
            print("Ban ro:", decrypt(message, key))


if __name__ == "__main__":
    main()
