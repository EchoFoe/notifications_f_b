# Базовый образ Python
FROM python:3.9
# Устанавливаем переменную окружения PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
# Копируем файл зависимостей и файлы проекта в контейнер
COPY pyproject.toml poetry.lock /app/
# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry
# Устанавливаем зависимости poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi
# Копируем все файлы проекта в контейнер
COPY . /app/
# Определяем порт для бэкенда
EXPOSE 8000
# Команда для запуска Django-приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
