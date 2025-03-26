# in kim tự tháp * ngược
n = int(input("n="))
for i in range(n,0,-1):
    # in dấu cách
    print(' '*(n-i), end='')
    # in dấu *
    print('* '*i)


# in kim tự tháp
print("=="*n)
for i in range(1,n+1,1):
    print(' '*(n-i), end='')
    print('* '*i)

    