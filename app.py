import gradio as gr 
from query import ask

def handle_query(question):
    result = ask(question)
    sources = "\n".join(f"*{s}" for s in result["sources"])
    return result["answer"], sources

with gr.Blocks() as demo:
    gr.Markdown("# Southern California Pizza RAG System")

    inp = gr.Textbook(label="Ask a question about Southern California pizza places")
    btn = gr.Button("Ask")

    answer = gr.Textbook(label="Answer", lines=8)
    sources = gr.Textbook(label="Retrieved from", lines=4)

    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

demo.launch()
