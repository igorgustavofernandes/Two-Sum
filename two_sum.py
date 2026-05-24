nums = []
nums_vistos = {}
target = 0

for c in range(4):
    nums.append(int(input('Enter a number: ')))
target = int(input('Enter the target sum: '))       

for i, num in enumerate(nums):
    complement = target - num
    if complement in nums_vistos:
        print(f'Complementary Index: {nums_vistos[complement]} Current Index {i}')
        break
    else:
        nums_vistos[num] =  i
    