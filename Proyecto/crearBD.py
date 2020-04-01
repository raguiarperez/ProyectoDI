import os
from sqlite3 import dbapi2

"""
    Genera la base de datos y le introduce unos datos iniciales.
"""
try:
    ###Creacion de la base de datos.
    baseDatos = dbapi2.connect("BaseDeDatos.dat")
    cursor = baseDatos.cursor()

    ###Creamcion de las tablas
    cursor.execute("create table proveedores(id text, nombre text,CIF text, direccion text, telefono text, correo text)")
    cursor.execute("create table productos(id text, nombre text , descripcion text, cantidadStock number, precioUnidad number,idProv text)")
    cursor.execute("create table facturasClientes(idFactura number, nombreCliente text, telefono text, direccion text, correo text)")
    cursor.execute("create table facturasInfo(idFactura number,idProducto text, cantidad number)")

    ###Rezlizamos Inserts en las tablas
    cursor.execute("insert into proveedores values('idprov1','Siemens','562-352-143','Av. Alcalde Lavadores Nº56','986456784','siemens@gmail.com')")
    cursor.execute("insert into proveedores values('idprov2','Codisin','150-488-654','Rua Sen nome Nª87','95528789563','Codisin@codisin.pt')")
    cursor.execute("insert into proveedores values('idprov3','Simaupro','563-234-789','C.Genaro de la Fuente Nº76','986097984','simaupro@empresasunidas.com')")

    cursor.execute("insert into productos values('232051760','6es7540-3220-age0','Decodificador Simatic', 15, 250.00,'idprov1')")
    cursor.execute("insert into productos values('255045198','6k7mup','Detector Inductivo', 30, 28.90, 'idprov2')")
    cursor.execute("insert into productos values('276043207','CHO10','Capota con salida lateral', 45, 17.90, 'idprov3')")

    cursor.execute("insert into facturasClientes values(1,'Atlantida','986475000','PT.L Beade Parcela Nª7','Atlantida@precisgal-group.com')")
    cursor.execute("insert into facturasClientes values(1,'Digamel','986502010','C. Subida del Capitan Nº54','administracion@digamel.org')")

    cursor.execute("insert into facturasInfo values(1,'232051760',2)")
    cursor.execute("insert into facturasInfo values(1,'255045198',1)")

    ###Realizamos commit en la BD
    baseDatos.commit()

###Cremos una excepcion para lo errores y finalmente cerramos la conexion
except (dbapi2.DatabaseError):
    print("ERROR BD")
finally:
    print("Cerramos conexionBD")
    cursor.close()
    baseDatos.close()