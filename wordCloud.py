from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(messages, author=None):
    # Filtrar mensajes por autor si es necesario
    if author:
        messages = [msg['message'] for msg in messages if msg['author'] == author]
    else:
        messages = [msg['message'] for msg in messages]

    # Unir todos los mensajes en un solo texto
    text = ' '.join(messages)

    # Generar la nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Mostrar la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Ejemplo de uso
generate_word_cloud(messages, author='Tu Novia')

