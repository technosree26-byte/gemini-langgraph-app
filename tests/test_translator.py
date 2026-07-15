from agents.translator_agent import translator_node


class FakeTranslator:
    def translate(self, text, source_language, target_language):
        return "Bonjour"


def test_translation():
    state = {
        "input_text": "Hello",
        "source_language": "English",
        "target_language": "French",
        "translated_text": "",
    }

    result = translator_node(
        state,
        translator=FakeTranslator()
    )

    assert result["translated_text"] == "Bonjour"