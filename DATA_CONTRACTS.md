# Database Schema (SQLite)
- `entities`: (id INTEGER PRIMARY KEY, name TEXT, type TEXT, aliases JSON)
- `entries`: (id INTEGER PRIMARY KEY, raw_text TEXT, structured_data JSON, embedding BLOB)

# Domain Schemas to Test
1. MechanicBrakes:
   - `axle`: "front" | "rear" | null
   - `pad_thickness_mm`: float | null
   - `rotor_condition`: string | null

2. BeekeeperInspection:
   - `hive_id`: int | null
   - `queen_seen`: bool | null
   - `temperament`: string | null
