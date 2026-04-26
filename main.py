import datetime
import hashlib

from app import generar_hash_obra
from sentinel import protocolo_sentinel
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Lógica Interna de Codex
def procesar_forense(contenido: bytes):
    # 1. Generar Hash Principal
    hash_obra = hashlib.sha256(contenido).hexdigest()
    
    # 2. Simular Protocolo Sentinel (Fragmentación)
    texto = contenido.decode('utf-8', errors='ignore')
    palabras = texto.split()
    snippets = []
    for i in range(0, min(len(palabras), 500), 50):  # Procesamos los primeros 500 para el demo
        frag = " ".join(palabras[i:i+10])
        h = hashlib.sha256(frag.encode()).hexdigest()[:12]
        snippets.append({"pos": i, "huella": h, "texto": frag[:30] + "..."})
    
    return hash_obra, snippets

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "resultado": None}) # type: ignore

@app.post("/proteger", response_class=HTMLResponse)
async def proteger(request: Request, file: UploadFile = File(...)):
    contenido = await file.read()
    hash_obra, snippets = procesar_forense(contenido)
    
    datos_sello = {
        "archivo": file.filename,
        "hash": hash_obra,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sentinel": snippets,
        "nom151": "CERT-VOSS-2026-X99"
    }
    
    return templates.TemplateResponse("index.html", {"request": request, "resultado": datos_sello})

if __name__ == "__main__":
    # Crea un archivo de prueba y muestra los resultados sin iniciar el servidor web.
    with open("libro_test.txt", "w", encoding="utf-8") as f:
        f.write("Este es el inicio de mi gran novela de Dark Country...")

    mi_hash = generar_hash_obra("libro_test.txt")
    print(f"Sello Digital: {mi_hash}")

    fragmentos = protocolo_sentinel("Este es el inicio de mi gran novela de Dark Country...")
    for frag in fragmentos:
        print(f"Fragmento en posición {frag['posicion']}: {frag['hash']}")
