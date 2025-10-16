from fastapi import FastAPI, File, UploadFile
import shutil
import os

app = FastAPI()

# Pasta para salvar as imagens
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-image/", tags=["Uploads"], summary="Envia uma imagem", description="Endpoint para fazer upload de uma imagem e salvar no servidor.")
async def upload_image(file: UploadFile = File(...)):
    # Caminho onde o arquivo será salvo
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Salva o arquivo no disco
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Imagem enviada com sucesso!"
    }
