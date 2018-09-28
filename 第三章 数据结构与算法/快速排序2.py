
from random import randint

def quick_sort(num_list):
    count = 0
    if len(num_list)==0 or len(num_list)==1:
        # print(count)
        return num_list
    middle = num_list.pop()
    smaller = []
    larger = []
    for num in num_list:
        if num < middle:
            smaller.append(num)
        else:
            larger.append(num)
    return quick_sort(smaller)+[middle]+quick_sort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(quick_sort(nums))
