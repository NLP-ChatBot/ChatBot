<h1 style="text-align: center;">Documentação do Projeto</h1>

---
<h2>Sumário</h2>
<div style="font-size: 15px">
    <ol>
        <li><a href="#dataset">Dataset</a></li>
        <li><a href="#test">Teste do Ambiente</li>
    </ol>
</div>

---
<h2 id="dataset">Dataset</h2>
<div style="font-size: 15px">
    <p>Os datasets utilizados vieram da plataforma <a href="https://www.kaggle.com">Kaggle</a>. As bases de dados escolhidas foram:</p>
    <ul style="font-style: italic">
        <li><a href="https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot">Dataset for chatbot</a></li>
        <li><a href="https://www.kaggle.com/datasets/yapwh1208/chatbot-ai-q-and-a">Chatbot Dataset (AI Q&A)</a></li>
        <li><a href="https://www.kaggle.com/datasets/saurabhprajapat/chatbot-training-dataset">Chatbot Training Dataset</a></li>
        <li><a href="https://www.kaggle.com/datasets/kreeshrajani/3k-conversations-dataset-for-chatbot">3K Conversations Dataset for ChatBot</a></li>
        <li><a href="https://www.kaggle.com/datasets/michau96/best-cities-to-live-by-chatgpt">Best cities to live by ChatGPT</a></li>
        <li><a href="https://www.kaggle.com/datasets/trinadhsingaladevi/chatbot-conversations-about-computer">Chatbot conversations about computer</a></li>
        <li><a href="https://www.kaggle.com/datasets/therealsampat/intents-for-first-aid-recommendations">First Aid Recommendations Intents</a></li>
    </ul>
    <p>Caso o dataset localizado em 'data/raw/chatbot_dataset.csv' seja excluído ou modificado é possível restaurar ele usando o script 'make_dataset.py' em 'data'. Para isso, é necessario um nome de usuário e senha para solicitar a base. O usuário e senha de acesso livre é 'user' para ambos os campos:</p>

```
$python data/make_dataset.py -u user -p user
```
</div>

<h2 id="test">Teste do Ambiente</h2>
<div style="font-size: 15px">
    <p>O Teste de ambiente verifica se todas as dependências estão nas versões corretas expecificadas nos arquivos `requirements.txt` e `pyproject.toml`. Para testar o ambiente existe duas opções:</p>
    <p>Utilizando o Poetry:</p>

```
$poetry run pytest test/
```
<p>Utilizando o venv ou conda:</p>
<p style="font-size: 14px; font-style: italic">Lembre-se de estar dentro do ambiente para executar o comando abaixo</p>

```
$pytest test/
```
</div>