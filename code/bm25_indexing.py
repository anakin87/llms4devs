# Install the Weaviate document store and the Weaviate-Haystack integration:
# https://docs.haystack.deepset.ai/docs/weaviatedocumentstore

import glob
from haystack_integrations.document_stores.weaviate.document_store \
    import WeaviateDocumentStore
from haystack import Pipeline
from haystack.components.converters import TextFileToDocument
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter


document_store = WeaviateDocumentStore(url="http://localhost:8080")

pipe = Pipeline()
pipe.add_component("converter", TextFileToDocument())
pipe.add_component("splitter", DocumentSplitter())
pipe.add_component("writer", DocumentWriter(document_store))
pipe.connect("converter", "splitter")
pipe.connect("splitter", "writer")

file_paths = glob.glob("data/*.txt")
pipe.run({"sources": file_paths})

print(document_store.count_documents())