
from pytube import YouTube

youtube_url='https://www.youtube.com/watch?v=NHzu69AMVFw'

yt=YouTube(youtube_url)

if(yt):
    print('Title:',yt.title)
    print('Views:',yt.views)
    print('Author:',yt.author)
    print('Description:',yt.description)