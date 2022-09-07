#  File: Boxes.py

#  Description: Finds the largest number of boxes that will fit inside of each other and the number of sets of those boxes that can be made.

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/10/2022

#  Date Last Modified: 3/10/2022

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
    memo = []
    for i in range(len(box_list)):  # build a list for all the nestings
        memo.append(1)
    
    memo[0] = 0 # assigns the box with 0x0x0 as 0
    memo = largest_nest(box_list, memo)

    pos = []
    for i in range(len(memo)):  #finds the position of the highest value in memo
        if memo[i] == max(memo):
            pos.append(i)
    
    num_max = 0
    for i in range(len(pos)):   # accounts for the event that there are multiple maximums in the memo
        num_max += num_largest(box_list, memo, box_list[pos[i]], max(memo) - 1)
    return max(memo), num_max

def largest_nest(box_list, memo):
    for i in range(len(memo)):
        for j in range(i):
            if does_fit(box_list[j], box_list[i]):
                memo[i] = max(memo[i], memo[j] + 1) #if they fit, take the maximum of either the original or the new + 1

    return memo

def num_largest(box_list, memo, box, nest):
    if nest == 1:
        sum = 0
        for i in range(len(memo)):
            if (memo[i] == 1) and (does_fit(box_list[i], box)):
                sum += 1    #sums all the boxes that fit and have a nest value of 1
        return sum

    else:
        sum = 0
        for i in range(len(memo)):
            if (memo[i] == nest) and (does_fit(box_list[i], box)):
                sum += num_largest(box_list[0:i], memo[0:i], box_list[i], nest - 1)
        return sum  #reduce the list of boxes and memo because the rest of the list becomes irrelevant

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
    # read the number of boxes 
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int (line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range (num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range (len(box)):
            box[j] = int (box[j])
        box.sort()
        box_list.append (box)

    # print to make sure that the input was read in correctly
    #print (box_list)
    #print()

    # sort the box list
    box_list.append([0, 0, 0])
    box_list.sort()

    # print the box_list to see if it has been sorted.
    #print (box_list)
    #print()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes (box_list)

    # print the largest number of boxes that fit
    print (max_boxes)

    # print the number of sets of such boxes
    print (num_sets)

if __name__ == "__main__":
    main()
