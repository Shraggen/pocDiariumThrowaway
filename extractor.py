import json
from pydantic import BaseModel
from typing import Type
from llama_cpp import Llama

class Extractor:
    def __init__(self, model_path: str):
        self.llm = Llama(model_path=model_path, n_ctx=2048, verbose=False)

    def extract(self, text: str, schema: Type[BaseModel], history: list = None) -> BaseModel:
        system_prompt = "You are a helpful data extraction assistant. Extract the JSON from the user's text."
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": text})

        response = self.llm.create_chat_completion(
            messages=messages,
            response_format={
                "type": "json_object",
                "schema": schema.model_json_schema()
            }
        )
        content = response["choices"][0]["message"]["content"]
        data = json.loads(content)
        return schema(**data)
