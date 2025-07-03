FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y curl sudo git

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Expose Ollama API port
EXPOSE 11434

# Start Ollama server
CMD ["ollama", "serve"]
