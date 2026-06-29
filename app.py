import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 AI Language Translation Tool")
st.write("Translate text between different languages.")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

source = st.selectbox("Select Source Language", list(languages.keys()))
target = st.selectbox("Select Target Language", list(languages.keys()))

text = st.text_area("Enter text to translate")

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed!")
        st.text_area("Translated Text", translated, height=150)

        if st.button("Copy Translation"):
            pyperclip.copy(translated)
            st.success("Copied to Clipboard!")
    else:
        st.warning("Please enter some text.")