import boto3
import json
import logging
from typing import List, Dict

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bedrock = boto3.client("bedrock-runtime")

class BedrockEmbedder:
    def __init__(self, model_id: str = "amazon.titan-embed-text-v1"):
        self.model_id = model_id

    def embed_chunks(self, chunks: List[Dict]) -> List[Dict]:
        embedded_chunks = []

        for chunk in chunks:
            body = json.dumps({
                "inputText": chunk["text"]
            })

            response = bedrock.invoke_model(
                modelId=self.model_id,
                body=body,
                accept="application/json",
                contentType="application/json"
            )

            response_body = json.loads(response["body"].read())
            embedding = response_body["embedding"]

            embedded_chunks.append({
                "id": chunk["id"],
                "embedding": embedding,
                "text": chunk["text"],
                "metadata": chunk["metadata"]
            })

        return embedded_chunks
