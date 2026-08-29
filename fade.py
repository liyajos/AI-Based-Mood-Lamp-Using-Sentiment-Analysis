# Import the RGBLED class to control an RGB LED
from gpiozero import RGBLED

# Import sleep to create delays between color changes
from time import sleep

# Initialize the RGB LED
# Red   -> GPIO 17
# Green -> GPIO 27
# Blue  -> GPIO 22
led = RGBLED(red=17, green=27, blue=22)

# Display a message when the program starts
print("Smooth RGB color fade running... Press Ctrl+C to stop.")

try:
    # Run the color fading sequence continuously
    while True:

        # Fade smoothly from Blue to Red
        for i in range(100):
            # Increase Red intensity while decreasing Blue intensity
            led.color = (i / 100, 0, 1 - i / 100)

            # Small delay for a smooth transition
            sleep(0.02)

        # Fade smoothly from Red to Green
        for i in range(100):
            # Decrease Red intensity while increasing Green intensity
            led.color = (1 - i / 100, i / 100, 0)

            # Small delay for a smooth transition
            sleep(0.02)

        # Fade smoothly from Green to Blue
        for i in range(100):
            # Decrease Green intensity while increasing Blue intensity
            led.color = (0, 1 - i / 100, i / 100)

            # Small delay for a smooth transition
            sleep(0.02)

# Handle Ctrl+C to stop the program safely
except KeyboardInterrupt:
    # Turn off the LED
    led.off()

    # Release the GPIO resources
    led.close()

    # Display a message indicating the program has stopped
    print("Program stopped.")