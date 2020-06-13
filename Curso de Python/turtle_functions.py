# -*- coding: utf-8 -*-
import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    
    make_square(dave)
    turtle.mainloop()
    
def make_square(dave):
    length = int(input('De que tamaño lo quiere? '))
    
    for i in range(4):
        make_line_and_turn(dave, 50)
    
def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)  

if __name__ == '__main__':
    main()