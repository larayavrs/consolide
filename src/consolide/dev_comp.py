from consolide.component import ConsolideComponent
from consolide.rendering import RenderContext

from consolide.row import Row
from consolide.label import Label
from consolide.box import Box

class DevComponent(ConsolideComponent):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.root = Row(
            terminal,
            [
                Box(terminal, Label(terminal, "Hello"), title="Box 1"),
                Box(terminal, Label(terminal, "World"), title="Box 2"),
            ],
            gap=4
        )

    def render(self, ctx: RenderContext) -> str:
        return self.root.render(ctx)

    def update(self):
        pass
    
    def destroy(self):
        pass