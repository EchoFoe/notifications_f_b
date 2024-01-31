# Используем официальный образ Node.js
FROM node:14-alpine
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
# Копируем файлы package.json и yarn.lock для установки зависимостей
COPY package.json yarn.lock ./
# Устанавливаем зависимости с помощью Yarn
RUN yarn install
# Копируем остальные файлы проекта
COPY . .
# Запускаем приложение Next.js в режиме разработки
CMD ["yarn", "dev"]