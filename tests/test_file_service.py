from io import BytesIO

from services.file_service import extract_text


class FakeTXT(BytesIO):

    name = "example.txt"


def test_txt():

    file = FakeTXT(b"Hello World")

    result = extract_text(file)

    assert result == "Hello World"
