"""Implements a Galois Field 2^32 and 2^8 calculator"""

def byte(x, n=8):
    return format(x, f"0{n}b")

def int16(x):
    return int(x, 16)

def hexf(x):
    return format(x, "02x".upper())

def gf_2_8_product(a, b):
    tmp = 0
    b_byte = bin(b)[2:]
    for i in range(len(b_byte)):
        tmp = tmp ^ (int(b_byte[-(i+1)]) * (a << i))

    mod = int("100011011", 2)
    exp = len(bin(tmp)[2:])
    diff =  exp - len(bin(mod)[2:]) + 1

    for i in range(diff):
        if byte(tmp, exp)[i] == "1":
            tmp = tmp ^ (mod << diff - i - 1)
    return tmp

def gf_2_8_calculator():
    print("Welcome to the GF(2^8) calculator!")
    print("Write 'help' to get help")
    command = input(">>> ")
    stack = []
    while True:
            if command == "q":
                break
            elif command == "help":
                print("This is a Postfix caculator")
                print("Write number in GF(2^8) in the hexadecimal form. Ex: 2A")
                print("Write '+' to sum the previous two numbers")
                print("Write '*' to multiply the previous two numbers")
                print("Write 'print' or 'p' to print the stack")
                print("Write 'clear' to clear the stack")
                print("Write 'q' to exit the calculator")
            elif command == "p" or command == "print":
                print(stack)
            elif command == "clear":
                stack = []
            elif command == "+":
                if len(stack) < 2:
                    print("Enter a number first!")
                else:
                    tmp = stack.pop() ^ stack.pop()
                    print("0x" +  hex(tmp)[2:].upper())
                    stack.append(tmp)
            elif command == "*":
                if len(stack) < 2:
                    print("Enter a number first!")
                else:
                    tmp = gf_2_8_product(stack.pop(), stack.pop())
                    print("0x" + hex(tmp)[2:].upper())
                    stack.append(tmp)
            else:
                stack.append(int(command, 16))
            command = input(">>> ") 

def gf_2_32_calculator():
    print("Welcome to the GF(2^32) calculator!")
    print("For a while, there is only the multiplication operation...")
    print()
    A = list(map(int16,reversed(input("A(x) coefficients: ").split())))
    B = list(map(int16,reversed(input("B(x) coefficients: ").split())))

    A_matrix = [[A[(3*i+j) % 4] for i in range(4)] for j in range(4)]
    D = []
    print()
    for i in range(4):
        D.append(0)
        for j in range(4):
            D[i] = D[i] ^ gf_2_8_product(A_matrix[i][j], B[j])
    print("0x" + "".join(list(map(hexf, reversed(D)))))

if __name__ == "__main__":
    print("Choose the calculator:")
    print("1 - GF(2^8) calculator")
    print("2 - GF(2^32) calculator")
    mode = input("> ")

    if mode == "1":
        gf_2_8_calculator()
    elif mode == "2":
        gf_2_32_calculator()
