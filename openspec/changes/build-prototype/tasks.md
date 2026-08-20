## 1. Local STT and SLM Setup

- [x] 1.1 Implement `stt.py` using `whisper-cpp-python` or `faster-whisper` and verify it can transcribe a local `.wav` file into text.
- [ ] 1.2 Implement `extractor.py` using `llama-cpp-python` with GBNF generation from Pydantic models, and verify it returns a valid JSON object.

## 2. Database and RAG

- [ ] 2.1 Implement `db.py` to initialize SQLite with `sqlite-vec` and create the `entities` and `entries` tables. Verify the tables are created.
- [ ] 2.2 Add embedding generation to `db.py` and verify we can save an entry with its embedding.
- [ ] 2.3 Implement vector search in `db.py` and verify we can retrieve top-K results based on cosine similarity.

## 3. Controller Loop and Integration

- [ ] 3.1 Implement the `main.py` controller loop that ties STT, extraction, and DB together. Verify the happy path logs a successfully saved entry.
- [ ] 3.2 Implement the explicit null clarification check in `main.py` and verify it logs a clarification prompt when fields are missing.
- [ ] 3.3 Ensure accumulated session state is passed to the extractor on clarification turns, and verify the model correctly fills the missing fields.
