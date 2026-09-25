import json
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-5.6-luna",
    input="Return exactly one character: A",
    top_p=0.98,
    max_output_tokens=64,
    tools=[],
    tool_choice="auto",
    background=False,
    store=False,
)
print(json.dumps({
    "scientific_execution": "NOT_PERFORMED",
    "diagnostic_only": True,
    "response_id": getattr(response, "id", None),
    "status": getattr(response, "status", None),
    "output_text": getattr(response, "output_text", ""),
    "incomplete_details": getattr(response, "incomplete_details", None),
    "model": getattr(response, "model", None),
    "usage": response.usage.model_dump() if hasattr(response.usage, "model_dump") else None
}, ensure_ascii=False, indent=2))
