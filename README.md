# Smart Fridge 
SmartFridge - это приложение для управления содержимым вашего холодильника, позволяющее сканировать QR-коды и отслеживать продукты.

## Возможности

Просмотр списка продуктов в холодильнике.
Сканирование QR-кодов для добавления или удаления информации о продуктах.
Ведение логов о действиях пользователей.
Типы продуктов и их категории для удобной навигации.
Авторизация пользователей для персонализированного опыта.
Онлайн-доступ

### Приложение доступно по следующей ссылке: SmartFridge.

## Установка

Для работы с проектом требуется Python версии 3.12.

Локальное развертывание

Склонируйте репозиторий на ваше устройство:
git clone https://github.com/resdt/SmartFridge.git
cd SmartFridge
- Установите зависимости с помощью pip:
```bash
pip install -r requirements.txt
```
- Запустите приложение через Streamlit:
```bash
streamlit run main.py
```

## Структура проекта

###### app/- Модули приложения:
 demand.py- Просмотр аналитики потребления. 
 home.py- Главная страница приложения. 
 login.py- Авторизация пользователей 
 logout.py- Завершение сеанса пользователя. 
 product_list.py- Отображение списка продуктов. 
 qr_scanner.py- Функционал сканирования QR-кодов. 


###### utils/- Вспомогательные модули: 
- connections.py- Управление подключением к базам данных. 
- main.py- Основной файл для запуска приложения. 
- poetry.lock и pyproject.toml - Файлы для управления зависимостями через Poetry. 
- requirements.txt- Список зависимых мест для установки.# holodilnic 
