# mergesortanimation.py
"""Sorting an array with merge sort."""
import numpy as np
import matplotlib.pyplot as plt

# calls recursive sort_array method to begin merge sorting
def merge_sort(data):
  sort_array(data, 0, len(data) - 1)
 
def sort_array(data, low, high):
  """Split data, sort subarrays and merge them into sorted array."""
  # test base case size of array equals 1
  if (high - low) >= 1: # if not base case
    middle1 = (low + high) // 2 # calculate middle of array
    middle2 = middle1 + 1 # calculate next element over
    print(f'split: {subarray_string(data, low, high)}')
    print(f' {subarray_string(data, low, middle1)}')
    print(f' {subarray_string(data, middle2, high)}\n')
    sort_array(data, low, middle1) # first half of array
    sort_array(data, middle2, high) # second half of array
    merge(data, low, middle1, middle2, high)
    
    
    plt.bar(list(range(10)), data)
    plt.pause(0.01)
    plt.clf()

def merge(data, left, middle1, middle2, right):
  left_index = left # index into left subarray
  right_index = middle2 # index into right subarray
  combined_index = left # index into temporary working array
  merged = [0] * len(data) # working array

  # output two subarrays before merging
  print(f'merge: {subarray_string(data, left, middle1)}')
  print(f' {subarray_string(data, middle2, right)}')
  while left_index <= middle1 and right_index <= right:
    # place smaller of two current elements into result
    # and move to next space in arrays
    if data[left_index] <= data[right_index]:
      merged[combined_index] = data[left_index]
      combined_index += 1
      left_index += 1
    else:
      merged[combined_index] = data[right_index]
      combined_index += 1
      right_index += 1
     
  if left_index == middle2:
    # if True, copy in rest of right array
    merged[combined_index:right + 1] = data[right_index:right + 1]
  else:
    # right array is empty, copy in rest of left array
    merged[combined_index:right + 1] = data[left_index:middle1 + 1]
    data[left:right + 1] = merged[left:right + 1] # copy back to data
  # output merged array
    print(f' {subarray_string(data, left, right)}\n')
# method to output certain values in array
def subarray_string(data, low, high):
  temp = ' ' * low # spaces for alignment
  temp += ' '.join(str(item) for item in data[low:high + 1])
  return temp
def main():
  data = np.array([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
  print(f'Unsorted array: {data}\n')
  merge_sort(data)
  print(f'\nSorted array: {data}\n')
 
  # call main if this file is executed as a script
main()

