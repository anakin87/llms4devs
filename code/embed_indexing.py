import glob
from haystack_integrations.document_stores.weaviate.document_store \
    import WeaviateDocumentStore
from haystack import Pipeline
from haystack.components.converters import TextFileToDocument
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder


document_store = WeaviateDocumentStore(url="http://localhost:8080")

pipe = Pipeline()
pipe.add_component("converter", TextFileToDocument())
pipe.add_component("splitter", DocumentSplitter())
pipe.add_component("embedder", SentenceTransformersDocumentEmbedder())
pipe.add_component("writer", DocumentWriter(document_store))
pipe.connect("converter", "splitter")
pipe.connect("splitter", "embedder")
pipe.connect("embedder", "writer")

file_paths = glob.glob("data/*.txt")
pipe.run({"sources": file_paths})