import os 
from groq import Groq 
from retrieval import retrieve

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a grounded QA assistant. You MUST follow these rules:

1. Answer ONLY using the information in the provided context.
2. If the context does not contain enough information, say:
   "I don't have enough information."
3. Do NOT use outside knowledge.
4. Cite the source filenames in your answer.
"""
def generate_answer(question, retrieved_chunks):
    context_text = "\n\n".join(
        f"[Source: {c['source']}] {c['text']}"
        for c in retrieved_chunks
    )

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context_text}

Question: {question}

Answer:
"""
    response = client.chat.completions.create(
        model ="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message["content"]

def ask(question, k=5):
    chunks = retrieve(question, k=k)
    sources = list({c["source"] for c in chunks})
    answer = generate_answer(question, chunks)

    return{
        "answer": answer,
        "sources": sources
    }
