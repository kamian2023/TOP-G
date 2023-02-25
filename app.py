import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more tate stuff in your ass
st.set_page_config(page_title="free TATE", page_icon=":muscle:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
        return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieur1("https://assets6.lottiefiles.com/packages/lf20_j6fywzxe.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("About TATE :muscle:")
    st.title("The Top G")
    st.write("He is the masculinity reviver, who is Top G")
    st.write("[Learn More >](https://youtube.com/shorts/cTMK4-XI93k?feature=share)")
# ---- WHY TATE IS innocent ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why TATE is innocent")
        st.write("##")
        st.write(
        """
        As you know recently the tate brothers have been arrested, but its false accusations because:

        -They have no proof.

        -Its the matrix.

        -Avro stinks AF

        -He is the Top G

        if you think he is innocent then post FREETOPG
        """
        )
        st.write("[YouTube channel >](https://www.youtube.com/user/MrBeast6000)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("TATE Theme Song")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        with text_column:
            st.subheader("TATE's theme song")
            st.write(
            """
            Listen to this masterpiece, you will feel like you are a beast!
            Its called tourner dans la vide.
            """
            )
            st.markdown("[Listen Here...](https://youtu.be/F3wpq-i150c)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in touch with FARHAN!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! GU KHAO !!!
    contact_form = """
    <form action="https://formsubmit.co/akhtermahfuza2022@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=true)
    with right_column:
        st.empty()

# ---- GOOGLE ADSENSE ----
<head><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2863019331434652"
     crossorigin="anonymous"></script></head>
