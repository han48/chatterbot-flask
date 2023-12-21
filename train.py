from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import glob

chatbot = ChatBot(
    'Sabitech',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry. I cannot answer this question!',
            'maximum_similarity_threshold': 0.80
        },
    ],
)

trainer = ChatterBotCorpusTrainer(chatbot)

path = r'./datasets/sabitech/*.yml'
for name in glob.glob(path):
    trainer.train(name)
