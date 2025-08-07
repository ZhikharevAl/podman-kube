import os
import socket

from fastapi import FastAPI

app = FastAPI(title="Demo FastAPI App", version="1.0.0")


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint that returns a greeting message and hostname."""
    hostname = socket.gethostname()
    return {
        "message": "Привет из FastAPI!",
        "hostname": hostname,
        "env": os.environ.get("DEMO_ENV", "default"),
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint to verify the service is running."""
    return {"status": "healthy"}


@app.get("/info")
async def info() -> dict[str, str]:
    """Information about the application."""
    return {
        "app_name": "demo-fastapi-app",
        "version": "1.0.0",
        "description": "Демонстрационное FastAPI приложение для Podman и Kubernetes",
    }
