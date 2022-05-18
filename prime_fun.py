def Prime(num):
    index=2
    while index<num:
        if num%index==0:
            return str(num)+" not a prime number"
            break
        index+=1
    else:
        return str(num)+" is a prime"
p=Prime(int(input()))
print("prime",p)
