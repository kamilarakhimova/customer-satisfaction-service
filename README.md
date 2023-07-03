# Customer Satisfaction Service

---

Данный проект демонстрирует построение ML-модели, предсказывающей удовлетворённость пассажира авиакомпании полётом, и дальнейшее представление её в виде интерактивного веб-приложения с использованием фреймворка Streamlit.

Увидеть результат можно [здесь](https://airline-client-satisfaction.streamlit.app/)!

![](https://gifyu.com/image/SQGzg)

---

## Структура проекта 

В папке `solution` располагаются тетрадки (Jupiter Notebook) с решением ML-части проекта. Более подробное описание можно найти в [readme](https://github.com/kamilarakhimova/customer-satisfaction-service/tree/main/solution/readme.md) этой папки.

Папка `.streamlit` содержит в себе файл конфигурации темы, цветов и шрифтов: `config.toml`.

В таблицах `airline_clients.csv` и `airline_clients_clean.csv` можно увидеть изначальный датасет и очищенный датасет (полученный после EDA).

В файле `model.pickle` находится предобученная модель.

В `requirements.txt` описаны требования к упаковке (касательно наличия необходимых библиотекам и их версий).

В файле `app.py` лежит непосредственно код сервиса на Streamlit, там же модель, предсказывающая целевую переменную.

---

## Как локально запустить проект?

Для локального запуска приложения Streamlit в корневой папке репозитория выполните следующие действия:

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```

Отлично. Теперь по ссылке [http://localhost:8501](http://localhost:8501) можете просмотреть свою локальную версию сервиса.

Наслаждайтесь!
