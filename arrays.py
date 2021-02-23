# get the product of all elements in an array
def products(nums):
    answer = 1
    for num in nums:
        answer = answer * num
    return answer

print(products([1, 2, 3, 4, 5, 6]))