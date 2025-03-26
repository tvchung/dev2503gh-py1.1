print("Devmaster, Xin chào Tiến Cường")

x = 1 + 2 + 3
print(x)

y=  1 + \
    2+\
    3
# in ra biến y
print("y =  ",y)

name = "Chuung Chuung"
Name = "Devmaster"
print(name)
print(Name)

class MyList:
    def __init__(self,items):
        self.items =items
    def __len__(self):
        return len(self.items)
    
my_list = MyList([1,4,2,6,3,5,7])
print(len(my_list))

str = "Hello world"
print(str)

print(str[0],str[1])
