from .models import Chofer, Vehiculo, Registrocontabilidad

def crear_vehiculo(nuevoPatente, nuevoMarca, nuevoModelo, anio):
    nuevo_vehiculo = Vehiculo(patente = nuevoPatente, marca = nuevoMarca, modelo = nuevoModelo, year = anio)
    nuevo_vehiculo.save()
    print('Vehiculo Creado Correctamente !')

def crear_chofer(nuevoRut, nuevoNombre, nuevoApellido, estadoActivo, fechaCreacion, patenteVehiculo):
    nuevoVehiculo = Vehiculo.objects.get(patente = patenteVehiculo) # Asigna un valor con la instancia del modelo Vehiculo.patente
    nuevo_chofer = Chofer(rut = nuevoRut, nombre = nuevoNombre, apellido = nuevoApellido, activo = estadoActivo, creacion_registro = fechaCreacion, vehiculo = nuevoVehiculo)
    nuevo_chofer.save()
    print('Chofer Creado Correctamente !')

def crear_registro_contable(nuevaFechaCompra, nuevoValor, patenteVehiculo):
    nuevoVehiculo = Vehiculo.objects.get(patente = patenteVehiculo) # Asigna un valor con la instancia del modelo Vehiculo.patente
    nuevo_registro = Registrocontabilidad(fecha_compra = nuevaFechaCompra, valor = nuevoValor, vehiculo = nuevoVehiculo)
    nuevo_registro.save()
    print('Registro Contable Creado Correctamente !')

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut = rut)
    chofer.activo = False
    chofer.save()
    print('Chofer Deshabilitado Correctamente !')

def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut = rut)
    chofer.activo = True
    chofer.save()
    print('Chofer Habilitado Correctamente !')

def deshabilitar_vehiculo():
    pass

def habilitar_vehiculo():
    pass

def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente = patente)

def obtener_chofer(rut):
    return Chofer.objects.get(rut = rut)

def asignar_chofer_a_vehiculo(rut, patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer = Chofer.objects.get(rut=rut)
    chofer.vehiculo = vehiculo 
    chofer.save()

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()

    for vehiculo in vehiculos:
        print(f'Patente:{vehiculo.patente} Marca:{vehiculo.marca.strip()} Modelo:{vehiculo.modelo.strip()} Año:{vehiculo.year}' )