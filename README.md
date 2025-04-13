# Language Trainer — Django веб-приложение для изучения слов

Это обучающее Django-приложение, где вы можете:
- Добавлять карточки с иностранными словами
- Загружать карточки списком
- Повторять слова в режиме тренировки
- Вести счёт правильных и неправильных ответов
- Искать слова по словарю

---

## Как запустить проект

### 1. Склонируйте репозиторий
```bash
git clone <repo-link>
cd language_trainer
```
---

### 2. Создайте виртуальное окружение и активируйте его

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

---

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

---

### 4. Примените миграции

```bash
python manage.py makemigrations
python manage.py makemigrations cards
python manage.py migrate
```

---

### 5. Запустите сервер разработки

```bash
python manage.py runserver
```

---

### 6. Откройте в браузере

Перейдите по адресу:

```
http://127.0.0.1:8000/
```

---

## Структура проекта

```
language_trainer/
│   ├── templates/       # HTML-шаблоны
├── db.sqlite3           # База данных
├── manage.py            # Управление проектом
├── language_trainer/    # Настройки Django
├── cards                # Модуль карточек
```

---
## Результаты pylint

С исправлением объективно неверных детектов (подключение .pylintrc): 9.84/10  

---

