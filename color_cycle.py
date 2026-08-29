# Import the RGBLED class from the gpiozero library
from gpiozero import RGBLED

# Import the sleep function to create delays
from time import sleep

# Initialize the RGB LED using the GPIO pins
# Red   -> GPIO 17
# Green -> GPIO 27
# Blue  -> GPIO 22
led = RGBLED(red=17, green=27, blue=22)

# List of RGB color values
# Each tuple represents (Red, Green, Blue) intensity
colors = [
    (1, 0, 0),      # Red
    (1, 0.5, 0),    # Orange
    (1, 1, 0),      # Yellow
    (0, 1, 0),      # Green
    (0, 0, 1),      # Blue
    (0.5, 0, 1),    # Purple
    (1, 1, 1)       # White
]

try:
    # Keep changing colors continuously
    while True:
        # Loop through each color in the list
        for color in colors:
            # Set the LED to the current color
            led.color = color

            # Wait for 0.5 seconds before changing to the next color
            sleep(0.5)

# Handle Ctrl+C to stop the program safely
except KeyboardInterrupt:
    # Turn off the LED
    led.off()

    # Release the GPIO resources
    led.close()

    # Display a message indicating the program has stopped
    print("Stopped")