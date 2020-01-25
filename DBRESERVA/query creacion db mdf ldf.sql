--implementando base de datos en sql server 

create database dbprueba 
drop database dbprueba

--implementanod la base de datos dbreserva
--verificar si ya existe la base de datos 
if DB_ID('DBRESERVA') is not null
begin
	use master 
	drop database DBRESERVA 
end 
go

--crear base de datos dbreserva
create database dbreserva

--guardar en dos archivos primarios(mdf) y uno log(ldf)
--archivos primarios 
on primary(
	name='dbreserva_mdf',
	filename='C:\DBRESERVA\dbreserva.mdf',--directorio a guardar
	size=15mb,--tamaño inicial
	maxsize=250mb,--tamaño maximo 
	filegrowth=10mb --incremento
),(
	name='dbreserva_ndf',--archivo secundario ndf
	filename='C:\DBRESERVA\dbreserva.ndf',--directorio a guardar
	size=15mb,--tamaño inicial
	maxsize=unlimited,--tamaño maximo ilimitado
	filegrowth=10mb --incremento

)

--archivo log
log on(
    name='dbreserva_ldf',
	filename='C:\DBRESERVA\dbreserva.ldf',--directorio a guardar
	size=15mb,--tamaño inicial
	maxsize=500mb,--tamaño maximo 
	filegrowth=10% --incremento en porcentaje
)
go


--usar base de datos 
use dbreserva

--IMPLEMENTAR LAS TABLAS 

--TABLA PAIS
create table PAIS
(
idpais char(4) not null primary key,
nombre varchar(30) not null unique
)



--TABLA PASAJERO
create table PASAJERO
(
idpasajero char(8) not null primary key,
nombre varchar(20) not null,
apaterno varchar(20) not null,
amaterno varchar(20) not null,
tip_documento varchar(30) not null,
num_documento varchar(12) not null,
fecha_nacimiento date not null,
idpais char(4) not null,
telefono varchar(15) null,
email varchar(50) not null unique ,
clave varchar(20) not null
)
go

--TABLA AEROPUERTO 
create table AEROPUERTO
(
idaeropuerto char(5) not null,
nombre varchar(50) not null,
idpais char(4) not null
)
go

--alterar la tabla aeropuerto 
alter table aeropuerto 
add constraint PK_aeropuerto_pais 
primary key nonclustered(idaeropuerto) --indice no agrupado
go

--campo nombre debe ser unico 
alter table aeropuerto add constraint 
UQ_aeropuerto_nombre unique(nombre)
go

--TABLA AEROLINEA 
create table AEROLINEA
(
idaerolinea int not null primary key,
ruc char(11) not null,
nombre varchar(40) not null,
)
go

--TABLA AVION 
create table AVION (
idavion char(5) not null primary key,
idaerolinea int not null,
fabricante varchar(40) null,
tipo varchar(3) not null
)
go

--AGREGAR FALTANTE 
alter table avion add capacidad int not null
go

--modificar campo tipo
alter table avion alter column tipo varchar(30) not null

--TABLA ASIENTO 
create table ASIENTO
(
idasiento int not null primary key,
letra char(2) not null,
fila int not null
)
go



--TABLA TARIFA 
 create table TARIFA
 (
 idtarifa int not null primary key,
 clase varchar(20) not null unique,
 impuesto money not null
 )
 go

 --TABLA RESERVA
  create table RESERVA
  (
  idreserva int not null primary key,
  costo money not null,
  fecha date null,
  observacion varchar(200)
  )
  go


  --RESTRICIONES CHECK Y DEFAULT
  --restriccion default 
  alter table reserva add constraint 
  DFL_reserva_fecha  
  default getdate() for fecha
  go


  --TABLA VUELO 
  create table VUELO(
  idasiento int not null,
  idaeropuerto char(5) not null,
  idreserva int not null,
  idavion char(5) not null,
  idtarifa int not null
  )
  go

  --implementar llaves primarias de la tabla vuelo 
  alter table vuelo 
  add primary key (idasiento,idaeropuerto,idreserva,idavion)
  go

  --CREAR TABLA PAGO 
  create table PAGO
  (
  idpago int not null primary key identity,
  idreserva int not null,
  fecha date default getdate(),
  idpasajero char(8) not null,
  monto money not null,
  tipo_comprobante varchar(20) not null,
  num_comprobante varchar(15) not null,
  impuesto decimal(5,2) not null
  )
  go

  --agregar restriccion check que no se ingresen fechas mayores  al a fecha actual
  alter table pago add constraint CHK_pago_fecha
  check (fecha <=getdate())
  go



  --IMPLEMENTAR LAS RELACIONES 
  --relación entre la tabla país y pasajero
  alter table pasajero add constraint 
  FK_pasajero_pais 
  foreign key(idpais) references pais(idpais)
  go

  --relacion entre la tabla aeropuerto y pais
  alter table aeropuerto add
  constraint FK_aeropuero_pais
  foreign key(idpais) references pais(idpais)
  go

  --relacion entre la tabla pago y pasajero 
  alter table pago add constraint 
  FK_pago_pasajero
  foreign key(idpasajero) references pasajero(idpasajero)
  go

  --relacion entre la tabla pago y reserva
  alter table pago add constraint 
  FK_pago_reserva 
  foreign key(idreserva) references reserva(idreserva)
  go

  --relacion tabla avion y aerolinea 
  alter table avion 
  add constraint FK_avion_aerolinea
  foreign key(idaerolinea) references aerolinea(idaerolinea)
  go

  --relacion entre la tabla vuelo y asiento
  alter table vuelo 
  add constraint FK_vuelo_asiento 
  foreign key(idasiento) references asiento(idasiento)
  go

--relacion entre la tabla vuelo y avion 
alter table vuelo 
add constraint FK_vuelo_avion
foreign key(idavion) references avion(idavion)
go

--relacion tabla vuelo y reserva
alter table vuelo 
add constraint FK_vuelo_reserva
foreign key(idreserva) references reserva(idreserva)
go

--relacion tabla vuelo y tarifa
alter table vuelo 
add constraint FK_vuelo_tarifa
foreign key(idtarifa) references tarifa(idtarifa)
go

--relacion entre tabla vuelo y aeropuerto
alter table vuelo 
add constraint FK_vuelo_aeropuerto
foreign key(idaeropuerto) references aeropuerto(idaeropuerto)
go



