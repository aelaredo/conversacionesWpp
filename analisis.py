from transformers import pipeline

def analyze_sentiment(messages, author=None):
    # Filtrar mensajes por autor si es necesario
    if author:
        messages = [msg['message'] for msg in messages if msg['author'] == author]
    else:
        messages = [msg['message'] for msg in messages]

    # Cargar el modelo de análisis de sentimientos
    sentiment_analyzer = pipeline('sentiment-analysis')

    # Analizar el sentimiento de cada mensaje
    results = sentiment_analyzer(messages)

    # Mostrar los resultados
    for msg, result in zip(messages, results):
        print(f'Mensaje: {msg}')
        print(f'Sentimiento: {result["label"]}, Confianza: {result["score"]:.2f}')
        print('---')

# Ejemplo de uso
analyze_sentiment(messages, author='Tu Novia')
