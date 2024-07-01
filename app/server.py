import os
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI
from pydantic import BaseModel
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow


Traceloop.init(
    "app.test",
    api_key=os.environ["TRACELOOP_API_KEY"],
    disable_batch=True,
)

openai = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


app = FastAPI()


class InputModel(BaseModel):
    question: str


@app.post("/answer", response_class=StreamingResponse)
def handle_answer(input: InputModel):
    return StreamingResponse(
        create_response_generator(openai, input.question),
        media_type="text/event-stream",
    )


@workflow("test_workflow_42")
def create_response_generator(openai: OpenAI, question: str):
    stream = openai.chat.completions.create(
        stream=True, model="gpt-4o", messages=[{"role": "user", "content": question}]
    )

    for chunk in stream:
        delta = chunk.choices[0].delta
        yield convert_to_event_stream("delta", delta)


def convert_to_event_stream(event: str, model: BaseModel) -> str:
    """
    Convert the given event and model into an event stream format.
    """
    return f"event: {event}\ndata: {model.model_dump_json()}\n\n"


def main():
    for event in create_response_generator(openai, "What is the capital of France?"):
        print(event)
