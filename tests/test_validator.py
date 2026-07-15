import pytest

from agents.validator_agent import validator_node


def test_empty_input():

    state = {

        "input_text": "",

        "uploaded_file": None,

        "error": "",

    }

    result = validator_node(state)

    assert result["error"] == "Please enter text."


def test_valid_input():

    state = {

        "input_text": "Hello",

        "uploaded_file": None,

        "error": "",

    }

    result = validator_node(state)

    assert result["error"] == ""
