# display the welcome page of our little reminder app

reminder1 = "aller acheter du lait"
reminder2 = "coder 30 minutes"
reminder3 = "envoyer une lettre a Maxime"
reminder_amount = 3

def display_welcome_page():
    # code to display the welcome page
    print("1-Display reminders")
    print("2-Create a reminder")
    print("3-Exit the program")

    # waiting for the answer
    user_choice = input("Please enter your choice (1, 2, or 3): ")
    if user_choice == "1":
        # code for displaying reminders
        display_reminders
        pass
    elif user_choice == "2":
        # code for creating a reminder
        pass
    elif user_choice == "3":
        # code for exiting the program
        pass
    else:
        print("Invalid choice. Please try again.")

display_welcome_page()
    
def display_reminders():
    while(todisplay =! reminder_amount):
        