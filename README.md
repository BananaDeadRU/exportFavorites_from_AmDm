# exportFavorites_from_AmDm

Rus:
Эта программа, написанная на Python, позволяет выгрузить избранные подборы пользователя в html файлы на компьютер.

Как пользоваться? 
1. Скачайте папку amdm и поместите её на рабочий стол. Важно: не удаляйте внутри папку html. Внутри неё лежит файл стиля css. Можно удалять файлы с расширением html, если они вам не нужны.
2. Запустите файл parse.exe и введите имя пользователя в консоли.
3. Дождитесь окончания работы программы.
4. По завершении, в папке amdm появится файл navigate.html. В нем содержатся гиперссылки на все загруженные файлы.

Некоторые песни могут не выгрузиться, потому что их гиперссылка ведет не на зеркало j119, а на обычный amdm.ru, который недоступен из России. Если такие песни будут найдены, то о них будет сообщено в консоли.

Eng:
This program, written in Python, allows you to upload the user's favorites to html files on your computer.

How to use it? 
1. Download the amdm folder and place it on your desktop. Important: do not delete the html folder inside. There is a css style file inside it. You can delete files with the html extension if you don't need them.
2. Run the file parse.exe and enter the username in the console.
3. Wait for the end of the program.
4. Upon completion, a file will appear in the amdm folder navigate.html. It contains hyperlinks to all downloaded files.

Some songs may not be uploaded because their hyperlink does not lead to the j119 mirror, but to the regular one amdm.ru which is not available from Russia. If such songs are found, they will be reported in the console.

Использованные библиотеки / used libs:
1. bs4
2. lxml
3. requests
4. re
5. random
6. time
7. os
