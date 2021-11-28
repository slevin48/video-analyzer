import streamlit as st
from streamlit_player import st_player, _SUPPORTED_EVENTS

url = 'https://www.youtube.com/watch?v=R2nr1uZ8ffc'
url = st.text_input('Youtube URL',url)

st.subheader("Parameters")

options = {
    "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
    "progress_interval": 1000,
    "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
    "playing": st.checkbox("Playing", False),
    "loop": st.checkbox("Loop", False),
    "controls": st.checkbox("Controls", True),
    "muted": st.checkbox("Muted", False),
}

event = st_player(url,**options)
st.write(event.data['played'])