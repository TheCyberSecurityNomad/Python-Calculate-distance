"""
My University project

"""
#-Function to prompt the user for an integer input
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():  #-Checks if the input is a digit
            return int(user_input)  #-Converts the input to an integer if valid
        else:
            print("Invalid input. Please enter a valid integer.")  #-Error message for invalid input


#-Function to calculate and print the distance traveled by the ball each minute
def calculate_distance_traveled(ball_speed, travel_time):
    base_speed = ball_speed
    print("-----------------------------\nHour  Distance Travelled\n-----------------------------")
    for hour in range(1, travel_time + 1):
        ball_speed += base_speed
        print(f"{hour}   {ball_speed}")


#-Main function to orchestrate the program flow
def main():
    while True:
        #-Prompting the user for the speed of the ball and travel time
        ball_speed = get_integer_input("What is the speed of the ball (in meters per minute)?: ")
        travel_time = get_integer_input("How many minutes has it traveled?: ")

        #-Calculating and printing the distance traveled by the ball
        calculate_distance_traveled(ball_speed, travel_time)

        #-Asking the user if they want to restart the program
        quit_program = input("\nDo you want to restart the program? (yes/no): ")
        if quit_program.upper() == 'Y' or quit_program.upper() == 'YES':
            continue
        elif quit_program.upper() == 'N' or quit_program.upper() == 'NO':
            break
        else:
            print("Invalid choice. Please enter Y or N.")  # Error message for invalid input


#-Entry point of the program
main()  #-Calling the main function to start the program
