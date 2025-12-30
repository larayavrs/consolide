from consolide.component import ConsolideComponent
from consolide.rendering import RenderContext

from consolide.label import Label
from consolide.box import Box

class DevComponent(ConsolideComponent):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.root = Box(
            terminal,
            Label(terminal, "Dev Component", align="center"),
            title="Demo"
        )

    def render(self, ctx: RenderContext) -> str:
        return self.root.render(ctx)

    def update(self):
        pass
    
    def destroy(self):
        pass