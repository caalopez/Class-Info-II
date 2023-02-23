class Mascota:

    def __init__(self) -> None:

        self.__nombre= ""
        self.__historia= 0
        self.__tipo= ""
        self.__peso= ""
        self.__fecha_ingreso= ""
        self.__lista_medicamento= []
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verMedicamentos(self):
        return self.__lista_medicamento

    def asignarNombre (self,n):
        self.__nombre=n
    def asignarHistoria (self,h):
        self.__historia=h
    def asignarTipo (self,t):
        self.__nombre=t
    def asignarPeso (self,p):
        self.__nombre=p
    def asignarFecha (self,f):
        self.__nombre=f
    def asignarMedicamento (self,m):
        self.__nombre=m

class Sistema:
    def __init__(self) -> None:
        self.__lista_mascotas= []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        return False

    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)

    
    def ingresarMascotas(self):
        self.__lista_mascotas.append(Mascota)

    def VerFechaIngreso(self,historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha()
        return None
    
    def VerMedicamento(self,historia):
        for masc in self.__lista_mascotas():
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos()
        return None
    
    def eliminarMascota(self,historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
               self.__lista_mascotas.remove(masc)
               return True
        return False
    
    def __init__(self) -> None:
        self.__lista_mascotas= []
        self.__numero_mascotas= len(self.__lista_mascotas)



class Medicamento:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__dosis= 0

    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis

    def asignarNombre(self,medi):
        self.__nombre= medi
    def asignarDosis(self,medi):
        self.__dosis= medi


