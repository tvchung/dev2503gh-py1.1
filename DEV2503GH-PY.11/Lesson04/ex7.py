
n=10

# for x in range(1,n,1):
#     print('  '*(n-x), end='')
#     for y in range(1,x+1,1):
#         print(y,end=' ')
#     for y in range(x-1,0,-1):
#         print(y,end=' ')
#     print('')
# print("----"*(n-1))


for i in range(1, n + 1):
    # In khoảng trắng để căn giữa
    print('  ' * (n - i), end='')

    # In tăng dần từ i đến (2*i - 1) rồi giảm dần về i
    for j in range(i, 2*i):
        print(j % 10, end=' ')

    for j in range(2*i - 2, i - 1, -1):
        print(j % 10, end=' ')

    print()