# Import the RGBLED class to control an RGB LED
from gpiozero import RGBLED

# Import sleep to add a short delay
from time import sleep

# Import the VADER sentiment analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the RGB LED
# Red   -> GPIO 17
# Green -> GPIO 27
# Blue  -> GPIO 22
led = RGBLED(red=17, green=27, blue=22)

# Create a sentiment analyzer object
analyzer = SentimentIntensityAnalyzer()

# Function to analyze text sentiment and set the LED color
def set_color_from_sentiment(text):
    # Calculate sentiment scores for the input text
    scores = analyzer.polarity_scores(text)

    # Get the overall sentiment score
    compound = scores["compound"]

    # Display the sentiment score
    print("\nSentiment score:", compound)

    # Set LED color based on the sentiment score
    if compound >= 0.4:
        print("Mood: Happy / Positive")
        led.color = (0, 1, 0)      # Green

    elif compound <= -0.4:
        print("Mood: Sad / Negative")
        led.color = (1, 0, 0)      # Red

    else:
        print("Mood: Neutral")
        led.color = (0, 0, 1)      # Blue

try:
    # Continuously accept user input
    while True:
        # Ask the user to enter a sentence
        text = input("\nType a sentence (or 'quit' to exit): ")

        # Exit the program if the user types "quit"
        if text.lower() == "quit":
            break

        # Check if the input is empty
        if text.strip() == "":
            print("Please type something.")
            continue

        # Analyze the sentiment and update the LED color
        set_color_from_sentiment(text)

        # Wait briefly before accepting the next input
        sleep(0.5)

# Handle Ctrl+C to stop the program safely
except KeyboardInterrupt:
    print("\nStopped by user.")

# Always execute cleanup before exiting
finally:
    # Turn off the LED
    led.off()

    # Release the GPIO resources
    led.close()

    # Display a confirmation message
    print("LED turned off cleanly.")