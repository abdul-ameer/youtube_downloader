from pytube import YouTube
from pywebio.input import *
from pywebio.output import *
from pywebio import SessionClosedException
from flask import Flask
from pywebio.platform.flask import webio_view
import argparse
from pywebio import start_server

app=Flask(__name__)

def predict():
    link=input("Enter YouTube Link: ")
    yt=YouTube(link)
    yt.streams.first().download()
    popup('Download Complete')

        
app.add_url_rule('/myapp','webio_view',webio_view(predict),methods=['GET','POST','options'])  
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=str,default=8080)
    args=parser.parse_args()
    
    start_server(predict,port=args.port())
#pp.run(host="localhost",port=80)
 
        
