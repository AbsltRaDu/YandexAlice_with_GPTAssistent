from dataclasses import dataclass
from typing import Literal

@dataclass
class Message:
    """Класс сообщения

    Raises:
        ValueError: Пустое сообщение
    """
    
    role: Literal["system", "user", "assistant"]
    content: str
    
    def __post_init__(self) -> None:
        
        if self.content == "":
            raise ValueError("Пустое сообщение недопустимо")
        