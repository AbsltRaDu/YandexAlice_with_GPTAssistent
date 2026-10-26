import pytest

from alice_gpt.domain.message import Message

def test_message_rejects_empty_content() -> None:
    """Проверяет запрет создания пустого сообщения"""
    
    with pytest.raises(ValueError):
        Message(role="user", content="")
        
def test_message_preserves_role_and_content() -> None:
    """Проверяет сохранение переданных роли и текста сообщения."""

    message = Message(role="user", content="Привет")

    # Проверяем значения полей, чтобы обнаружить их изменение при создании.
    assert message.role == "user"
    assert message.content == "Привет"
