from consolide.component import ConsolideComponent
from consolide.rendering import RenderContext

class Box(ConsolideComponent):
    def __init__(self, terminal, child: ConsolideComponent, title: str | None = None):
        super().__init__(terminal)
        self.child = child
        self.title = title
    
    def render(self, ctx: RenderContext) -> str:
        if ctx.width < 2 or ctx.height < 2:
            return ""
        inner_width = ctx.width - 2
        lines = []
        lines.append("┌" + "─" * inner_width + "┐")
        if self.title and ctx.height >= 4:
            title = self.title[:inner_width].center(inner_width)
            lines.append("│" + title + "│")
            lines.append("├" + "─" * inner_width + "┤")
        used = len(lines) + 1
        content_heigth = max(0, ctx.height - used)
        child_ctx = RenderContext(inner_width, content_heigth)
        content = self.child.render(child_ctx).splitlines()
        for i in range(content_heigth):
            line = content[i] if i < len(content) else ""
            lines.append("│" + line.ljust(inner_width)[:inner_width] + "│")
        lines.append("└" + "─" * inner_width + "┘")
        return "\n".join(lines)
    
    def update(self) -> None:
        self.child.update()

    def destroy(self) -> None:
        self.child.destroy()