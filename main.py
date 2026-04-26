from app import generar_hash_obra
from sentinel import protocolo_sentinel

# Crea un archivo de prueba
with open("libro_test.txt", "w") as f:
    f.write("Este es el inicio de mi gran novela de Dark Country...")

# Ejecuta el sello
mi_hash = generar_hash_obra("libro_test.txt")
print(f"Sello Digital: {mi_hash}")

# Ejecuta el protocolo Sentinel
fragmentos = protocolo_sentinel("Este es el inicio de mi gran novela de Dark Country...")
for frag in fragmentos:
    print(f"Fragmento en posición {frag['posicion']}: {frag['hash']}")