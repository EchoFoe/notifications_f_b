### Инструкция по проекту

Для работы проекта потребуются:

- Python
- Postgresql
- Next.js
- Django
- DRF

1. Клонировать проект:
    ```
    git clone https://github.com/EchoFoe/notifications_f_b.git
    ```
### Backend

2. Виртуальное окружение для бэкенда создается за счёт poetry. Файлы poetry.lock и pyproject.toml прилагаются, поэтому для бэкенда достаточно:
    ```
    cd backend 
    poetry install
    ```
3. Разверните БД и в файле `.env` укажите свои конфиги
4. Создайте суперпользователя:
    ```
    poetry run python manage.py createsuperuser 
    ```
5. Произведите миграции и запустите сервер бэкенда:
    ```
    poetry run python manage.py migrate
    poetry run python manage.py runserver 
    ```
6. Зайдите в админку http://127.0.0.1:8000/admin/ под своим суперпользователем и создайте ещё одного юзера, присвойте ему права персонала.
7. Залейте фикстуры в приложение notifications:
    ```
    poetry run python manage.py loaddata notifications/fixtures/notifications.json 
    ```
8. Запустите тесты:
    ```
    poetry run python manage.py test notifications.tests.notification_api_test
    ```
9. Увидеть список уведомлений можно в админке: http://127.0.0.1:8000/admin/notifications/notification/
10. Представление для получения списка уведомлений: http://127.0.0.1:8000/api/notifications/
11. Представление для получения статистики по уведомлениям: http://127.0.0.1:8000/api/notification-stats/

### Frontend

1. Виртуальное окружение для фронтенда создается за счет yarn:
     ```
     cd frontend 
     yarn install
     ```
2. Запустить сервер разработки фронтенда:
     ``` 
     yarn dev
     ```
3. Перейти по адресу http://localhost:3000/auth
4. Зайти в свой аккаунт, который создавали на бэкенде
5. Зарегистрировать другой аккаунт
