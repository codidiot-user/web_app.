import streamlit as st
from rembg import remove
from PIL import Image

def removebg(img):
    input = Image.open(img)
    return remove(input)

def main():
    st.title("Background remover App")
    uploaded = st.file_uploader("Choose an Image...", type=["jpeg","jpg","png"])

    if uploaded is not None:
        st.image(uploaded, caption="uploaded image")
        st.write("Processing Image..")
        result=removebg(uploaded)
        st.image(result, caption="Result")


if __name__ == '__main__':
    main()