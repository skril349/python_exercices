def devolver_distintos(num1,num2,num3):
    suma = num1+num2+num3
    if suma <10:
        return min(num1,num2,num3)
    if suma > 15:
        return max(num1,num2,num3)
    if suma > 10 and suma < 15:
        nums = [num1,num2,num3]
        nums.sort()
        return nums[1]

print(devolver_distintos(1,7,9))