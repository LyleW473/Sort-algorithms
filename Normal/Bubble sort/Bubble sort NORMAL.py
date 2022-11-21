# Bubble sort algorithm

def BubbleSort(list):
    sort_index = 0
    sorted_flag = True
    while sort_index < len(list) - 1 : 

        # Check if the first element of the list is less than or equal the element after it
        if list[sort_index] <= list[sort_index + 1]:
            #print(list[sort_index], "and", list[sort_index + 1], "are in the right order")
            pass

        # If the first element is greater than the element after it
        elif list[sort_index] > list[sort_index + 1]:
            # Swap their values
            list[sort_index], list[sort_index + 1] = list[sort_index + 1], list[sort_index] 
            # Set the sorted flag to False, as a swap has been made 
            sorted_flag = False

        # Increment the index
        sort_index += 1

        # Check if by the end of the iteration if there have been any swaps. If any swaps were made then that means it isn't sorted
        if sort_index == len(list) -1 and sorted_flag == False:
            # Reset the sort index so that it starts swapping again from the beginning of the list
            sort_index = 0
            # Assume that the list is sorted until proven False
            sorted_flag = True

        # Check if by the end of the iteration, if there have been no swaps, that means that the list is sorted.
        if sort_index == len(list) -1 and sorted_flag == True:
            print(f"The list is now sorted : {list}")