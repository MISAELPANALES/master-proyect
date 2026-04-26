import hashlib

def protocolo_sentinel(texto, tamaño_bloque=100):
    # Divide el texto en fragmentos (snippets) para rastreo parcial
    palabras = texto.split()
    fragmentos = []
    for i in range(0, len(palabras), tamaño_bloque):
        fragmento = " ".join(palabras[i:i + tamaño_bloque])
        hash_fragmento = hashlib.sha256(fragmento.encode()).hexdigest()
        fragmentos.append({
            "posicion": i,
            "hash": hash_fragmento
        })
    return fragmentos

# Esto permite que si cambian una palabra, los demás fragmentos sigan siendo válidos.