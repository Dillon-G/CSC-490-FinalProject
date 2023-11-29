from flask import Flask, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/image_gen')
def display_image():
    # Example URL, replace this with your actual image URL
    
    with open("image.txt", "r") as file:
        image_url = file.read().strip()
    # Fetch the image from the URL
    response = requests.get(image_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Serve the image using Flask's send_file function
        return send_file(BytesIO(response.content), mimetype='image/png')
    else:
        return "Failed to fetch image"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)