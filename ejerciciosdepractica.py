class Tren:
    def __init__(self, id_tren, longitud):
        self.id_tren = id_tren
        self.longitud = longitud
        
    def mostrar_info(self):
        return f"ID del tren: {self.id_tren}, Longitud: {self.longitud}m"

class Locomotora(Tren):
    def __init__(self, id_tren, longitud, potencia):
        super().__init__(id_tren, longitud)
        self.potencia = potencia
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Potencia: {self.potencia}HP"

class VagonCarga(Tren):
    def __init__(self, id_tren, longitud, capacidad_carga):
        super().__init__(id_tren, longitud)
        self.capacidad_carga = capacidad_carga
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Capacidad de carga: {self.capacidad_carga}kg"

class VagonPasajeros(Tren):
    def __init__(self, id_tren, longitud, num_asientos):
        super().__init__(id_tren, longitud)
        self.num_asientos = num_asientos
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Número de asientos: {self.num_asientos}"

# Ejemplo de uso
if __name__ == "__main__":
    locomotora = Locomotora("L001", 15, 5000)
    vagon_carga = VagonCarga("VC001", 20, 5000)
    vagon_pasajeros = VagonPasajeros("VP001", 25, 50)
    
    print(locomotora.mostrar_info())
    print(vagon_carga.mostrar_info())
    print(vagon_pasajeros.mostrar_info())
