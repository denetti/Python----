num = int(input())
sumc = 0

while (num != 0):
    sumc = sumc + num % 10
    num = num // 10
print(sumc)
