import discord, datetime, random, json, requests, time, os #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
from funciones import *

bot = commands.Bot(command_prefix = '_')

@bot.event
async def on_message(message):

    ### Variables ###
    direccion = './Servidores/' + str(message.guild.name) + '_' + str(message.guild.id)
    direccion_archivo_de_stks = direccion + '/users/stks_' + str(message.author)+ '_' + str(message.author.id)+ '_.txt' # Es la dirección donde se encuentra el archivo del usuario en cuestión.
    id_canal = message.channel.id

    if not os.path.exists('Servidores'):
        os.mkdir('Servidores')

    if not os.path.exists(direccion): # Prepara la carpeta en caso de que no exista

        os.mkdir(direccion)
        os.mkdir(direccion + '/users')


    if message.author.id == message.guild.owner_id and message.content.startswith('set_stk_channel:'): # Setea el Canal de stickers, si el mensaje lo envía quien sea propietarie del server.

        await message.delete()

        set_stk_channel(id_canal, (direccion + '/stk_channel.txt'))
        embed = embed_simple_msj('Canal Seteado!', 0xb1b36f)

        await message.channel.send(embed = embed)

    elif os.path.exists(direccion + '/stk_channel.txt'): # Si existe el archivo que contiene la id del canal. Este es el nido de if's para stickers.

        if message.content.startswith('stk'): # Comandos de Stickers

            if message.content.startswith('stk:'): # Envía el stk.

                trash, tag = message.content.split(':')

                link = carga_stk(direccion_archivo_de_stks, tag)

                await message.delete()

                embed = discord.Embed(color = 0xff9900, url = 'https://www.instagram.com/traduxionesvaratas/', title = 'Sticker Bot')
                embed.set_image(url = link)

                await message.channel.send(embed = embed)

            elif message.content.startswith('stk_lista:'): # Envía la lista de tags disponibles.

                await message.delete()

                lista = lista_de_tags(direccion_archivo_de_stks)

                embed = embed_simple_msj(lista, 0x0823FF)

                await message.channel.send(embed = embed)

            elif message.content.startswith('stk_delete:'): # Borra un stk.

                if len(message.content.split(':')) == 2:

                    await message.delete()

                    trash, tag = message.content.split(':')

                    contenido = delete_stk(direccion_archivo_de_stks, tag)

                    mensaje = embed_simple_msj(contenido, 0x999999)

                    await message.channel.send(embed = mensaje)

        elif id_canal == retorno_id_canal(direccion + '/stk_channel.txt') and not message.author.bot: # Carga los stickers

            if not os.path.exists(direccion_archivo_de_stks):
                archivo_temporal = open(direccion_archivo_de_stks, 'x')
                archivo_temporal.close()

            if contador_archivos(direccion_archivo_de_stks) > 10:
                embed = embed_simple_msj(f'Ya llegaste al límite homie...', 0xCC20AF)
                await message.channel.send(embed = embed)

            elif message.content == '':
                embed = embed_simple_msj(f'Te falto ponerle la etiqueta {algo_relleno[random.randint(0, (len(algo_relleno) - 1))]}!', 0xCC20AF)
                await message.channel.send(embed = embed)

            elif len(message.attachments) >= 1:
                url = str(message.attachments[0])
                tag = str(message.content)
                archivo_stickers(direccion_archivo_de_stks, url, tag)



###  Comandos para el bot  ###


bot.run('ssss')

