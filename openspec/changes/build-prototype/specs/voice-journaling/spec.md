## Purpose

Provides offline voice journaling by processing audio to structured JSON and storing it for local vector retrieval.

## ADDED Requirements

### Requirement: Extract structured data from voice
The system SHALL process an audio file and extract a structured JSON response corresponding to a pre-defined schema, running completely offline.

#### Scenario: All required fields are present
- **WHEN** the user utterance contains all required fields for the active schema
- **THEN** the system extracts a complete JSON object without triggering a clarification

#### Scenario: Missing required fields
- **WHEN** the user utterance is missing required fields for the active schema
- **THEN** the system extracts explicit null values for missing fields and returns a clarification prompt

### Requirement: Save and retrieve entries
The system SHALL save completed entity records and entries into a local datastore, and generate vector embeddings for semantic search.

#### Scenario: Store a completed entry
- **WHEN** a complete JSON object is extracted and the corresponding entity is verified
- **THEN** the system saves the raw text and JSON into the local store and generates an embedding

#### Scenario: Retrieve entries via query
- **WHEN** a user issues a search query
- **THEN** the system retrieves the top-K most similar historical entries and formulates a summary response
