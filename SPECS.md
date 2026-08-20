# Pipeline Flow
1. Audio File (.wav, 16kHz mono) -> STT Module -> Raw Transcript string.
2. Raw Transcript + Active Schema Name -> SLM Module -> Structured JSON object.
3. Structured JSON -> Entity Resolver:
   - Check if entity exists in SQLite.
   - If missing required fields -> return Clarification Prompt.
   - If complete -> Save to `entries` and generate embedding for RAG.
4. Voice Query -> Vector Search -> Top-K context -> SLM Summary string.
