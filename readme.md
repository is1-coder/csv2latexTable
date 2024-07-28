# commands(Ubuntu)

python3 -m venv venv

source ./venv/bin/activate

pip install -r .\requirements.txt

python main.py

pyinstaller main.py --onefile --noconsole

# commands(Windows)

python3 -m venv venv

source ./venv/Script/activate

pip install -r .\requirements.txt

python main.py

pyinstaller main.py --onefile --noconsole