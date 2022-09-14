def arb_args(*args):
    print(args)

def inner_func(int1, int2):
    def add():
        add_result = int1 + int2
        return(add_result)
    def sub():
        sub_result = int1 - int2
        return(sub_result)
    return(add(), sub())

def lunch_lady(name, pref="Mystery Meat"):
    print(name, pref)

def sum_n_product(int1, int2):
    sum = int1 + int2
    prod = int1 * int2
    return(sum, prod)

alias_arb_args = arb_args

def arb_mean(*args):
    total = 0
    for i in args:
        total += i
    print("The average is",total/len(args))

def arb_longest_string(*args):
    length = 0
    longest = ""
    for i in args:
        if len(i) > length:
            length = len(i)
            longest = i
    return(longest)

# Part 3 
def name_args(**kwargs):
    for i, name in kwargs.items():
        print(i, name)
name_args(jaxon = "johnson", joey = "hoellerich")

def all_true(statements):
    return all(statements)



def one_true(statements):
    return any(statements)

def recursive_factorial(n):
  if n <= 1:
    return 1
  else:
    return n * recursive_factorial(n-1)

def recursive_deduplicate(my_str,i=0):
    if len(my_str) <= 1 or i == len(my_str)-1:
        return my_str
    else:
        return recursive_deduplicate(my_str,i+1)

def recursive_reverse(str, i=0):
    if len(str)==0:
        return ""
    elif i == len(str)-1:
        return str[0]
    else:
        return str[-1-i] + recursive_reverse(str, i+1)

