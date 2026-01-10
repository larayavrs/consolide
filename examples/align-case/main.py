from consolide.app import ConsolideApp

from consolide.components import Label
from consolide.layouts import Align, Padding

def main():
    def root(terminal):
        return Align(
            terminal,
            Padding(
                terminal,
                Label(terminal, "Aligned center/middle"),
                padding=1
            ),
            horizontal="center",
            vertical="middle",
        )

    app = ConsolideApp(root=root)
    app.run()

if __name__ == "__main__":
    main()