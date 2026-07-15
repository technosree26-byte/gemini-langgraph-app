"""LangGraph workflow definitions."""
from langgraph.graph import StateGraph, END

from app.state import TranslationState

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

builder.add_edge("validator", "retriever")
builder.add_edge("retriever", "translator")
builder.add_edge("translator", "speech")
builder.add_edge("speech", END)

translation_graph = builder.compile()