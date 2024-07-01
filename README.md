# Large Language Models for Developers - from zero to your first LLM application
- [🍿 Talk - 1st edition - Open Source Day 2024](https://www.youtube.com/watch?v=L6sUztYJXT8)
- [🍿 Talk - 2nd edition - PyCon Italy 2024](https://www.youtube.com/watch?v=R_C0IJmAHrQ)
- [🧑‍🏫 Slide deck](./slide_deck.pdf)

Material for the homonymous talk.

<details><summary>📝 Abstract</summary>
The rise of ChatGPT and Large Language Models has revolutionized the tech landscape, leaving developers overwhelmed by the infinite opportunities and intrigued by the technical challenges posed by their complex nature.

This session provides a developer-centric introduction to LLMs, focused on practical applications. No pre-existing knowledge of LLMs and NLP is required.

You will gain insights into: using closed and open-source models, how to effectively prompt LLMs, vector databases, implementing Retrieval Augmented Generation applications (answer generation based on your data), building more complex applications.

Through a hands-on approach, I will show code examples using open-source tools: Haystack LLM framework, Hugging Face Transformers, Ollama, and more. I will also show how you can switch from proprietary to open models.
</details>

## 📚 Resources and code ‍💻


- [Haystack LLM framework](#haystack-llm-framework)
- [Start from a proprietary model](#start-from-a-proprietary-model)
- [Switch to local open LLMs with Ollama](#switch-to-local-open-llms-with-ollama)
  - [Chat with Mistral](#chat-with-mistral)
- [Prompt Engineering](#prompt-engineering)
- [RAG](#rag)
  - [Naive RAG](#naive-rag)
  - [Web RAG](#web-rag)
- [Retrieval](#retrieval)
  - [Document Stores and Retrievers](#document-stores-and-retrievers)
  - [Keyword-based Retrieval (BM25)](#keyword-based-retrieval-bm25)
  - [Embedding/vector Retrieval](#embeddingvector-retrieval)
  - [Hybrid Retrieval](#hybrid-retrieval)
- [From Demo to Production](#from-demo-to-production)
  - [Choose a good Language Model](#choose-a-good-language-model)
  - [Choose a LLM inference solution](#choose-a-llm-inference-solution)
  - [Evaluation](#evaluation)
  - [Deployment](#deployment)
- [Beyond RAG...](#beyond-rag)
- [There is much more!](#there-is-much-more)


### Haystack LLM framework
- [Website](https://haystack.deepset.ai?utm_campaign=developer-relations&utm_source=pycon-it)
- [GitHub](https://github.com/deepset-ai/haystack)
- [Main concepts](https://docs.haystack.deepset.ai/docs/components_overview?utm_campaign=developer-relations&utm_source=pycon-it)

### Start from a proprietary model
- [Code snippet](./code/start.py)
- [OpenAI Generator docs](https://docs.haystack.deepset.ai/docs/openaigenerator?utm_campaign=developer-relations&utm_source=pycon-it)

### Switch to local open LLMs with Ollama
- [Ollama-Haystack integration](https://haystack.deepset.ai/integrations/ollama?utm_campaign=developer-relations&utm_source=pycon-it)
- Code snippets: [run Ollama](./code/ollama.sh); [use Ollama in Haystack](./code/switch_to_ollama.py)

#### Chat with Mistral
- [ChatMessage docs](https://docs.haystack.deepset.ai/docs/data-classes#chatmessage)
- [Code snippet](./code/chat_w_mistral.py)

### Prompt Engineering
- [OpenAI guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [promptingguide.ai](https://www.promptingguide.ai/)

### RAG
- [Introduction to RAG with code examples](https://haystack.deepset.ai/blog/rag-pipelines-from-scratch?utm_campaign=developer-relations&utm_source=pycon-it)

#### Naive RAG
- [Code snippet](./code/naive_rag.py)

#### Web RAG
- [Docs](https://docs.haystack.deepset.ai/docs/serperdevwebsearch?utm_campaign=developer-relations&utm_source=pycon-it)

### Retrieval

#### Document Stores and Retrievers
- [Document Store abstraction](https://docs.haystack.deepset.ai/docs/document-store?utm_campaign=developer-relations&utm_source=pycon-it)
- [Choosing a Document Store](https://docs.haystack.deepset.ai/docs/choosing-a-document-store?utm_campaign=developer-relations&utm_source=pycon-it)
- [Retrievers](https://docs.haystack.deepset.ai/docs/retrievers?utm_campaign=developer-relations&utm_source=pycon-it)

#### Keyword-based Retrieval (BM25)
- Introduction to keyword-based retrieval: [Bag of Words and TF-IDF](https://github.com/anakin87/neural-search-pills/blob/main/pills/sparse-bow-tfidf.md); [BM25](https://github.com/anakin87/neural-search-pills/blob/main/pills/sparse-bm25.md)
- [BM25 Indexing Pipeline - code snippet](./code/bm25_indexing.py)
- [BM25 RAG Pipeline - code snippet](./code/bm25_rag.py)

#### Embedding/vector Retrieval
- Introduction to vector retrieval: [From sparse representations to Language Models](https://github.com/anakin87/neural-search-pills/blob/main/pills/from-sparse-to-lm.md); [Dense Passage Retrieval](https://github.com/anakin87/neural-search-pills/blob/main/pills/dpr.md); [Sentence Transformers for Dense Retrieval](https://github.com/anakin87/neural-search-pills/blob/main/pills/sbert.md)
- [Embedding Indexing Pipeline - code snippet](./code/embed_indexing.py)
- [Embedding RAG Pipeline - code snippet](./code/embed_rag.py)

#### Hybrid Retrieval
- [Retrieve and Re-Rank](https://github.com/anakin87/neural-search-pills/blob/main/pills/retrieve-re-rank.md)
- [Hybrid Retrieval Tutorial](https://haystack.deepset.ai/tutorials/33_hybrid_retrieval?utm_campaign=developer-relations&utm_source=pycon-it)

### From Demo to Production

#### Choose a good Language Model
- [LLM Evals and Benchmarking](https://osanseviero.github.io/hackerllama/blog/posts/llm_evals/) - Great blog post by Omar San Seviero
- [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- [LMSYS Chatbot Arena Leaderboard](https://chat.lmsys.org/)
- [Open ITA LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

#### Choose a LLM inference solution
- [Docs](https://docs.haystack.deepset.ai/docs/choosing-the-right-generator?utm_campaign=developer-relations&utm_source=pycon-it)

#### Evaluation
- [Docs](https://docs.haystack.deepset.ai/docs/evaluation?utm_campaign=developer-relations&utm_source=pycon-it)

#### Deployment
- [Serialization of Pipelines](https://docs.haystack.deepset.ai/docs/serialization?utm_campaign=developer-relations&utm_source=pycon-it)
- [Hayhooks](https://docs.haystack.deepset.ai/docs/hayhooks?utm_campaign=developer-relations&utm_source=pycon-it)
- [Deployment guides](https://docs.haystack.deepset.ai/docs/deployment?utm_campaign=developer-relations&utm_source=pycon-it)

### Beyond RAG...
- [Haystack cookbook](https://github.com/deepset-ai/haystack-cookbook)
- [Multilingual RAG from a podcast](https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/multilingual_rag_podcast.ipynb)
- [Hacker News summarizer](https://huggingface.co/spaces/Tuana/hackernews-summaries)
- [Information extraction via LLMs](https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/information_extraction_raven.ipynb)
- [AutoQuizzer](https://huggingface.co/spaces/deepset/autoquizzer)

### There is much more!
- [File converters](https://docs.haystack.deepset.ai/docs/file-converters?utm_campaign=developer-relations&utm_source=pycon-it)
- Observability: [logging](https://docs.haystack.deepset.ai/docs/logging?utm_campaign=developer-relations&utm_source=pycon-it) and [tracing](https://docs.haystack.deepset.ai/docs/tracing?utm_campaign=developer-relations&utm_source=pycon-it)
- Function calling: [docs](https://docs.haystack.deepset.ai/docs/function-calling?utm_campaign=developer-relations&utm_source=pycon-it) and [tutorial](https://haystack.deepset.ai/tutorials/40_building_chat_application_with_function_calling?utm_campaign=developer-relations&utm_source=pycon-it)

- Conclusion: ["The Shift from Models to Compound AI Systems" - blog post](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/)
