from typing import List, Dict
import uuid

class TextChunker:
    def __init__(self, chunk_size: int = 800, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str, source: str) -> List[Dict]:
        """
        Splits text into overlapping chunks with metadata.
        """
        words = text.split()
        chunks = []
        start = 0

        while start < len(words):
            end = start + self.chunk_size
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)

           chunks.append({
        "id": str(uuid.uuid4()),
        "text": chunk_text,
        "metadata": {
            "source": source,
            "tenant_id": tenant_id,
            "start_word": start,
            "end_word": end
                }
            })

            start = end - self.overlap

        return chunks

