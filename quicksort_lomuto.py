import sys
from typing import List
input = []

for i in sys.argv[1:]:
    input.append(int(i))


print("## Quick sort ## ");
print(f"\nInput: {input}");


def partition(nums: List[int], start: int, end: int) -> int :
    # Lomuto's partition aims to identify elements lower or equals the current pivot
    # place them before it, and them at the end place the pivot after all of them.
    pivot = nums[start]

    # swapIndex kind counts the amount of swaps done, but it aims to tell us which index
    # should be used to place the next number lower than the pivot
    swapIndex = start
    
    # the iteration index will start with the 'start + 1' value, since our pivot is already
    # the value on the 'start' position, there is no need to check the same value twice
    for index in range(start+1,end+1):

        # if the pivot value is greater than the current iteration value
        if(pivot>nums[index]):
            # we might increase the swapIndex
            swapIndex+=1
            # and swap the values
            nums[swapIndex], nums[index] = nums[index], nums[swapIndex]
    # we are moving to the left each number lower than the current pivot value
    # the swapIndex stores the next available index to place a value which is lower than the pivot.
    
    # at the end of the iteration, we are moving the pivot value to the correct place
    # by swapping it with the last swapped value, since we are sure that it will be
    # greater than any value on it's left side
    nums[start], nums[swapIndex] = nums[swapIndex], nums[start]

    # the swapIndex is returned because we just assigned the pivot value to it
    # so now it represents the pivot index
    return swapIndex
    
def quicksort(nums: List[int], start: int, end:int):
    if(start<end):
        pivot = partition(nums,start,end)
        quicksort(nums,start, pivot-1)
        quicksort(nums,pivot+1, end)

    return nums



print(f"Result: {quicksort(input,0,len(input)-1)}")
    