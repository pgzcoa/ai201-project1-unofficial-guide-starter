# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? --> My domain focuses on identifying the best pizza in Southern California using reviews and descriptions from Yelp, Google Maps, Reddit threads, and local food guides.  This information is scattered across many platforms, making it difficult for people to compare quality, price, and style in one place. My system will make this knowledge searchable so people can quickly find the best pizza options on their preferences of pizza.  This is valuable because pizza quality varies by city, locals know hidden gems, and official sources don't compile this information. Pizza is a very popular and comfort food. 


## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 |Eater LA |Best pizza in OC |https://la.eater.com/maps/best-pizza-orange-county |
| 2 |LA Times |Pizza Coverage |https://latimes.com/food |
| 3 |Reddit |local inland empire favorite pizza spots |https://www.reddit.com/r/InlandEmpire/search?q=pizza&restrict_sr=1 |
| 4 |Yelp |Mountain Mike's Pizza |https://yelp.com/biz/mountain-mikes-pizza-ontario |
| 5 |Yelp |Terra Mia Pizzeria |https://www.yelp.com/biz/terra-mia-pizzeria-laguna-hills |
| 6 |Yelp |Bella Forno Pizzeria |https://www.yelp.com/biz/bella-forno-pizzeria-redlands |
| 7 |Google Maps |Best pizza in Southern California | https://www.google.com/maps/search/best+pizza+in+southern+california|
| 8 |Google Maps |best pizza in Northridge |https://www.google.com/maps/search/best+pizza+in+northridge+ca |
| 9 |Google Maps |best pizza in Long Beach |https://www.google.com/maps/search/best+pizza+in+long+beach+ca |
| 10 |Google Maps |best pizza in San Diego |https://www.google.com/maps/search/best+pizza+in+san+diego+ca |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 50 tokens

**Overlap:** 10 - 15 tokens

**Reasoning:**
My documents are mostly short reviews from Google Maps, Yelp, Reddit, LA Times, and Eater LA. These reviews are usually short,and small chunk size keeps each opinion self contained instead of mixing multiple restaurants together.  A 50 token chunk is enough to capture a full review while staying focused.  I am adding 10 - 15 tokens of overlap so that if a review is slightly longer than one chunk, important details(like the restaurant name or the main opinion)are not cut off between the chunks.  If the chunks are too small the retrieval would return incomplete reviews.  If the chunks were too large then unrelated reviews would get merged and the accuracy would be reduced.  This chunk size and overlap would give a clean precise retrieval for short reviews.
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-Mini-L6-v2
It does not weight a lot,fast, and performs well on short reviews. Since my documents are small reviews I do not need a large or expensive embedding model.
**Top-k:**
3 - 5 chunks per query
If I retrieve too few chunks then I could miss important reviews.  If I retrieve too many then I could get reviews from restaurants that are not related to the best pizza places in Southern California.
**Production tradeoff reflection:**
If this were a real production system with no cost constraints, I would consider larger and more powerful embedding models like all-mpnet-base-v2 or Open AI text embedding models.  Bigger models can caputure more details in long reviews, handle multilingual text, and improve accuracy for domain-specific language. The tradeoff is higher compute cost, slower retrieval, and increased latency. For this project all-MiniLM-L6-v2 provides the right balance of speed, cost, and accuracy for short review style documents.
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 |What are the highest rated pizza places in Southern California? | Bella Forno Pizzeria(Redlands) and Bronx Pizza (San Diego) and (Mulberry Street Pizza(Beverly Hills) and Terra Mia Pizzeria (Laguna Hills)|
| 2 |Which pizza spots offer the best value for the price? | Big Slice Pizza(Long Beach) and Pisa Pizza (San Bernardino)|
| 3 |Which pizza places are most recommended by locals and students? |Terra Mia (Laguna Hills) and top Northridge/Long Beach Google Maps picks |
| 4 |What pizza restaurants have consistent reviews across multiple counties and across multiple platforms? |Terra Mia, Bella Forno, and Mountain Mike's |
| 5 |Which pizza places in Southern California have the fastest and most reliable delivery?  |Mountain Mike's (Ontario) & Bronx Pizza(San Diego) |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Important details might get split across chunks

2.Retrieval may bring restaurants that do not fit the query and give irrelevant results

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---
   Flowchart
   A[Document Ingestion(Python file loading)]----> B[Chunking(50-token chunks + 10 - 15 overlap)]
   B---> C[Embedding + Vector Store (all-MiniLM-L6-v2 + ChromaDB)]
   C---> D[Retrieval (Top-k = 3-5)]
   D --> E[Generation (LLM uses retrieved chunks)]
## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)  

     - What you'll give it as input (which sections of this planning.md, which requirements)


     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

     AI Plan

     Document
     I will verify the output by checking that all documents load correctly and match the file paths that I specify.

     Chunking
     I will verify the output by running the function on a sample review and confirming the chunk sizes and overlap match my specifications.

     Embedding + Vector Store
     I expect it to produce the code so that it initializes the model, embeds each chunk, and inserts them into the vector store. I will verify by checking that the database contains the correct number of embeddings.

     Retrieval
     I will verify the output by testing queries from Evaluation Plan and confirming that the retrieved chunks match the expected restaurants or reviews.

     Generation
     I will verify this by running the 5 evaluation questions and checking whether the answers match the expected results.

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
