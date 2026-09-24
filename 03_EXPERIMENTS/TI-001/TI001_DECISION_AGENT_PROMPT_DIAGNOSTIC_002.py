import json
from pathlib import Path
from openai import OpenAI

MODEL = "gpt-5.6-luna"
TOP_P = 0.98
MAX_OUTPUT_TOKENS = 64

def main():
    repo = Path(__file__).resolve().parents[2]
    prompt_path = repo / "03_EXPERIMENTS" / "TI-001" / "TI001_DECISION_AGENT_BASE_PROMPT_001.md"
    prompt = prompt_path.read_text(encoding="utf-8")
    synthetic_input = """Current decision input:
Current state: S0
Currently executable transformations: [a, b, c]

Decision-time information is complete. Return exactly one executable transformation identifier."""

    client = OpenAI()
    response = client.responses.create(
        model=MODEL,
        instructions=prompt,
        input=synthetic_input,
        top_p=TOP_P,
        max_output_tokens=MAX_OUTPUT_TOKENS,
        tools=[],
        tool_choice="auto",
        background=False,
        store=False,
    )

    print(json.dumps({
        "scientific_execution": "NOT_PERFORMED",
        "diagnostic_only": True,
        "diagnostic": "prompt/input isolation with increased output budget",
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "response_id": getattr(response, "id", None),
        "status": getattr(response, "status", None),
        "output_text": getattr(response, "output_text", None),
        "incomplete_details": getattr(response, "incomplete_details", None),
        "output": getattr(response, "output", None),
        "usage": getattr(response, "usage", None),
        "model": getattr(response, "model", None),
    }, default=lambda o: o.model_dump() if hasattr(o, "model_dump") else str(o), indent=2))

if __name__ == "__main__":
    main()
