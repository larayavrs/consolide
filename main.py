import time

from consolide.widgets.card import Card
from consolide.widgets.input import Input
from consolide.widgets.progress import ProgressBar
from consolide.core.layout import Column, Row
from consolide.core.renderer import Renderer

def main() -> None:
    renderer = Renderer()

    name_input = Input("Enter your name: ")
    name = name_input.ask()

    card = Card(
        title="Hello World",
        lines=[f"Welcome {name}", "This is a card", "with multiple lines"],
    )

    progress = ProgressBar(100, "Loading")

    layout = Column([
        name_input,
        Row([card, progress]),
    ])

    for _ in range(100):
        progress.tick()
        renderer.refresh([layout])
        time.sleep(0.05)

if __name__ == "__main__":
    main()