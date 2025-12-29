from consolide.component import ConsolideComponent
from consolide.label import Label

class DevComponent(ConsolideComponent):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.label = Label(terminal, "Hello, from consolide!")

    def render(self):
        self.label.render()
    
    def update(self):
        pass
    
    def destroy(self):
        pass