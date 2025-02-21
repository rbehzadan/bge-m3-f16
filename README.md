# BGE-M3-F16 Docker Image

This repository provides a multi-architecture (AMD64 & ARM64) Docker image for serving BGE-M3 embeddings using `llama.cpp`.

## Usage

### Run with Docker
```sh
docker run -d --name bge-m3-f16 -p 8080:8080 rbehzadan/bge-m3-f16
```

## API
Once running, the server is available at `http://localhost:8080`.

## License
[MIT](LICENSE)

