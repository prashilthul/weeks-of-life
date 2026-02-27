#!/bin/bash
# life-tui/install.sh - uv + venv setup

set -e

echo "Week-of-life-tui with uv + venv..."

cd "$(dirname "$0")"

# 1. make example-config.toml if not 
if [ ! -f "example-config.toml" ]; then
    cat > example-config.toml << 'EOF'
target_years = 80 
birthdate = "2006-11-14"  # YYYY-MM-DD - EDIT THIS TO CUSTOMIZE
EOF
    echo "Created example-config.toml - EDIT YOUR BIRTHDATE before running 'life'"
fi

# 2. Remove existing .venv if present
if [ -d ".venv" ]; then
    echo "Clearing existing .venv..."
    rm -rf .venv
fi

# 3. make a fresh venv + install
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e .

# 4. Create ~/.local/bin/life symlink (update if exists)
mkdir -p ~/.local/bin
rm -f ~/.local/bin/life  # Remove old symlink
ln -sf "$(pwd)/.venv/bin/life" ~/.local/bin/life
chmod +x ~/.local/bin/life

# 5. Setup user config (only copy if doesn't exist)
mkdir -p ~/.config/life
if [ ! -f ~/.config/life/config.toml ]; then
    cp example-config.toml ~/.config/life/config.toml
    echo "Config created: nano ~/.config/life/config.toml"
else
    echo "ℹ Config exists: ~/.config/life/config.toml"
fi

echo "SUCCESS! Run: life"
# echo "Edit ~/.config/life/config.toml with your birthdate first!"
