
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
youtube_url='https://www.youtube.com/watch?v=RObw_WRbX6k'

Video_id=YouTube(youtube_url).video_id
transcript= YouTubeTranscriptApi.get_transcript(Video_id)
Video_view= YouTube(youtube_url).views
text_transcript=""

for segment in transcript:
    text_transcript += segment['text'] + " "
print(text_transcript)
print(Video_view)