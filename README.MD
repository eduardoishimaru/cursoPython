Set-ExecutionPolicy Unrestricted

Set-ExecutionPolicy -Scope CurrentUser 1

pip freeze > requirements.txt
pip freeze

#Recriar ambiente virtual
pip install -r .\requirements.txt


pip install autopep8

pip index versions pymysql

(venv) PS C:\Users\Eduardo\Documents\GitHub\cursoPython> pip index versions pymysql
WARNING: pip index is currently an experimental command. It may be removed/changed in a future release without prior warning.
pymysql (1.1.1)
Available versions: 1.1.1, 1.1.0, 1.0.3, 1.0.2, 1.0.1, 0.10.1, 0.10.0, 0.9.3, 0.9.2, 0.9.1, 0.9.0, 0.8.1, 0.8.0, 0.7.11, 0.7.10, 0.7.9, 0.7.8, 0.7.7, 0.7.6, 0.7.5, 0.7.4, 0.7.3, 0.7.2, 0.7.1, 0.7.0, 0.6.7, 0.6.6, 0.6.4, 0.6.3, 0.6.2, 0.6.1, 0.6, 0.5, 0.4, 0.3

pip install pymysql==1.0.1


otav.me