import datetime

def generar_constancia_nom151(hash_obra):
    # Simulación de la estructura ASN.1/XML que entrega un PSC
    constancia = {
        "emisor": "Codex PSC Autorizado",
        "fecha_cierta": datetime.datetime.now().isoformat(),
        "hash_original": hash_obra,
        "estatus": "Certificado e Inmutable"
    }
    return constancia