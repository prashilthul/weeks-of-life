#!/usr/bin/env python3
from textual.app import App, ComposeResult
from textual.widgets import Footer
from textual.containers import Container
from .grid import LifeGrid
from .config import load_config


class LifeApp(App):
    CSS_PATH = None
    
    TITLE = "Life in Weeks"
    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
        ("r", "refresh", "Refresh"),
    ]

    def __init__(self):
        super().__init__()
        self.birthdate, self.target_years = load_config()

    def compose(self) -> ComposeResult:
        yield Container(
            LifeGrid(self.birthdate, self.target_years),
        )
        yield Footer()


def run_life():
    app = LifeApp()
    app.run()


if __name__ == "__main__":
    run_life()
