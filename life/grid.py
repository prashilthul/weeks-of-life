from textual.widget import Widget
from textual.reactive import reactive
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from datetime import datetime
from dateutil import parser

MIN_WIDTH = 110  # eyeballed this
MIN_HEIGHT = 40  # eyeballed this


class LifeGrid(Widget):

    lived_weeks = reactive(0)

    def __init__(self, birthdate: str, target_years: int):
        super().__init__()
        self.birthdate_str = birthdate
        self.target_years = target_years
        self.total_weeks = int(target_years * 52)
        self.birthdate = parser.parse(birthdate)

    def on_mount(self):
        self.calculate_weeks()

    def calculate_weeks(self):
        today = datetime.now()
        days = (today - self.birthdate).days
        self.lived_weeks = max(0, days // 7)

    def render(self):

        width = self.size.width
        height = self.size.height

        if width < MIN_WIDTH or height < MIN_HEIGHT:

            msg = Text()
            msg.append("Terminal Too Small\n\n", style="bold red")
            msg.append(f"Minimum required: {MIN_WIDTH} x {MIN_HEIGHT}\n")
            msg.append(f"Current size: {width} x {height}", style="dim")

            return Panel(
                Align.center(msg, vertical="middle"),
                border_style="red",
            )
        weeks_per_year = 52
        years = self.target_years

        lived = self.lived_weeks
        total = self.total_weeks
        remaining = max(0, total - lived)

        grid = Text()

        week_index = 0

        for year in range(years):

            if week_index >= total:
                break

            for week in range(weeks_per_year):

                if week_index >= total:
                    break

                # if week_index < lived:
                #     grid.append("■ ", style="bold white")
                # else:
                #     grid.append("· ", style="dim")
                if week_index < lived:
                    grid.append("● ", style="accent")
                else:
                    grid.append("○ ", style="dim")
                week_index += 1

            grid.append("\n")

        stats = Text()
        stats.append("\n")
        stats.append(f"Lived: {lived:,} weeks", style="bold")
        stats.append("   ")
        stats.append(f"Remaining: {remaining:,} weeks", style="dim")

        content = Text()
        content.append("Your Life in Weeks\n\n", style="bold cyan")
        content.append(grid)
        content.append(stats)

        return Panel(
            Align.center(content),
            border_style="bright_black",
            padding=(1, 2),
        )

    def on_resize(self):
        self.refresh()
