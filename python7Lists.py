# nums = [5,6,1,0,3, True, "word",[78,25,14]]
# nums[0] = 50
# nums[5] = "exbool"
# print(nums[-1][1])

# numbers = [5,4,9]
# numbers.append(100)
# numbers.insert(1,3)
# numbers.extend([65,34,12])
# # numbers.reverse()
# numbers.sort()
# numbers.pop()
# numbers.remove(4)
# numbers.clear()
# print(numbers)

# nums = [43, 5, 1, "word", True]
# for i in nums:
#     i *= 2
#     print(i)

n = int(input("Enter lenghth: "))

user_list = []

i = 0
while i < n:
    string = "Enter element #" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)