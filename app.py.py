import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Multi-Language Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------- UI STYLE ----------
st.markdown("""
<style>
h1 { color: #4b0082; }
textarea { font-size: 16px !important; }
</style>
""", unsafe_allow_html=True)

st.title("🌍 Global Multi-Language Translator")

# ---------- LANGUAGE LIST ----------
languages = {
    # Indian Languages
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Odia": "or",
    "Assamese": "as",

    # World Languages
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Italian": "it",
    "Turkish": "tr",
    "Dutch": "nl"
}

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("✏️ Source Text")
    source_text = st.text_area(
        "Enter text to translate",
        height=200,
        placeholder="Type any language text..."
    )

with col2:
    st.subheader("🌐 Target Language")
    target_lang = st.selectbox(
        "Select Target Language",
        list(languages.keys())
    )

# ---------- TRANSLATE ----------
if st.button("✨ Translate"):
    clean_text = source_text.strip()

    if clean_text == "":
        st.warning("⚠️ Please enter some text to translate")
    else:
        try:
            translated_text = GoogleTranslator(
                source="auto",
                target=languages[target_lang]
            ).translate(clean_text)

            st.success("✅ Translation Successful")

            st.text_area(
                "Translated Output",
                value=translated_text,
                height=200,
                disabled=True
            )

            st.code(translated_text)  # easy copy

        except Exception as e:
            st.error("❌ Translation failed. Please try again.")
