# Master_sript
Script for workshop Verb WordNet

В качестве входных данных необходима csv таблица с глаголами и их моделями управления и тексты. 
Формат текстов не важен и изменить его можно в 20 строке кода.
Выходным файлом является csv таблица, имеющая 4 столбца: Verb1, Verb2, same contstr, same context

В первых двух столбцах указываются родственные глаголы, во вторых двух столбцах указывается то, что эти глаголы имеют общую модель управления, а также 4 и более схожих контекстов, отличающихся друг от друга.

Сначала программа на основе таблицы глаголов и моделей управления составляет список глаголов, имеющих схожую модель управления.
Далее находятся контексты длинной 5 для каждого глагола. Затем если глагол и глагол, имеющий схожую модель управления, имеют 4 и более схожих контекстов, то они записываются в выходящий файл-таблицу.

Так как автор не имеет права загружать все тексты, с которыми работала программа, сюда было загруженно небольшое их количество, а также файл, схожий по строению. В этом файле специально были написаны предложения, которые точно дадут запись в выходную таблицу.
