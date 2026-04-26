import hashlib

def generar_hash_obra(archivo_path):
    sha256_hash = hashlib.sha256()
    with open(archivo_path, "rb") as f:
        # Leemos el archivo en bloques para no saturar la memoria
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Ejemplo de uso
# hash_resultado = generar_hash_obra("manuscrito.docx")
# print(f"Huella Digital Codex: {hash_resultado}")  