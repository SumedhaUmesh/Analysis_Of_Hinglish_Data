from flask import Flask, render_template, url_for, request, redirect
from Integrator import instaOutput, output, senti
from image import image_extract
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    return render_template('analyze.html')

@app.route('/text', methods = ['GET', 'POST'])
def text():
    Text = request.form['text']
    outData = output(Text)
    return render_template("output.html", OText = outData[0], conf = outData[1], IText = Text, flag=1)

@app.route('/link', methods = ['GET', 'POST'])
def link():
    Link = request.form['link']
    return render_template("link.html", Text = instaOutput(Link))

@app.route('/image', methods = ['GET', 'POST'])
def image():
    Image = request.form['image']
    outData = output(image_extract(Image))
    return render_template("output.html", IText = Image, OText = outData[0], conf = outData[1],flag=2)

@app.route('/<IText>/<OText>/report', methods=['GET'])
def report(IText, OText):
    return render_template("report.html", IText=IText, OText=OText)

@app.route('/<OText>/sentiment_analysis')
def sentiments(OText):
    return render_template("sentiments.html", OText=OText, senti = senti(OText))

if __name__ == '__main__':
    app.run(debug=True)