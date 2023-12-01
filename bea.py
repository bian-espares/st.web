from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Programming is the best",page_icon=":hala:",layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',  unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form = Image.open("images/jon.jpg")
img_github = Image.open("images/github.png")

 

with st.container():
    st.subheader('Hi,my name is BIANCA FAITH ESPARES')
    st.title('Programming, Logic and Design')
    st.write('Life is like programming, there might be some errors but we can correct it.')
    st.write('ITS HARD BUT ITS FUN')
    st.write('[Learn More >](https://www.youtube.com/watch?v=VqgUkExPvLY)')

with st.container():
    st.write('---')
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What to know?")
        st.write("##")
        st.write(
            """
            I am currently studying at SNSU 
         -I have choosen BSCpE course
            -I am struggling to most of my subject because, my senior high life it was very different.
            """
        )
        st.write("-I have choosen BSCpE course")
    st.write("[For more information >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with right_column:
    st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write("---")
    st.write("My Inspiration")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_contact_form)

with text_column:
    st.subheader("He is JON EDJAY BAGANI ESPARES")
    st.write(
        """
        He is 1year old. He arrive in my life in a very unexpected time and situation.
        Now he is my everything, the reason why I am keep standing up after many failure. 
        He change me into a better version of myself.
        """     
        )
    st.markdown("[watch the video...](https://www.facebook.com/reel/1410154259577343)")

with st.container():
    st.write("---")
    st.write("my project")
    st.write("##")
    image_column, text_column = st.columns((1,2))

with image_column:
    st.image(img_github)

with text_column:
    st.subheader("What is GitHub?")
    st.write(
        """
         Github, Inc. is a platform and cloud-based service for software development and version contron, 
         allowing developer to store and manage the codes.
        """     
        )
    st.markdown("[watch the video...](https://github.com/bian-espares/st.web)")

with st.container():
    st.write("---")
    st.header('for Any concerns You Can Contact Me!')
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/esparesbiancafaith@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message  here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
