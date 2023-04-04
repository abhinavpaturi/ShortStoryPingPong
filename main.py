import spacy
import random

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Define a dictionary of prompts to continue the story
prompts = {
  "treasures": [
    "They found a chest full of gold coins.",
    "They discovered a map leading to a hidden treasure."
  ],
  "foes": [
    "They battled a group of fierce pirates.",
    "They encountered a giant octopus."
  ],
  "seas": [
    "They braved a raging storm.",
    "They navigated through a treacherous maze of rocks."
  ],
  "pirates": [
    "They fought their way through a horde of undead pirates.",
    "They narrowly escaped a pirate ambush."
  ]
}


# Define a function to generate a response based on user input
def generate_response(user_input):
  # Process the user input with spaCy
  doc = nlp(user_input)
  # Check if the user input contains a prompt keyword
  for token in doc:
    if token.text.lower() in prompts.keys():
      # Randomly select a response from the prompts dictionary
      response = random.choice(prompts[token.text.lower()])
      return response
  # If no prompt keyword is found, generate a default response
  return "Interesting story! What happens next?"


# Start the conversation
print("Let's create a story together! Tell me what happens next.")
while True:
  # Get user input
  user_input = input("You: ")
  # Generate a response
  response = generate_response(user_input)
  # Print the response
  print("Bot: " + response)
