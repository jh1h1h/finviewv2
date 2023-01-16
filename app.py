from flask import Flask, render_template
import tensorflow as tf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def MLModel():
    model = tf.keras.models.load_model('./model')
    return str(model.predict([[5915,6284,7635,8063,8332,9294,9966,10421,10413,11585,12090,11749,12711,16892,17744,21191,21000,21440,25684,22177,23181,21179,22684,27703,33286,31210,32566,34302,37338,40966]]))


if __name__ == '__main__':
    app.run(debug=True)
