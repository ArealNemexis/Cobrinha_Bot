import datetime
import discord
from discord.ext import commands
import random 
import requests

token_FILE = open('token.txt', 'r')

token = token_FILE.readline()


bot = commands.Bot(command_prefix='>>')
@bot.command()
async def ping(ctx):
    """Escreve 'Pong!'"""
    await ctx.send('Pong!')

@bot.command()
async def moeda(ctx):
    """Joga uma moeda e informa se foi cara ou coroa (completamente aleatorio)"""
    opc = ['Cara', 'Coroa']
    await ctx.send(random.choice(opc))

@bot.command()
async def aleatorio(ctx, arg1, arg2):
    """
    Escreve um numero entre os dois numeros inteiros passados
    >>aleatorio 3 6
    """
    try:
        await ctx.send(randint(int(arg1), int(arg2)))
    except:
        await ctx.send('Deu Bo')

@bot.command()
async def say(ctx,my,name):
    """
    >>say my name
    Informa o nome do autor da mensagem
    """
    if my == 'my' and name == 'name':
        nada = str(ctx.author)
        autor, oq = nada.split('#')
        await ctx.send(autor)
    else:
        await ctx.send('Deu Bo')

@bot.command()
async def time(ctx):
    """
    Informa a data e hora atual
    """
    now = datetime.datetime.now().strftime("Data: %d/%m/%Y Hora: %H:%M")
    print(now)
    await ctx.send(f'```{now}```')

@bot.command()
async def python(ctx, *args):
    """
    >>python import this
        escreve o louvor ao python
    
    >>python nosso
        escreve a oração do python
    """
    argumento = args
    if argumento[0] == 'import' and argumento[1] == 'this':
        await ctx.send('```DEUS ABENÇOE OS QUE PROGRAMAM EM PYTHON\nE TENHA PIEDADE DOS HEREGES QUE PROGRAMAM EM JAVA\nSOMENTE OS PYTHONICOS ASCENDERÃO AO REINO DAS COBRAS```')
    elif argumento[0] == 'nosso':
        await ctx.send('```Python nosso que estais no vscode\nSantificado seja Van Rossum\nVenha a nós o vosso código, seja feita a vossa vontade assim na Maratona como no Céu. O codigo nosso de cada dia nos dai hoje, perdoai-nos as nossas gambiarras assim como nós perdoamos a quem programa em Java, e não nos deixeis cair em tentação(PHP), mas livrai-nos do JavaScript. Amém```')
    else:
        await ctx.send("```\nBad arguments\n```")

@bot.command()
async def mussum(ctx):
    """
    Escreve a Mussum Ipsum
    """
    await ctx.send("```\nMussum Ipsum, cacilds vidis litro abertis. Admodum accumsan disputationi eu sit. Vide electram sadipscing et per. Delegadis gente finis, bibendum egestas augue arcu ut est. Quem num gosta di mim que vai caçá sua turmis! Viva Forevis aptent taciti sociosqu ad litora torquent.\n```")

@bot.command()
async def upper(ctx, *, arg):
    """
    Escreve o texto passado totalmente em caixa alta
    """
    await ctx.send(arg.upper())

@bot.command()
async def lower(ctx, *, arg):
    """
    Escreve o texto passado totalmente em caixa baixa
    """
    await ctx.send(arg.lower())
    
@bot.command()
async def covid(ctx):
    """Retorna os casos confirmados e mortes por covid-19 no Brasil"""
    r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil')
    r = dict(r.json())
    await ctx.send(f"```Pais: Brasil\nCasos confirmados: {r['data']['confirmed']}\nMortes: {r['data']['deaths']}\n#fiqueemcasa```")

@bot.command()
async def escreva(ctx, *, arg):
    """
    Escreve o texto passado
    """
    await ctx.send(arg)

@bot.command()
async def java(ctx):
    await ctx.send(f"voteban 1/5 {ctx.author}")

@bot.command()
async def doc(ctx, arg):
    """
    retorna o link de documentação do nome da linguagem passada
    """
    doc_dict = {
        'python':'Ja disse que te amo hoje?\nhttps://www.python.org/doc/versions/\nUsa e abusa da melhor linguagem do universo',
        'java':'JOGA ESSA PORRA FORA E ENTRA AQUI https://www.python.org/doc/versions/',
        'c':'Alguem ta chorando pra apc 2 aqui hein?\nhttps://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html',
        'javascript':'La vem o JSboy, vai me dizer que tem um newbettle e sai com rapazes também?\ntoma essa droga logo: https://devdocs.io/javascript/',
        'js':'La vem o JSboy, vai me dizer que tem um newbettle e sai com rapazes também?\ntoma essa droga logo: https://devdocs.io/javascript/',
        'php':'Mano para de usar droga na humilda, vou te passar só por que quem programa em PHP tem baixa capacidade cognitiva\nhttps://www.php.net/manual/pt_BR/',
        'brainfuck':'Na brisa na noia http://cocoadocs.org/docsets/Brainfuck/0.0.1/',
    }

    value = doc_dict.get(arg.lower(), 'Essa linguagem ai eu não assumo o BO de procurar não\nRecomendo essa daqui: https://www.python.org/doc/versions/')

    await ctx.send(value)



@bot.command()
async def teste(ctx):
    await ctx.send('```![Discord Logo](https://ddragon.leagueoflegends.com/cdn/10.8.1/img/champion/Alistar.png)```')
bot.run(token)
