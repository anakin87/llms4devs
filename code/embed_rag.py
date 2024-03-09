from haystack_integrations.document_stores.weaviate.document_store import (
    WeaviateDocumentStore,
)
from haystack_integrations.components.retrievers.weaviate import (
    WeaviateEmbeddingRetriever
)
from haystack import Pipeline
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack_integrations.components.generators.ollama import OllamaGenerator
from haystack.components.embedders import SentenceTransformersTextEmbedder

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
rag_pipeline.add_component("text_embedder", SentenceTransformersTextEmbedder())
rag_pipeline.add_component(
    name="retriever", instance=WeaviateEmbeddingRetriever(document_store=document_store, top_k=5)
)
rag_pipeline.add_component(
    instance=PromptBuilder(template=prompt_template), name="prompt_builder"
)
rag_pipeline.add_component(instance=OllamaGenerator(model="mistral"), name="llm")
rag_pipeline.connect("text_embedder", "retriever")
rag_pipeline.connect("retriever", "prompt_builder.documents")
rag_pipeline.connect("prompt_builder", "llm")


question = """Audioslave was formed by members of two bands. 
Can you name the bands and summarize the Audioslave sound with a short bulleted list?"""

print(rag_pipeline.run(
    {
        "text_embedder": {"text": question},
        "prompt_builder": {"question": question},
    }
))