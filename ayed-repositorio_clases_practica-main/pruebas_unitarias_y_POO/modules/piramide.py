import math

class Piramide:
    # *** Constructor: Debe validar que base_longitud y altura sean positivos, luego asignarlos a los atributos
    def __init__(self, base_longitud, altura):
        # Escriban su código acá
        if base_longitud<=0 or altura<=0:
            raise ValueError("Base y altura deben ser positivos")
        self.__base_longitud=base_longitud
        self.__altura=altura

    # *** Método getter base_longitud
    @property
    def base_longitud(self):
        # Escriban su código acá
        return self.__base_longitud

    # *** Método getter altura
    @property
    def altura(self):
        # Escriban su código acá
        return self.__altura

    # *** Método setter base_longitud: Debe validar que el valor sea positivo
    @base_longitud.setter
    def base_longitud(self, nueva_base_longitud):
        # Escriban su código acá
        if nueva_base_longitud <=0:
            raise ValueError("La base debe ser positiva")
        self.__base_longitud=nueva_base_longitud
    

    # *** Método setter altura: Debe validar que el valor sea positivo
    @altura.setter
    def altura(self, nueva_altura):
        # Escriban su código acá
        if nueva_altura <=0:
            raise ValueError ("La altura debe ser positiva")
        self.__altura=nueva_altura          
    
    # *** Método volumen: Debe calcular (base_longitud² * altura) / 3
    def volumen(self):
        # Escriban su código acá
        return ((self.base_longitud**2)*self.altura)/3
    
    # *** Método area_superficial: Fórmula area = base_longitud * (base_longitud + math.sqrt(4*altura² + (base_longitud/2)²))
    def area_superficial(self):
        # Escriban su código acá
        return (self.base_longitud*(self.base_longitud+ math.sqrt(4*(self.altura**2)+(self.base_longitud/2)**2)))


if __name__ == "__main__":
    piramide=Piramide(4,-6)
    volumen=piramide.volumen()
    print("el volumen:", volumen)
    area=piramide.area_superficial()
    print("area:",area)



















# ↓ Solución ↓


































# class Piramide:
#     def __init__(self, base_longitud, altura):
#         if base_longitud <= 0 or altura <= 0:
#             raise ValueError("base_longitud y altura deben ser positivos")
#         self.__base_longitud = base_longitud
#         self.__altura = altura

#     @property
#     def base_longitud(self):
#         return self.__base_longitud

#     @property
#     def altura(self):
#         return self.__altura

#     @base_longitud.setter
#     def base_longitud(self, nueva_base_longitud):
#         if nueva_base_longitud <= 0:
#             raise ValueError("La base_longitud debe ser positiva")
#         self.__base_longitud = nueva_base_longitud

#     @altura.setter
#     def altura(self, nueva_altura):
#         if nueva_altura <= 0:
#             raise ValueError("La altura debe ser positiva")
#         self.__altura = nueva_altura
    
#     def volumen(self):
#         return (self.base_longitud ** 2 * self.altura) / 3
    
#     def area_superficial(self):
#         area = self.base_longitud * (self.base_longitud + math.sqrt(4*self.altura**2 + (self.base_longitud/2)**2))
#         return area