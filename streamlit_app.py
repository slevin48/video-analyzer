import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re

st.title('YouTube Video Transcript Extractor')

url = st.text_input('Enter YouTube URL', 'https://www.youtube.com/watch?v=R2nr1uZ8ffc')

def extract_video_id(url):
    # Extracts the video ID from a YouTube URL
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None

if st.button('Get Transcript'):
    video_id = extract_video_id(url)
    if not video_id:
        st.error("Invalid YouTube URL.")
    else:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([entry['text'] for entry in transcript])
            st.subheader("Transcript:")
            st.write(full_text)
        except Exception as e:
            st.error(f"Could not retrieve transcript: {e}")