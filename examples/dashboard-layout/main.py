from consolide.app import ConsolideApp

from consolide.layouts import Box, Center, Column, Row, Spacer
from consolide.components import Label


def main() -> None:
    def root(terminal):
        # Sidebar
        sidebar = Box(
            terminal,
            Label(terminal, "Dashboard\n- Home\n- Stats\n- Settings"),
            title="Sidebar",
        )
        # Give the main area more horizontal weight than the sidebar.
        sidebar.weight = 1

        # Main content column
        header = Box(terminal, Label(terminal, "Consolide Dashboard"), title="Header")
        stats = Box(terminal, Label(terminal, "Stats area"), title="Stats")
        details = Box(terminal, Label(terminal, "Details area"), title="Details")

        main_column = Column(
            terminal,
            [
                header,
                Spacer(terminal, weight=1),
                stats,
                Spacer(terminal, weight=1),
                details,
            ],
            gap=0,
        )

        # Center the main column vertically/horizontally within its allotted space.
        main_centered = Center(terminal, main_column)
        main_centered.weight = 3

        # Top-level layout: sidebar | spacer | main
        root_row = Row(
            terminal,
            [
                sidebar,
                Spacer(terminal, weight=1),
                main_centered,
            ],
            gap=4,
        )

        return root_row

    app = ConsolideApp(root=root)
    app.run()


if __name__ == "__main__":
    main()
