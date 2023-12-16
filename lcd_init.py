from gpiozero import Button
from signal import pause
import os

# Function to handle button press event
def on_button_press():
    print("Button pressed! LCD setup initiated.")
    
    # Replace the following command with your LCD setup commands
    lcd_setup_command = "your_lcd_setup_command_here"
    
    # Execute the LCD setup command
    os.system(lcd_setup_command)
    
    print("LCD setup complete.")

# Create a button object for the setup button
setup_button = Button(17)  # Replace 17 with the GPIO pin connected to your button

# When the button is pressed, call the on_button_press function
setup_button.when_pressed = on_button_press

# Keep the program running
pause()
