from typing import Protocol

from alice_gpt.domain.message import Message


class LLMProvider(Protocol):
    """Описывает получение ответа LLM независимо от конкретного API."""

    async def generate(self, messages: list[Message]) -> str:
        """Генерирует ответ, не изменяя переданный список и его сообщения.

        Args:
            messages: Сообщения в порядке диалога.

        Returns:
            Текст ответа модели после завершения асинхронного вызова.
        """
        # Контракт задаёт требования; обращение к API реализует провайдер.
        ...
