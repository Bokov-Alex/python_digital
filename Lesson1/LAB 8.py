fibo=list(input("Enter a fibonnachi list:"))
for i in range(2,len(fibo)):
    if fibo[i]!=fibo[i-1]+fibo[i-2]:
        break
print("this is not a fibonnachi list")
