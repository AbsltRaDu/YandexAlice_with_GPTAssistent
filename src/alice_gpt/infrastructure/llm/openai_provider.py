from openai import AsyncOpenAI

from alice_gpt.domain.message import Message

class OpenAIProvider:
    """Преобразует сообщения приложения и запрашивает ответы через API OpenAI."""

    def __init__(self, client: AsyncOpenAI, model: str) -> None:
        """Сохраняет готовый клиент и имя модели для запросов генерации.

        Args:
            client: Асинхронный клиент, создаваемый и закрываемый внешним кодом.
            model: Имя модели, передаваемое при запросе генерации.
        """
        self._client = client
        self._model = model
        
    async def generate(self, messages: list[Message]) -> str:
        """Генерирует ответ, не изменяя переданный список и его сообщения.

        Args:
            messages: Список сообщений в порядке диалога.

        Returns:
            Текст ответа модели.
        """
        
        # Создаём новые словари формата API, сохраняя исходные сообщения.
        input_messages = [
            {"role": message.role, "content": message.content}
            for message in messages
        ]
        response = await self._client.responses.create(model=self._model, input=input_messages)
        
        return response.output_text
        
        
