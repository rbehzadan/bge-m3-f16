# BGE-M3-F16 Docker Image

This repository provides a multi-architecture (AMD64 & ARM64) Docker image for serving [BGE-M3](https://huggingface.co/BAAI/bge-m3) embeddings using [llama.cpp](https://github.com/ggml-org/llama.cpp).

## Usage

### Run with Docker
```sh
docker run -d --name bge-m3-f16 -p 8080:8080 rbehzadan/bge-m3-f16
```

### Run with Docker Compose
Create a `docker-compose.yml` file:
```yaml
services:
  bge-m3-f16:
    container_name: bge-m3-f16
    image: rbehzadan/bge-m3-f16
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    ports:
      - "8080:8080"
```

Start the service:
```sh
docker compose up -d
```

## API Usage

Once the container is running, you can send text to `/embedding` to get the embedding vector.

Example using Python:
```python
import requests

response = requests.post("http://localhost:8080/embedding", json={"content": "This is a test! I have a cookie. It is delicious."})
embedding = response.json()[0]['embedding'][0]

print(f"Embedding size: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
```

### Expected Output:
```
Embedding size: 1024
First 5 values: [-0.052899, 0.041320, -0.022369, -0.024708, -0.009957]
```

## License
[MIT](LICENSE)

