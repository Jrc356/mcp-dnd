FROM python:3.13-slim AS base
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app

FROM base AS builder
RUN pip install --no-cache-dir poetry==2.1.3
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV POETRY_CACHE_DIR=/tmp/poetry_cache
COPY pyproject.toml poetry.lock ./
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

FROM base AS runtime
ENV PYTHONUNBUFFERED=1
COPY . /app/
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
EXPOSE 8000
ENTRYPOINT [ "python", "main.py" ]
