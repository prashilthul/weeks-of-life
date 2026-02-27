from pathlib import Path
from datetime import date
import tomlkit


def load_config():
    path = Path.home() / ".config/life/config.toml"
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        config = tomlkit.document()
        config["birthdate"] = "1995-01-01"
        config["target_years"] = 90

        with open(path, "w") as f:
            f.write(tomlkit.dumps(config))

        print(f"Created config at {path}")
        print("Please edit it and re-run.")
        exit(0)

    with open(path, "r") as f:
        config = tomlkit.parse(f.read())

    return config["birthdate"], config["target_years"]