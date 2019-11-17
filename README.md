## Stepiq.org

Финальный проект, подробности - https://stepik.org/lesson/201964/step/14?unit=176022

## Запуск тестов

Для запуска необходимо иметь chromedriver для соответствующей версии ОС:
(необходимо положить в корень проекта)

https://chromedriver.chromium.org/downloads

Для запуска версий необходим python3 (python3.4+):
* можно поставить зависимости из requirements.txt в системный питон (если он есть)
* или же поднять виртуальное окружение:

в директории проекта выполнить:

python3 -m venv venv

source venv/bin/activate

Сами тесты запускаются следующим образом:

python -m pytest -v --tb=line --language=en -m need_review

*меткой need_review отмечены тесты, обозначенные для проверки.  
