# VS Code Plugin: Case Converter

## Авторство
* **Автор:** Еремченко Владимир Алексеевич, Группа: М3309

## Описание плагина
Плагин "Case Converter" для Visual Studio Code предоставляет набор удобных команд для быстрого изменения регистра выделенного текста в активном редакторе. Это значительно упрощает работу с кодом, особенно при необходимости приводить переменные или функции к определенному стилю именования (camelCase, snake_case, kebab-case).

## Возможности

Плагин добавляет следующие команды, доступные через палитру команд (Ctrl+Shift+P):

1.  **Case Converter: В ВЕРХНИЙ РЕГИСТР**
    * Преобразует выделенный текст в заглавные буквы (UPPERCASE).
    * Пример: `Hello world` -> `HELLO WORLD`

2.  **Case Converter: в нижний регистр**
    * Преобразует выделенный текст в строчные буквы (lowercase).
    * Пример: `Hello World` -> `hello world`

3.  **Case Converter: в camelCase**
    * Преобразует выделенный текст в стиль `camelCase`.
    * Пример: `hello_world` -> `helloWorld`; `Hello World` -> `helloWorld`

4.  **Case Converter: в snake_case**
    * Преобразует выделенный текст в стиль `snake_case`.
    * Пример: `helloWorld` -> `hello_world`; `Hello World` -> `hello_world`

5.  **Case Converter: в kebab-case**
    * Преобразует выделенный текст в стиль `kebab-case`.
    * Пример: `helloWorld` -> `hello-world`; `Hello World` -> `hello-world`

## Установка и использование

### Установка (для пользователя)
1. Откройте Visual Studio Code.
2. Перейдите в раздел "Расширения" (Ctrl+Shift+X).
3. В строке поиска наберите "Case Converter".
4. Нажмите кнопку "Установить" рядом с плагином (после публикации).

### Использование
1. Откройте любой текстовый файл в VS Code.
2. Выделите часть текста, регистр которого вы хотите изменить.
3. Откройте палитру команд (Ctrl+Shift+P).
4. Начните набирать "Case Converter" и выберите желаемую команду из списка.

## История изменений проекта

```bash
* 03da418 (HEAD -> master, origin/master) Initial commit
