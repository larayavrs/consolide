import os
import sys
import pytest

# Windows-only test
pytestmark = pytest.mark.skipif(os.name != "nt", reason="Windows-only")

class _DummyTTY:
    def isatty(self):
        return True
    def write(self, s: str) -> None:
        pass
    def flush(self) -> None:
        pass


def test_consolide_app_initializes_root_component(monkeypatch):
    if os.name != "nt":  # extra guard for safety
        pytest.skip("Windows-only test")

    # Provide a dummy stdout that claims to be a TTY
    monkeypatch.setattr(sys, "stdout", _DummyTTY())

    from consolide.app import ConsolideApp  # imported after monkeypatch
    from consolide.component import ConsolideComponent
    from consolide.terminal import Terminal

    def root_factory(terminal, **kwargs):
        from consolide.dev_comp import DevComponent
        return DevComponent(terminal)

    app = ConsolideApp(root_factory)
    assert app is not None
    assert hasattr(app, "root")
    assert isinstance(app.root, ConsolideComponent)
    assert isinstance(app.terminal, Terminal)
    assert app.root.terminal is app.terminal
