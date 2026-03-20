## Пет-проект по автоматизации тестирования

Каталог `api_tests` содержит API тесты на reqres.in

Каталог `ui_tests` содержит UI тесты на demoqa.com

### Запуск

Установка зависимостей
```shell
pip install -r requirements.txt
```

Запуск всех тестов из корневого каталога
```shell
pytest . -v
allure serve allure-results
```
