## Why

We need to build the initial prototype for the offline voice journaling application as defined in our ADRs and design documents. The goal is to prove the core concept of extracting structured data from messy voice transcripts entirely on-device, without relying on external network APIs, while using edge-optimized SLMs and local vector search for RAG.

## What Changes

- Implement the main controller loop (`main.py`)
- Implement the Speech-to-Text module using `whisper-cpp-python` or `faster-whisper` (`stt.py`)
- Implement the SLM extraction and clarification engine with `llama-cpp-python` using Pydantic + GBNF (`extractor.py`)
- Implement the local SQLite store with `sqlite-vec` for embeddings and entity/entry storage (`db.py`)
- Add tests to ensure robust JSON extraction and handling of explicit nulls (`test_...`)

## Capabilities

### New Capabilities
- `voice-journaling`: Processing audio to structured JSON with SLM and STT, including the clarification loop, and storing entities/entries in SQLite for local vector search (RAG).

### Modified Capabilities

## Impact

- Adds core Python modules (`main.py`, `stt.py`, `extractor.py`, `db.py`)
- Introduces dependencies on `llama-cpp-python`, `faster-whisper` / `whisper-cpp-python`, `sqlite-vec`, `pydantic`
- Establishes the primary pipeline for the application.
