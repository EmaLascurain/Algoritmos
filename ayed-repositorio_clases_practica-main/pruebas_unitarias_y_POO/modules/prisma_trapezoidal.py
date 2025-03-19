import math

class PrismaTrapezoidal:
    def __init__ (self, base_menor,base_mayor, lado, altura_trapecio, altura_prisma):
        if base_menor<=0 or base_mayor<=0 or lado <=0 or altura_trapecio <=0 or altura_prisma<=0:
            raise ValueError("Los valores deben ser positivos")
        self.__base_menor=base_menor
        self.__base_mayor=base_mayor
        self.__lado=lado
        self.__altura_trapecio=altura_trapecio
        self.__altura_prisma=altura_prisma
    
    @property
    def base_menor(self):
        return self.__base_menor
    @property
    def base_mayor(self):
        return self.__base_mayor
    @property
    def lado(self):
        return self.__lado
    @property
    def altura_trapecio(self):
        return self.__altura_trapecio
    @property
    def altura_prisma(self):
        return self.__altura_prisma
    def volumen(self):
        return((((self.__base_mayor+self.__base_menor)/2)*3)*self.__altura_prisma)
    def area_superficial(self):
        return((self.__base_mayor+self.__base_menor)*self.__altura_trapecio)+(self.__base_mayor+self.__base_menor+self.__lado*2)*self.__altura_prisma

# Área = (B + b)*h + (B + b + 2d)*H
        # (8+4)*3 + (8+4+2*5)*10 = 36 + (22)*10 = 36 + 220 = 256
















































# class PrismaTrapezoidal:
#     def __init__(self, base_mayor, base_menor, lado, altura_trapecio, altura_prisma):
#         if base_mayor <= 0 or base_menor <= 0 or lado <= 0 or altura_trapecio <= 0 or altura_prisma <= 0:
#             raise ValueError("Todos los valores deben ser positivos")
#         self.base_mayor = base_mayor
#         self.base_menor = base_menor
#         self.lado = lado
#         self.altura_trapecio = altura_trapecio
#         self.altura_prisma = altura_prisma
    
#     def volumen(self):
#         return (((self.base_mayor + self.base_menor) / 2) * self.altura_trapecio) * self.altura_prisma
    
#     def area_superficial(self):
#         return (self.base_mayor + self.base_menor) * self.altura_trapecio + (self.base_mayor + self.base_menor + 2 * self.lado) * self.altura_prisma