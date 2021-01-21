import blipblipfiles


def main():
    blipblipfiles.setupREADME()
    file = open('README.md', 'r', encoding='utf8')
    print(file.read())
    file.close()


if __name__ == "__main__":
    main()
