from app import XoApplication


def main():
    size = 3
    mode = input("Войдите в режим 'server' или 'client': ")
    hostname = input("Введите имя хоста (по умолчанию «localhost»): ")
    char = input("«Введите «X» или «O»: ")

    if not hostname:
        hostname = 'localhost'

    app = XoApplication(size, mode, hostname, char)
    app.start()


if __name__ == "__main__":
    main()
