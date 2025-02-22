import requests
from typing import List

def get_embedding(text: str, server_url: str = "http://localhost:8080") -> List[float]:
    """
    Fetches the embedding vector for a given text using the BGE-M3-F16 API.

    Args:
        text (str): The input text to be embedded.
        server_url (str): The base URL of the embedding server (default: "http://localhost:8080").

    Returns:
        List[float]: The embedding vector (length 1024).
    """
    try:
        response = requests.post(f"{server_url}/embedding", json={"content": text})
        response.raise_for_status()  # Raise an error for HTTP errors (4xx, 5xx)

        data = response.json()
        if isinstance(data, list) and len(data) > 0 and "embedding" in data[0]:
            return data[0]["embedding"][0]

        raise ValueError("Unexpected response format from embedding API.")

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error communicating with embedding server: {e}")

# Example usage
if __name__ == "__main__":
    text = "This is a test! I have a cookie. It is delicious."
    embedding = get_embedding(text)
    print(f"Embedding size: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")

