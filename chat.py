import openai

openai.api_key = ""  # colocar la key personal de la pagina openai

chat_history = []

while True:
    prompt = input('Enter a prompt: ')

    if prompt == "exit":
        break
    else:

        chat_history.append({'role': 'user', 'content': prompt})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            stream=True
        )

        messages = []

        for chunk in response:
            chunk_message = chunk["choices"][0]["delta"]
            messages.append(chunk_message)
            full_reply = ''.join([m.get('content', '') for m in messages])

            print(full_reply)

            print("\033[H\033[J", end="")  # codigo que limpia la consola

        chat_history.append({'role': "assistant", 'content': full_reply})
        print(full_reply)
