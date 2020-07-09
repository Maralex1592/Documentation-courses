
def main():
    cont = 0
    with open('The Zen of Python copy.txt') as f:
        #print(f.readlines())

        for line in f:
            cont += line.count('\n')
        print(cont)

if __name__ == '__main__':
    main()
    