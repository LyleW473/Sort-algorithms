# Importing modules
import pygame, sys
from pygame.locals import * 

# Initialising pygame
pygame.font.init()

# Screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Title
pygame.display.set_caption("Bubble sort")

# Colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
DIMGREY = (105,105,105)


# Fonts
user_input_font = pygame.font.SysFont("Bebas Neue",40)
instruction_font = pygame.font.SysFont("Bebas Neue",25)
sort_completed_font = pygame.font.SysFont("Bebas Neue",70)
time_font = pygame.font.SysFont("Bebas Neue",50)

# Variables holding the value of the border;s starting x and y positions
border_x_position = 100
border_y_position = 100

# Lists
""" These are the lists and variables used when scaling the items all up """
temp_list = [] # Holds every height of the items inside each stage of the sort. (A list full of individual items)
other_list = [] # Used to temporarily hold the heights, so that I can separate them into stages again (A shorter list full of individual items, depending on how many items each stage has)
item_height_list = [] # Holds lists of each stage with their item heights 

once = True # Variable used to only perform certain actions once

# Counters used in the scaling process
count = 0
total_count = 0
# Indexes used to reference the stage and items inside the item heights list
stage_index = 0
item_index = 0

# Input process
input_process = True # Variable to indicate whether we are in the input process or not
# User input variables
user_text = '' # Holds the numbers that the user types in to the input box
user_input_rectangle = pygame.Rect((screen_width / 2) + 50, screen_height - 70, 200, 50) # Input box rectangle

num_of_list_items = 0 # Holds the number of list items that the user wants their list to have
user_items_list = [] # Holds the numbers (items) that the user inputs inside a list 

# Sorting process
sorting_process = False # Variable to indicate whether we are in the sorting process or not
call_bubble_sort = False #  Variable to call the bubble sort once
sort_stages_list = [] # A list which takes in the stages of the list after the sort algorithm has been performed
original_list = [] # A list that will hold the 

# Restart process
restart_process = False

def BubbleSort(list):
    sort_index = 0
    sorted_flag = True
    while sort_index < len(list) - 1 : 

        # Check if the first element of the list is less than or equal the element after it
        if list[sort_index] <= list[sort_index + 1]:
            # Then do nothing
            pass

        # If the first element is greater than the element after it
        elif list[sort_index] > list[sort_index + 1]:
            # Swap their values
            list[sort_index], list[sort_index + 1] = list[sort_index + 1], list[sort_index] 
            # Set the sorted flag to False, as a swap has been made 
            sorted_flag = False

        # Create a copy of the current list
        temporary_list = list.copy()
        # Add it to a new list which will hold all the stages of the list
        sort_stages_list.append(temporary_list)
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

    return list

def draw_text(text, font, text_colour, x, y):
    image = font.render(text, True, text_colour)
    screen.blit(image, (x, y))

run = True
while run:
    # Limit FPS to 60
    clock.tick(60)
    # Fill the screen with white
    screen.fill(WHITE)


    # Draw the border rectangle 
    # X co-ordinate = 100
    # Y co-ordinate = 100
    pygame.draw.rect(screen, BLACK, (border_x_position - 10, border_y_position - 10, 610, 610), 5)

    # The height between the border is 95 to 695  = 600, this is the background colour of the box
    pygame.draw.rect(screen, DIMGREY, (95, 95, 600, 600), 0)



    # Input process handling
    if input_process == True:
        # Draw the user text onto the screen, position it to be where the user input box / rectangle is 
        if num_of_list_items == 0:
            # Draw the text for what I want the user to enter into the input box
            draw_text("Enter the number of items you want in your list", instruction_font, BLACK, user_input_rectangle.x - 410, user_input_rectangle.y + 15)
        
        # If the number of items inside of the items list is not equal to the amount of items the user asked for (meaning we are still asking for the user to enter list items)
        elif len(user_items_list) != num_of_list_items:
            # Draw the enter list items list
            draw_text("Enter list items", instruction_font, BLACK, user_input_rectangle.x - 170, user_input_rectangle.y + 15)

        

        elif len(user_items_list) == num_of_list_items:
            # List used to display the original list (before it was sorted)
            original_list = user_items_list.copy() 

            sort_stages_list.append(user_items_list.copy()) # Add the very first list into the stages list, this is so that the very first stage (before it is sorted), is displayed on the screen

            # We are now complete with the input process
            input_process = False

            # Allow for the sorting process to be performed on the list that the user entered
            sorting_process = True
            call_bubble_sort = True

        # User text
        text_image = user_input_font.render(user_text, True, RED)
        screen.blit(text_image, (user_input_rectangle.x + 5, user_input_rectangle.y + 10))
        pygame.draw.rect(screen, BLACK, user_input_rectangle, 2)

        # Set the input box to increase in width along with the text
        user_input_rectangle.width = max(200, text_image.get_width() + 10) # The max function returns the largest of the input values, so the minimum starting size of the text box will be 200 pixels
       
    # During the input process, display whatever the user inputs into the list
    if input_process == True:
        draw_text(str(user_items_list), user_input_font, BLACK, 100 , 45)
    # Even after the input process, display the original list (before it was sorted)
    # Note: I changed the list drawn because, user_items_list will change once sorted, so it would display the sorted version of the list
    else:
        draw_text(str(original_list), user_input_font, BLACK, 100 , 45)

    # Draw the "Your list" text regardless if the input process is ongoing or not
    draw_text("Your list", user_input_font, BLACK, 100, 10)

    # Draw center line
    #pygame.draw.line(screen, BLACK, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if sorting_process == True:
        # Calculate widths of each item
        item_width = 600 / len(user_items_list) 

        # Perform this operation once
        if once == True:
            # Call the bubble sort once, and assign it to a new list, which will be used in the sorting operations
            list_selected = BubbleSort(user_items_list)

            # The largest height would be the largest item in the list, this would be the last item in the list because it has already been sorted
            # Then find out whats the maximum scale we can apply to the largest item in the list, that way it won't go outside the border
            maximum_scale = round((600 / list_selected[len(list_selected) - 1]),2)
            
            # For each stage inside the sort stages list
            for stage in sort_stages_list:
                
                # For each item, multiply them 
                for item in stage:
                    item_height = item * maximum_scale # The multiplier part
                    temp_list.append(item_height)

            # Since the length of the temporary list will change in the next section, assign a new variable to be this length.
            original_length_of_list = len(temp_list)

            once = False

        # Separating the large list of scaled heights into lists 

        if total_count < original_length_of_list:

            # Separate them depending on the amount of items in each "stage"
            if count != len(stage):
                # Add the item to another list
                other_list.append(temp_list[0])

                # Pop the first item in the temporary list
                temp_list.pop(0)

                # Increment counters
                count += 1
                total_count += 1
                
            # If all the items have been added in the first "stage", reset the first list and add it to the "lists of lists"
            if count == len(stage):
                # Add the list holding stage-length items into another list
                item_height_list.append(other_list)
                # Reset temps
                other_list = []
                count = 0
                # Increment total count
                total_count += 1
        else:

            # Draw all x rectangles, depending on the length of the list.
            for i in range(0, len(list_selected)):
                pygame.draw.rect(screen, WHITE, ((border_x_position - 5) + (i * item_width), 695 - (item_height_list[stage_index][item_index + i]), item_width, item_height_list[stage_index][item_index + i]), 5)
            # Wait 0.25 seconds between each swap
            pygame.time.delay(250)

            # Record the time that the last swap was made, this will be used later to measure how long its been since the last stage has been shown.
            last_swap_time = pygame.time.get_ticks()

            # If the stage index isn't equal to the length of the list (which holds all the stages with their item heights)
            if stage_index != len(item_height_list) - 1:
                # Look at the next stage
                stage_index += 1
            # If the stage index has reached the end of the amount of stages inside the item heights list, that means the algorithm is finished
            else: 
                # We are now complete with the sorting process
                sorting_process = False
                call_bubble_sort = False
                
    # If the input and sorting process have both been completed
    if sorting_process == False and input_process == False:
        # If 5 seconds have not passed since the last stage was displayed, do the following:
        if pygame.time.get_ticks() - last_swap_time < 5000:
            # Draw the final stage of the sort (just to display it)
            for i in range(0, len(user_items_list)):
                pygame.draw.rect(screen, WHITE, ((border_x_position - 5) + (i * item_width), 695 - (item_height_list[stage_index][item_index + i]), item_width, item_height_list[stage_index][item_index + i]), 5)

            # Draw the text displaying that the sort has been completed  
            draw_text("Bubble sort complete", sort_completed_font, GREEN, (screen_width / 2) - 255, (screen_height / 2) - 30)

            # Draw the timer to display how long until the program restarts / resets
            draw_text(("Time: " + str(round(5 - (pygame.time.get_ticks() - last_swap_time) / 1000))), time_font, BLACK, 342, 10)

            # Draw the text displaying the sorted list
            draw_text("Sorted list", user_input_font, BLACK, 100, 710)
            draw_text(str(user_items_list), user_input_font, BLACK, 100, 750)
        else:
            # If 5 seconds have passed
            # Allow for the restart process to begin
            restart_process = True

    if restart_process == True:
    # Reset all of the variables and lists used 
        temp_list = [] 
        other_list = [] 
        item_height_list = []

        once = True

        count = 0
        total_count = 0
        stage_index = 0
        item_index = 0

        input_process = True
        num_of_list_items = 0
        user_items_list = []

        # Note, sorting_process and call_bubble_sort have already been reset to default 
        sort_stages_list = []
        original_list = []

        # We are now complete with the restart process
        restart_process = False


    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()
        # Check if any keyboard button was pressed
        if event.type == pygame.KEYDOWN:
            # Only when we are looking for input do the following
            if input_process == True:
                # If the backspace / delete button is pressed
                if event.key == pygame.K_BACKSPACE:
                    # Remove the last item inside the text
                    user_text = user_text[:-1]
                # If the enter / return key is pressed
                elif event.key == pygame.K_RETURN:
                    # Check for if we are looking for the number of list items. An additional to check to ensure that the user is inputting anything
                    if num_of_list_items == 0 and len(user_text) > 0:
                        # Convert the user text into integers
                        num_of_list_items = int(user_text)

                    # If we are past the first input stage, where I ask for the number of list items, this means we are asking for the list items. An additional to check to ensure that the user is inputting anything
                    elif num_of_list_items != 0 and len(user_text) > 0: 
                        # Add the item (numbers) that the player wants to add to their  list
                        user_items_list.append(int(user_text))

                    # Empty the user text so new input can be collected
                    user_text = ''

                # If neither the backspace key or the enter key is pressed then. This section covers the typing input
                else:  
                    # Check according to the unicode number, if it is a number (48 to 57 is numbers 1 to 9)
                    if 48 <= event.key <= 57:
                        # First stage
                        # Allow for a number from 0 to 9(inclusive)
                        if num_of_list_items == 0 and len(user_text) < 1:
                            # Add the number to the user input text
                            user_text += event.unicode
                        # Second stage:
                        # Allow for a number from 0 to 999 (inclusive)
                        elif num_of_list_items != 0 and len(user_text) < 3:
                            # Add the number to the user input text
                            user_text += event.unicode


    # Update display
    pygame.display.update()
