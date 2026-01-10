from consolide.app import ConsolideApp

from consolide.layouts import Box, Column, Spacer
from consolide.components import Label


def main() -> None:
    def root(terminal):
        return Column(
            terminal,
            [
                Box(terminal, Label(terminal, "Top"), title="Section 1"),
                Spacer(terminal),
                Box(terminal, Label(terminal, "Bottom"), title="Section 2"),
            ],
            gap=0,
        )

    app = ConsolideApp(root=root)
    app.run()


if __name__ == "__main__":
    main()