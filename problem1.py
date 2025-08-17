num=[2,4,6,8,10]
small=num[0]
for i in range(len(num)):
    if num[i] < small:
        small = num[i]
print("The smallest number is:", small)
