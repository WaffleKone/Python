def hello():
    print("Hello there!")
hello()

def pack(first, second, third):
    new_list = [first, second, third]
    return(new_list)

print(pack("Sandwich", "Chips", "Cookie"))

def eat_lunch(list):
    for i in range(len(list)):
        if i == 0:
            print(f"First I eat {list[0]}")
        else:
            print(f"Next I eat {list[i]}")
    print(f"My lunchbox is empty!")

eat_lunch(pack("Sandwich", "Chips", "Cookie"))

        