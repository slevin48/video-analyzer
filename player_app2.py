import streamlit as st
from streamlit_player import st_player
st.title('Video Analyzer')

options = {
    "events": ["onProgress"]
}


url = 'https://www.youtube.com/watch?v=R2nr1uZ8ffc'
url = st.text_input('Youtube URL',url)

event = st_player(url,**options,key="youtube_player")
st.write(event.data['playedSeconds'])