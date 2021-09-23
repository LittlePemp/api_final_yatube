# api_final

## Описание

```
Данный API создан для работы с запросами к моделям Постов, Подписчиков и Комментариев с реализацией JWT.

:white_check_mark: URL: '/api/v1/<posts, groups, follows, jwt>/'
```

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:LittlePemp/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Примеры

* Получение списка постов
```
http://127.0.0.1:8000/api/v1/posts/
```

Ответ:
```
{
	'www': 'qwqwe'
}
```

* Получение данных по определенному посту
```
http://127.0.0.1:8000/api/v1/posts/1
```

Ответ:
```
{
	'www': 'qwqwe'
}
```