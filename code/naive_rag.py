from haystack import Pipeline, Document
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack_integrations.components.generators.ollama import OllamaGenerator

# Create the knowledge base
documents = [
    Document(content="Italian Super Cup is an annual super cup tournament in Italian football."),
    Document(content="The tournament was established in 1988 and the first title was won by AC Milan."),
    Document(content="In 2024, the tournament was won by Inter.")]

# Build a RAG pipeline
prompt_template = """
Given these documents, answer the question.
Documents:
{% for doc in documents %}
    {{ doc.content }}
{% endfor %}
Question: {{question}}
Answer:
"""

prompt_builder = PromptBuilder(template=prompt_template)

rag_pipeline = Pipeline()
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", OllamaGenerator(model="mistral"))
rag_pipeline.connect("prompt_builder", "llm")

# Ask a question
question = "Who won the Italian Super Cup in 2024?"
res = rag_pipeline.run({"question": question, "documents": documents})

print(res["llm"]["replies"])