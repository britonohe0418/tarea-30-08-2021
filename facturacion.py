from datetime import date,datetime

class Empresa:
    def __init__(self,nom="El mas Barato",ruc="0999999999",tel="042971234",dir="Juan Montalvo y Pedro Carbo"):
        self.nombre = nom
        self.ruc = ruc
        self.telefono = tel
        self.direccion = dir
    def mostrarEmpresa(self):
        print("Empresa: {:17}Ruc:{}".format(self.nombre,self.ruc))

from abc import ABC, abstractmethod
class Cliente():
    def __init__(self,nom,ced,tel):
        self.nombre = nom
        self.cedula = ced
        self.telefono = tel
    
    @abstractmethod
    def getCedula(self):
        return self.cedula
    

    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)

class ClienteCorporativo(Cliente):
    def __init__(self,nom,ced,tel,contrato):
        super().__init__(nom,ced,tel)
        self.__contrato=contrato


    @property
    def contrato(self):  # getter: obtener el valor del atributo privado
        return self.__contrato
    @contrato.setter
    def contrato(self, value):  # setter: asigna un valor al atributo privado
        if value:
            self.__contrato = value
        else:
            self.__contrato = 'Sin contrato'

    def mostrarCliente(self):
        print(self.nombre,self.__contrato)

class ClientePersonal(Cliente):
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom,ced,tel)
        self.__promocion=promocion

    @property
    def promocion(self): # getter: obtener el valor del atributo privado
        return self.__promocion
    
    def mostrarCliente(self):
        print("Cliente: {:13}Cedula: {}".format(self.nombre,self.cedula))
    
    def getCedula(self):
        return super().getCedula()

class Articulo:
    secuencia=0
    iva = 0.12
    def __init__(self,des,pre,sto):
        Articulo.secuencia += 1
        self.codigo = Articulo.secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)

class DetVenta:
    linea=0

    def __init__(self,articulo,cantidad):
        DetVenta.linea += 1
        self.lineaDetalle = DetVenta.linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad


class CabVenta:
    def __init__(self,fac,fecha,cliente,tot=0):
        self.factura = fac
        self.fecha = fecha
        self.cliente = cliente
        self.total = tot
        self.detalleVen = []

    def agregarDetalle(self,articulo,cantidad):
        detalle = DetVenta(articulo,cantidad)
        self.total += detalle.precio*detalle.cantidad
        self.detalleVen.append(detalle)
    
    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:17} Ruc:{}".format(empNombre,empRuc))
        print("Factura#:{:13}Fecha:  {}".format(self.factura,self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo    Precio Cantidad Subtotal")
        for det in self.detalleVen:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))
        print("Total Venta:{:26}".format(self.total))

#cli1 = ClientePersonal("Daniel","0992214888","099214847")
# empresa = Empresa()
# cli1 = ClientePersonal("Daniel","0992214888","099214847",False)
# print(cli1.getCedula())
# art1 = Articulo("Aceite",3,100)
# art2 = Articulo("Coca cola",1,200)
# today = date.today()
# fecha = date(2021,8,15)
# venta = CabVenta('F0001',date.today(),cli1)
# venta.agregarDetalle(art1,3)
# venta.agregarDetalle(art2,2)
# venta.mostrarVenta(empresa.nombre,empresa.ruc)


class InterfaceSistemaPago(ABC):
    @abstractmethod
    def pago(self):
        pass
    
    @abstractmethod
    def saldo(self):
        pass

class PagoTarjetaImplements(InterfaceSistemaPago):

    def pago(self):
        return "Pago tarjeta"
    
    def saldo(self):
        return "Saldo Tarjetarebajado"

class ImplementsPagoContrato(InterfaceSistemaPago):
    def pago(self):
        return "Pago Contrato2"
    
    def saldo(self):
        return "Saldo Contrato rebajado"


class Vendedor():
    def __init__(self,nombre):
        self.nombre = nombre
    
    def moduloPago(self,contrato):
        return contrato.pago()
    

pagoTarjeta = PagoTarjetaImplements()
print(pagoTarjeta.pago())
Contrato = ImplementsPagoContrato()
# print(Contrato.pago())
ven1 = Vendedor("Daniel")
print(ven1.moduloPago(Contrato))
