import discord, datetime, random, json, requests, time #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos

### Stickers ###

def set_stk_channel(i_d, direccion):

    archivo = open(direccion, 'w') # Es la direccion del main.py, pero sumado el '/stk_channel.txt'

    archivo.write(str(i_d))

    archivo.close()

def retorno_id_canal(nombre_de_archivo): # Retorna la id que contiene el archivo indicado

        archivo = open(nombre_de_archivo, 'r')

        linea = archivo.readline()

        i_d = int(linea)

        return i_d

def archivo_stickers(direccion, url, tag):

    stk = open(direccion, 'a')

    contador = contador_archivos(direccion) + 1

    linea = str(contador) + ',' + url + "," + tag + '\n'

    stk.write(linea)

    stk.close()

def carga_stk(direccion, tag):

    archivo = open(direccion, 'r')

    linea = archivo.readline().strip()
    seg = linea.split(',')

    while linea != '' and seg[2] != tag:

        linea = archivo.readline().strip()
        seg = linea.split(',')

    archivo.close()

    return str(seg[1])

def lista_de_tags(direccion): # Arma una lista con los tags.

    archivo = open(direccion, 'r')

    linea = archivo.readline().strip()

    lista = 'Tags: - '

    while linea != '':

        seg = linea.split(',')

        lista = lista + seg[2] + ' - '

        linea = archivo.readline().strip()

    archivo.close()

    return lista

def array_stk(direccion): # Carga los datos del archivo en cuestión en una lista

    archivo = open(direccion, 'r')

    linea = archivo.readline().strip()

    lista = []

    while linea != '' :

        lista.append(linea)

        linea = archivo.readline().strip()

    archivo.close()

    return lista

def delete_stk(direccion, tag): # Borra un sticker y recarga el archivo.

    lista = array_stk(direccion)
    largo = len(lista)

    i = 0 # Contador
    SALIR = False


    while not SALIR or i < largo - 1:

        seg = lista[i].split(',')

        if seg[2] == tag:

            lista.remove(lista[i])
            SALIR = True

        i += 1

    if SALIR == True:

        archivo = open(direccion, 'w')

        largo = len(lista)

        for i in range(largo):

            linea = list[i]

            archivo.write(linea)

        archivo.close()

        mensaje = f'El tag "{tag}" fue erradicado...'

    else:

        mensaje = f'El tag "{tag}" no fue encontrado... raris...'

    return mensaje



### Embed ###

def embed_simple_msj(contenido, color):

    embed = discord.Embed(description = contenido, color = color)

    return embed

### Funciones Varias ###

def contador_archivos(nombre_de_archivo):

    archivo = open(nombre_de_archivo, 'r')

    linea = archivo.readline().strip()

    contador = 0

    while linea != '':

        linea = archivo.readline().strip()
        contador += 1

    return contador


### Cosas Random ###

algo_relleno = ('salame', 'rata', 'bld', 'rey', 'reina', 'zapallo', 'papa frita')

### Pruebas ###
direccion = './Servidores/Pruebas_921487305577996360'
#print(retorno_id_canal(direccion + '/stk_channel.txt'))