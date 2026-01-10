from consolide.app import ConsolideApp

from consolide.layouts import Box, Center, Padding
from consolide.components import Label


def main() -> None:
    def root(terminal):
        label = Label(terminal, "Centered in a Box", align="left")
        boxed = Box(terminal, Padding(terminal, label, padding=1), title="Center example")
        return Center(terminal, boxed)

    app = ConsolideApp(root=root)
    app.run()


if __name__ == "__main__":
    main()