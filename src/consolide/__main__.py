from consolide.dev_comp import DevComponent
from consolide.app import ConsolideApp

def main() -> None:
    app = ConsolideApp(
        root=DevComponent
    )
    app.run()

if __name__ == "__main__":
    main()