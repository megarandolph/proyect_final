import sys
import marshal
import os
import requests
import json
from string import Template
from numpy import *
import collections

class pokemon():
    nombre= ""
    fdia= ""
    fmes= ""
    fresta= ""
    latitud= ""
    longitud= ""
    comidaf= ""
    tipods= ""
    fano= ""
    tipo= ""
    signo=""
    img=""

pokemones= []


try:
    ñ =open("datos.dat","br")
    et= marshal.load(ñ)
    for z in et:
        b= pokemon()
        b.nombre= z[0]
        b.fdia= z[1]
        b.fmes=z[2]
        b.fresta=z[3]
        b.latitud= z[4]
        b.longitud= z[5]
        b.comidaf= z[6]
        b.tipods= z[7]
        b.fano= z[8]
        b.tipo=z[9]
        b.signo=z[10]
        b.img=z[11]
        pokemones.append(b)
    ñ.close()
    print("Se encontraron",len(pokemones),"pokemones")
except EOFError:
    print("No hay datos..")

def menu():
    print("Programa Especializados en Pokemones")
    print("1 - Agregar Pokemon")
    print("2 - Ver Pokemones")
    print("3 - Reportes")
    print("4 - Exportar Pokemon")
    print("5 - Exportar Mapa")
    print("6 - Salir")
    et= input("Ingresa a donde quieres ir: ")
    if (et== "1"):
        agregarpokemon()
    elif (et== "2"):
        verpokemones()
    elif (et== "3"):
        reportes()
    elif (et== "4"):
        exportarP()
    elif (et== "5"):
        exportarM()
    elif (et== "6"):
        datos=[]
        for b in pokemones:
            p=[]
            p.append(b.nombre)
            p.append(b.fdia)
            p.append(b.fmes)
            p.append(b.fresta)
            p.append(b.latitud)
            p.append(b.longitud)
            p.append(b.comidaf)
            p.append(b.tipods)
            p.append(b.fano)
            p.append(b.tipo)
            p.append(b.signo)
            p.append(b.img)

            datos.append(p)
    
        a= open("datos.dat","bw")
        marshal.dump(datos,a)
        a.close()
        print("Bye Bye")
        sys.exit()
        
    else:
        print("introduzca una opcion valida")
        menu()

url_api = 'https://pokeapi.co/api/v2/pokemon/'
def get_pokemon_data(url_pokemon= ''):
    pokemon_data = {
        "name": '',
        "types": ""
    }

    response = requests.get(url_pokemon)
    data = response.json()
    try:
        pokemon_data['name'] = data['name']
        pokemon_data['types'] = data['types']
        return pokemon_data
    except:
        print("Agrege un nombre valido")
        agregarpokemon()


    
def agregarpokemon():
    print("Agregar un pokemon")
    b= pokemon()
    b.nombre=input("Digite el nombre de el pokemon: ")
    
    pokemon_data_url = url_api + b.nombre
    data = get_pokemon_data(pokemon_data_url)

    pokemon_type = [types['type']['name'] for types in data['types']]
    name = ("".join([name for name in data['name']]))

    if b.nombre == name:
        print("nombre pokemon valido")
    else:
        print("Agrege un nombre valido")
        agregarpokemon()

    b.fdia=int(input("Digite su dia de nacimiento: "))
    b.fmes=int(input("Digite su mes de nacimiento(numero de Mes): "))
    if ((b.fmes==1) and (b.fdia>=20)) or ((b.fmes==2) and (b.fdia<=18)):
        b.signo = ("Acuario")
    if ((b.fmes==2) and (b.fdia>=19)) or ((b.fmes==3) and (b.fdia<=20)):
        b.signo = ("Piscis")
    if ((b.fmes==3) and (b.fdia>=21)) or ((b.fmes==4) and (b.fdia<=19)):
        b.signo = ("Aries")
    if ((b.fmes==4) and (b.fdia>=20)) or ((b.fmes==5) and (b.fdia<=20)):
        b.signo = ("Tauro")
    if ((b.fmes==5) and (b.fdia>=21)) or ((b.fmes==6) and (b.fdia<=20)):
        b.signo = ("Gemenis")
    if ((b.fmes==6) and (b.fdia>=21)) or ((b.fmes==7) and (b.fdia<=22)):
        b.signo= ("Cancer")
    if ((b.fmes==7) and (b.fdia>=23)) or ((b.fmes==8) and (b.fdia<=22)):
        b.signo = ("Leo")
    if ((b.fmes==8) and (b.fdia>=23)) or ((b.fmes==9) and (b.fdia<=22)):
        b.signo = ("Virgo")
    if ((b.fmes==9) and (b.fdia>=23)) or ((b.fmes==10) and (b.fdia<=22)):
        b.signo = ("Libra")
    if ((b.fmes==10) and (b.fdia>=23)) or ((b.fmes==11) and (b.fdia<=21)):
        b.signo = ("Escorpio")
    if ((b.fmes==11) and (b.fdia>=22)) or ((b.fmes==12) and (b.fdia<=21)):
        b.signo = ("Sagitario")
    if ((b.fmes==12) and (b.fdia>=22)) or ((b.fmes==1) and (b.fdia<=19)):
        b.signo = ("Capricornio")
    b.signo
    b.fresta=int(input("Digite su año de nacimiento: ")) 
    b.latitud=input("Digite la latitud (donde fue encontrado): ")
    b.longitud=input("Digite la longitud (donde fue encontrado): ")
    b.comidaf=input("Indroduzca su comida favorita: ")
    b.tipods=input("Introduzca su tipo de sangre: ")
    edad= int(2018-b.fresta)
    b.fano= (edad)
    b.tipo= (", ".join(pokemon_type))
    b.img= (b.nombre+".jpg")

    pokemones.append(b)
    input("Presione para regresar al menu")
    menu()

def verpokemones():
    print("Existen",len(pokemones),"pokemones")
    for b in pokemones:
        print("""Nombre: """+str(b.nombre)+"""\n Dia: """+str(b.fdia)+"""\n Mes: """+str(b.fmes)+"""\n Año: """+str(b.fresta)+"""\n Tipo de sangre: """+str(b.tipods)+"""\n Signo zodiacal: """+str(b.signo)+"""\n Tipo de pokemon: """+str(b.tipo)+"""\n""")
    input("Presione enter para regresar al menu")
    menu()

def reportes():
    print("Reportes")
    print("\n1 - Cumpleaños por mes")
    print("2 - Tipos de pokemones")
    print("3 - Comida por tipo")
    print("4 - menu")
    et= input("Ingresa a donde quieres ir: ")
    if (et== "1"):
        cumplemes()
    elif (et== "2"):
        portipo()
    elif (et== "3"):
        porcomida()
    elif (et== "4"):
        menu()

def cumplemes():
    for b in pokemones:
        l=int(input("Digite el mes:"))
        if l == b.fmes:
            veces= pokemones.count(b.fmes)
            print("""\nCumpleaños en el mes: """+str(b.fmes)+"""=>"""+str(b.nombre))

    input("Enter para regresar a reporte")
    reportes()

def portipo():
    for b in pokemones:
        veces= pokemones.count('b.tipo')
        print("""\nLos tipos que tenemos son: """+str(b.tipo)+"""="""+str(veces+1))
    input("Enter para regresar a reportes")
    reportes()

def porcomida():
    for b in pokemones:
        print("""\nComida por tipo: """+str(b.tipo)+"""=>"""+str(b.comidaf))
    
    input("Enter para regresar a reportes")
    reportes()

        
def exportarP():
    input("Enter para guardar y exportar los pokemones ")

    plantilla= file_get_contents("prueba.html")
    final=[]
    for b in pokemones:
        et= """ <tr>
        <td>"""+str(b.nombre)+"""</td> <td>"""+str(b.fdia)+"""</td> <td>"""+str(b.fmes)+"""</td>
        <td>"""+str(b.fresta)+"""</td> <td>"""+str(b.signo)+"""</td> <td>"""+str(b.fano)+"""</td><td><img height="250" width="450" src="pokemon718/ """+str(b.img)+""""></td></tr> """
        final.append(et)

    sep= " "
    e = sep.join(final)
    plantilla = plantilla.replace('{TABLA}', e)

    f = open ("pokemones.html","w")
    f.writelines(plantilla)
    f.close()

    input("Enter para regresar al menu")
    menu()

def file_get_contents(filename):
    if os.path.exists(filename):
        fp= open(filename,"r")
        content = fp.read()
        fp.close
        return content

def exportarM():
    input("Enter para guardar y exportar el mapa")

    plantilla= file_get_contents("ejemplo.html")
    final=[]
    for b in pokemones:
        et= """ L.marker(["""+str(b.latitud)+""","""+str(b.longitud)+"""])
            .addTo(map)
            .bindPopup('"""+str(b.nombre)+""",\t y su edad es """+str(b.fano)+"""\t a&ntildeos'); """
        final.append(et)

    sep= " "
    e = sep.join(final)
    plantilla = plantilla.replace('{MARCADORES}', e)

    f = open ("mapa.html","w")
    f.writelines(plantilla)
    f.close()

    input("Enter para regresar al menu")
    menu()

    
menu()
