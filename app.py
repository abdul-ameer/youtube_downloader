from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        link = str(request.form['Youtube Downloader'])
        yt=YouTube(link)
        yt.streams.first().download()
        #popup('Download Complete')
        return render_template('index.html',prediction_text="Download Complete Have a LOOK")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
 
        
