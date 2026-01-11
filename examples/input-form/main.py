from consolide.app import ConsolideApp

from consolide.components import Title, Subtitle, Input
from consolide.layouts import Column, Box, Spacer


def main() -> None:
    def root(terminal):
        title = Title(terminal, "User Login")
        subtitle = Subtitle(terminal, "This input is display-only for now")

        username_input = Input(
            terminal,
            placeholder="Enter username",
            focused=True,
        )

        password_input = Input(
            terminal,
            placeholder="Enter password",
        )

        form = Column(
            terminal,
            [
                Box(terminal, title, title="Title"),
                Box(terminal, subtitle, title="Subtitle"),
                Spacer(terminal, weight=1),
                Box(terminal, username_input, title="Username"),
                Box(terminal, password_input, title="Password"),
            ],
            gap=1,
        )

        return form

    app = ConsolideApp(root=root)
    app.run()


if __name__ == "__main__":
    main()
