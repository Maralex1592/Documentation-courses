# -*- coding: utf-8 -*- 

def run():
    with open('numbers.txt', 'w') as f:
        for num in range(0, 11):
            f.write(str(num))

if __name__ == '__main__':
    run()

    