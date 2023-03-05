import requests
import streamlit as st
from streamlit_lottie import st_lottie
import html

# Find more tate stuff in your ass
st.set_page_config(page_title="free TATE", page_icon=":muscle:", layout="wide")

def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
        return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieur1("https://assets6.lottiefiles.com/packages/lf20_j6fywzxe.json")

# ---- GOOGLE ADSENSE ----

# ---- HEADER SECTION ----
with st.container():
    st.subheader("About TATE :muscle:")
    st.title("The Top G")
    st.write("Andrew Tate is a British kickboxer, former world champion, entrepreneur, and social media personality. Born on December 1, 1986, in Washington, England, Tate started his kickboxing career at the age of eight under the guidance of his father. Since then, he has won numerous championships in kickboxing, including the World Kickboxing Association (WKA) World Championship in 2016. Aside from being a successful athlete, Tate is also an entrepreneur and founder of the company, Tate Enterprises. He has also gained popularity on social media, particularly on YouTube, where he shares his thoughts on various topics, including fitness, business, and personal development. However, Tate has also been the subject of controversy due to his outspoken opinions and behavior. He has been criticized for his views on women, race, and mental health, which some consider to be offensive and harmful. In 2018, he was accused of making derogatory remarks about women during an appearance on the reality TV show, Celebrity Big Brother. Despite the controversies surrounding him, Tate has remained active in his career and personal endeavors. He continues to compete in kickboxing and has also expanded his business ventures, including launching a cryptocurrency company. In conclusion, Andrew Tate is a multifaceted individual who has achieved success in various areas of his life. While he has faced criticism for his controversial opinions and behavior, he has also gained a following for his athleticism, entrepreneurship, and social media presence. Whether one agrees with his views or not, there is no denying that Tate is a unique and intriguing figure in the world of sports and entertainment.")
    st.write("[Learn More >](https://youtu.be/dQw4w9WgXcQ)")
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

        -Fariha apu is cool.

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
