def fib(num):
    l = []
    if num <= 0:
        return "error"
    if num == 1:
        l = [1]
    elif num == 2:
        l = [1, 1]
    else:
        l = [1, 1]
        i = 2
        while i <= num:
            l.append(l[i-1] + l[i-2])
            i += 1
    return(l)
num = int(input("how many fibonacci numbers should i print? "))

print(fib(num))