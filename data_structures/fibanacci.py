def fibanacci(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    
    return fibanacci(position-1) + fibanacci(position -2)

print(fibanacci(9))
print(fibanacci(11))
print(fibanacci(0))

series=''
for i in range(10): 
    fib_val = fibanacci(i)
    series = series + str(fib_val)
    if i < 9:
        series= series+','
    

print('Fibanacci Series: {}'.format(series))