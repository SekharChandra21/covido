from flask import Flask, request, jsonify, render_template, send_from_directory
from predict import classify_using_bytes

app = Flask(__name__)

app.config['IMAGES_FOLDER'] = 'static/images/'
app.config['MODEL_PATH'] = 'diseases3.h5'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/news')
def news():
    print(request.path)
    return render_template('news.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/research')
def research():
    return render_template('index.html')

@app.route('/predict-image', methods = ['POST'])
def predict_image():
    if request.method == 'POST':
        image = request.files.get('image')
        if image:
            image_source = image.read()

                # prediction 
            result = classify_using_bytes(image_source, app.config['MODEL_PATH'], 299)

            return result
        
        else:
            return {
                'error': '404'
            }

@app.route('/display-image/<filename>')
def display_image(filename):
    return send_from_directory(app.config['IMAGES_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
