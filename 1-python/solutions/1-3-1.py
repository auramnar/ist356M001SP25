def average (list_of_numbers):
    total = 0
    count = 0

    for number in list_of_numbers:
        total += number
        count += 1
    return total/count


nums = [10, 20, 10, 5]
avg = average(nums)
print(f"Average of {nums} is {avg}")


'''
def average(list_of_numbers):
    #do stuff
    total = sum(list_of_numbers)
    count = len(list_of_numbers)
    return total/count

'''


'''
def average2(numlist):
    count = 0
    total = 0
for num in numlist:
    count = count +1
    total = total +1
return total/count
