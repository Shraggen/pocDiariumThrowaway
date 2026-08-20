## Context

This is the implementation of the core architecture outlined in the existing `design.md` and `docs/adr/0001-slm-extraction-and-state.md`. 
We are building a flat, component-based functional architecture with `main.py`, `stt.py`, `extractor.py`, and `db.py`.

## Goals / Non-Goals

**Goals:**
- Implement the local pipeline from audio ingestion to JSON extraction to SQLite vector storage.
- Support a clarification loop via accumulated session state for missing data.
- Ensure 100% offline functionality.

**Non-Goals:**
- Complex UI (this is just the backend prototype).
- Supporting multiple STT or SLM engines simultaneously (we will just pick one per component: `faster-whisper` for STT and `llama-cpp-python` for SLM).

## Decisions

1. **Extraction engine**: We will use `llama-cpp-python` with GBNF grammar generation from Pydantic schemas. (As per ADR-0001).
2. **Missing data**: Enforce explicit nulls in Pydantic schemas to trigger the entity resolver's clarification prompt.
3. **Database**: Use `sqlite-vec` to manage embeddings and JSON structured data side-by-side in a local SQLite file.
4. **Session State**: The `main.py` controller will manage an accumulated session history, passing it to `extractor.py` on subsequent turns for context preservation.

## Risks / Trade-offs

- **Risk: Hardware Requirements** -> Mitigation: Use Q4 quantized edge models like `Llama-3.2-3B-Instruct` for fast performance and `faster-whisper` for STT.
- **Risk: Hallucinated JSON Keys** -> Mitigation: Strict GBNF grammars mapped directly from Pydantic models.
