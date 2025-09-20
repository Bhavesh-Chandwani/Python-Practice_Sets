for i in range(1, 8):
    if i == 3:
        print("→ Using continue at i =", i)
        continue      # skips this iteration
    
    if i == 5:
        print("→ Using pass at i =", i)
        pass          # does nothing, loop continues
    
    if i == 7:
        print("→ Using break at i =", i)
        break         # loop ends completely
    
    print("Current value of i:", i)

print("Loop finished")
