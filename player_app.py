import streamlit as st
from streamlit_player import st_player
import pytube
import os

try:
    os.mkdir('downloads')
except:
    pass

st.title('Video Analyzer')

url = 'https://www.youtube.com/watch?v=R2nr1uZ8ffc'
url = st.text_input('Youtube URL',url)

options = {
    "events": ["onProgress"],
}

event = st_player(url,**options,key="youtube_player")

# Select frame
select = st.button('Select frame')

if select:
    st.write(event.data['playedSeconds'])
    
# Download Youtube video
dl = st.button('Download')

if dl:   
    youtube = pytube.YouTube(url)
    videos = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    l = [s.resolution + " (" + str(round(s.filesize/2**10/2**10)) + " MB)" for s in videos]
    i = st.radio("Select resolution",range(len(videos)),format_func = lambda x: l[x])
    video = videos[i]
    st.write(video)
    title = video.title
    path = video.download('downloads')
    st.text(title)
    # st.video(path,format='video/mp4', start_time=0)
