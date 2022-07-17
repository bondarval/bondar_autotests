# Selenium WebDriver tests on Python with pytest framework
## Описание
Автоматизация сценариев для поиска в Яндексе текста и изображения. 
Уделено внимание поиску и подтверждению нахождения критически важных для 
сценариев действия пользователей элементов. Автотесты построены на тестовом фреймворке pytest. 
## Используемые технологии
Подробный перечень приведен в requirements.txt.
Наиболее важны:
- Python 3.9
- Selenium 4.3.0
- Selenium WebDriver for Chrome
- pytest 7.1.2

## Способ установки
 - Установить и активировать виртуальное окружение
```bash
python -m venv venv
source venv/Scripts/activate
```
 - Установить зависимости requirements.txt
```bash
pip install -r requirements.txt
```
 - Инициализировать вебдрайвер для Сhrome.
```
Для этого необходимо в файле conftest.py задать для Chrome аргумент ("your/path/to/chromedriver.exe")
```
 - Запустить фреймворк pytest
```bash
pytest
```

## Исполнитель задания
Бондарь Валерий Александрович