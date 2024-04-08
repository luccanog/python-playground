import sys
from typing import List
input = []

for i in sys.argv[1:]:
    input.append(int(i))


print("## Quick sort ## ");
print(f"\nInput: {input}");


def quicksort(nums: List[int]):
    if len(nums) < 2:
        return nums

    pivot = nums[0];
    lower = [];
    greater = [];

    for num in nums[1:]:
        if(num>pivot):
            greater.append(num)
        else:
            lower.append(num)
    
    return quicksort(lower) + [pivot] + quicksort(greater)


print(f"Result: {quicksort(input)}")
    