from types import SimpleNamespace
from unittest.mock import patch

from app.ask import ask


def test_ask_displays_input_and_output_token_counts(capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=34,
        ),
        text="回答",
    )
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **kwargs: response)
    )

    with (
        patch("app.ask.genai.Client", return_value=client),
        patch("app.ask.get_api_key", return_value="key"),
    ):
        result = ask("質問")

    output = capsys.readouterr().out
    assert result == "回答"
    assert "入力: 12" in output
    assert "出力: 34" in output