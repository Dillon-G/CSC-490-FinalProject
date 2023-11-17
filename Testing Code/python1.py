from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
def index():
    image_url = sys.argv[1]
    print(image_url)
    return render_template('./mainpage.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
