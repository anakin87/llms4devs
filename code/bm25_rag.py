from haystack_integrations.document_stores.weaviate.document_store import (
    WeaviateDocumentStore,
)
from haystack_integrations.components.retrievers.weaviate.bm25_retriever import (
    WeaviateBM25Retriever,
)
from haystack import Pipeline
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack_integrations.components.generators.ollama import OllamaGenerator

# Create a RAG query pipeline
prompt_template = """
    Given these documents, answer the question.\nDocuments:
    {% for doc in documents %}
        {{ doc.content }}
    {% endfor %}

    \nQuestion: {{question}}
    \nAnswer:
    """

document_store = WeaviateDocumentStore(url="http://localhost:8080")

rag_pipeline = Pipeline()
rag_pipeline.add_component(
    name="retriever", instance=WeaviateBM25Retriever(document_store, top_k=5)
)
rag_pipeline.add_component(
    instance=PromptBuilder(template=prompt_template), name="prompt_builder"
)
rag_pipeline.add_component(instance=OllamaGenerator(model="mistral"), name="llm")
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")

question = "who is Samuel Thomas Fender?"
print(rag_pipeline.run(
    {
        "retriever": {"query": question},
        "prompt_builder": {"question": question},
    }
))