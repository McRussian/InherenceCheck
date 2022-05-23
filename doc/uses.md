

## <a name=running_programm></a>Запуск программы

Для запуска программы нужен интерпретатор питона версии не ниже 3.6.
Программа запускается с помощью терминала, и все управление происходит при помощи терминала.
Программе для работы нужны некоторые файлы:

- formula, в этом файле записаны имена тех формул, которые встречаются в секвенциях
- rule, в этом файле записаны те правила, при помощи которых проверятся вывод
- variable, в этом файле записаны имена переменных, которые встречаются в секвенции

При запуске программы необходимо указать путь к этим файлам.
Для указания необходимых файлов используются различные ключи:

- '--variable', '-v' - для указания файла с переменными
- '--formula', '-f' - для указания файла с формулами
- '--rule', '-r' - для указания файла с набором правил

По умолчанию берутся те файлы, которые лежат в каталоге data.

После того как указанные файлы считались, и настроился парсер, можно проверять дерево вывода.
Для этого запускается цикл, в котором запрашивается имя файла с деревом вывода.
Мы должны ввести имя файла, или ключевое слова 'exit' или 'quit' для выхода.
По умолчанию, берется файл с деревом вывода из каталога data. 
Пример файла с деревом вывода - tree1.
Если вывод корректен, то информация об этом появится в консоли.
Все сообщения об ошибках будут записаны в файл журнала - log.txt