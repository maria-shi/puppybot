# Puppy bot
Puppy bot - это Telegram-бот, который по запросу пользователя присылает [смешные гифки с собаками](https://thedogapi.com/).

### Технологии, используемые в проекте
* [Python 3.7](https://docs.python.org/3.7/)
* [Python-telegram-bot 13.7](https://pypi.org/project/python-telegram-bot-raw/13.7/)
* [Python-dotenv 0.19](https://pypi.org/project/python-dotenv/0.19.0/)
* [Requests 2.26](https://requests.readthedocs.io/en/latest/)

### Запуск проекта
Клонируйте репозиторий и перейдите в него в командной строке:
```
https://github.com/maria-shi/puppybot.git
```
```
cd puppybot
```
Создайте и активируйте виртуальное окружение:
```
py -3.7 -m venv venv
```
```
source venv/Scripts/activate
```
Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Создайте файл с переменными окружения .env:
```
touch .env
```

Создайте Telegram-бота с помощью [@BotFather](https://telegram.me/BotFather). В процессе вы получите API-токен вида: `0000000000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`. Создайте в файле **.env** константу TOKEN и установите ей значение полученного токена: 
```
TOKEN=0000000000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
Запустите работу бота в командной строке:
```
python puppybot.py
```
Перейдите в диалог с ботом по ссылке, полученной от [@BotFather](https://telegram.me/BotFather) (t.me/<название бота>) и введите команду `/start`.

### Автор
[@maria-shi](https://github.com/maria-shi)
