## Пошаговая инструкция по созданию GUI-приложения «Currency Converter» на Python

### 1. Создание интерфейса
- Используйте библиотеку `tkinter` для графического интерфейса.
- Добавьте:
  - выпадающие списки для выбора исходной и целевой валюты;
  - поле для ввода суммы;
  - кнопку «Конвертировать»;
  - таблицу (Treeview) для отображения истории.

### 2. Подключение внешнего API
- Для получения курсов валют используйте, например, *exchangerate-api.com*.
- Пример запроса:
  ```
  https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD
  ```
- В ответе получите актуальные курсы.

### 3. Сохранение и загрузка истории
- Используйте модуль `json` для сохранения истории конвертаций в файл.
- При запуске приложения загружайте историю из файла и отображайте в таблице.

### 4. Проверка корректности ввода
- Сумма должна быть положительным числом.
- При ошибке выводите сообщение пользователю.

### 5. Использование Git
1. Инициализируйте репозиторий:
   ```bash
   git init
   ```
2. Добавьте файлы:
   ```bash
   git add .
   ```
3. Сделайте коммит:
   ```bash
   git commit -m "Initial commit"
   ```
4. Создайте репозиторий на *GitHub*/*GitLab* и залейте проект:
   ```bash
   git remote add origin <URL_репозитория>
   git push -u origin master
   ```

### 6. README (пример в формате .md)
```markdown
# Currency Converter

## Автор: Иван Иванов

## Описание
Простое приложение для конвертации валют с использованием внешнего API, сохранением истории и графическим интерфейсом.

## Требования
- Python 3.x
- Библиотеки: `tkinter`, `requests`

## Установка
1. Установите зависимости:
   ```
   pip install requests
   ```
2. Получите API-ключ на exchangerate-api.com и вставьте в код.

## Использование
1. Запустите файл `currency_converter.py`.
2. Выберите валюты, введите сумму, нажмите «Конвертировать».
3. История сохраняется в `history.json`.

## Примеры тестов
- Введите сумму «100», выберите USD → RUB, нажмите кнопку.
- Проверьте, что результат отображается и сохраняется в истории.
```

### Пример кода (Python + tkinter)
```python
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

API_KEY = 'YOUR_API_KEY'
HISTORY_FILE = 'history.json'

def load_history():
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

def convert():
    from_currency = from_var.get()
    to_currency = to_var.get()
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите положительное число!")
        return

    url = f"https://v6.exchangerate-api.## Пошаговая инструкция по созданию GUI-приложения «Currency Converter» на Python

### 1. Создание интерфейса
- Используйте библиотеку `tkinter` для графического интерфейса.
- Добавьте:
  - выпадающие списки для выбора исходной и целевой валюты;
  - поле для ввода суммы;
  - кнопку «Конвертировать»;
  - таблицу (Treeview) для отображения истории.

### 2. Подключение внешнего API
- Для получения курсов валют используйте, например, *exchangerate-api.com*.
- Пример запроса:
  ```
  https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD
  ```
- В ответе получите актуальные курсы.

### 3. Сохранение и загрузка истории
- Используйте модуль `json` для сохранения истории конвертаций в файл.
- При запуске приложения загружайте историю из файла и отображайте в таблице.

### 4. Проверка корректности ввода
- Сумма должна быть положительным числом.
- При ошибке выводите сообщение пользователю.

### 5. Использование Git
1. Инициализируйте репозиторий:
   ```bash
   git init
   ```
2. Добавьте файлы:
   ```bash
   git add .
   ```
3. Сделайте коммит:
   ```bash
   git commit -m "Initial commit"
   ```
4. Создайте репозиторий на *GitHub*/*GitLab* и залейте проект:
   ```bash
   git remote add origin <URL_репозитория>
   git push -u origin master
   ```

### 6. README (пример в формате .md)
```markdown
# Currency Converter

## Автор: Иван Иванов

## Описание
Простое приложение для конвертации валют с использованием внешнего API, сохранением истории и графическим интерфейсом.

## Требования
- Python 3.x
- Библиотеки: `tkinter`, `requests`

## Установка
1. Установите зависимости:
   ```
   pip install requests
   ```
2. Получите API-ключ на exchangerate-api.com и вставьте в код.

## Использование
1. Запустите файл `currency_converter.py`.
2. Выберите валюты, введите сумму, нажмите «Конвертировать».
3. История сохраняется в `history.json`.

## Примеры тестов
- Введите сумму «100», выберите USD → RUB, нажмите кнопку.
- Проверьте, что результат отображается и сохраняется в истории.
```

### Пример кода (Python + tkinter)
```python
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

API_KEY = 'YOUR_API_KEY'
HISTORY_FILE = 'history.json'

def load_history():
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

def convert():
    from_currency = from_var.get()
    to_currency = to_var.get()
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите положительное число!")
        return

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    data = response.json()
    if data['result'] == 'success':
        result = data['conversion_result']
        history = load_history()
        history.append({
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "result": result,
            "date": data['time_last_update_utc']
        })
        save_history(history)
        update_history_table()
        result_label.config(text=f"Результат: {result:.2f} {to_currency}")
    else:
        messagebox.showerror("Ошибка", "Не удалось получить курс валют.")

def update_history_table():
    for i in history_table.get_children():
        history_table.delete(i)
    for entry in load_history():
        history_table.insert('', 'end', values=(
            entry['from'],
            entry['to'],
            entry['amount'],
            entry['result'],
            entry['date']
        ))

root = tk.Tk()
root.title("Currency Converter")

# Интерфейс (выбор валют, ввод суммы, кнопка)
from_var = tk.StringVar(value="USD")
to_var = tk.StringVar(value="RUB")
amount_entry = tk.Entry(root)
convert_button = tk.Button(root, text="Конвертировать", command=convert)
result_label = tk.Label(root, text="Результат: ")

# Таблица истории
history_table = ttk.Treeview(root, columns=("From", "To", "Amount", "Result", "Date"), show='headings')
for col in history_table["columns"]:
    history_table.heading(col, text=col)
history_table.pack()

# Размещение элементов (упрощённо)
from_menu = ttk.Combobox(root, textvariable=from_var, values=["USD", "EUR", "RUB"])
to_menu = ttk.Combobox(root, textvariable=to_var, values=["USD", "EUR", "RUB"])
from_menu.pack()
to_menu.pack()
amount_entry.pack()
convert_button.pack()
result_label.pack()
update_history_table()

root.mainloop()
```
**Примечание:** не забудьте заменить `YOUR_API_KEY` на ваш реальный ключ и доработать интерфейс по своему вкусу. Проект можно выложить на GitHub и добавить ссылку в *README*.
