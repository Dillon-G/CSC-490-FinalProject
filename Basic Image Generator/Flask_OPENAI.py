from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Authenticate with the OpenAI API
openai.api_key = "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"  # Replace with your actual API key

@app.route('/', methods=['GET', 'POST'])
def generate_image():
    if request.method == 'POST':
        # Get the pet description from the user
        pet_description = request.form['pet_description']

        # Specify the image prompt using the user input
        prompt = f"Pixel art of a {pet_description} in a cute 8bit style. Show full body of animal"

        # Generate the image
        response = openai.Image.create(prompt=prompt, n=1, size="256x256")

        # Get the URL of the generated image
        image_url = response['data'][0]['url']
        # Generate the image

        print("Generated Image URL:", image_url)
        print("Prompt:", prompt)

        return render_template('image.html', image_url=image_url)
    

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
