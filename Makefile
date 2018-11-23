.PHONY: venv

setup:
	virtualenv -p python3 venv
	. venv/bin/activate; pip install -r requirements.txt
	
clean:
	rm -rf venv
