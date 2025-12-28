from consolide.component import ConsolideComponent

class DevComponent(ConsolideComponent):
    def render(self) -> None:
        self.terminal.write("Rendering DevComponent")

    def update(self) -> None:
        pass

    def destroy(self) -> None:
        self.terminal.write("Destroying DevComponent")