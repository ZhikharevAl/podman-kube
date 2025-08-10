# Demo FastAPI App для Podman и Kubernetes

Демонстрационное FastAPI приложение с поддержкой контейнеризации через Podman и развертывания в Kubernetes.

## 🚀 Особенности

- **FastAPI** - современный, быстрый веб-фреймворк для создания API
- **UV** - быстрый менеджер пакетов Python для управления зависимостями
- **Podman** - контейнеризация без демона
- **Kubernetes** - оркестрация контейнеров
- **GitHub Actions** - автоматизированные проверки качества кода
- **Pre-commit hooks** - автоматическое форматирование и линтинг

## 📋 Требования

- Python 3.13.5+
- UV package manager
- Podman
- Kubernetes (minikube, kind, или кластер)

## 🛠️ Установка и запуск

### Локальная разработка

1. **Клонирование репозитория:**

   ```bash
   git clone <repository-url>
   cd podman-kube
   ```

2. **Установка зависимостей:**

   ```bash
   # Установка UV (если не установлен)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Установка зависимостей проекта
   uv sync
   ```

3. **Настройка pre-commit hooks:**

   ```bash
   uv run pre-commit install
   ```

4. **Запуск приложения:**

   ```bash
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Доступ к приложению:**
   - API: <http://localhost:8000>
   - Документация Swagger: <http://localhost:8000/docs>
   - ReDoc: <http://localhost:8000/redoc>

### Контейнеризация с Podman

1. **Сборка образа:**

   ```bash
   podman build -t python-app:latest -f Containerfile .
   ```

2. **Запуск контейнера:**

   ```bash
   podman run -d -p 8000:8000 --name python-app python-app:latest
   ```

3. **Создание tar архива образа:**

   ```bash
   podman save -o my-python-app.tar localhost/python-app:latest
   ```

### Развертывание в Kubernetes

1. **Загрузка образа в кластер (для minikube):**

   ```bash
   minikube image load my-python-app.tar
   ```

2. **Применение манифестов:**

   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

3. **Проверка статуса:**

   ```bash
   kubectl get pods
   kubectl get services
   ```

4. **Доступ к приложению:**

   ```bash
   # Для minikube
   minikube service python-app-service

   # Или через port-forward
   kubectl port-forward service/python-app-service 8080:80
   ```

## 📡 API Endpoints

- `GET /` - Главная страница с информацией о хосте
- `GET /health` - Проверка состояния приложения
- `GET /info` - Информация о приложении

## 🔧 Разработка

### Проверка качества кода

```bash
# Линтинг с Ruff
uv run ruff check .

# Форматирование кода
uv run ruff format .

# Проверка типов с Pyright
uv run pyright .

# Запуск всех проверок
uv run pre-commit run --all-files
```

### Структура проекта

```
.
├── .github/
│   ├── actions/          # Переиспользуемые GitHub Actions
│   └── workflows/        # CI/CD пайплайны
├── main.py              # Основной файл приложения
├── pyproject.toml       # Конфигурация проекта и зависимости
├── Containerfile        # Инструкции для сборки образа
├── deployment.yaml      # Kubernetes Deployment
├── service.yaml         # Kubernetes Service
├── .dockerignore        # Исключения для Docker/Podman
├── .pre-commit-config.yaml  # Конфигурация pre-commit hooks
└── uv.lock             # Заблокированные версии зависимостей
```

## 🏗️ CI/CD

Проект использует GitHub Actions для автоматической проверки качества кода:

- **Проверка lockfile**: Убеждается, что uv.lock актуален
- **Линтинг**: Ruff проверка и форматирование
- **Типизация**: Проверка типов с Pyright

## 🔧 Конфигурация

### Переменные окружения

- `DEMO_ENV` - Окружение приложения (по умолчанию: "default")

### Настройка Ruff

Конфигурация линтера находится в `pyproject.toml`:

- Длина строки: 100 символов
- Python версия: 3.13
- Включены все правила с исключениями для документации

## 🚀 Масштабирование

Для изменения количества реплик в Kubernetes:

```bash
kubectl scale deployment python-app-deployment --replicas=5
```

## 📝 Логи

Просмотр логов приложения:

```bash
# Podman
podman logs python-app

# Kubernetes
kubectl logs -f deployment/python-app-deployment
```
