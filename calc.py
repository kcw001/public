# get two integer parameters
# return sum
def plus(x, y):
    return x+y

def subtraction(x, y):
    return x-y

def multiplication(x, y):
    return x*y

def division(x, y):
    if y == 0:
        print("0으로 나눌 수 없습니다")
    else:
        return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus, 2: subtraction, 3: multiplication, 4: division")
        check = int(input())
        if check == 1:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", plus(x,y))
        elif check == 2:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", subtraction(x,y))
        elif check == 3:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", multiplication(x,y))
        elif check == 4:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", division(x,y))
        elif check > 4:
            print("unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()