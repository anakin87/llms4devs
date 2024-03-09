# install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# start the Ollama server
ollama serve

# run this command in another shell session to pull the Mistral model
ollama pull mistral