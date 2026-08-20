# Role & Rules
You are building an offline voice journaling prototype with local STT and GBNF-constrained SLM extraction.

## Tech Stack
- Python 3.11+
- Audio / STT: `whisper-cpp-python` or `faster-whisper`
- Local SLM: `llama-cpp-python` (with Grammar / GBNF support)
- Vector DB: `sqlite-vec` or pure numpy cosine similarity
- Test Framework: `pytest`

## Strict Constraints
1. NEVER call external network APIs (OpenAI, Anthropic, etc.). Everything must run locally.
2. ALWAYS enforce JSON extraction via GBNF grammars or explicit Pydantic JSON schemas.
3. Keep code modular: STT, SLM extractor, Entity Store, and Evaluator must be separate modules.
