# Supongamos que tienes una lista de ambientes como esta:
ambientes = [
    {"id": 1, "nombre": "Sala de Reuniones", "capacidad": 10, "ubicacion": "Oficina A", "descripcion": "Una sala de reuniones equipada."},
    {"id": 2, "nombre": "Oficina Ejecutiva", "capacidad": 2, "ubicacion": "Piso 5", "descripcion": "Una oficina para ejecutivos."},
    # Otros ambientes
]

def obtener_ambiente_por_id(ambiente_id):
    for ambiente in ambientes:
        if ambiente["id"] == ambiente_id:
            return ambiente
    return None  # Si no se encuentra ningún ambiente con ese ID