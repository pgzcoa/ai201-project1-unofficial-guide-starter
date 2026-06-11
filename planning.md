# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? --> My domain focuses on identifying the best pizza in Southern California using reviews and descriptions from Yelp, Google Maps, Reddit threads, and local food guides.  This information is scattered across many platforms, making it difficult for students to compare quality, price, and style in one place. My system will make this knowledge searchable so people can quickly find the best pizza options on their preferences of pizza.


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

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

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

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
