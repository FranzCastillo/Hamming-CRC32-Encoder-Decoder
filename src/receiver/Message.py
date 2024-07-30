from dataclasses import dataclass, field


@dataclass
class Message:
    algorithm: str
    message: list[str] = field(default_factory=list)
