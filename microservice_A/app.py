from flask import Flask, request
import os
import search_image

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    try:
        with open('request.txt', 'r') as file:
            keyword = file.read().strip()
        
        image_path = search_image.search_and_download_image(keyword)

        with open('response.txt', 'w') as file:
            if image_path:
                file.write(f"Image saved at {image_path}")
            else:
                file.write("No image found")
        
        return "Search completed and response written to response.txt", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    app.run(debug=True)