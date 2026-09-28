import streamlit as st
import requests

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 Language Translation Tool")
st.write(
    "Translate text from one language to another using an online translation service."
)

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

text = st.text_area(
    "Enter text to translate:",
    height=150
)

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


def translate_text(text, source_code, target_code):

    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source_code}|{target_code}"
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if data.get("responseStatus") != 200:
        raise Exception(
            data.get("responseDetails", "Translation failed")
        )

    return data["responseData"]["translatedText"]


if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():

        st.warning("Please enter some text.")

    elif source_language == target_language:

        st.info("Source and target languages are the same.")
        st.write(text)

    else:

        try:
            source_code = languages[source_language]
            target_code = languages[target_language]

            translated_text = translate_text(
                text,
                source_code,
                target_code
            )

            st.success("✅ Translation completed!")

            st.subheader("Translated Text")

            st.text_area(
                "Result:",
                translated_text,
                height=150
            )

        except requests.exceptions.RequestException as e:

            st.error("❌ Unable to connect to the translation API.")
            st.write(f"Error: {e}")

        except Exception as e:

            st.error("❌ Translation failed.")
            st.write(f"Error: {e}")