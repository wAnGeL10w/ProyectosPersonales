#Programa para dar de alta información de empleados/usuarios
import re

def validnom():
    #Lista para contener los nombres compuestos con la, el, del, etc
    exep_noms=["de","del","la","el"]
    #Busco las coincidencias de nombre que inicien con MAY y terminen con MIN
    while True:
        nom=input("Escribe el nombre: ")
        pat=re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+$")
        #res es una lista que guarda todas las councidencias (sin espacios en blanco)
        if re.match(pat,nom):
            #Hago todas las letras minúsculaa, después las iniciales mayuculas
            nom=nom.lower()
            #Por cada espacio que haya le añado una de las palabras ingresadas con un solo espacio
            #de separación
            nom = " ".join(nom.split())
            print("Nombre ingresado con éxito!\n")
            break
        else:
            print("Nombre inválido. Solo letras y espacios permitidos\n")
    #lista_nomb=pat.findall(nom)
    lista_nomb=nom.split()
    
    for pos in range(len(lista_nomb)):
        #Si el nombre no está en la lista de excepciones es porque porque es
        #nombre "normal" no compuesto y lo vuelvo capitalize
        if lista_nomb[pos] not in exep_noms:
            lista_nomb[pos]=lista_nomb[pos].capitalize()
    
    #Uno los elementos de la lista separados por un espacio para añadir el nombre
    nomb=" ".join(lista_nomb)
    return nomb

#Sirve si guardo la coincidencia con un formato distinto (con findall)
def impriminom(array):
    for i in range (len(array)):
        if i==len(array)-1:
            print(array[i])
        else:
            print(array[i],end=" ")

def validedad():
    while True:
        try:
            edad=int(input("Escriba la edad: "))
        except ValueError:
            print("Error de valor, intente de nuevo\n")
        else:
            #Solo personas mayores de edad
            if edad<18:
                continue
            else:
                break
    return edad

def validtel():
    while True:
        #Solicito la fecha en el formato indicado
        tel=input("Escribe el numero en el formato XX-XXXX-XXXX\n")
        pat=re.compile(r"\d{2}-\d{4}-\d{4}")
        if re.match(pat,tel):
            print("Teléfono añadido con éxito!")
            break
        else:
            print("Formato incorrecto, intenta de nuevo!\n")
    return tel

def validbiciesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def validfnac():
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    #Lista con los dias de cada mes
    dias_meses=[31,28,31,30,31,30,31,31,30,31,30,31]

    while True:
        fecha=input("Escribe la fecha de nacimiento en el formato DD/MM/YYYY\n")
        pat=re.compile(r"([0][1-9]|[1-2][0-9]|[3][0-1])/([0][1-9]|[1][1-2])/([19][6-9][0-9]|[20][0-2][0-5])")
        if re.match(pat,fecha):
            #Variable para dividir los datos en distintos grupos y trabajar con ellos
            fecha_div=pat.search(fecha)
            #Asigno valores a variables que me servirán p
            dia=int(fecha_div.group(1))
            mes=int(fecha_div.group(2))
            año=int(fecha_div.group(3))

            if mes == 2:
                if validbiciesto(año):
                    #Porque si es biciesto
                    if 1<=dia<=29:
                        break
                    else:
                        print("Dia no válido para Febrero en año biciesto\n")
                else:
                    #Si no es biciesto
                    if 1<=dia<=28:
                        break
                    else:
                        print("Dia no valido para Febrero en año no biciesto\n")
            else:
                #Para todos los meses que no sean febrero
                if 1<=dia<=dias_meses[mes-1]:
                    break
                else:
                    print(f"Dia no valido para el mes de {meses[mes-1]}\n")    
        #En caso de que ningún formato coincida                
        else:
            print("Formato no valido, vuelve a intentar\n")
    return fecha

def validestado():
    entidades_curp={
    "AGUASCALIENTES": "AS",
    "BAJA CALIFORNIA": "BC",
    "BAJA CALIFORNIA SUR": "BS",
    "CAMPECHE": "CC",
    "COAHUILA": "CL",
    "COLIMA": "CM",
    "CHIAPAS": "CS",
    "CHIHUAHUA": "CH",
    "CIUDAD DE MEXICO": "DF",
    "DURANGO": "DG",
    "GUANAJUATO": "GT",
    "GUERRERO": "GR",
    "HIDALGO": "HG",
    "JALISCO": "JC",
    "MEXICO": "MC",  # Estado de México
    "MICHOACAN": "MN",
    "MORELOS": "MS",
    "NAYARIT": "NT",
    "NUEVO LEON": "NL",
    "OAXACA": "OC",
    "PUEBLA": "PL",
    "QUERETARO": "QT",
    "QUINTANA ROO": "QR",
    "SAN LUIS POTOSI": "SP",
    "SINALOA": "SL",
    "SONORA": "SR",
    "TABASCO": "TC",
    "TAMAULIPAS": "TS",
    "TLAXCALA": "TL",
    "VERACRUZ": "VZ",
    "YUCATAN": "YN",
    "ZACATECAS": "ZS",
    # Nacidos en el extranjero
    "NACIDO EN EL EXTRANJERO": "NE"
}
    while True:
        estado=input("Escribe el estado en mayusculas sin acentos: ").strip().upper()
        #Si el estado pertenece al diccionario de estados
        if estado in entidades_curp:
            #Guardo su clave para usarla después para validar el CURP
            cve_estado=entidades_curp[estado]
            break
        else:
            print("El estado no pertenece a México, intenta de nuevo\n")
    return cve_estado

def validsexo():
    generos={
        "MASCULINO":"H",
        "FEMENINO":"M",
        "HOMBRE":"H",
        "MUJER":"M"
    }
    while True:
        sexo=input("Ingrese su sexo en mayusculas: ").strip().upper()
        #Si el sexo pertenece al diccionario de generos
        if sexo in generos:
            cve_sexo=generos[sexo]
            break
        else:
            print("Género no valido, intente de nuevo\n")
    return cve_sexo

#Me falta completar y mejorar esta función
def validcurp(nombre,fecha):
    exep_noms=["de","del","la","el"]
    estados=[]
    #Nombre es la cadena de caracteres y apoyo es una lista con los nombres y apellidos de la persona
    apoyo=nombre.split(" ")
    #Si existe alguna coincidencia
    '''FALTA MODIFICAR IF Y ELSE'''
    if set(exep_noms) & set(apoyo):
        cve_estado=validestado()
        cve_sexo=validsexo()
        print()
    else:
        cve_estado=validestado()
        cve_sexo=validsexo()
        print()
    return None

def validcorreo():
    #Posibles dominios que pueda escribir el usuario
    dominios=["com","not","org","edu","ngo","mx"]
    while True:
        email=input("Escribe el correo: ")
        pat=re.compile(r"^\w+@[a-zA-Z0-9.-]+\.[a-z]{2,}$")
        if re.match(pat,email):
            datos=email.split("@")
            dominio=datos[1].split(".")
            #Yo se que en esta posicion viene ya sea hotmail, gmail, etc
            correo=dominio.pop(0)
            if set(dominios) & set(dominio):
                email=datos[0]+"@"+correo+"."+".".join(dominio)
            else:
                print("Alguno de los dominios no es valido\n")
                continue
            break
        else:
            print("Formato no valido para el correo\n")
    return email

'''Cosas que me faltan validar en funciones:
    -CURP (en proceso)
    -Cve empleado (un numero entero y ya)
'''