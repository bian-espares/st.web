from PIL import image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Programming is the best",page_icon=":hala:",layout="wide")


lottie_coding = "https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json"
img_contact_form = Image.open("juan")
 

with st.container():
    st.subheader('Hi,my name is BIANCA FAITH ESPARES')
    st.title('Programming, Logic and Design')
    st.write('Life is like programming there might be some errors but we can correct it.')
    st.write('ITS HARD BUT ITS FUN')
    st.write('[Learn More >](https:://pythonandvda.com)')

with st.container():
    st.write('---')
    left_column, right_column =st.columns(2)
    with left_column:
        st.header("What to do")
        st.write("##")
        st.write(
            """
            On My studies at SNSU
            -I have choosen BSCpE course 
            - i am struggling to most of my subject because in my senior high life it was very different
            kung wala moy paki paki ignore
            """
        )
    st.write("[For more information >](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with right_column:
    st_lottie(lottie_coding, height=300, key='coding')

with st.container():
    st.write("---")
    st.write("my project")
    st.write("##")
    image_culomn, text_column = st.columns((1,2))
with image_column:


with text_culomn:
    st.subheader("Integrate lottie animation inside your streamlit app")
    st.write(
        """
        learn how to use lottie files in streamlit!
        animation make our web app more engaging and fun, and lottie file is the easist way to do it
        in this tutorial, i will show how to do it. 
        """     
        )
    st.markdown("[watch the video...](https://youtu.be/TXSOitGoINE)")


