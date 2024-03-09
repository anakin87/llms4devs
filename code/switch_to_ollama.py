# Install the Ollama-Haystack integration:
# ! pip install ollama-haystack

from haystack_integrations.components.generators.ollama import OllamaGenerator

generator = OllamaGenerator(model="mistral")
print(generator.run(prompt="Where is Florence?"))

# {'replies': [' Florence is a city in the region of Tuscany...'], ...}
