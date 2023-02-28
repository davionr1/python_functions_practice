def hello():
    print("Hello")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(list):
    if(list):
        print(f"First I eat{list}")
        if(list):
            print(f"Next I eat{list}")
    else:
        print("My lunch box is empty")

hello()
print(pack(1,2,3))
eat_lunch([])
eat_lunch(" burrito")
eat_lunch(["pizza","pasta","sandwich","apples"])