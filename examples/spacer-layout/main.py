from consolide.app import ConsolideApp

from consolide.box import Box
from consolide.column import Column
from consolide.label import Label
from consolide.spacer import Spacer


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