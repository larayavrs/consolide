from consolide.component import ConsolideComponent

if __name__ == "__main__":
    print("Hello world from Consolide!")

    component = ConsolideComponent()
    component.render()
    component.update()
    component.destroy()