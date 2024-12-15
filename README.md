# Recipamatic

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
