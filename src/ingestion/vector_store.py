import json
import logging
import requests
from typing import List, Dict

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class OpenSearchVectorStore:
    def __init__(self, endpoint: str, index_name: str):
        self.endpoint = endpoint
        self.index_name = index_name
        self.headers = {"Content-Type": "application/json"}

    def create_index(self):
        mapping = {
            "settings": {
                "index": {
                    "knn": True
                }
            },
            "mappings": {
                "properties": {
                    "embedding": {
                        "type": "knn_vector",
                        "dimension": 1536
                    },
                    "text": {
                        "type": "text"
                    },
                    "metadata": {
                        "type": "object"
                    }
                }
            }
        }

        response = requests.put(
            f"{self.endpoint}/{self.index_name}",
            headers=self.headers,
            data=json.dumps(mapping)
        )

        logger.info(f"Index creation response: {response.text}")

    def store_embeddings(self, embedded_chunks: List[Dict]):
        for chunk in embedded_chunks:
            document = {
                "embedding": chunk["embedding"],
                "text": chunk["text"],
                "metadata": chunk["metadata"]
            }

            response = requests.post(
                f"{self.endpoint}/{self.index_name}/_doc/{chunk['id']}",
                headers=self.headers,
                data=json.dumps(document)
            )

            logger.info(f"Stored chunk {chunk['id']} → {response.status_code}")
