def decimal_to_binary(n):
    binary = 0
    i = 0
    while n > 0 :
        rem = n % 2
        c = pow(10, i)
        binary+= rem * c
        n //=2
        i+=1
    
    print(binary)

decimal_to_binary(17)