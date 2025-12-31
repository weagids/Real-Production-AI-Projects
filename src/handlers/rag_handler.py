import json
import logging

from ingestion.embedder import BedrockEmbedder
from ingestion.vector_store import OpenSearchVectorStore
from prompts.rag_prompt import build_rag_prompt
from llm.bedrock_llm import BedrockLLM

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize clients outside handler (best practice)
embedder = BedrockEmbedder()
llm = BedrockLLM()

VECTOR_ENDPOINT = "https://your-opensearch-endpoint"
INDEX_NAME = "enterprise-genai-knowledge"

vector_store = OpenSearchVectorStore(
    endpoint=VECTOR_ENDPOINT,
    index_name=INDEX_NAME
)

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        question = body.get("question")

        if not question:
            return _response(400, "Question is required")

        logger.info(json.dumps({
            "event": "question_received",
            "question": question
        }))

        # 1️⃣ Embed query
        query_embedding = embedder.embed_chunks([
            {"id": "query", "text": question, "metadata": {}}
        ])[0]["embedding"]

        # 2️⃣ Retrieve context
        search_results = vector_store.search(query_embedding, top_k=5)

        if not search_results:
            return _response(200, "No relevant information found.")

        context_text = "\n\n".join(
            f"Source: {r['metadata'].get('source')}\n{r['text']}"
            for r in search_results
        )

        logger.info(json.dumps({
            "event": "answer_generated",
            "sources": [r['metadata'].get("source") for r in search_results]
        }))

        # 3️⃣ Build prompt
        prompts = build_rag_prompt(context_text, question)

        # 4️⃣ Generate answer
        answer = llm.generate_answer(
            system_prompt=prompts["system"],
            user_prompt=prompts["user"]
        )

        return _response(200, answer)

    except Exception as e:
        logger.exception("RAG processing failed")
        return _response(500, "Internal server error")


def _response(status_code, message):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": message})
    }
