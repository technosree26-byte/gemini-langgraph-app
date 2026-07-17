from langgraph.graph import StateGraph, END

from app.state import TranslationState
from app.router import input_router, speech_router

from agents.validator_agent import validator_node
from agents.retriever_agent import retriever_node
from agents.translator_agent import translator_node
from agents.speech_agent import speech_node

builder = StateGraph(TranslationState)

builder.add_node("validator", validator_node)
builder.add_node("retriever", retriever_node)
builder.add_node("translator", translator_node)
builder.add_node("speech", speech_node)

builder.set_entry_point("validator")

# Decide whether to go to retriever or translator
builder.add_conditional_edges(
    "validator",
    input_router,
    {
        "retriever": "retriever",
        "translator": "translator",
    },
)

# After retriever, always translate
builder.add_edge("retriever", "translator")

# Decide whether to generate speech
builder.add_conditional_edges(
    "translator",
    speech_router,
    {
        "speech": "speech",
        "output": END,
    },
)

builder.add_edge("speech", END)

translation_graph = builder.compile()