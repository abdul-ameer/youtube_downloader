from pytube import YouTube
from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    link=input("Enter YouTube Link: ")
    yt=YouTube(link)
    yt.streams.first().download()
    popup('Download Complete')
    return

        
    
if __name__=='__main__':
    bmicalculator()