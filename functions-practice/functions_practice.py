def hello():
    print("Hello")


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]


def eat_lunch(list):
    if (list):
        print(f"First I eat{list}")
        if (list):
            print(f"Next I eat{list}")
    else:
        print("My lunch box is empty")

# Practice part 4 assignment functions


def max_num(num1, num2, num3):
    num_list = [num1, num2, num3]
    print(max(num_list))


def mult_list(num_array):
    result = 1
    for i in num_array:
        result *= i
    return result


def rev_string(string):
    for i in reversed(string):
        print(i)


def num_within(num, beg_range, end_range):
    if num > beg_range and num < end_range:
        return True
    else:
        return False


def pascal(numRows):
  
  for i in range(numRows):
    print(' '*(numRows-i), end='')
    
    print(' '.join(str(11**i)))

    
# hello()
# print(pack(1,2,3))
# eat_lunch([])
# eat_lunch(" burrito")
# eat_lunch(["pizza","pasta","sandwich","apples"])

# Practice part 4 assignment outputs
print(max_num(44, 100, 4))
list = [2,2,2]
print(mult_list(list))
rev_string("today")
print(num_within(5, 0, 10))

print(pascal(5))