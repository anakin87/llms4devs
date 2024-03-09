# Install Haystack:
# ! pip install haystack-ai

import os
from haystack.components.generators import OpenAIGenerator

# Set an environment variable for the OpenAI API key 
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

generator = OpenAIGenerator()
print(generator.run(prompt="Where is Florence?"))