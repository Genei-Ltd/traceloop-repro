# Traceloop repro

## Setup

### Environment configuration

Copy `.env.example` to `.env` and set the appropriate values.

### Service setup

1. Install python 3.12.3 (and activate if using pyenv or similar)
   ```bash
   # visit https://github.com/pyenv/pyenv#getting-pyenv for more information
   brew install pyenv
   # see above...
   pyenv install 3.12.3
   pyenv global 3.12.3
   ```
   
2. Install poetry
    ```bash
    curl -sSL https://install.python-poetry.org | python -
    ```

3. Add poetry to path and restart shell
    ```bash
    # in ~/.bashrc, ~/.zshrc or equivalent
    export PATH="$HOME/.local/bin:$PATH"
    ```

4. Config poetry to use virtual envs in project (optional)
    ```bash
    poetry config virtualenvs.in-project true
    ```

5. Add dotenv plugin for poetry
    ```bash
    poetry self add poetry-dotenv-plugin
    ```

6. Create virtual environment and install dependencies
    ```bash
    poetry env use python
    poetry install
    ```

## Test broken case

In one terminal:
```sh
poetry run serve
```

In another terminal:
```sh
curl -X POST "http://127.0.0.1:8080/answer" -H "Content-Type: application/json" -d '{"question": "What is the capital of France?"}'
```

## Test not broken case
```sh
poetry run main
```
