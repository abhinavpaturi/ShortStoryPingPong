import openai
import re

# Initialize OpenAI API client
openai.api_key = ("Your api key here")


def get_story_continuation(prompt, tokens=30):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    n=1,
    max_tokens=tokens,
    temperature=0.7,
  )
  continuation = response.choices[0].text.strip()
  return re.sub(r"\n+", " ", continuation)


def short_story_teller():
  print("Welcome to the short story teller!")
  turns = int(input("How many turns? "))

  story = []
  for turn in range(turns):
    if turn % 2 == 0:
      user_input = input("\nUser: ")
      story.append(user_input)
      if turn == 0:
        continue
    else:
      prompt = f"{story[-1]}"
      bot_input = get_story_continuation(prompt)
      print(f"Bot: {bot_input}")
      story.append(bot_input)

  full_story = " ".join(story)
  print(f"\nThe short story is:\n{full_story}")


if __name__ == "__main__":
  short_story_teller()
