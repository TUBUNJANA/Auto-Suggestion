from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from trie import Trie
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()
trie = Trie()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware to log request data
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logging.info(f"{request.method} {request.url.path} - {round(process_time, 4)}s")
    return response

@app.get("/suggest")
async def suggest(query: str):
    logging.info(f"Received suggestion request: {query}")
    suggestions = trie.search(query)
    if not suggestions:
        logging.info(f"No suggestions found for '{query}'. Adding to trie.")
        trie.insert(query)
        return {"message": "No suggestions found. Query added to trie."}
    logging.info(f"Suggestions for '{query}': {suggestions}")
    return {"suggestions": suggestions}

@app.post("/add")
async def add_sentence(sentence: str):
    logging.info(f"Adding sentence: {sentence}")
    trie.insert(sentence)
    return {"message": "Sentence added successfully."}

@app.get("/debug/trie")
async def get_trie_data():
    logging.info("Accessing full trie data for debugging.")
    return trie.to_dict()