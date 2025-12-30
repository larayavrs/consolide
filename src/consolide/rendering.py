from dataclasses import dataclass

@dataclass(frozen=True)
class RenderContext:
    width: int
    height: int