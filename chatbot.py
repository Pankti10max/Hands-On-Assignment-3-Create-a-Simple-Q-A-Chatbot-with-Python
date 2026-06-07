from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
bot = ChatBot(
    "AssignmentBot"
)

# Train chatbot
trainer = ListTrainer(bot)

conversation = [
    "Good morning",
    "Hello! How are you today?",
    "I am fine",
    "That's great to hear.",
    "What is your name?",
    "My name is AssignmentBot.",
    "Do you like hats?",
    "Yes, hats are interesting."
]

trainer.train(conversation)

print("Chatbot is ready!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("user: ")

    if user_input.lower() == "exit":
        print("bot: Goodbye!")
        break

    response = bot.get_response(user_input)
    print("bot:", response)
