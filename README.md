⚙️ 1. Verifique o Python

Abra o terminal e digite:

python --version


Se aparecer algo como Python 3.10+, siga adiante.

📁 2. Crie uma pasta para o projeto

Exemplo:

mkdir fastapi_upload
cd fastapi_upload

📄 3. Crie o arquivo main.py

Dentro da pasta, crie o arquivo main.py com o conteúdo abaixo:

from fastapi import FastAPI, File, UploadFile
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Imagem enviada com sucesso!"
    }

📦 4. Instale as dependências

No terminal:

pip install fastapi uvicorn

🚀 5. Execute o servidor
uvicorn main:app --reload


Você verá algo assim:

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

🌐 6. Teste no navegador

Acesse:

http://127.0.0.1:8000/docs

➡️ A interface Swagger aparecerá.
Clique em POST /upload-image, depois em Try it out, envie um arquivo e execute o teste.