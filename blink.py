# Import the LED class to control a single LED
from gpiozero import LED

# Import sleep to create delays
from time import sleep

# Initialize the red LED connected to GPIO pin 17
red = LED(17)

try:
    # Run the blinking sequence continuously
    while True:
        # Turn the LED on
        red.on()

        # Keep the LED on for 1 second
        sleep(1)

        # Turn the LED off
        red.off()

        # Keep the LED off for 1 second
        sleep(1)

# Handle Ctrl+C to stop the program safely
except KeyboardInterrupt:
    # Turn off the LED
    red.off()

    # Release the GPIO resources
    red.close()

    # Display a message indicating the program has stopped
    print("Program stopped safely.")