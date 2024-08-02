name = "malayalam"

s=0
for i in range(0,len(name)):
    if(name[i] != name[len(name)-1-i]):
        s+=1
        break;
i+=1

if(s==0):
    print("Palindrome")
else:
    print("Not Palindrome")