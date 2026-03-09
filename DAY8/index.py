# f = open("hello.txt",'w')
# f.write("Hello Python")
# data1 = input()
f = open("index.html","r")
data = f.readlines(-1)

print(data)
f.close()