# weeks-of-life

A terminal user interface (TUI) calendar that visualizes your life in weekly blocks, inspired by the "Life in Weeks" concept. Built with Python using Textual and Rich.

---

## Overview

Each row represents one year of life across 52 weeks. The interface calculates the total number of weeks lived based on your birthdate and renders completed weeks alongside remaining weeks relative to a target life expectancy.

### Features

- Visual calendar grid with filled and unfilled indicators.
- Configurable birthdate and target lifespan via TOML.
- Live stats displaying weeks lived vs. weeks remaining.
- Terminal size validation (requires minimum 110x40 dimensions).
- Built with Python `textual`, `rich`, and `tomlkit`.

---

## Requirements

- Python 3.10+
- Terminal emulator with at least 110 columns and 40 rows

---

## Installation

### Option 1: Automated setup with uv (Recommended)

Clone the repository and run the install script:

```bash
git clone https://github.com/prashilthul/weeks-of-life.git
cd weeks-of-life
chmod +x install.sh
./install.sh
```

The installer will:
1. Create a virtual environment using `uv`.
2. Install dependencies and the `life` command in editable mode.
3. Symlink the executable to `~/.local/bin/life`.
4. Generate the default configuration file at `~/.config/life/config.toml`.

### Option 2: Manual Installation with pip

```bash
git clone https://github.com/prashilthul/weeks-of-life.git
cd weeks-of-life

python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Configuration

Configuration is located at `~/.config/life/config.toml`. If the file does not exist, running the application creates one with default values:

```toml
birthdate = "2000-01-01"
target_years = 80
```

- `birthdate`: Date of birth in `YYYY-MM-DD` format.
- `target_years`: Projected target lifespan in years.

---

## Usage

Run the command from your terminal:

```bash
life
```

Or execute directly with Python:

```bash
python -m life.app
```

### Key Bindings

| Key | Action |
| --- | --- |
| `Ctrl+Q` | Quit the application |
| `R` | Refresh calendar grid |

---

## Project Structure

```
weeks-of-life/
├── life/
│   ├── app.py        # Textual application lifecycle and keybindings
│   ├── config.py     # Configuration parser and loader (~/.config/life/config.toml)
│   └── grid.py       # Grid calculations, rendering logic, and terminal resize handler
├── install.sh        # Setup script for virtual environment and symlinks
├── pyproject.toml    # Package metadata and CLI entrypoint definition
└── README.md
```

---

## License

This project is open-source under the MIT License.
