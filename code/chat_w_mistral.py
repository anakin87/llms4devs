from haystack_integrations.components.generators.ollama import OllamaChatGenerator
from haystack.dataclasses import ChatMessage

generator = OllamaChatGenerator(model="mistral")

messages = []

while True:
  msg = input("Enter your message or Q to exit\n🧑 ")
  if msg=="Q":
    break
  messages.append(ChatMessage.from_user(msg))
  response = generator.run(messages=messages)
  assistant_resp = response['replies'][0]
  print("🤖 "+assistant_resp.content)
  messages.append(assistant_resp)