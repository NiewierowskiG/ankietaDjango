Instukcja napisana dla systemu operacyjnego Windows
Wymagania systemowe:
- Python w wersji minimum 3.6

1. Uruchamiamy PowerShell jako administrator
1. Wchodzimy do folderu ankietaDjango
2. instalujemy potrzebne biblioteki (pip install -r .\requirements.txt)
3. Aktualizujemy bazę danych (python manage.py makemigrations) oraz (python manage.py migrate)
4. Uruchamiamy aplikacje (python manage.py runserver 0.0.0.0:8000)
5. Bazowa strona na którą chcemy się dostać to 127.0.0.1:8000/ankieta/
