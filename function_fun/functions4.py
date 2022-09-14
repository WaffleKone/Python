def max_num(num1, num2, num3):
    max = 0
    if(num1 > num2):
        max = num1
    elif(num1 == num2):
        print("There are multiple maximum numbers")
    else:
        max = num2
    if(max < num3):
        max = num3
    elif(max == num3):
        print("There are multiple maximum numbers")
    return(max)

def mult_list(list):
    product = list[0]
    if(len(list) > 1):
        for i in list[1:]:
            product = product * i
    return(product)

def rev_string(str):
    return(str[::-1])

def num_within(num, beg, end):
    return(num in range(beg, end+1))

triangle = [[1],[1,1]]
def pascal(n):
  if n == 1:
    print(triangle[0])
  else:
    row_num = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_num - 1]
      
      length = len(row_prev)+1
      for i in range(length):
        
        if i == 0:
          row.append(1)
        
        elif i > 0 and i < length-1:
          row.append(triangle[row_num-1][i-1]+triangle[row_num-1][i])
        
        else:
          row.append(1)
      triangle.append(row)
      row_num += 1
    for row in triangle:
      print(row)

print(max_num(2, 7, 3), mult_list([7,7,2]), rev_string("marathon"), num_within(12, 4, 9), pascal(14))