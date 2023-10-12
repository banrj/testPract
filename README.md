# testPract
убрал из .gitignore .env 
чтобы ты не создавала его сама
если файла alembic.ini нет, тo пишем ```alembic init migration```
После накатываем миграцию ```alembic upgrade head```
Ecли есть файла alembic.ini сразу пишем миграцию ```alembic upgrade head```
