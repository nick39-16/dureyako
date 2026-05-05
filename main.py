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
