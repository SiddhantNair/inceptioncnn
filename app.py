""" Object detection using Inception V3 and ImageNet"""
from flask import Flask, request, render_template
from inception_net import classify_image
APP = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@APP.route('/')
def hello():
    """ Display app to User """
    return render_template('index.html')


@APP.route('/classify', methods=['POST'])
def classify():
    """ Sample test Route to Neural Net """
    image = request.files['image']
    label, prob = classify_image(image)
    return f"{label} - {prob:.2f}"


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=80)
