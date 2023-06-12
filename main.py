import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="my webpage", page_icon="", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_OT15QW.json")
with st.container():
    st.subheader('''Hi, my name is Hafiz.
    penangrians and nasi kandar lovers!''')
    st.title("a future computer science student")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in writing code")
    st.title("Regular student in science stream foundation program")
    st.write("[My Instagram](https://instagram.com/damnhafiz?igshid=OGQ5ZDc2ODk2ZA==)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("I am currently studying in foundation program at UITM Pusat Asasi Dengkil and i am also also graduated from prestigious high school which is MRSM taiping")
            
        # Add more statements as needed within the left_column context

    with right_column:
        st_lottie(lottie_coding,height=300, key="coding")


   
