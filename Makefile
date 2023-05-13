help:
	@echo "make install-poetry: Instala as dependências do projeto utilizando o modulo do Poetry."
	@echo "make install-venv: Instala as dependências do projeto utilizando o modulo pip do Python (Recomendado utilizar um ambiente isolado como o venv ou conda antes de instalar)."

install-poetry:
	@poetry install

install-venv:
	@pip install -r requirements.txt