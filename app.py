import re

def parse_whatsapp_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.getvalue().decode("utf-8").split("\n")

    messages = []
    for line in lines:
        # Usamos una expresión regular para extraer la fecha, el autor y el mensaje
        match = re.match(r'\[(.*?)\] (.*?): (.*)', line)
        if match:
            date, author, message = match.groups()
            messages.append({'date': date, 'author': author, 'message': message})

    return messages

# Ejemplo de uso
file_path = 'chat.txt'
messages = parse_whatsapp_chat(file_path)

