import streamlit as st
from app import parse_whatsapp_chat
from wordCloud import generate_word_cloud
from analisis import analyze_sentiment

def main():
    st.title('Análisis de Conversaciones de WhatsApp')

    # Subir archivo de chat
    uploaded_file = st.file_uploader("Sube tu archivo de chat de WhatsApp", type="txt")

    if uploaded_file is not None:
        messages = parse_whatsapp_chat(uploaded_file)

        # Seleccionar autor
        authors = list(set([msg['author'] for msg in messages]))
        selected_author = st.selectbox('Selecciona un autor', authors)

        # Generar nube de palabras
        if st.button('Generar Nube de Palabras'):
            generate_word_cloud(messages, author=selected_author)

        # Analizar sentimientos
        if st.button('Analizar Sentimientos'):
            analyze_sentiment(messages, author=selected_author)

if __name__ == '__main__':
    main()
