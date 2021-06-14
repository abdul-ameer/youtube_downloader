from pytube import YouTube
from pywebio.input import *
from pywebio.output import *
from pywebio import SessionClosedException

def app():
    link=input("Enter YouTube Link: ")
    yt=YouTube(link)
    yt.streams.first().download()
    popup('Download Complete')
    return

        
    
if __name__=='__main__':
    try:
        app()
    except SessionClosedException:
        print("The Session was Closed Unexpectedly")
        
