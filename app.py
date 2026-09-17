import streamlit as st
from deep_translator import MyMemoryTranslator

# Page settings
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Language Translation Tool")
st.write("Translate text from one language to another using an online translation service.")

# Supported languages
languages = {
    "English": "en-GB",
    "Telugu": "te-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-LK",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Spanish": "es-ES",
    "French": "fr-FR",
    "German": "de-DE",
    "Japanese": "ja-JP",
    "Korean": "ko-KR",
    "Chinese": "zh-CN"
}

# Text input
text = st.text_area(
    "Enter text to translate:",
    placeholder="Type your text here..."
)

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "From:",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "To:",
        list(languages.keys()),
        index=1
    )

# Translate button
if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.info("Please select two different languages.")

    else:
        try:
            translator = MyMemoryTranslator(
                source=languages[source_language],
                target=languages[target_language]
            )

            translated_text = translator.translate(text)

            st.subheader("Translated Text")
            st.success(translated_text)

            st.code(translated_text)

            st.info("You can copy the translated text from the box above.")
        except Exception as error:
            st.error("Translation failed. Please try again.")
            st.caption(f"Error: {error}")

            