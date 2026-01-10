from consolide.app import ConsolideApp
from consolide.components import Label

def main():
    app = ConsolideApp(
        root=Label,
        root_kwargs={
            "text": "Hello from Label example!"
        }
    )
    app.run()

if __name__ == "__main__":
    main()