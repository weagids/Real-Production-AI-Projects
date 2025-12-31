def build_rag_prompt(context: str, question: str) -> dict:
    system_prompt = (
        "You are an enterprise knowledge assistant. "
        "Answer the question using ONLY the provided context. "
        "If the answer is not present in the context, say: "
        "'I do not have sufficient information to answer this question.' "
        "Be concise, factual, and professional."
    )

    user_prompt = (
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer:"
    )

    return {
        "system": system_prompt,
        "user": user_prompt
    }
