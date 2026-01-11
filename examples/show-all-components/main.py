from consolide.app import ConsolideApp

from consolide.components import Label, Text, Title, Subtitle, Input
from consolide.rendering import RenderContext
from consolide.component import ConsolideComponent


class ShowAllComponents(ConsolideComponent):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.components = [
            Label(terminal, "Label"),
            Text(terminal, "Text"),
            Title(terminal, "Title"),
            Subtitle(terminal, "Subtitle"),
            Input(terminal, value="Input", placeholder="Enter..."),
        ]

    def render(self, ctx: RenderContext) -> str:
        lines = []
        for comp in self.components:
            line = comp.render(RenderContext(ctx.width, 1))
            lines.append(line)
        return "\n".join(lines)

    def update(self) -> None:
        pass

    def destroy(self) -> None:
        pass


def main():
    def root(terminal):
        return ShowAllComponents(terminal)

    app = ConsolideApp(root=root)
    app.run()


if __name__ == "__main__":
    main()
