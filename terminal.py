from chatterbot import ChatBot

chatbot = ChatBot(
    'Sabitech',
    read_only=True,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry. I cannot answer this question!',
            'maximum_similarity_threshold': 0.80
        },
    ],
)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
