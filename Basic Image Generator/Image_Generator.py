import sys
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Authenticate with the OpenAI API
openai.api_key = "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"  # Replace with your actual API key


def receive_message_and_respond():
    # Check if an argument (message) has been passed from python1.py
    if len(sys.argv) > 1:
        received_message = sys.argv[1]
        pet_description = received_message
        # Specify the image prompt using the user input
        prompt = f"Pixel art of a {pet_description} in a cute 8bit style. Show full body of animal"

        # Generate the image
        response = openai.Image.create(prompt=prompt, n=1, size="256x256")

        # Get the URL of the generated image
        image_url = response['data'][0]['url']
        # Generate the image

        print(image_url)
    else:
        print("No message received from python1.py")

# Call function to receive and process the message, and send a response
receive_message_and_respond()
