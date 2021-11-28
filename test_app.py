import streamlit as st
import streamlit.components.v1 as components
# import pyautogui
# import keyboard

# if keyboard.read_key() == "p":
#         st.write("You pressed p")

# st.checkbox("Test",value=True)
st.text("1/4: What is Streamlit")

# st.write(pyautogui.locateOnScreen('img/pattern2.png'))

path = "downloads/14 What is Streamlit.mp4"
st.video(path,format='video/mp4', start_time=0)

# bootstrap 4 collapse example
components.html(
    """
    <div></div>
    <style>
    div {
    width: 400px;
    height: 200px;
    padding: 20px;
    margin: 50px auto;
    background: purple;
    }
    </style>
    
    <script>
    let elem = document.querySelector('div');
    let rect = elem.getBoundingClientRect();
    for (var key in rect) {
    if(typeof rect[key] !== 'function') {
        let para = document.createElement('p');
        para.textContent  = `${ key } : ${ rect[key] }`;
        document.body.appendChild(para);
    }
    }
    </script>
    """,
    height=600,
)