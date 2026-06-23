def add(*args):
    total = 0
    
    for num in args:
        total += num
        
    return total

print(add(2, 4, 7))

