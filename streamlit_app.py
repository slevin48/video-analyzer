import streamlit as st
from streamlit_player import st_player
import pytube
import moviepy.editor as mp
import speech_recognition as sr
import os, base64
from datetime import time,timedelta
from PIL import Image
import pytesseract

try:
    os.mkdir('downloads')
except OSError as error:
    print(error)

st.title('Video Analyzer')

st.markdown('Features')

fs = st.checkbox("Frame Selection")
if fs:
    ocr = st.checkbox("Optical Character Recognition")
vts = st.checkbox("Video 2 Speech")
if vts:
    stt = st.checkbox("Speech 2 Text")

# 2 modes: youtube or local
src = st.radio("Youtube Download or Local Upload",["Download","Upload"])
# st.write(src)
if src == "Upload":
    up = st.file_uploader("Upload a video", type=["mp4"])

    if up is not None:
        with open(os.path.join("downloads",up.name),"wb") as f:
            f.write(up.getbuffer())
        st.video(up,format='video/mp4', start_time=0)
        path = 'downloads/'+up.name
else:
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
    dl = st.checkbox('Download')
    
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
        st.video(path,format='video/mp4', start_time=0)

try:
    
    print(path)
    my_clip = mp.VideoFileClip(path)
    duration = int(my_clip.duration)
    minutes, seconds = divmod(duration, 60)

    if fs:
        t = st.slider("Select frame",step=timedelta(seconds=1),min_value=time(minute=0,second=0),max_value=time(minute=minutes,second=seconds),format = "mm:ss")
        time = t.second + 60*t.minute
        f = my_clip.get_frame(time)
        st.image(f)
        save = st.button("save frame + ocr")
        if save:
            Image.fromarray(f).save("downloads/frame_"+str(time)+".jpg")
            with open("downloads/frame_"+str(time)+".jpg", "rb") as file:
                dlframe = st.download_button("Download frame",data=file,file_name="frame_"+str(time)+".jpg",mime="image/png")
            if ocr:
                txt = pytesseract.image_to_string(f)
                st.markdown(txt)

    if vts:
        # Video to Audio
        my_clip.audio.write_audiofile("downloads/"+title+".wav")
        # my_clip.audio.write_audiofile("downloads/speech.wav")
        st.text("Duration: "+str(duration))
        st.audio("downloads/"+title+".wav", format='audio/wav')

        if stt:
            # ## Speech to text
            r = sr.Recognizer()
            # break in 60 sec intervals
            audioFile = sr.AudioFile("downloads/speech.wav")
            i = 0
            audiolist = []
            while i*60 < duration:
                with audioFile as source:
                    audio = r.record(source, offset=i*60, duration=60)
                    audiolist.append(audio)
                i += 1

            with open("downloads/speech.txt","w") as f:
                for audio in audiolist:
                    txt = r.recognize_google(audio)
                    f.write(txt)
                    st.text(txt)

            data = open("downloads/speech.txt", "r").read()
            b64 = base64.b64encode(data.encode()).decode()
            st.markdown(f'<a href="data:file/txt;base64,{b64}" download="speech.txt">speech.txt</a>',unsafe_allow_html=True)
except NameError:
    print('No video to process')