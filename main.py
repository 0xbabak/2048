import random
import numpy as np
import msvcrt
import os

#print nxn size matrix
def matrix_print(matrix, size):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end='  ')
        print('')

#generate a random cordinate of x and y
def coordinate_generate(size):
    return random.randint(0, size - 1), random.randint(0, size - 1)

def shift_left(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != 0:
                x = i
                y = j
                while y >= 1 and y < size and matrix[x][y-1] == 0:
                    matrix[x][y-1] = matrix[x][y]
                    matrix[x][y] = 0
                    y = y - 1
    return matrix 


def shift_right(matrix, size):
    for i in range(size):
        for j in range(size - 1, -1, -1):
            if matrix[i][j] != 0:
                x = i
                y = j
                while y >= 0 and y < size - 1 and matrix[x][y+1] == 0:
                    matrix[x][y+1] = matrix[x][y]
                    matrix[x][y] = 0
                    y = y + 1
    return matrix 

def shift_up(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != 0:
                x = i
                y = j
                while x >= 1 and x < size and matrix[x-1][y] == 0:
                    matrix[x-1][y] = matrix[x][y]
                    matrix[x][y] = 0
                    x = x - 1
    return matrix 

def shift_down(matrix, size):
    for i in range(size - 1, -1, -1):
        for j in range(size):
            if matrix[i][j] != 0:
                x = i
                y = j
                while x >= 0 and x < size - 1 and matrix[x+1][y] == 0:
                    matrix[x+1][y] = matrix[x][y]
                    matrix[x][y] = 0
                    x = x + 1
    return matrix 

def get_key():
    key = msvcrt.getch()
    if key == b'\xe0':
        return msvcrt.getch()
    return key




print("WELCOME TO 2048")

# Set a default value for high_score if it's not already defined
high_score = 0 if 'high_score' not in locals() else high_score

print(f"High Score: {high_score}")

ch = input("Press any button to play | Press Q to quit: ")

while ch.upper() != "Q":
    # Get user input for area size
    area_size = int(input("Please enter an area size: "))
    matrix = np.zeros((area_size, area_size), dtype=int)
    x , y = coordinate_generate(area_size)
    matrix[x][y] = 2
    a, b = coordinate_generate(area_size)
    while a == x and b == y:
        a , b = coordinate_generate(area_size)
    matrix[a][b] = 2

    os.system("cls" if os.name == "nt" else "clear")

    matrix_print(matrix, area_size)
    import keyboard

    while True:
        key = get_key().decode('utf-8')
        os.system("cls" if os.name == "nt" else "clear")  # Clear the console screen

        if key == 'w':
            shift_up(matrix, area_size)
        elif key == 'd':
            shift_right(matrix, area_size)
        elif key == 'a':
            shift_left(matrix, area_size)
        elif key == 's':
            shift_down(matrix, area_size)

        a, b = coordinate_generate(area_size)
        while matrix[a][b] != 0:
            a, b = coordinate_generate(area_size)
        matrix[a][b] = 2
        matrix_print(matrix, area_size)

