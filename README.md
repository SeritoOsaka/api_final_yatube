# Как запустить проект:
## Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:SeritoOsaka/api_final_yatube.git

## Cоздать и активировать виртуальное окружение:
python -m venv venv

source venv/bin/activate

## Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip

pip install -r requirements.txt

## Выполнить миграции:
python manage.py migrate

## Запустить проект:
python manage.py runserver
