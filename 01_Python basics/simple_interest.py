principal = int(input("Enter the amount taken: "))
ROI = float(input("Enter the rate of interest in percentge: "))
time = int(input("Enter the duration in years: "))
Simple_Interest = (principal*ROI*time)/100
print(f"The rate of interest on the given principal amount {principal} is {ROI}% for {time} years is {Simple_Interest} ")
