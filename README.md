# Recipamatic

## Development Environment

This project uses VSCode with Agent Mode optimizations. The following configuration files enhance the development experience:

- `.vscode/settings.json` - Editor settings for Python and Svelte development
- `.vscode/launch.json` - Debug configurations
- `.vscode/tasks.json` - Common development tasks
- `.vscode/extensions.json` - Recommended extensions
- `.github/copilot/context.json` - Project context for AI assistants

## Installation

To install the package, run the following command:

### Python backend

```bash
poetry install
```

### Frontend

```bash
...
```

## Setup

To setup the package, create a `.env` file in `~/cred/recipamatic/.env` with the following content:

```bash
RECIPAMATIC_SAMPLE_ENV_VAR=sample
```

And for VSCode to recognize the environment file, add the following line to the
workspace [settings file](.vscode/settings.json):

```json
"python.envFile": "/home/pmn/cred/recipamatic/.env"
```

Note that the path to the `.env` file should be absolute.

## Testing

To run the tests, use the following command:

```bash
poetry run pytest
```

or use the VSCode interface.

## IDEAs
