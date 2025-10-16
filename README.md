# Discord Bot

A small collection of simple Discord bot scripts. Each file in this repository contains a focused utility that demonstrates a particular Discord bot feature using discord.py.

Warning: Some of the included examples change nicknames to explicit text. Use responsibly and only in servers where you have permission.

## Included scripts

- `main.py` — Minimal example that connects a bot and prints when it's online. Useful as a starting point.
- `mcserver.py` — Periodically queries a Minecraft server (via `mcstatus`) and updates the bot's presence with current player count.
- `role.py` — Continuously changes a role's colour to random values ("rainbow role" effect). Requires Manage Roles permission.
- `useranima.py` — Animates a specific user's nickname by cycling through frames. Requires Manage Nicknames permission and should not be used to harass.

## Requirements

- Python 3.8+ (Windows users: this repo sets an event loop policy for compatibility)
- `discord.py` (rewrite branch compatible; the code uses `discord` package)
- `mcstatus` (only required for `mcserver.py`)

Install dependencies:

```powershell
python -m pip install -U pip
pip install discord.py mcstatus
```

If you prefer a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate; pip install -U pip; pip install discord.py mcstatus
```

## Configuration

Before running any script, open the file and replace the placeholder token and IDs with your real values:

- `TOKEN` / `token` — Your bot token from the Discord Developer Portal.
- `GUILD_ID` — Your server (guild) ID (integer).
- `ROLE_ID` — The role ID to modify in `role.py`.
- `USER_ID` — The user ID to animate in `useranima.py`.

Example: in `role.py`

```py
TOKEN = "Your Discord Tokens"
GUILD_ID = 1363040679953170502
ROLE_ID = 1421475734681030677
```

Permissions needed for the bot account (grant at least these):

- View Channels
- Send Messages (if you add commands later)
- Manage Roles (for `role.py`)
- Manage Nicknames (for `useranima.py`)

## Usage

Run a script from the repository root. Example:

```powershell
python main.py
python mcserver.py
python role.py
python useranima.py
```

Only run one script at a time per bot token — each script logs in as a full client.

## Safety and etiquette

- Be careful with scripts that modify roles or nicknames. Only use them in servers where you have permission and the action is welcome.
- `useranima.py` contains explicit text in the animation frames. Edit the `frames` list before use to remove or change any offensive content.

## Extending the bot

These scripts are deliberately small and focused. To build a more maintainable bot consider:

- Using `discord.ext.commands.Bot` for commands and better structure.
- Storing configuration and secrets in environment variables or a `.env` file (never commit tokens).
- Combining features into a single process with cogs/extensions.

## License

This repository contains example code and is provided as-is. No license file is included — add one if you intend to share or publish.

## Contact

If you need help adapting any script or want suggestions for safer alternatives, open an issue or message the repo owner.
