import os

from services.gtts_service import generate_audio


class FakeTTS:

    def save(self, filename):

        with open(filename, "w") as f:

            f.write("audio")


def test_audio(monkeypatch):

    import services.gtts_service

    monkeypatch.setattr(

        services.gtts_service,

        "gTTS",

        lambda text, lang: FakeTTS(),
    )

    filename = generate_audio(

        "Hello",

        "English",
    )

    assert os.path.exists(filename)
