def recursion(to_num, from_num = 1):
    if from_num > to_num:
        return 
    else:
        print(from_num)
        recursion(to_num, from_num + 1)

print(recursion(6))

def recursion_down(num):
    if num == 0:
        return
    else:
        print(num)
        recursion_down(num - 1)

print(recursion_down(9))

def fibonacci(num):
    if num == 0:
        print("cant do this")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(4))