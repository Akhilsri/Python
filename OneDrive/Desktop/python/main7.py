import os

# f = open("demo.txt", "r+") #("file_name" , "mode")
# data = f.read()
# # f.readline()
# print(data)
# print(type(data))
# f.close()


f = open("demo.txt", "a")
f.write("\nI love Paneer")

os.remove("os.txt")
