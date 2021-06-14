from pytube import YouTube
from pywebio.input import *
from pywebio.output import *
from pywebio import SessionClosedException
from flask import Flask
from pywebio.platform.flask import webio_view

app=Flask(__name__)

def predict():
    link=input("Enter YouTube Link: ")
    yt=YouTube(link)
    yt.streams.first().download()
    popup('Download Complete')

        
app.add_url_rule('/myapp','webio_view',webio_view(predict),methods=['GET','POST','options'])  
app.run(host="localhost",port=80)
 
        
