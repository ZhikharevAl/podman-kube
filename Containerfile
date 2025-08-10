FROM python:3.13.5-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv


RUN uv sync --frozen --no-dev

COPY main.py .

ENV PYTHONPATH=/app
ENV DEMO_ENV=production

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
