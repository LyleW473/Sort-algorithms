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
item_font = pygame.font.SysFont("Bebas Neue", 25)

# Variables holding the value of the border;s starting x and y positions
border_x_position = 100
border_y_position = 100

# Lists
""" These are the lists and variables used when scaling the items all up """
temp_list = [] # Holds every height of the items inside each stage of the sort. (A list full of individual items)
other_list = [] # Used to temporarily hold the heights, so that I can separate them into stages again (A shorter list full of individual items, depending on how many items each stage has)
item_height_list = [] # Holds lists of each stage with their item heights 


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

current_item = 0 # Used when calculating maximum_scale (the maximum scale that should be applied to all of the items)
greatest_item = 0 # Used when calculating maximum_scale (the maximum scale that should be applied to all of the items)

# Restart process
restart_process = False

def BubbleSort(list, height_scale):
    sort_index = 0
    sorted_flag = True
    temp_list = []
    while sort_index < len(list) - 1 : 
        
        #  Scaling the items and placing them in a separate list
        # Create a copy of the list at this current iteration 
        copy_list = list.copy()
        # Iterate through that list copy and scale it according to the maximum height scale
        for i in range(0, len(copy_list)):
            scaled_item = copy_list[i] * height_scale
            # Add the scaled item to the temporary list
            temp_list.append(scaled_item)
        # Add the list of scaled items to another list which will hold all stages of the sort
        sort_stages_list.append(temp_list)

        # Empty the temporary list
        temp_list = []

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

            # We are now complete with the input process
            input_process = False

            # Allow for the sorting process to be performed on the list that the user entered
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

    # Preparing and calling the bubble sort
    if call_bubble_sort == True:

        # Calculate item width
        item_width = 600 / num_of_list_items
        
        # Calculate maximum scale that should be applied to the items
        # Loop through the user's list and check which is the largest item in the list
        for i in range(0, len(user_items_list)):
            current_item = user_items_list[i]
            if current_item > greatest_item:
                greatest_item = current_item


        # The maximum scale that can be applied would be the amount of space I have inside of the border divided by the greatest item
        maximum_scale = round(600 / greatest_item, 2)

        # Call the bubble sort function and feed in the user items list and the maximum scale as parameters
        BubbleSort(user_items_list, maximum_scale)        

        # Set the call bubble sort variable to False so that it doesn't get called again
        call_bubble_sort = False
        # Allow for the sorting process to begin
        sorting_process = True


    # If the sorting process has been allowed
    if sorting_process == True:
        # Draw all x rectangles, depending on the length of the list.
        for i in range(0, num_of_list_items):
            pygame.draw.rect(screen, WHITE, ((border_x_position - 5) + (i * item_width), 695 - (sort_stages_list[stage_index][item_index + i]), item_width, sort_stages_list[stage_index][item_index + i]), 5)
            # Draw a text at the in the centre of each item, at the y co-ordinate, 500
            draw_text(str(round(sort_stages_list[stage_index][item_index + i] / maximum_scale)), item_font, BLACK, (border_x_position - 5) + (i * item_width) + (item_width / 2) - 14, 500)
        # Wait 0.25 seconds between each swap
        pygame.time.delay(250)
        # Record the time that the last swap was made, this will be used later to measure how long its been since the last stage has been shown.
        last_swap_time = pygame.time.get_ticks()

        # If the stage index isn't equal to the length of the list (which holds all the stages with their item heights)
        if stage_index != len(sort_stages_list) - 1:
            # Look at the next stage
            stage_index += 1
        # If the stage index has reached the end of the amount of stages inside the item heights list, that means the algorithm is finished
        else: 
            # We are now complete with the sorting process
            sorting_process = False

    # If the input and sorting process have both been completed
    if sorting_process == False and input_process == False:
        # If 5 seconds have not passed since the last stage was displayed, do the following:
        if pygame.time.get_ticks() - last_swap_time < 5000:
            # Draw the final stage of the sort (just to display it)
            for i in range(0, len(user_items_list)):
                pygame.draw.rect(screen, WHITE, ((border_x_position - 5) + (i * item_width), 695 - (sort_stages_list[stage_index][item_index + i]), item_width, sort_stages_list[stage_index][item_index + i]), 5)
                draw_text(str(round(sort_stages_list[stage_index][item_index + i] / maximum_scale)), item_font, BLACK, (border_x_position - 5) + (i * item_width) + (item_width / 2) - 14, 500)

            # Draw the text displaying that the sort has been completed  
            draw_text("Bubble sort complete", sort_completed_font, GREEN, (screen_width / 2) - 255, (screen_height / 2) - 30)

            # Draw the timer to display how long until the program restarts / resets
            draw_text(("Time: " + str(round(5 - (pygame.time.get_ticks() - last_swap_time) / 1000))), time_font, BLACK, 342, 10)

            # Draw the text displaying the sorted list
            draw_text("Sorted list", user_input_font, BLACK, 100, 710)
            draw_text(str(user_items_list), user_input_font, BLACK, 100, 750)
        # If 5 seconds have passed
        else:
            # Allow for the restart process to begin
            restart_process = True

    if restart_process == True:
    # Reset all of the variables and lists used 
        stage_index = 0
        item_index = 0

        input_process = True
        num_of_list_items = 0
        user_items_list = []

        # Note, sorting_process and call_bubble_sort have already been reset to default 
        sort_stages_list = []
        original_list = []

        # Reset the variables for the scaling of the items
        maximum_scale = 0
        current_item = 0
        greatest_item = 0

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
