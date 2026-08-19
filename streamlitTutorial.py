import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello GPT")
name = st.text_input("ask your question")

st.write("This is your streamlit app")

st.text("lets get started")
name=st.text_input("enter your name")
if st.button("greet"):
    st.success(f"Hello {name}!")

#how to upload csv file
upload_file = st.file_uploader("Upload CSV", type="csv")
if upload_file:
    import pandas as pd
    df = pd.read_csv(upload_file)
    st.dataframe(df)

    st.header("This is header")
    st.subheader("This is subheader")
    st.markdown("[Link](https://streamlit.io/)")
    st.text_area("write your message")
    st.number_input('pick a number',min_value=0,max_value=10)
    st.slider("choose a range",0,100)
    st.selectbox("select a fruit", ["apple", "banana", "mango"])
    st.multiselect("select language", ["python", "java", "c++", "C"])
    st.radio("pick one", ["option A", "option A"])
    st.checkbox("I agree terms and conditions")

    if st.checkbox("show details"):
        st.info("here are more details")

#form tag
with st.form("login form"):   
        username = st.text_input("enter username")
        password = st.text_input("password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            st.success(f"Welcome {username}")


df = pd.DataFrame(np.random.randn(20,3), columns=["A", "B", "C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.video("https://www.youtube.com/watch?v=rkV7--wYUJ8&list=RDrkV7--wYUJ8&start_radio=1")
st.image("https://picsum.photos/200/300",caption="sample image",)