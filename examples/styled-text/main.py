from consolide.app import ConsolideApp

from consolide.components import Text, Title, Subtitle
from consolide.layouts import Column, Box, Spacer


def main() -> None:
    def root(terminal):
        title = Title(terminal, "Consolide Styled Text")
        subtitle = Subtitle(terminal, "Colors and emphasis")

        body = Text(
            terminal,
            "This is a simple text block rendered with ANSI colors.",
            fg="green",
        )

        warning = Text(
            terminal,
            "Be careful with line width when using colored text.",
            fg="yellow",
            bold=True,
        )

        column = Column(
            terminal,
            [
                Box(terminal, title, title="Title"),
                Box(terminal, subtitle, title="Subtitle"),
                Spacer(terminal, weight=1),
                Box(terminal, body, title="Body"),
                Box(terminal, warning, title="Warning"),
            ],
            gap=1,
        )

        return column

    app = ConsolideApp(root=root)
    app.run()


if __name__ == "__main__":
    main()
