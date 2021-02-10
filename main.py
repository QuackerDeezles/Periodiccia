import discord
import keep_alive
import os
import random

from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = 'p ')
status = cycle([f'p help = Help Command', 'https://bit.ly/39O9N7t'])
client.remove_command('help')

helpMenuDesc = """
`p help` - Shows this!
`p <element_symbol>` - Gives information about an element
`p list <page_number>` - Reference to symbols to use for the element commands **There are 12 pages btw**
`p table` - Shows the whole periodic table
`p mendeleev` -  This command tells you a bit about who Mendeleev is, and some helpful resources to learn about him.
`p socials` - Use this command to see the social accounts of the developer!
`p devbio` - Use this command to learn about QuackerDeezlesYT, the developer of me! **There are 3 pages btw**
`p botsite` - Periodiccia website, just made!
`p vote` - Please vote Periodiccia on top.gg and Discord Bot List!

**Join our official server!** https://bit.ly/3b4JbPd or `p server`.

**It would be very appreciated if you could invite my bot to your server! :slight_smile:**
https://bit.ly/39O9N7t

**There are some hidden commands in this bot. If you find a specific one, it will give you all the other ones! :smirk:**
Hope you find them!

**Made by QuackerDeezlesYT#3393**
If you have any questions, feel free to DM him!
"""
@client.command(aliases=['huh', 'what'])
async def help(ctx):
  em = discord.Embed(title = 'Welcome to Periodiccia!', description = helpMenuDesc, color = discord.Color.purple())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  await ctx.send(embed = em)

@client.event
async def on_ready():
  change_status.start()
  print("The bot is ready!")

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

@client.command(aliases=['elements'])
async def list(ctx, page = 1):
  if page == 1:

    em = discord.Embed(title = 'List of the Elements', description = 'Hydrogen (`H`)\nHelium (`He`)\nLithium (`Li`)\nBeryllium (`Be`)\nBoron (`B`)\nCarbon (`C`)\nNitrogen (`N`)\nOxygen (`O`)\nFlourine (`F`)\nNeon (`Ne`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 2:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Sodium (`Na`)\nMagnesium (`Mg`)\nAluminum (`Al`)\nSilicon (`Si`)\nPhosphorus (`P`)\nSulfur (`S`)\nChlorine (`Cl`)\nArgon (`Ar`)\nPotassium (`K`)\nCalcium (`Ca`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 3:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Scandium (`Sc`)\nTitanium (`Ti`)\nVanadium (`V`)\nChromium (`Cr`)\nManganese (`Mn`)\nIron (`Fe`)\nCobalt (`Cu`)\nNickel (`Ni`)\nCopper (`Co`)\nZinc (`Zn`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 4:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Gallium (`Ga`)\nGermanium (`Ge`)\nArsenic (`As`)\nSelenium (`Se`)\nBromine (`Br`)\nKyrpton (`Kr`)\nRibidium (`Rb`)\nStrontium (`Sr`)\nYttrium (`Y`)\nZirconium (`Zr`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 5:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Niobium (`Nb`)\nMolybdenum (`Mo`)\nTechnetium (`Tc`)\nRuthenium (`Ru`)\nRhodium (`Rh`)\nPalladium (`Pd`)\nSilver (`Ag`)\nCandium (`Cd`)\nIndium (`In`)\nTin (`Sn`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 6:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Antimony (`Sb`)\nTellurium (`Te`)\nIodine (`I`)\nXenon (`Xe`)\nCaesium (`Cs`)\nBarium (`Ba`)\nLanthanum (`La`)\nCerium (`Ce`)\nPraseodymium (`Pr`)\nNeondymium (`Nd`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 7:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Prothemium (`Pm`)\nSamarium (`Sm`)\nEuropium (`Eu`)\nGadolinium (`Gd`)\nTerbium (`Tb`)\nDysprosium (`Dy`)\nHolmium (`Ho`)\nErbium (`Er`)\nThulium (`Tm`)\nYtterbium (`Yb`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 8:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Lutetium (`Lu`)\nHafnium (`Hf`)\nTantalum (`Ta`)\nTungsten (`W`)\nRhenium (`Re`)\nOsmium (`Os`)\nIridium (`Ir`)\nPlatinum (`Pt`)\nGold (`Au`)\nMercury (`Hg`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 9:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Thallium (`Tl`)\nLead (`Pb`)\nBismuth (`Bi`)\nPolonium (`Po`)\nAstatine (`At`)\nRadon (`Rn`)\nFrancium (`Fr`)\nRadium (`Ra`)\nActinium (`Ac`)\nThorium (`Th`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 10:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Protactinium (`Pa`)\nUranium (`U`)\nNeptunium (`Np`)\nPlutonium (`Pu`)\nAmericium (`Am`)\nCurium (`Cm`)\nBerkelium (`Bk`)\nCalifornium (`Cf`)\nEinsteinium (`Es`)\nFermium (`Fm`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 11:
    
    em = discord.Embed(title = 'List of the Elements', description = 'Mendelevium (`Md`)\nNobelium (`No`)\nLawrencium (`Lr`)\nRutherfordium (`Rf`)\nDubnium (`Db`)\nSeaborgium (`Sg`)\nBohrium (`Bh`)\nHassium (`Hs`)\nMeitnerium (`Mt`)\nDarmstadtium (`Ds`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 12:

    em = discord.Embed(title = 'List of the Elements', description = 'Roentgenium (`Rg`)\nCopernicium (`Cn`)\nNihonium (`Nh`)\nFlerovium (`Fl`)\nMoscovium (`Mc`)\nLivermorium (`Lv`)\nTennessine (`Ts`)\nOganesson (`Og`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)

@client.command()
async def Ve(ctx):
  em = discord.Embed(title = '**VERITASIUM**', description = 'Mass of KNOWLEDGE, YouTube Channel =\n https://www.youtube.com/user/1veritasium', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807399043822518323.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def H(ctx):
  em = discord.Embed(title = '**Hydrogen**', description = '1st Element, Mass of 1.008', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806237831613775885.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def He(ctx):
  em = discord.Embed(title = '**Helium**', description = '2nd Element, Mass of 4.0026, **Noble Gas**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806566745980665926.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Li(ctx):
  em = discord.Embed(title = '**Lithium**', description = '3rd Element ,Mass of 6.94, **Alkali Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806567984415768678.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Be(ctx):
  em = discord.Embed(title = '**Beryllium**', description = '4th Element, Mass of 9.0122, **Alkaline Earth Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806569567593168906.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def B(ctx):
  em = discord.Embed(title = '**Boron**', description = '5th Element, Mass of 10.81, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806572191826968656.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def C(ctx):
  em = discord.Embed(title = '**Carbon**', description = '6th Element, Mass of 12.011, **Nonmetal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806609579890835466.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def N(ctx):
  em = discord.Embed(title = '**Nitrogen**', description = '7th Element, Mass of 14.077, **Nonmetal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610043762901042.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def O(ctx):
  em = discord.Embed(title = '**Oxygen**', description = '8th Element, Mass of 15.999, **Nonmetal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610357668937748.png?v=1' )
  await ctx.send(embed = em)

@client.command()
async def F(ctx):
  em = discord.Embed(title = '**Flourine**', description = '9th Element, Mass of 18.998, **Halogen**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610601761570836.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ne(ctx):
  em = discord.Embed(title = '**Neon**', description = '10th Element, Mass of 20.180, **Noble Gas**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806611638672949269.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Na(ctx):
  em = discord.Embed(title = '**Sodium**', description = '11th Element, Mass of 22.990, **Alkali Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806611195548794912.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mg(ctx):
  em = discord.Embed(title = '**Magnesium**', description = '12th Element, Mass of 23.405, **Alkaline Earth Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612129914159114.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Al(ctx):
  em = discord.Embed(title = '**Aluminum**', description = '13th Element, Mass of 26.982, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612299808636948.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Si(ctx):
  em = discord.Embed(title = '**Silicon**', description = '14th Element, Mass of 28.085, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612488745386004.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def P(ctx):
  em = discord.Embed(title = '**Phosphorus**', description = '15th Element, Mass of 30.974, **Nonmetal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612670932975646.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def S(ctx):
  em = discord.Embed(title = '**Sulfur**', description = '16th Element, Mass of 32.06, **Nonmetal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612864936181811.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cl(ctx):
  em = discord.Embed(title = '**Chlorine**', description = '17th Element, Mass of 32.06, **Halogen**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806613436347187250.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ar(ctx):
  em = discord.Embed(title = '**Argon**', description = '18th Element, Mass of 39.948, **Noble Gas**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806613620657750086.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def K(ctx):
  em = discord.Embed(title = '**Potassium**', description = '19th Element, Mass of 39.098, **Alkali Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628580200939551.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ca(ctx):
  em = discord.Embed(title = '**Calcium**', description = '20th Element, Mass of 40.078, **Alkaline Earth Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628602259046480.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sc(ctx):
  em = discord.Embed(title = '**Scandium**', description = '21th Element, Mass of 44.956, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628627847708683.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ti(ctx):
  em = discord.Embed(title = '**Titanium**', description = '22th Element, Mass of 47.867, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628650354475089.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def V(ctx):
  em = discord.Embed(title = '**Vanadium**', description = '23th Element, Mass of 50.942, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628668347777024.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cr(ctx):
  em = discord.Embed(title = '**Chromium**', description = '24th Element, Mass of 51.996, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630723296952330.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mn(ctx):
  em = discord.Embed(title = '**Manganese**', description = '25th Element, Mass of 54.938, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630771581779988.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fe(ctx):
  em = discord.Embed(title = '**Iron**', description = '26th Element, Mass of 55.845, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630803467141151.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Co(ctx):
  em = discord.Embed(title = '**Cobalt**', description = '27th Element, Mass of 58.933, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630849117814845.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ni(ctx):
  em = discord.Embed(title = '**Nickel**', description = '28th Element, Mass of 58.693, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630871225860106.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cu(ctx):
  em = discord.Embed(title = '**Copper**', description = '29th Element, Mass of 63.546, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639082914054184.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Zn(ctx):
  em = discord.Embed(title = '**Zinc**', description = '30th Element, Mass of 65.38, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639415828938802.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ga(ctx):
  em = discord.Embed(title = '**Gallium**', description = '31th Element, Mass of 69.723, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639435323539496.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ge(ctx):
  em = discord.Embed(title = '**Germanium**', description = '32th Element, Mass of 72.63, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639480726880268.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def As(ctx):
  em = discord.Embed(title = '**Arsenic**', description = '33th Element, Mass of 74.922, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639501648330765.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Se(ctx):
  em = discord.Embed(title = '**Selenium**', description = '34th Element, Mass of 78.97, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806736485788287027.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Br(ctx):
  em = discord.Embed(title = '**Bromine**', description = '35th Element, Mass of 79.004, **Halogen**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806737203832160336.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Kr(ctx):
  em = discord.Embed(title = '**Krypton**', description = '36th Element, Mass of 83.80, **Noble Gas**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806737863960952862.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Rb(ctx):
  em = discord.Embed(title = '**Rubidium**', description = '37th Element, Mass of 85.468, **Alkali Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738015644418078.png?v=1')
  await ctx.send(embed = em)
  
@client.command()
async def Sr(ctx):
  em = discord.Embed(title = '**Strontium**', description = '38th Element, Mass of 87.62, **Alkaline Earth Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738197517959169.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Y(ctx):
  em = discord.Embed(title = '**Yttrium**', description = '39th Element, Mass of 88.906, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738408671019018.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Zr(ctx):
  em = discord.Embed(title = '**Zirconium**', description = '40th Element, Mass of 91.224, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738696300527656.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Nb(ctx):
  em = discord.Embed(title = '**Niobium**', description = '41th Element, Mass of 92.906, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738922637099018.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mo(ctx):
  em = discord.Embed(title = '**Molybdenum**', description = '42th Element, Mass of 95.95, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806739137947369502.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tc(ctx):
  em = discord.Embed(title = '**Technetium**', description = '43th Element, Mass of 98, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806739458296381500.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ru(ctx):
  em = discord.Embed(title = '**Ruthenium**', description = '44th Element, Mass of 101.07, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806740984279859220.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Rh(ctx):
  em = discord.Embed(title = '**Rhodium**', description = '45th Element, Mass of 102.91, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806741372124004372.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pd(ctx):
  em = discord.Embed(title = '**Palladium**', description = '46th Element, Mass of 106.42, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806741800853307392.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ag(ctx):
  em = discord.Embed(title = '**Silver**', description = '47th Element, Mass of 107.87, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742042054099025.png?v=1')
  await ctx.send(embed = em)
  
@client.command()
async def Cd(ctx):
  em = discord.Embed(title = '**Cadmium**', description = '48th Element, Mass of 112.41, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742338411298887.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def In(ctx):
  em = discord.Embed(title = '**Indium**', description = '49th Element, Mass of 114.52, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806745134343520317.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sn(ctx):
  em = discord.Embed(title = '**Tin**', description = '50th Element, Mass of 118.71, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806743088475144213.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sb(ctx):
  em = discord.Embed(title = '**Antimony??????**', description = '51th Element, Mass of 121.76, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806743967370182689.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Te(ctx):
  em = discord.Embed(title = '**Tellerium**', description = '52th Element, Mass of 127.60, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806744271704031242.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def I(ctx):
  em = discord.Embed(title = '**Iodine**', description = '53th Element, Mass of 126.90, **Halogen**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742859163631626.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Xe(ctx):
  em = discord.Embed(title = '**Xenon**', description = '54th Element, Mass of 131.29, **Noble Gases**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806745520797384764.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cs(ctx):
  em = discord.Embed(title = '**Cesium**', description = '55th Element, Mass of 132.91, **Alkali Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746036362149939.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ba(ctx):
  em = discord.Embed(title = '**Barium**', description = '56th Element, Mass of 137.33, **Alkaline Earth Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746477622722610.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def La(ctx):
  em = discord.Embed(title = '**Lanthanium**', description = '57th Element, Mass of 138.91, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746907807318016.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ce(ctx):
  em = discord.Embed(title = '**Cerium**', description = '58th Element, Mass of 140.12, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747109360795649.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pr(ctx):
  em = discord.Embed(title = '**Praseodymium**', description = '59th Element, Mass of 140.91, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747420624027718.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Nd(ctx):
  em = discord.Embed(title = '**Neodynium**', description = '60th Element, Mass of 144.25, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747639017766922.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pm(ctx):
  em = discord.Embed(title = '**Promethium**', description = '61th Element, Mass of 145, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954923534712854.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sm(ctx):
  em = discord.Embed(title = '**Samarium**', description = '62th Element, Mass of 150.36, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954959626567710.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Eu(ctx):
  em = discord.Embed(title = '**Europium**', description = '63th Element, Mass of 151.96, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954988865585172.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Gd(ctx):
  em = discord.Embed(title = '**Gadolinium (for geometry dash players)**', description = '64th Element, Mass of 157.25, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806955066371473459.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tb(ctx):
  em = discord.Embed(title = '**Terbium**', description = '65th Element, Mass of 158.93, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806955083731828737.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Dy(ctx):
  em = discord.Embed(title = '**Dysprosium**', description = '66th Element, Mass of 162.50, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956618608148537.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ho(ctx):
  em = discord.Embed(title = '**Holmium**', description = '67th Element, Mass of 164.93, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956660878082139.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Er(ctx):
  em = discord.Embed(title = '**Erbium**', description = '68th Element, Mass of 167.26, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956695682809897.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tm(ctx):
  em = discord.Embed(title = '**Thulium**', description = '**69**th Element :smirk:, Mass of 168.93, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956747393597441.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Yb(ctx):
  em = discord.Embed(title = '**Ytterbium**', description = '70th Element, Mass of 173.05, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956775248101387.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Lu(ctx):
  em = discord.Embed(title = '**Lutetium**', description = '71th Element, Mass of 174.94, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959504725246012.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Hf(ctx):
  em = discord.Embed(title = '**Hafnium**', description = '72th Element, Mass of 178.49, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959523256336425.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ta(ctx):
  em = discord.Embed(title = '**Tantalum**', description = '73th Element, Mass of 180.95, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959549986635807.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def W(ctx):
  em = discord.Embed(title = '**Tungsten BIG W POG**', description = '74th Element, Mass of 183.84, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959566642085888.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Re(ctx):
  em = discord.Embed(title = '**Rhenium**', description = '75th Element, Mass of 186.21, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959608748441620.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Os(ctx):
  em = discord.Embed(title = '**Osmium**', description = '76th Element, Mass of 190.23, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962799565340692.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ir(ctx):
  em = discord.Embed(title = '**Iridium**', description = '77th Element, Mass of 192.22, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962871555850352.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pt(ctx):
  em = discord.Embed(title = '**Platinum**', description = '78th Element, Mass of 195.08, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962912220151829.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Au(ctx):
  em = discord.Embed(title = '**Gold**', description = '79th Element, Mass of 196.97, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962930531696650.png?v=1')
  await ctx.send(embed = em)
  
@client.command()
async def Hg(ctx):
  em = discord.Embed(title = '**Mercury**', description = '80th Element, Mass of 200.59, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962950479806577.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tl(ctx):
  em = discord.Embed(title = '**Thallium**', description = '81th Element, Mass of 204.38, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994333910827028.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pb(ctx):
  em = discord.Embed(title = '**Lead**', description = '82th Element, Mass of 207.2, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994370648735784.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Bi(ctx):
  em = discord.Embed(title = '**Bismuth**', description = '83th Element, Mass of 208.98, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994390026682398.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Po(ctx):
  em = discord.Embed(title = '**Polonium**', description = '84th Element, Mass of 209, **Metalloid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994440916697128.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def At(ctx):
  em = discord.Embed(title = '**Astatine**', description = '85th Element, Mass of 210, **Halogen**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994457672417310.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Rn(ctx):
  em = discord.Embed(title = '**Radon**', description = '86th Element, Mass of 222, **Noble Gas**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996687691579444.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fr(ctx):
  em = discord.Embed(title = '**Francium**', description = '87th Element, Mass of 223, **Alkali Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996743065305121.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ra(ctx):
  em = discord.Embed(title = '**Radium**', description = '88th Element, Mass of 226, **Alkaline Earth Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996771599024128.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ac(ctx):
  em = discord.Embed(title = '**Actinium**', description = '89th Element, Mass of 227, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996804897341520.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Th(ctx):
  em = discord.Embed(title = '**Thorium**', description = '90th Element, Mass of 232.04, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996833288716328.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pa(ctx):
  em = discord.Embed(title = '**Protactinium**', description = '91th Element, Mass of 231.04, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998911327272983.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def U(ctx):
  em = discord.Embed(title = '**Uranium**', description = '92th Element, Mass of 238.03, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998950375587881.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Np(ctx):
  em = discord.Embed(title = '**Neptunium**', description = '93th Element, Mass of 237, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998967928750184.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pu(ctx):
  em = discord.Embed(title = '**Plotunium**', description = '94th Element, Mass of 244, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998986611228673.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Am(ctx):
  em = discord.Embed(title = '**Americium**', description = '95th Element, Mass of 243, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806999002138279938.png?v=1')
  await ctx.send(embed = em)


@client.command()
async def Cm(ctx):
  em = discord.Embed(title = '**Curium**', description = '96th Element, Mass of 247, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293411362209812.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Bk(ctx):
  em = discord.Embed(title = '**Berkelium**', description = '97th Element, Mass of 247, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293439963430953.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cf(ctx):
  em = discord.Embed(title = '**Californium**', description = '98th Element, Mass of 251, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293504198934552.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Es(ctx):
  em = discord.Embed(title = '**Einsteinium**', description = '99th Element, Mass of 252, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293534545379338.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fm(ctx):
  em = discord.Embed(title = '**Fermium**', description = '100th Element!!, Mass of 257, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293586600624148.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Md(ctx):
  em = discord.Embed(title = '**Mendelevium**', description = '101th Element, Mass of 258, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295147468390470.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def No(ctx):
  em = discord.Embed(title = '**Nobelium**', description = '102th Element, Mass of 259, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295176645017640.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Lr(ctx):
  em = discord.Embed(title = '**Lawrencium**', description = '103th Element, Mass of 262, **Lanthanoid**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295198635098124.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Rf(ctx):
  em = discord.Embed(title = '**Rutherfordium**', description = '104th Element, Mass of 267, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295217425317889.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Db(ctx):
  em = discord.Embed(title = '**Dubnium**', description = '105th Element, Mass of 268, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295240201437186.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sg(ctx):
  em = discord.Embed(title = '**Seaborgium**', description = '106th Element, Mass of 269, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298519945838603.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Bh(ctx):
  em = discord.Embed(title = '**Bohrium**', description = '107th Element, Mass of 270, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298541457244290.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Hs(ctx):
  em = discord.Embed(title = '**Hassium**', description = '108th Element, Mass of 277, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298715798470699.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mt(ctx):
  em = discord.Embed(title = '**Meitnerium**', description = '109th Element, Mass of 278, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298735620882482.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ds(ctx):
  em = discord.Embed(title = '**Darmstadtium**', description = '110th Element, Mass of 281, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298754495381595.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Rg(ctx):
  em = discord.Embed(title = '**Roentgenium**', description = '111th Element, Mass of 282, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319083724832769.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cn(ctx):
  em = discord.Embed(title = '**Copernicium**', description = '112th Element, Mass of 285, **Transition Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319128355766322.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Nh(ctx):
  em = discord.Embed(title = '**Nihonium**', description = '113th Element, Mass of 286, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319155892158544.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fl(ctx):
  em = discord.Embed(title = '**Flerovium**', description = '114th Element, Mass of 289, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319188757676072.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mc(ctx):
  em = discord.Embed(title = '**Moscovium**', description = '115th Element, Mass of 289, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319204868128768.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Lv(ctx):
  em = discord.Embed(title = '**Livermorium**', description = '116th Element, Mass of 293, **Other Metal**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319250514739220.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ts(ctx):
  em = discord.Embed(title = '**Tennessine**', description = '117th Element, Mass of 294, **Halogen**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319266311012413.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Og(ctx):
  em = discord.Embed(title = '**Oganesson**', description = '118th Element (finally we are done!), Mass of 294, **Noble Gas**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319288561008711.png?v=1')
  await ctx.send(embed = em)

#hidden command
@client.command()
async def dm(ctx):
  await ctx.author.send(':rage: aw shit you found me :rage:\nI guess you want to know the secret commands right?\nFine.\n`clear` would clear messages and is **not** a moderation command. For example, `p clear 3` would clear 3 messages.\nWho doesn not want free hugs? Do `p freehugs` for free hugs. This was a fanmade command!\n`p gif` = Science gif\n`p billnye` is a randomized gif with the one and only Bill Nye!\n`p rsl` gives the entire script of the Raid Shadow Legends! This command was also fanmade :slight_smile:\n`p quack`  - Quack someone by typing either `p quack <username>` or `p quack @<username>`.\n\nYou happy now? Also do not tell about this command to anyone - not even your best friend. Developer would be :face_with_symbols_over_mouth: lmao')

#hidden command
@client.command(aliases = ['delete'])
async def clear(ctx, amount=0):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

#hidden command
@client.command(aliases = ['raid', 'shadow', 'legends'])
async def rsl(ctx):
  await ctx.author.send('**This message is sponsored by Raid Shadow Legends, one of the biggest mobile role-playing games of 2021 and it is totally free! Currently almost 10 million users have joined Raid over the last six months, and it is one of the most impressive games in its class with detailed models, environments and smooth 60 frames per second animations! All the champions in the game can be customized with unique gear that changes your strategic buffs and abilities! The dungeon bosses have some ridiculous skills of their own and figuring out the perfect party and strategy to overtake them is a lot of fun! Currently with over 300,000 reviews, Raid has almost a perfect score on the Play Store! The community is growing fast and the highly anticipated new faction wars feature is now live, you might even find my squad out there in the arena! It is easier to start now than ever with rates program for new players you get a new daily login reward for the first 90 days that you play in the game! So what are you waiting for? Go to the video description, click on the special links and you will get 50,000 silver and a free epic champion as part of the new player program to start your journey! Good luck and I will see you there!**')
  
#hidden command
@client.command(aliases = ['hug', 'hugs'])
async def freehugs(ctx):
  await ctx.author.send("https://tenor.com/view/running-hug-embrace-imiss-you-good-to-see-you-again-gif-15965620")

#hidden command
@client.command()
async def gif(ctx):
  gifs = ['https://tenor.com/view/carbon-is-highly-reactive-with-other-elements-sensitive-responsive-active-neil-degrasse-tyson-gif-15827677', 'https://tenor.com/view/massiveunregulatednitrogendioxide-gif-19415452', 'https://tenor.com/view/drinks-margarita-liquid-nitrogen-dry-ice-gif-3384966', 'https://tenor.com/view/mundschutz-mask-breathe-gif-17200590','https://tenor.com/view/gold-rich-daffy-duck-money-gif-10195329',]
  await ctx.send(f'For the love of science and elements {random.choice(gifs)}')

#hidden command
@client.command(aliases = ['bill', 'nye'])
async def billnye(ctx):
  billnye_gifs = ['https://tenor.com/view/bill-nye-billnye-sciencerules-science-gif-5866727',  'https://tenor.com/view/bill-nye-party-horn-confetti-sarcastic-like-child-gif-5499505', 'https://tenor.com/view/bill-nye-head-explode-mindblown-gif-4903176', 'https://tenor.com/view/tongue-out-crazy-gif-11927272', 'https://tenor.com/view/memes-bill-nye-the-science-gif-5930649', 'https://tenor.com/view/mic-drop-drop-the-mic-serious-boss-bill-nye-gif-8166361', 'https://tenor.com/view/bill-nye-bill-nye-the-science-guy-scienceguy-consider-gif-7391226', 'https://tenor.com/view/dance-bill-nye-bill-nye-the-science-guy-bill-nye-dance-dancing-gif-5603636']
  await ctx.send(f'You cannot have enough Bill Nye {random.choice(billnye_gifs)}')

#hidden command
@client.command()
async def quack(ctx, *, member : discord.Member):

    await member.send(":duck: :duck: **I think you just got quacked ohhhh** :duck: :duck:")

@client.command(aliases = ['dmitri'])
async def mendeleev(ctx):
  em = discord.Embed(title = '**Dmitri Ivanovich Mendeleev was a Russian chemist and inventor. He is best remembered for formulating the Periodic Law and creating a farsighted version of the periodic table of elements.**', description = 'http://en.wikipedia.org/wiki/Dmitri_Mendeleev\nhttps://www.britannica.com/biography/Dmitri-Mendeleev\nhttps://www.biography.com/scientist/dmitri-mendeleyev', color = discord.Color.red())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806396194196029460.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['soc'])
async def socials(ctx):
  em = discord.Embed(title = '**QuackerDeezlesYT Socials**',description = '**YouTube Channel**\nhttps://www.youtube.com/channel/UC6PKOburRMFSjwTCQcL4wbQ?view_as=subscriber', color = discord.Color.orange())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['site', 'website'])
async def botsite(ctx):
  em = discord.Embed(title = '**PERIODICCIA WEBSITE**', description ='https://sites.google.com/view/periodiccia/home', color = discord.Color.green())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def vote(ctx):
  em = discord.Embed(title = '**UPVOTE ME PLEASE :pleading_face:**', description ='**DiscordBotList**\nhttps://discordbotlist.com/bots/quacc-ducc/upvote\n**Top.gg**\nhttps://top.gg/bot/767190721534361631/vote', color = discord.Color.purple())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806252058851803136.png?v=1')
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806252169765584976.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['serv', 'guild'])
async def server(ctx):
  em = discord.Embed(title = '**Official Periodiccia Server**', description ='https://discord.gg/W6JHRPWvJd **STILL UNDER CONSTRUCTION**', color = discord.Color.purple())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['periodictable', 'periodic'])
async def table(ctx):
  await ctx.send(file = discord.File("periodictable2.jpg"))

@client.command(aliases = ['bio', 'dev'])
async def devbio(ctx, page = 1):
  if page == 1:

    em = discord.Embed(title = 'This is QuackerDeezlesYT', description = '**Page 1 of 3 - About Me**\n\n**I am a math fanatic, hardcore music lover, Geometry Dash and Fall Guys gamer, and puzzle enthusiast.**\n\n**More on the Music Aspect**\n\nI do everything; make music, listen to music, and learn music! My favorite music to listen is EDM (which covers Dubstep, Drum and Bass, and Trap) as well as Hiphop/R&B. I play the piano (for 10.5 years and counting) and percussion (for 4 years and counting). I make sure that with playing music and listening music, I keep learning more and more music theory. I also just started composing my own EDM music, and posting them on SoundCloud and YouTube.\n\n**More on the Video Games Aspect**\n\nI have been playing **Geometry Dash** for the past 6-7 years. I have actually spent 8 dollars on that game without in-app purchases; First few years on an iPad, then a year on my phone, and currently I play the game on my PC for the past 2 months and counting. My hardest level I have ever completed is 11 Demon EA, a hard demon. The game is so amazing, which is why I have played it for such a long time!\n\n**Fall Guys** is one, amazing feel-good game. I got the game right when I got my PC, and I have been playing it ever since. It is super fun, just hoping that there would be constant updates. Otherwise, 10/10.\n\nIf you have any good video game recommendations, DM Me!', color = discord.Color.purple())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
    await ctx.send(embed = em)
  elif page == 2:
    
    em = discord.Embed(title = 'This is QuackerDeezlesYT', description = '**Page 2 of 3 - Discord Experience**\n\n**Why did I decide to make this bot?**\n\nTo be honest, I never liked programming. For who I want to be, writing random abbreviations was at the bottom of my priority list. A few months after I made a Discord account, I planned on making a Discord Bot. It felt fun seeing people type commands and in an instant my bot will respond, so why not try it out?\n\nIf you go to the URL of DiscordBotLists vote page (not top.gg) you will see quacc-ducc and not periodiccia. Quacc Ducc was 1.0, a bot with literally no purpose. It was not going well and was offline most of the time. I decided to take a stand. One of the commands of Quacc Ducc was `elem`, which would give out information about the Elements, similar to what Periodiccia is doing right now. I got a thought - why not make a bot just on this? I worked super hard on it, and it is paying off, with people constantly using it. I am realizing that me not trying out programming could have blocked a door that I have myself opened.\n\n**Moderation**\n\nI am an admin of 3 servers with member counts of 160, 250, and 110. Those servers are the ones I advertised on the third page of this bio, you can find them by typing `p devbio 3`. In addition to this, I am a Stream Moderator of 2 streamers with follower counts 200 and 350.\n\nI will be very happy if you make me a staff member in your server! Would be truly appreciated :grinning:', color = discord.Color.purple())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
    await ctx.send(embed = em)

  elif page == 3:
    
    em = discord.Embed(title = 'This is QuackerDeezlesYT', description = '**Page 3 of 3 - Recommended Servers**\n\nhttps://discord.gg/Xt8UQj2neY\n\n**__60hz Gang__** is the ultimate Geometry Dash Server. We are a fun, inclusive community who loves all things Geometry Dash. Geometry Dash is a entertaining, stimulating, geometrical, rhythm and music based game. The community that we hold is very friendly and loves to help people make levels, complete levels, collaborate with others, and to be there for any help. We have very friendly and active members/staff. We would love you to join - and so would you!\n\nhttps://discord.com/invite/hDghRHmpnQ\n\nWelcome to **__Gumball Nation__**! A gaming, community server designed to have fun and no other reason. We also encourage Dank Memers to join to meet other Dank Memers!\n\nhttps://discord.gg/yQ2N6AxSGM\n\nWe are __**idks**__, a friendly gaming server that would do huge giveaways once they reach 1000 members lol', color = discord.Color.purple())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
    await ctx.send(embed = em)

keep_alive.keep_alive()
client.run("my token")
