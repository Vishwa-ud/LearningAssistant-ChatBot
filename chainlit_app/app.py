import chainlit as cl
from your_rag_module import rag_pipeline

@cl.on_message
async def handle_message(message: cl.Message):
    answer, sources = rag_pipeline(message.content)
    await cl.Message(content=answer).send()