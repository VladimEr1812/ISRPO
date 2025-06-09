import * as vscode from 'vscode';

// Вспомогательные функции для преобразования регистра
function toCamelCase(text: string): string {
    return text.replace(/[^a-zA-Z0-9]+(.)?/g, (match, chr) => chr ? chr.toUpperCase() : '').replace(/^./, (match) => match.toLowerCase());
}

function toSnakeCase(text: string): string {
    return text.replace(/([A-Z])/g, "_$1").toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
}

function toKebabCase(text: string): string {
    return text.replace(/([A-Z])/g, "-$1").toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

// Главная функция для преобразования выделенного текста
function convertSelectionCase(converter: (text: string) => string, caseName: string) {
    const editor = vscode.window.activeTextEditor;

    if (!editor) {
        vscode.window.showInformationMessage('Нет активного текстового редактора.');
        return;
    }

    const document = editor.document;
    const selection = editor.selection;

    if (selection.isEmpty) {
        vscode.window.showInformationMessage('Пожалуйста, выделите текст для преобразования.');
        return;
    }

    const selectedText = document.getText(selection);
    const convertedText = converter(selectedText);

    editor.edit(editBuilder => {
        editBuilder.replace(selection, convertedText);
    }).then(success => {
        if (success) {
            vscode.window.showInformationMessage(`Текст преобразован в ${caseName}.`);
        } else {
            vscode.window.showErrorMessage('Не удалось преобразовать текст.');
        }
    });
}

// Функция активации расширения
export function activate(context: vscode.ExtensionContext) {
    console.log('Поздравляем, ваш плагин "Case Converter" теперь активен!');

    // Регистрируем команды
    let disposableUpper = vscode.commands.registerCommand('case-converter.toUppercase', () => {
        convertSelectionCase(text => text.toUpperCase(), 'верхний регистр');
    });
    let disposableLower = vscode.commands.registerCommand('case-converter.toLowercase', () => {
        convertSelectionCase(text => text.toLowerCase(), 'нижний регистр');
    });
    let disposableCamel = vscode.commands.registerCommand('case-converter.toCamelCase', () => {
        convertSelectionCase(toCamelCase, 'camelCase');
    });
    let disposableSnake = vscode.commands.registerCommand('case-converter.toSnakeCase', () => {
        convertSelectionCase(toSnakeCase, 'snake_case');
    });
    let disposableKebab = vscode.commands.registerCommand('case-converter.toKebabCase', () => {
        convertSelectionCase(toKebabCase, 'kebab-case');
    });


    // Добавляем команды в подписки контекста, чтобы они были доступны
    context.subscriptions.push(
        disposableUpper,
        disposableLower,
        disposableCamel,
        disposableSnake,
        disposableKebab
    );
}

// Функция деактивации расширения
export function deactivate() {}