# ADR 0001: SLM Extraction and State Management

## Status
Accepted

## Context
We are building an offline voice journaling prototype that uses local Speech-to-Text (STT) and Small Language Models (SLMs) to extract structured data from user transcripts. 

A core challenge is how to reliably extract this data into predefined schemas (e.g., `MechanicBrakes`, `BeekeeperInspection`) and how to gracefully handle "missing" data when the user's initial utterance doesn't contain all required fields. We need a robust mechanism to ask clarification questions and merge the user's follow-up answers back into the state.

## Decisions

### 1. Extraction Method: Pydantic + GBNF
We will define our domain schemas as Pydantic models. We will inject the schema definition into the SLM's system prompt so it understands the semantic meaning of the fields. Simultaneously, we will use `llama-cpp-python` to generate a GBNF grammar from the Pydantic model to strictly constrain the SLM's output syntax, ensuring valid JSON.

### 2. Missing Data Handling: Explicit Nulls
The SLM will be instructed to output explicit `null` values for any schema fields that are not mentioned in the transcript (e.g., `{"axle": null}`). This allows the deterministic Python `Entity Resolver` to easily iterate over the keys and trigger clarification prompts for required fields that are `None`.

### 3. Model Selection
We will use edge-optimized instruct models (such as `Llama-3.2-3B-Instruct` or `Llama-3.1-8B-Instruct`) quantized to Q4. These models are specifically tuned for tool calling and JSON formatting, and their small parameter count ensures low latency for local execution.

### 4. Clarification Loop: Accumulated Session State
When a user is asked a follow-up question (e.g., "Which axle?"), we will maintain the conversational turns in a session buffer. 
For the next extraction pass, we will pass the entire context to the SLM:
1. The Schema
2. The current extracted JSON state
3. The transcript history
4. The latest user utterance

**Reasoning:** Voice interactions are unpredictable. A user might answer the specific question but also provide additional out-of-band information (e.g., "Front axle, and also note the rotor was grooved"). A stateless "Targeted Update" prompt would drop this extra context. Sending the full context allows the SLM to handle multi-field additions naturally. On a 1B-3B model, the latency penalty for the extra context tokens (~40 tokens) is negligible (~30-50ms), while the robustness gain is significant.
