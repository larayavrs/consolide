from consolide.component import ConsolideComponent
from consolide.label import Label
from consolide.container import Container

class DevComponent(ConsolideComponent):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.root = Container(
            terminal,
            children=[
                Label(terminal, "Consolide Dev Component"),
                Label(terminal, "This is a dev component hello world"),
                Label(terminal, "Another line :D"),
            ],
        )

    def render(self):
        self.root.render()

    def update(self):        
        pass
    
    def destroy(self):
        pass