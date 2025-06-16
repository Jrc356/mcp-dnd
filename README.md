# D&D MCP Server

## Overview

D&D MCP Server is a Dungeons & Dragons 5th Edition Knowledge Base server, built on [FastMCP](https://github.com/ianstormtaylor/fastmcp). It exposes D&D 5e content (spells, monsters, equipment, classes, races, and more) via a Model Context Protocol (MCP) API, making it easy to integrate D&D data into AI and automation workflows.

## Features

- Browse all official D&D 5e API categories
- Fetch details for spells, monsters, equipment, and more

## Project Status

I'm mostly just messing around with MCP's, this is not really meant to be useable... maybe...

## Requirements

- Python 3.13+
- Docker (optional, for containerized deployment)
- make

## Quick Start

### Local (Poetry)

```sh
make setup
poetry run python main.py
```

### Docker Compose (with Make)

Build and run in detached mode:

```sh
make build-and-run
```

Or build and run attached (see logs in terminal):

```sh
make build-and-run-attached
```

Stop and remove containers:

```sh
make clean
```

## Configuration

Edit `config.py` to adjust API endpoints, logging, and other settings.

## Logging

Logs are written to `logs/dnd-mcp-server.log` by default.

## Testing

Unit tests are located in the `tests/` directory. To run tests:

```sh
poetry run pytest
```

## Usage with MCP Clients

To use this server with an MCP-compatible client, add it to your `mcp.json` configuration. For example, if using VS Code with the MCP extension, add one of the following to your `.vscode/mcp.json`:

### Docker-based server (recommended)

```jsonc
{
  "servers": {
    "dnd": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "dnd-mcp-app"
      ],
      "cwd": "${workspaceFolder}"
    }
  }
}
```

- Make sure to build the Docker image first (e.g., `make build`).
- The server will be available as the `dnd` provider in your MCP client.

### Local Python server (no Docker)

```jsonc
{
  "servers": {
    "dnd": {
      "type": "stdio",
      "command": "poetry",
      "args": [
        "run",
        "python",
        "main.py"
      ],
      "cwd": "${workspaceFolder}"
    }
  }
}
```

- Make sure dependencies are installed (`make setup` or `poetry install`).
- This will run the server directly using your local Python environment.
