import discord
import keep_alive
import os
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = 'p ')
client.remove_command('help')


@client.event
async def on_ready():
  print("The bot is ready!")

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"My Developer code Me"))

@client.command(aliases = ['huh', 'what'])
async def help(ctx, args = None):
 if not args:
  em = discord.Embed(title = '__Welcome to Periodiccia!__', description = '**Here are the commands for Periodiccia.**\n\n:1234: **Element Command List** `p help elements`\n\n:information_source: **Info Command List** `p help info`\n\n:smile: **Fun Command List** `p help fun`\n\n:grinning: **Join our official server!** https://bit.ly/3b4JbPd or `p server`.\n\n:pleading_face: **It would be very appreciated if you could invite my bot to your server!** https://bit.ly/39O9N7t\n\n:pleading_face: Please vote me on top.gg! https://top.gg/bot/767190721534361631/vote or `p vote`\n\n:question: DM QuackerDeezlesYT#3393 (the developer) if you have any help!\n\nBtw my pronouns are she/her', color = discord.Color.purple())
  em.set_footer(text = 'You are now viewing the help page.')
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  await ctx.send(embed = em)
 else:
  if args == 'elements':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', description = '**:1234: __Element Commands__**\n\n:atom: `p <element_symbol>` - Gives information about an element\n\n:scroll: `p elements <page_number>` - Reference to symbols to use for the element commands. **12 pages**\n\n:atom: `p ions` - Gives some pretty common polyatomic ions that you will have to memorize in your chemistry class. \n\n:man: `p mendeleev` -  This command tells you a bit about who Mendeleev is, and some helpful resources to learn more about him.', color = discord.Color.purple())
    em.set_footer(text="You are now viewing the help elements page.")
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif args == 'info':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', description = ':information_source: **__Info Commands__**\n\n:scroll: `p devbio` - Use this to learn about the dev, QuackerDeezlesYT! (**3 Pages**) You can find his socials by entering `p socials`.\n\n:computer: `p botsite` - My Website! Check me out! \n\n:man_raising_hand: `p vote` - Please vote me on top.gg and Discord Bot List!\n\n:ok_hand: `p tips` - Tips and videos to learn how to easily use me.', color = discord.Color.purple())
    em.set_footer(text="You are now viewing the help info page.")
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif args == 'fun':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', description = '**:smile: __Fun and Meme Commands__**\n\n:people_hugging: `p freehugs` - Free Hugs! Fanmade\n\n:video_camera: `p gif` - Science gif\n\n:magnet: `p billnye` - Randomized Bill Nye gif\n\n:scroll: `p rsl` gives the entire script of the Raid Shadow Legends! Fanmade\n\n:duck: `p quack @<username>` - Quack! Fanmade\n\n:lipstick: `p pp` - See how big your pp is!\n\n:sweat_drops: `p squirt` A generator to see how wet you are.\n\n:tv: `p waifu` - See a randomized selection of waifus!\n\n:man_facepalming: `p bruh @<username>` - Get a random annoying gif sent into your DMs.\n\n:speaking_head: `p say {text}` The bot will say whatever you want!', color = discord.Color.purple())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    em.set_footer(text="You are now viewing the help fun page.")
    await ctx.send(embed = em)
  else:
    pass

@client.command()
async def elements(ctx, page = 1):
  if page == 1:

    em = discord.Embed(title = 'List of the Elements 1', description = 'Hydrogen (`H`)\nHelium (`He`)\nLithium (`Li`)\nBeryllium (`Be`)\nBoron (`B`)\nCarbon (`C`)\nNitrogen (`N`)\nOxygen (`O`)\nFlourine (`F`)\nNeon (`Ne`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 2:
    
    em = discord.Embed(title = 'List of the Elements 2', description = 'Sodium (`Na`)\nMagnesium (`Mg`)\nAluminum (`Al`)\nSilicon (`Si`)\nPhosphorus (`P`)\nSulfur (`S`)\nChlorine (`Cl`)\nArgon (`Ar`)\nPotassium (`K`)\nCalcium (`Ca`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 3:
    
    em = discord.Embed(title = 'List of the Elements 3', description = 'Scandium (`Sc`)\nTitanium (`Ti`)\nVanadium (`V`)\nChromium (`Cr`)\nManganese (`Mn`)\nIron (`Fe`)\nCobalt (`Co`)\nNickel (`Ni`)\nCopper (`Cu`)\nZinc (`Zn`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 4:
    
    em = discord.Embed(title = 'List of the Elements 4', description = 'Gallium (`Ga`)\nGermanium (`Ge`)\nArsenic (`As`)\nSelenium (`Se`)\nBromine (`Br`)\nKyrpton (`Kr`)\nRibidium (`Rb`)\nStrontium (`Sr`)\nYttrium (`Y`)\nZirconium (`Zr`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 5:
    
    em = discord.Embed(title = 'List of the Elements 5', description = 'Niobium (`Nb`)\nMolybdenum (`Mo`)\nTechnetium (`Tc`)\nRuthenium (`Ru`)\nRhodium (`Rh`)\nPalladium (`Pd`)\nSilver (`Ag`)\nCandium (`Cd`)\nIndium (`In`)\nTin (`Sn`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    em.set_footer(text="Do people still like cat videos?")
    await ctx.send(embed = em)
  elif page == 6:
    
    em = discord.Embed(title = 'List of the Elements 6', description = 'Antimony (`Sb`)\nTellurium (`Te`)\nIodine (`I`)\nXenon (`Xe`)\nCaesium (`Cs`)\nBarium (`Ba`)\nLanthanum (`La`)\nCerium (`Ce`)\nPraseodymium (`Pr`)\nNeondymium (`Nd`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 7:
    
    em = discord.Embed(title = 'List of the Elements 7', description = 'Prothemium (`Pm`)\nSamarium (`Sm`)\nEuropium (`Eu`)\nGadolinium (`Gd`)\nTerbium (`Tb`)\nDysprosium (`Dy`)\nHolmium (`Ho`)\nErbium (`Er`)\nThulium (`Tm`)\nYtterbium (`Yb`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 8:
    
    em = discord.Embed(title = 'List of the Elements 8', description = 'Lutetium (`Lu`)\nHafnium (`Hf`)\nTantalum (`Ta`)\nTungsten (`W`)\nRhenium (`Re`)\nOsmium (`Os`)\nIridium (`Ir`)\nPlatinum (`Pt`)\nGold (`Au`)\nMercury (`Hg`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 9:
    
    em = discord.Embed(title = 'List of the Elements 9', description = 'Thallium (`Tl`)\nLead (`Pb`)\nBismuth (`Bi`)\nPolonium (`Po`)\nAstatine (`At`)\nRadon (`Rn`)\nFrancium (`Fr`)\nRadium (`Ra`)\nActinium (`Ac`)\nThorium (`Th`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 10:
    
    em = discord.Embed(title = 'List of the Elements 10', description = 'Protactinium (`Pa`)\nUranium (`U`)\nNeptunium (`Np`)\nPlutonium (`Pu`)\nAmericium (`Am`)\nCurium (`Cm`)\nBerkelium (`Bk`)\nCalifornium (`Cf`)\nEinsteinium (`Es`)\nFermium (`Fm`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 11:
    
    em = discord.Embed(title = 'List of the Elements 11', description = 'Mendelevium (`Md`)\nNobelium (`No`)\nLawrencium (`Lr`)\nRutherfordium (`Rf`)\nDubnium (`Db`)\nSeaborgium (`Sg`)\nBohrium (`Bh`)\nHassium (`Hs`)\nMeitnerium (`Mt`)\nDarmstadtium (`Ds`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)
  elif page == 12:

    em = discord.Embed(title = 'List of the Elements 12', description = 'Roentgenium (`Rg`)\nCopernicium (`Cn`)\nNihonium (`Nh`)\nFlerovium (`Fl`)\nMoscovium (`Mc`)\nLivermorium (`Lv`)\nTennessine (`Ts`)\nOganesson (`Og`)', color = discord.Color.orange())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
    await ctx.send(embed = em)

@client.command()
async def ions(ctx):
  em = discord.Embed(title = 'Common Polyatomic Ions', description = 'NH4+    -    **Ammonium**\nCH3COO-    -    **Acetate**\nCN-    -    **Cyanide**\nOH-    -    **Hydroxide**\nMno4-    -    **Permanganate**\nNO3-    -    **Nitrate**\nNO2-    -    **Nitrite**\nClO4-    -    **Perchlorate**\nCl03-    -    **Chlorate**\nCl02-    -    **Chlorite**\nClO-    -    **Hypochlorite**\nHSO4-    -    **Hydrogen Sulfate**\nHCO3-  -  **Hydrogen Carbonate**\nH2PO4-  -  **Dihydrogen Phosphate**', color = discord.Color.orange())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  em.set_footer(text="A cool memorization tool")
  await ctx.send(embed = em)

@client.command()
async def tips(ctx):
  em = discord.Embed(title = '**Tips and Tricks + Help Videos**', description = '**1. Introduction** - https://www.youtube.com/watch?v=yaaj5PkE290 ', color = discord.Color.purple())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  em.set_footer(text="Please subscribe to QuackerDeezles, he spends a good amount of his time making videos about me!")
  await ctx.send(embed = em)

@client.command()
async def Ve(ctx):
  em = discord.Embed(title = '**VERITASIUM**', description = 'Mass of KNOWLEDGE, YouTube Channel =\n https://www.youtube.com/user/1veritasium', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807399043822518323.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def H(ctx):
  em = discord.Embed(title = '**Hydrogen**', description = '1st Element, Mass of 1.008\n**Henry Cavendish FRS** was an English natural philosopher, scientist, and an important experimental and theoretical chemist and physicist. He is noted for his **discovery of hydrogen**, which he termed "inflammable air".', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806237831613775885.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def He(ctx):
  em = discord.Embed(title = '**Helium**', description = '2nd Element, Mass of 4.0026, **Noble Gas**\nThe first **evidence of helium** was obtained on August 18th, 1868 by French **astronomer Jules Janssen.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806566745980665926.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Li(ctx):
  em = discord.Embed(title = '**Lithium**', description = '3rd Element, Mass of 6.94, **Alkali Metal**\n**Johan August Arfwedson** was a **Swedish chemist** who discovered the **chemical element lithium** in 1817 by **isolating it as a salt.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806567984415768678.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Be(ctx):
  em = discord.Embed(title = '**Beryllium**', description = '4th Element, Mass of 9.0122, **Alkaline Earth Metal**\nBeryllium was discovered by French **pharmacist Louis Nicolas Vanquelin** in 1798. He determined that this new metal was a **component of beryl and emeralds.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806569567593168906.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def B(ctx):
  em = discord.Embed(title = '**Boron**', description = '5th Element, Mass of 10.81, **Metalloid**\n**Boron** was discovered by **Joseph-Louis Gay-Lussac and Louis-Jaques Thénard**, French chemists, and **independently by Sir Humphry Davy**, an English chemist, in 1808. They all **isolated boron by combining boric acid with potassium.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806572191826968656.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def C(ctx):
  em = discord.Embed(title = '**Carbon**', description = '6th Element, Mass of 12.011, **Nonmetal**\nUnfortunately, **no one knows who discovered carbon.** It is one of the few elements that was known since ancient times. The **earliest use of carbon** was sometime around **3750 BC.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806609579890835466.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def N(ctx):
  em = discord.Embed(title = '**Nitrogen**', description = '7th Element, Mass of 14.077, **Nonmetal**\n**Daniel Rutherford** was a Scottish **physician, chemist and botanist** who is known for the isolation of **nitrogen in 1772.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610043762901042.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def O(ctx):
  em = discord.Embed(title = '**Oxygen**', description = '8th Element, Mass of 15.999, **Nonmetal**\n**Oxygen was discovered about 1772** by a Swedish chemist, **Carl Wilhelm Scheele**, who obtained it by **heating potassium nitrate, mercuric oxide, and many other substances.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610357668937748.png?v=1' )
  await ctx.send(embed = em)

@client.command()
async def F(ctx):
  em = discord.Embed(title = '**Flourine**', description = '9th Element, Mass of 18.998, **Halogen**\n**Ferdinand Frédéric Henri Moissan** was a French chemist and pharmacist who **won the 1906 Nobel Prize** in Chemistry for his work in **isolating fluorine from its compounds**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610601761570836.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ne(ctx):
  em = discord.Embed(title = '**Neon**', description = '10th Element, Mass of 20.180, **Noble Gas**.\nWho discovered **neon**? In 1898, English chemist **Morris W. Travers** and Scottish chemist **William Ramsay** discovered this all-important chemical element in the City of London in England.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806611638672949269.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Na(ctx):
  em = discord.Embed(title = '**Sodium**', description = '11th Element, Mass of 22.990, **Alkali Metal**\n**Sir Humphry Davy**, a British chemist, discovered **sodium in 1807**. He found the element by **isolating it from caustic soda using electrolysis.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806611195548794912.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mg(ctx):
  em = discord.Embed(title = '**Magnesium**', description = '12th Element, Mass of 23.405, **Alkaline Earth Metal**\n**Joseph Black** was a Scottish **physicist and chemist**, known for his discoveries of magnesium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612129914159114.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Al(ctx):
  em = discord.Embed(title = '**Aluminum**', description = '13th Element, Mass of 26.982, **Other Metal**\n**Hans Christian Ørsted was a Danish physicist and chemist who discovered that electric currents create magnetic fields, which was the first connection found between electricity and magnetism. Oersteds law and the Oersted are named after him.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612299808636948.png?v=1')
  em.set_footer(text="Ø is the Twenty One Pilots O, that's pretty swag")
  await ctx.send(embed = em)

@client.command()
async def Si(ctx):
  em = discord.Embed(title = '**Silicon**', description = '14th Element, Mass of 28.085, **Metalloid**\n**Silicon** was discovered by **Jöns Jacob Berzelius**, a Swedish chemist, in 1824 by **heating chips of potassium in a silica container** and then carefully **washing away the residual by-products.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612488745386004.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def P(ctx):
  em = discord.Embed(title = '**Phosphorus**', description = '15th Element, Mass of 30.974, **Nonmetal**\n**Hennig Brand** was a German **merchant, pharmacist and alchemist**, who lived and worked in Hamburg. He is the **discoverer of** the chemical element **phosphorus.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612670932975646.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def S(ctx):
  em = discord.Embed(title = '**Sulfur**', description = '16th Element, Mass of 32.06, **Nonmetal**\nThe credit for discovering sulfur is given to **Hennig Brand** (1669), however it was **identified by Antoine Lavoisier in 1777**. But scholars believe that no single person was responsible for discovering this non-metallic element because it has **been in usage since ancient times for alchemy and other purposes.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612864936181811.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cl(ctx):
  em = discord.Embed(title = '**Chlorine**', description = '17th Element, Mass of 35.45, **Halogen**\n**Carl Wilhelm Scheele** is a German Swedish chemist who **independently discovered** oxygen, **chlorine**, and manganese.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806613436347187250.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ar(ctx):
  em = discord.Embed(title = '**Argon**', description = '18th Element, Mass of 39.948, **Noble Gas**\n**Sir John Rayleigh**, a peer by inheritance, was a British physicist. He **discovered argon, an inert gas**, that **earned him the 1904 Nobel Prize** in physics award. He is also known for “Rayleigh Scattering.”', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806613620657750086.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def K(ctx):
  em = discord.Embed(title = '**Potassium**', description = '19th Element, Mass of 39.098, **Alkali Metal**\n**Potassium** was discovered in 1807 by British scientist **Sir Humphry Davy**, who derived it from caustic potash where was it discovered and when his first successes came in 1807 with the **separation of potassium from molten potash and of sodium from common salt.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628580200939551.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ca(ctx):
  em = discord.Embed(title = '**Calcium**', description = '20th Element, Mass of 40.078, **Alkaline Earth Metal**\nIt was only during the year of 1808 did calcium get isolated and taken as a particular element in itself. And the person who discovered calcium was Englishman **Sir Humphrey Davy.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628602259046480.png?v=1')
  em.set_footer(text="Ayyyy him again")
  await ctx.send(embed = em)

@client.command()
async def Sc(ctx):
  em = discord.Embed(title = '**Scandium**', description = '21th Element, Mass of 44.956, **Transition Metal**\n**Lars Fredrik Nilson** was the discoverer. He discovered scandium in 1879. The name **scandium came from the place it was discovered - Scandinavia**. Lars Fredrik Nilson created 2 grams of high purity scandium oxide.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628627847708683.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ti(ctx):
  em = discord.Embed(title = '**Titanium**', description = '22th Element, Mass of 47.867, **Transition Metal**\n**William Gregor** was the British **clergyman and mineralogist** who discovered the elemental metal titanium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628650354475089.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def V(ctx):
  em = discord.Embed(title = '**Vanadium**', description = '23th Element, Mass of 50.942, **Transition Metal**\n**Andrés Manuel del Río y Fernández** was a Spanish–Mexican **scientist, naturalist and engineer** who discovered **compounds of vanadium in 1801.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628668347777024.png?v=1')
  em.set_footer(text = "That's a pretty long name")
  await ctx.send(embed = em)

@client.command()
async def Cr(ctx):
  em = discord.Embed(title = '**Chromium**', description = '24th Element, Mass of 51.996, **Transition Metal**\n**Chromium was discovered by Louis-Nicholas Vauquelin** while experimenting with a material known as **Siberian red lead**, also known as the mineral **crocoite (PbCrO 4)**, in 1797.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630723296952330.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mn(ctx):
  em = discord.Embed(title = '**Manganese**', description = '25th Element, Mass of 54.938, **Transition Metal**\nProposed to be an **element by Carl Wilhelm Scheele in 1774**, manganese was **discovered by Johan Gottlieb Gahn**, a Swedish chemist, by **heating the mineral pyrolusite (MnO 2) in the presence of charcoal** later that year.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630771581779988.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fe(ctx):
  em = discord.Embed(title = '**Iron**', description = '26th Element, Mass of 55.845, **Transition Metal**\nUnfortunately, **no one knows who was the first person to discover iron.** Iron has been **used since prehistory.** The Ancient Egyptians and Sumerians began using **iron on the tips of spears and in some ornaments around 4000 BC.** They obtained the **iron from meteorites** that hit the earth.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630803467141151.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Co(ctx):
  em = discord.Embed(title = '**Cobalt**', description = '27th Element, Mass of 58.933, **Transition Metal**\n**Georg Brandt** was a **Swedish chemist and mineralogist who discovered cobalt.** He was the **first person to discover a metal unknown in ancient times.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630849117814845.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ni(ctx):
  em = discord.Embed(title = '**Nickel**', description = '28th Element, Mass of 58.693, **Transition Metal**\n**Axel Fredrik Cronstedt** was a **Swedish mineralogist and chemist** who discovered the **element nickel in 1751** as a **mining expert with the Bureau of Mines.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630871225860106.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cu(ctx):
  em = discord.Embed(title = '**Copper**', description = '29th Element, Mass of 63.546, **Transition Metal**\nUnfortunately, **no one knows who discovered copper.** Copper **occurs in nature uncombined with any other things.** Therefore, it has been recognized and **used by civilizations for thousands of years.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639082914054184.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Zn(ctx):
  em = discord.Embed(title = '**Zinc**', description = '30th Element, Mass of 65.38, **Transition Metal**\nIn 1746, **German chemist Andreas Marggraf** figured out how to **isolate zinc by heating carbon and calamine** (the stuff in calamine lotion).', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639415828938802.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ga(ctx):
  em = discord.Embed(title = '**Gallium**', description = '31th Element, Mass of 69.732, **Other Metal**\n**Paul-Émile Lecoq de Boisbaudran, also called François Lecoq de Boisbaudran**, was a French **chemist known for his discovery of gallium**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639435323539496.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ge(ctx):
  em = discord.Embed(title = '**Germanium**', description = '32th Element, Mass of 72.61, **Metalloid**\n**Clemens Alexander Winkler** was a **German chemist** who discovered the **element germanium in 1886**, solidifying Dmitri Mendeleevs theory of periodicity.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639480726880268.png?v=1')
  em.set_footer(text="Mendeleev shoutout woohoo")
  await ctx.send(embed = em)

@client.command()
async def As(ctx):
  em = discord.Embed(title = '**Arsenic**', description = '33th Element, Mass of 74.922, **Metalloid**\nArsenic was discovered by **Albertus Magnus in 1250.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639501648330765.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Se(ctx):
  em = discord.Embed(title = '**Selenium**', description = '34th Element, Mass of 78.96, **Metalloid**\n**Selenium was discovered by Jöns Jakob Berzelius** in 1817 as a **byproduct of the production of sulfuric acid.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806736485788287027.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Br(ctx):
  em = discord.Embed(title = '**Bromine**', description = '35th Element, Mass of 79.004, **Halogen**\nBromine was discovered in 1826 by the **French chemist Antoine-Jérôme Balard** in the **residues from the manufacture of sea salt at Montpellier.** He liberated the element by **passing chlorine through an aqueous solution of the residues, which contained magnesium bromide.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806737203832160336.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Kr(ctx):
  em = discord.Embed(title = '**Krypton**', description = '36th Element, Mass of 83.80, **Noble Gas**\nKrypton was discovered on May 30, 1898 by **Sir William Ramsay, a Scottish chemist, and Morris M. Travers, an English chemist**, while studying liquefied air.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806737863960952862.png?v=1')
  em.set_footer(text = "SUPERMAN OMGGGG")
  await ctx.send(embed = em)

@client.command()
async def Rb(ctx):
  em = discord.Embed(title = '**Rubidium**', description = '37th Element, Mass of 85.468, **Alkali Metal**\nRubidium was discovered in 1861 by **Robert Bunsen and Gustav Kirchhoff, in Heidelberg, Germany**, in the mineral **lepidolite through flame spectroscopy.** Because of the bright red lines in its emission spectrum, they chose a name derived from the **Latin word rubidus, meaning "deep red".**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738015644418078.png?v=1')
  await ctx.send(embed = em)
  
@client.command()
async def Sr(ctx):
  em = discord.Embed(title = '**Strontium**', description = '38th Element, Mass of 87.62, **Alkaline Earth Metal**\n**Humphry Davy** in London **isolated the soft, silvery metal** of the new element **using electrolysis.** The Scottish village was called Strontian, the mineral found there, strontianite and the **new element strontium.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738197517959169.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Y(ctx):
  em = discord.Embed(title = '**Yttrium**', description = '39th Element, Mass of 88.906, **Transition Metal**\nYttrium was discovered by **Johan Gadolin, a Finnish chemist**, while **analyzing the composition of the mineral gadolinite** in 1789.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738408671019018.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Zr(ctx):
  em = discord.Embed(title = '**Zirconium**', description = '40th Element, Mass of 91.224, **Transition Metal**\nIn the Middle Ages colourless **gemstones of zircon were thought to be an inferior kind of diamond**, but that was **shown to be wrong** when a German chemist, **Martin Klaproth (1743-1817), analysed one in 1789** and discovered zirconium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738696300527656.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Nb(ctx):
  em = discord.Embed(title = '**Niobium**', description = '41th Element, Mass of 92.906, **Transition Metal**\nNiobium was **discovered in 1801 by Charles Hatchett** in an ore called **columbite** sent to England in the 1750s by John Winthrop the Younger, the first goveror of Connecticut, USA. The metal niobium was **first prepared in 1864** by Blomstrand, who reduced the chloride by **heating it in a hydrogen atmosphere.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814906461720805376.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mo(ctx):
  em = discord.Embed(title = '**Molybdenum**', description = '42th Element, Mass of 95.95, **Transition Metal**\nIn 1768, the Swedish scientist **Carl Wilhelm Scheele** determined that **molybdenite was a sulfide compound of an as-yet unidentified element**, by decomposing it in **hot nitric acid** and heating the product in air to yield a **white oxide powder.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806739137947369502.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tc(ctx):
  em = discord.Embed(title = '**Technetium**', description = '43th Element, Mass of 98.907, **Transition Metal\nTechnetium was the first **artificially produced element.** It was isolated by **Carlo Perrier and Emilio Segrè in 1937**. Technetium was created by bombarding molybdenum atoms with deuterons that had been accelerated by a device called a **cyclotron.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806739458296381500.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ru(ctx):
  em = discord.Embed(title = '**Ruthenium**', description = '44th Element, Mass of 101.07, **Transition Metal**\nRuthenium was discovered by **Karl Karlovich Klaus**, a Russian chemist, in 1844 while analyzing the **residue of a sample of platinum ore** obtained from the Ural mountains.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806740984279859220.png?v=1')
  em.set_footer(text="Triple K: Karl Karlovich Klaus")
  await ctx.send(embed = em)

@client.command()
async def Rh(ctx):
  em = discord.Embed(title = '**Rhodium**', description = '45th Element, Mass of 102.91, **Transition Metal**\nRhodium was discovered by **William Hyde Wollaston**, an English chemist, in 1803 shortly after his discovery of the element palladium. He obtained rhodium from a **sample of platinum ore that was obtained from South America.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806741372124004372.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pd(ctx):
  em = discord.Embed(title = '**Palladium**', description = '46th Element, Mass of 106.42, **Transition Metal**\n**William Hyde Wollaston** was an English chemist and physicist who is famous for discovering the chemical elements palladium and rhodium. He also developed a way to process platinum ore into malleable ingots.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806741800853307392.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ag(ctx):
  em = discord.Embed(title = '**Silver**', description = '47th Element, Mass of 107.87, **Transition Metal**\nNo one knows who discovered silver, but it was German physicist **Johann Heinrich Schultze** who used **silver nitrate to invent photography in 1727.** Since then, the lustrous Silver element has become **even more precious** as science and technology have discovered more and more uses.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742042054099025.png?v=1')
  await ctx.send(embed = em)
  
@client.command()
async def Cd(ctx):
  em = discord.Embed(title = '**Cadmium**', description = '48th Element, Mass of 112.41, **Transition Metal**\nCadmium was discovered by **Friedrich Strohmeyer**, a German chemist, in 1817 while **studying samples of calamine (ZnCO 3)**. When heated, Strohmeyer noticed that some **samples of calamine glowed with a yellow color while other samples did not.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742338411298887.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def In(ctx):
  em = discord.Embed(title = '**Indium**', description = '49th Element, Mass of 114.82, **Other Metal**\nIndium was discovered in 1863 when **German Chemists Ferdinand Reich and Hieronymous Theodor Richter tested ores from Saxony**,where they worked. They made the discovery after **dissolving the minerals from these ores and testing for thallium**, which was already known at the time, **with spectroscopy.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806745134343520317.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sn(ctx):
  em = discord.Embed(title = '**Tin**', description = '50th Element, Mass of 118.71, **Other Metal**\nJames Smith found the **rich deposit of tin at Mount Bischoff.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806743088475144213.png?v=1')
  em.set_footer(text="That's it?")
  await ctx.send(embed = em)

@client.command()
async def Sb(ctx):
  em = discord.Embed(title = '**Antimony??????**', description = '51th Element, Mass of 121.76, **Metalloid**\nNicolas Lémery, a French chemist, was the **first person to scientifically study antimony and its compounds.** He published his findings in 1707. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806743967370182689.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Te(ctx):
  em = discord.Embed(title = '**Tellerium**', description = '52th Element, Mass of 127.60, **Metalloid**\nTellurium was discovered by **Franz Joseph Müller von Reichenstein**, a Romanian mining official.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806744271704031242.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def I(ctx):
  em = discord.Embed(title = '**Iodine**', description = '53th Element, Mass of 126.90, **Halogen**\nIt was discovered by French chemist **Bernard Courtois in 1811** whereby Gay-Lussac subsequently suggested the name "iode", from the Greek word ιώδες (iodes) for violet, **because of the color of iodine vapor.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742859163631626.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Xe(ctx):
  em = discord.Embed(title = '**Xenon**', description = '54th Element, Mass of 131.29, **Noble Gases**\nXenon was discovered in England by the **Scottish chemist William Ramsay and English chemist Morris Travers** in September 1898, shortly after their discovery of the elements krypton and neon. **They found xenon in the residue left over from evaporating components of liquid air.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806745520797384764.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cs(ctx):
  em = discord.Embed(title = '**Cesium**', description = '55th Element, Mass of 132.91, **Alkali Metal**\nCesium was discovered by **Robert Wilhelm Bunsen and Gustav Robert Kirchhoff**, German chemists, in 1860 through the **spectroscopic analysis of Durkheim mineral water.** They named cesium after the **blue lines** they observed in its **spectrum.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746036362149939.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ba(ctx):
  em = discord.Embed(title = '**Barium**', description = '56th Element, Mass of 137.33, **Alkaline Earth Metal**\n**Vincenzo Casciarolo, a 17th-century Italian alchemist,** first noticed barium in the form of **unusual pebbles that glowed** for years after exposure to heat.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746477622722610.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def La(ctx):
  em = discord.Embed(title = '**Lanthanium**', description = '57th Element, Mass of 138.91, **Lanthanoid**\nLanthanum was discovered by **Carl Gustaf Mosander, a Swedish chemist**, in 1839. Mosander was searching for **impurities** he believed existed within **samples of cerium**. He treated **cerium nitrate with dilute nitric acid** and found a new substance he **named lanthana.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746907807318016.png?v=1')
  em.set_footer(text = "Lanthanium is a lanthanoid. Pretty simple fact.")
  await ctx.send(embed = em)

@client.command()
async def Ce(ctx):
  em = discord.Embed(title = '**Cerium**', description = '58th Element, Mass of 140.12, **Lanthanoid**\nCerium was discovered in 1803 by **Jacob Berzelius and Wilhelm von Hisinger in Sweden**. They discovered the new element in a **rare reddish-brown mineral** now known as cerite, a cerium-lanthanide silicate.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747109360795649.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pr(ctx):
  em = discord.Embed(title = '**Praseodymium**', description = '59th Element, Mass of 140.91, **Lanthanoid**\n**Carl Auer von Welsbach** (1858–1929), discovered praseodymium in 1885.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747420624027718.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Nd(ctx):
  em = discord.Embed(title = '**Neodynium**', description = '60th Element, Mass of 144.25, **Lanthanoid**\nAustrian chemist **Carl Auer von Welsbach** discovered neodymium in 1885 by separating **ammonium didymium nitrate prepared from didymia** (a mixture of rare-earth oxides) into a **neodymium fraction and a praseodymium fraction by repeated crystallization.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747639017766922.png?v=1')
  em.set_footer(text="That sounds very complex to me.")
  await ctx.send(embed = em)

@client.command()
async def Pm(ctx):
  em = discord.Embed(title = '**Promethium**', description = '61th Element, Mass of 145, **Lanthanoid**\nPromethium was the **last rare earth element of the lanthanide series** to be discovered. It was discovered in 1945 by **Jacob A. Marinsky, Lawrence E. Glendenin, and Charles D. Coryell**, although its existence had been predicted in 1902 by Czech chemist Bohuslav Brauner.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954923534712854.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sm(ctx):
  em = discord.Embed(title = '**Samarium**', description = '62th Element, Mass of 150.36, **Lanthanoid**\nSamarium was discovered in 1879 by the **French chemist Paul-Émile Lecoq de Boisbaudran** and named after the mineral samarskite from which it was isolated.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954959626567710.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Eu(ctx):
  em = discord.Embed(title = '**Europium**', description = '63th Element, Mass of 151.96, **Lanthanoid**\nEuropium was first **found in 1892 by Paul Émile Lecoq de Boisbaudran**, who obtained basic fractions from samarium-gadolinium concentrates which had **spectral lines not accounted** for by samarium or gadolinium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954988865585172.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Gd(ctx):
  em = discord.Embed(title = '**Gadolinium**', description = '64th Element, Mass of 157.25, **Lanthanoid**\nGadolinium was **discovered in 1880 by Jean Charles de Marignac**, who detected its oxide by using **spectroscopy**. It is named after the mineral gadolinite, one of the **minerals in which gadolinium is found.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806955066371473459.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tb(ctx):
  em = discord.Embed(title = '**Terbium**', description = '65th Element, Mass of 158.93, **Lanthanoid**\n**Swedish chemist Carl Gustaf Mosander discovered terbium** in 1843. He detected it as an **impurity in yttrium oxide**. Yttrium is **named after the village of Ytterby** in Sweden. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806955083731828737.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Dy(ctx):
  em = discord.Embed(title = '**Dysprosium**', description = '66th Element, Mass of 162.50, **Lanthanoid**\nDysprosium was first **identified in 1886 by Paul Émile Lecoq de Boisbaudran**, but it was **not isolated** in pure form until the **development of ion-exchange techniques** in the 1950s.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814920279892951070.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ho(ctx):
  em = discord.Embed(title = '**Holmium**', description = '67th Element, Mass of 164.93, **Lanthanoid**\nHolmium was discovered through isolation by **Swedish chemist Per Theodor Cleve and independently by Jacques-Louis Soret and Marc Delafontaine** who observed it **spectroscopically** in 1878.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956660878082139.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Er(ctx):
  em = discord.Embed(title = '**Erbium**', description = '68th Element, Mass of 167.26, **Lanthanoid**\nErbium was **discovered by Carl Gustaf Mosander** in 1843. Mosander was working with a sample of what was thought to be the **single metal oxide yttria, derived from the mineral gadolinite.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956695682809897.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tm(ctx):
  em = discord.Embed(title = '**Thulium**', description = '69th Element, Mass of 168.93, **Lanthanoid**\nThulium was **discovered in 1879 by Per Teodor Cleve**, who named the oxide thulia after an ancient name for Scandinavia.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956747393597441.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Yb(ctx):
  em = discord.Embed(title = '**Ytterbium**', description = '70th Element, Mass of 173.05, **Lanthanoid**\nYtterbium was discovered by the **Swiss chemist Jean Charles Galissard de Marignac** in the year 1878. While examining samples of gadolinite, Marignac found a new component in the earth then known as erbia, and **he named it ytterbia, for Ytterby, the Swedish village near where he found the new component of erbium.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956775248101387.png?v=1')
  em.set_footer(text = "When Ytterby gets all the recognition")
  await ctx.send(embed = em)

@client.command()
async def Lu(ctx):
  em = discord.Embed(title = '**Lutetium**', description = '71th Element, Mass of 174.97, **Lanthanoid**\nLutetium was independently discovered in 1907 by French scientist **Georges Urbain**, Austrian mineralogist **Baron Carl Auer von Welsbach**, and American chemist **Charles James**. All of these researchers found lutetium as an **impurity** in the mineral ytterbia.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814924472015519754.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Hf(ctx):
  em = discord.Embed(title = '**Hafnium**', description = '72th Element, Mass of 178.49, **Transition Metal**\nHafnium was **discovered by Dirk Coster**, a Danish chemist, and **George Charles de Hevesy**, a Hungarian chemist, in 1923. They used a method known as **X-ray spectroscopy** to study the arrangement of the **outer electrons of atoms** in samples of **zirconium ore.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959523256336425.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ta(ctx):
  em = discord.Embed(title = '**Tantalum**', description = '73th Element, Mass of 180.95, **Transition Metal**\nTantalum was discovered by **Anders Gustaf Ekenberg**, a Swedish chemist, in 1802 in **minerals obtained from Ytterby, Sweden.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959549986635807.png?v=1')
  em.set_footer(text="Ah yes, another Ytterby shoutout")
  await ctx.send(embed = em)

@client.command()
async def W(ctx):
  em = discord.Embed(title = '**Tungsten**', description = '74th Element, Mass of 183.84, **Transition Metal**\nTungsten was discovered in 1783 by **Juan José and Fausto Elhuyar**, Spanish chemists and brothers.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959566642085888.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Re(ctx):
  em = discord.Embed(title = '**Rhenium**', description = '75th Element, Mass of 186.21, **Transition Metal**\nIn 1925 the discovery of rhenium was announced by **German chemists Walter Noddack, Ida Tacke, and Otto Berg.** They detected the element in the minerals columbite, gadolinite, molybdenite, and in platinum ore.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959608748441620.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Os(ctx):
  em = discord.Embed(title = '**Osmium**', description = '76th Element, Mass of 190.23, **Transition Metal**\nOsmium was **discovered in 1803 by English chemist Smithson Tennant.** This discovery came about through research into platinum ore that was **first discovered in Columbia in the 17th century.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962799565340692.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ir(ctx):
  em = discord.Embed(title = '**Iridium**', description = '77th Element, Mass of 192.22, **Transition Metal**\nIridium was discovered in 1803 among **insoluble impurities** in natural platinum. **Smithson Tennant**, the primary discoverer, named iridium after the **Greek goddess Iris**, personification of the **rainbow**, because of the **striking and diverse colors** of its salts.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962871555850352.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pt(ctx):
  em = discord.Embed(title = '**Platinum**', description = '78th Element, Mass of 195.08, **Transition Metal**\nPlatinum was discovered in South America independently by **Antonio de Ulloa in 1735** and by **N. Wood in 1741**, but it had been in use by pre-Columbian Indians.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962912220151829.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Au(ctx):
  em = discord.Embed(title = '**Gold**', description = '79th Element, Mass of 196.97, **Transition Metal**\n**No single person discovered gold** but there are many **traces** of its use by ancient peoples. One early reference to it was made by Tushratta, a king of Mitanni (now northern Syria) in 2600 BC. He remarked that **there was more gold than dust in Egypt.** Such **abundance** of gold especially in Nubia **made Egypt a rich country.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962930531696650.png?v=1')
  await ctx.send(embed = em)
  
@client.command()
async def Hg(ctx):
  em = discord.Embed(title = '**Mercury**', description = '80th Element, Mass of 200.59, **Transition Metal**\nIt is **not known who discovered mercury**, but it has been **found in Egyptian tombs** dating back over 3,500 years. Mercury was also known to the ancient Chinese and Hindus.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962950479806577.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Tl(ctx):
  em = discord.Embed(title = '**Thallium**', description = '81th Element, Mass of 204.38, **Other Metal**\nThallium was discovered by **Sir William Crookes** in 1861. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994333910827028.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pb(ctx):
  em = discord.Embed(title = '**Lead**', description = '82th Element, Mass of 207.2, **Other Metal**\nEarly evidence of lead include **lead beads from 6400 BC in Turkey**, and verse 15:10 of the Book of Exodus. Lead was also discovered **independently by the Egyptians, Babylonians, Assyrians and Chinese.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994370648735784.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Bi(ctx):
  em = discord.Embed(title = '**Bismuth**', description = '83th Element, Mass of 208.98, **Other Metal**\n**Claude François Geoffroy** was a French chemist. In 1753 he **proved the chemical element bismuth to be distinct from lead**, becoming the official discoverer of the element.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814927082051338280.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Po(ctx):
  em = discord.Embed(title = '**Polonium**', description = '84th Element, Mass of 209, **Metalloid**\nPolonium was discovered in 1898 by **Marie and Pierre Curie**, when it was extracted from the uranium ore pitchblende and **identified solely by its strong radioactivity.** Polonium was **named after Marie Curies homeland of Poland.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994440916697128.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def At(ctx):
  em = discord.Embed(title = '**Astatine**', description = '85th Element, Mass of 210, **Halogen**\nAstatine was discovered in 1940 by **Dale Corson, Kenneth McKenzie, and Emilio Segre at Berkley**. It was not until three years later, however, that **astatine was found in nature.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994457672417310.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Rn(ctx):
  em = discord.Embed(title = '**Radon**', description = '86th Element, Mass of 222, **Noble Gas**\nRadon was discovered by **Friedrich Ernst Dorn, a German chemist**, in 1900 while studying **radium’s decay chain.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996687691579444.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fr(ctx):
  em = discord.Embed(title = '**Francium**', description = '87th Element, Mass of 223, **Alkali Metal**\nFrancium was discovered by **Marguerite Perey in France** (from which the element takes its name) in 1939. It was the **last element first discovered in nature, rather than by synthesis.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996743065305121.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ra(ctx):
  em = discord.Embed(title = '**Radium**', description = '88th Element, Mass of 226, **Alkaline Earth Metal**\nRadium was discovered by **Marie Sklodowska-Curie and her husband Pierre Curie on 21 December 1898**, in a **uraninite (pitchblende) sample** from Jáchymov.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996771599024128.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ac(ctx):
  em = discord.Embed(title = '**Actinium**', description = '89th Element, Mass of 227, **Lanthanoid**\nActinium was discovered in 1899 by **André-Louis Debierne**, a French chemist, while experimenting with **new methods of separating rare earth oxides.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996804897341520.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Th(ctx):
  em = discord.Embed(title = '**Thorium**', description = '90th Element, Mass of 232.04, **Lanthanoid**\nThorium was discovered by **Jöns Jacob Berzelius in 1828, in Stockholm, Sweden**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996833288716328.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pa(ctx):
  em = discord.Embed(title = '**Protactinium**', description = '91th Element, Mass of 231.04, **Lanthanoid**\nProtactinium was first identified in 1913 by **Kazimierz Fajans and Oswald Helmuth Göhring.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998911327272983.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def U(ctx):
  em = discord.Embed(title = '**Uranium**', description = '92th Element, Mass of 238.03, **Lanthanoid**\n**Martin Heinrich Klaproth** was a German chemist who discovered uranium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998950375587881.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Np(ctx):
  em = discord.Embed(title = '**Neptunium**', description = '93th Element, Mass of 237, **Lanthanoid**\nNeptunium was discovered by **Edwin McMillan and Philip Abelson** in 1940.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998967928750184.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Pu(ctx):
  em = discord.Embed(title = '**Plotunium**', description = '94th Element, Mass of 244, **Lanthanoid**\nPlutonium was discovered in 1941 by scientists **Joseph W. Kennedy, Glenn T. Seaborg, Edward M. McMillan and Arthur C. Wohl** at the University of California, Berkeley. The discovery occurred when the team **bombarded uranium-238 with deuterons** that had been accelerated in a **cyclotron device**, which created **neptunium-238 and two free neutrons**. The neptunium-238 then **decayed into plutonium-238** through beta decay. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998986611228673.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Am(ctx):
  em = discord.Embed(title = '**Americium**', description = '95th Element, Mass of 243, **Lanthanoid**\nAmericium was first **produced in 1944 by the group of Glenn T. Seaborg from Berkeley, California,** at the Metallurgical Laboratory of the University of Chicago, a part of the Manhattan Project.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806999002138279938.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cm(ctx):
  em = discord.Embed(title = '**Curium**', description = '96th Element, Mass of 247, **Lanthanoid**\nCurium was first intentionally produced and identified in July 1944 by the **group of Glenn T. Seaborg at the University of California, Berkeley.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293411362209812.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Bk(ctx):
  em = discord.Embed(title = '**Berkelium**', description = '97th Element, Mass of 247, **Lanthanoid**\nAlthough very small amounts of berkelium were possibly produced in previous nuclear experiments, it was first intentionally synthesized, isolated and identified in December 1949 by Glenn T. Seaborg, Albert Ghiorso, Stanley G. Thompson, and Kenneth Street, Jr.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293439963430953.png?v=1')
  em.set_footer(text="Berkeley and Seaborg now")
  await ctx.send(embed = em)

@client.command()
async def Cf(ctx):
  em = discord.Embed(title = '**Californium**', description = '98th Element, Mass of 251, **Lanthanoid**\n It was discovered in 1950 by the **researchers of University of California, Berkeley.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293504198934552.png?v=1')
  em.set_footer(text = "Berkeley shoutouts galore")
  await ctx.send(embed = em)

@client.command()
async def Es(ctx):
  em = discord.Embed(title = '**Einsteinium**', description = '99th Element, Mass of 252/254, **Lanthanoid**\nEinsteinium was **discovered as a component of the debris** of the first hydrogen bomb explosion in 1952, and **named after Albert Einstein.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293534545379338.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fm(ctx):
  em = discord.Embed(title = '**Fermium**', description = '100th Element!!, Mass of 257, **Lanthanoid**\nFermium was first observed in the fallout from the Ivy Mike nuclear test. The element was **named after Enrico Fermi.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293586600624148.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Md(ctx):
  em = discord.Embed(title = '**Mendelevium**', description = '101th Element, Mass of 258, **Lanthanoid**\nMendelevium, the **ninth transuranium element of the actinide series** to be discovered, was **first identified by Seaborg** and others in 1955 as a product of the bombardment of the einsteinium isotope 253 Es with helium ions.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295147468390470.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def No(ctx):
  em = discord.Embed(title = '**Nobelium**', description = '102th Element, Mass of 259, **Lanthanoid**\nNobelium is named after Alfred Nobel, the inventor of dynamite. The element was officially discovered in April 1958 in Berkeley, California, by Albert Ghiorso, Glenn Seaborg, Torbørn Sikkeland and John R. Walton.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295176645017640.png?v=1')
  em.set_thumbnail(text = "Seaborg is a madman")
  await ctx.send(embed = em)

@client.command()
async def Lr(ctx):
  em = discord.Embed(title = '**Lawrencium**', description = '103th Element, Mass of 262, **Lanthanoid**\n Lawrencium was discovered at the University of California, Berkeley, by **Albert Ghiorso, Torbjørn Sikkeland, Almon E. Larsh and Robert M. Latimer in 1961.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295198635098124.png?v=1')
  em.set_footer(text = "berkeley madness")
  await ctx.send(embed = em)

@client.command()
async def Rf(ctx):
  em = discord.Embed(title = '**Rutherfordium**', description = '104th Element, Mass of 261/267, **Transition Metal**\nRutherfordium was the first transactinide or super-heavy element to be discovered. Rutherfordium **may first have been synthesized in 1964** when a team of scientists at Dubna, Russia, led by Georgy Flerov, **bombarded a plutonium target** with neon ions.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295217425317889.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Db(ctx):
  em = discord.Embed(title = '**Dubnium**', description = '105th Element, Mass of 268, **Transition Metal**\nDubnium does not occur naturally on Earth and is **produced artificially.** The Soviet Joint Institute for Nuclear Research **(JINR) claimed the first discovery of the element in 1968**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295240201437186.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Sg(ctx):
  em = discord.Embed(title = '**Seaborgium**', description = '106th Element, Mass of 266, **Transition Metal**\nSeaborgium was **discovered by Albert Ghiorso and others** in 1974 at The Lawrence Berkeley Laboratory in California', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298519945838603.png?v=1')
  em.set_footer(text="He has his own element...")
  await ctx.send(embed = em)

@client.command()
async def Bh(ctx):
  em = discord.Embed(title = '**Bohrium**', description = '107th Element, Mass of 264, **Transition Metal**\nBohrium was first **discovered by a team of scientists in Dubna, Russia, in 1976.** The discovery was **confirmed by Peter Armbruster, Gottfried Münzenber and their team** working in Darmstadt, Germany, in 1981.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298541457244290.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Hs(ctx):
  em = discord.Embed(title = '**Hassium**', description = '108th Element, Mass of 269, **Transition Metal**\nIt was discovered in 1984 by two famous German physicists **Peter Armbruster and Gottfried Munzenber.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298715798470699.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mt(ctx):
  em = discord.Embed(title = '**Meitnerium**', description = '109th Element, Mass of 268, **Transition Metal**\nMeitnerium was **first synthesized on August 29, 1982** by a German research team led by **Peter Armbruster and Gottfried Münzenberg.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298735620882482.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ds(ctx):
  em = discord.Embed(title = '**Darmstadtium**', description = '110th Element, Mass of 281, **Transition Metal**\nDarmstadtium was first **created on November 9, 1994**, at the Institute for Heavy Ion Research in Darmstadt, Germany, by **Peter Armbruster and Gottfried Münzenberg**, under the direction of Sigurd Hofmann.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298754495381595.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Rg(ctx):
  em = discord.Embed(title = '**Roentgenium**', description = '111th Element, Mass of 282, **Transition Metal**\n: Roentgenium is named for **scientist Wilhelm Conrad Röentgen, who discovered X-rays.** It is discovered by the **Gesellschaft fur Schwerionenforschung team** led by Peter Armbruster and Gottfried Münzenber in late 1994.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319083724832769.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Cn(ctx):
  em = discord.Embed(title = '**Copernicium**', description = '112th Element, Mass of 285, **Transition Metal**\nCopernicium was first **made by research scientists led by Sigurd Hofmann at the Heavy Ion Research Laboratory** in Darmstadt, Germany in 1996.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319128355766322.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Nh(ctx):
  em = discord.Embed(title = '**Nihonium**', description = '113th Element, Mass of 286, **Other Metal**\nNihonium was discovered on **August 12, 2012 by Kosuke Morita’s RIKEN collaborative team** in Japan. It was the first chemical **element ever discovered in Asia.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319155892158544.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Fl(ctx):
  em = discord.Embed(title = '**Flerovium**', description = '114th Element, Mass of 289, **Other Metal**\nThe element is **Named after the Flerov Laboratory of Nuclear Reactions of the Joint Institute for Nuclear Research in Dubna, Russia**, where the element was **discovered in 1998.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319188757676072.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Mc(ctx):
  em = discord.Embed(title = '**Moscovium**', description = '115th Element, Mass of 288, **Other Metal**\nIt was created and **announced by scientists at the Joint Institute for Nuclear Research** in Dubna, Russia, and scientists at the Lawrence **Livermore National Laboratory** in the United States.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319204868128768.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Lv(ctx):
  em = discord.Embed(title = '**Livermorium**', description = '116th Element, Mass of 293, **Other Metal**\nIt was discovered in 2000 by by science **teams led by Yuri Oganessian and Ken Moody.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319250514739220.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Ts(ctx):
  em = discord.Embed(title = '**Tennessine**', description = '117th Element, Mass of 294, **Halogen**\nTennessine was discovered by **scientists at Vanderbilt, the University of Tennessee and Oak Ridge National Laboratory.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319266311012413.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def Og(ctx):
  em = discord.Embed(title = '**Oganesson**', description = '118th Element (finally we are done!), Mass of 294, **Noble Gas**\nThe first to claim the discovery of oganesson was **Polish physicist Robert Smolańczuk**, who published a report of his discovery in 1998. According to the physicist, **he discovered oganesson during the fusion of atomic nuclei** that form the synthesis of superheavy atoms.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319288561008711.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['raid', 'shadow', 'legends'])
async def rsl(ctx):
  await ctx.author.send('**This message is sponsored by Raid Shadow Legends, one of the biggest mobile role-playing games of 2021 and it is totally free! Currently almost 10 million users have joined Raid over the last six months, and it is one of the most impressive games in its class with detailed models, environments and smooth 60 frames per second animations! All the champions in the game can be customized with unique gear that changes your strategic buffs and abilities! The dungeon bosses have some ridiculous skills of their own and figuring out the perfect party and strategy to overtake them is a lot of fun! Currently with over 300,000 reviews, Raid has almost a perfect score on the Play Store! The community is growing fast and the highly anticipated new faction wars feature is now live, you might even find my squad out there in the arena! It is easier to start now than ever with rates program for new players you get a new daily login reward for the first 90 days that you play in the game! So what are you waiting for? Go to the video description, click on the special links and you will get 50,000 silver and a free epic champion as part of the new player program to start your journey! Good luck and I will see you there!**')

@client.command(aliases = ['hug', 'hugs'])
async def freehugs(ctx):
  await ctx.author.send("https://tenor.com/view/running-hug-embrace-imiss-you-good-to-see-you-again-gif-15965620")

@client.command()
async def bruh(ctx, *, member : discord.Member):
  bruh = ['https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825', 'https://tenor.com/view/get-stick-bugged-lol-gif-18023988', 'https://tenor.com/view/distraction-henry-stickman-gif-18396154']
  await member.send(f'{random.choice(bruh)}')

@client.command()
async def gif(ctx):
  gifs = ['https://tenor.com/view/carbon-is-highly-reactive-with-other-elements-sensitive-responsive-active-neil-degrasse-tyson-gif-15827677', 'https://tenor.com/view/massiveunregulatednitrogendioxide-gif-19415452', 'https://tenor.com/view/drinks-margarita-liquid-nitrogen-dry-ice-gif-3384966', 'https://tenor.com/view/mundschutz-mask-breathe-gif-17200590','https://tenor.com/view/gold-rich-daffy-duck-money-gif-10195329',]
  await ctx.send(f'For the love of science and elements {random.choice(gifs)}')

@client.command(aliases = ['bill', 'nye'])
async def billnye(ctx):
  billnye_gifs = ['https://tenor.com/view/bill-nye-billnye-sciencerules-science-gif-5866727',  'https://tenor.com/view/bill-nye-party-horn-confetti-sarcastic-like-child-gif-5499505', 'https://tenor.com/view/bill-nye-head-explode-mindblown-gif-4903176', 'https://tenor.com/view/tongue-out-crazy-gif-11927272', 'https://tenor.com/view/memes-bill-nye-the-science-gif-5930649', 'https://tenor.com/view/mic-drop-drop-the-mic-serious-boss-bill-nye-gif-8166361', 'https://tenor.com/view/bill-nye-bill-nye-the-science-guy-scienceguy-consider-gif-7391226', 'https://tenor.com/view/dance-bill-nye-bill-nye-the-science-guy-bill-nye-dance-dancing-gif-5603636', 'https://tenor.com/view/bill-nye-science-fuck-yeah-balloon-suggestive-gif-5410510', 'https://tenor.com/view/bill-nye-science-science-guy-gif-5410511', 'https://tenor.com/view/nonsense-bill-nye-wtf-gif-8493714', 'https://tenor.com/view/bill-nye-science-guy-safety-glasses-off-gif-15789510', 'https://tenor.com/view/bill-nye-bill-nye-the-science-guy-science-slut-wink-gif-7731218']
  await ctx.send(f'You cannot have enough Bill Nye {random.choice(billnye_gifs)}')

@client.command(aliases = ['vote'])
async def upvote(ctx):
  em = discord.Embed(title = '**UPVOTE ME PLEASE :pleading_face:**',description = '**top.gg**\nhttps://top.gg/bot/767190721534361631/vote\n**Discord Bot List**\nhttps://discordbotlist.com/bots/quacc-ducc/upvote', color = discord.Color.orange())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
  em.set_footer(text="Upvote me for 69 years of good luck!")
  await ctx.send(embed = em)



@client.command()
async def quack(ctx, *, member : discord.Member):

    await member.send(":duck: :duck: **I think you just got quacked ohhhh** :duck: :duck:")

@client.command(aliases = ['dmitri'])
async def mendeleev(ctx):
  em = discord.Embed(title = '**Dmitri Ivanovich Mendeleev was a Russian chemist and inventor. He is best remembered for formulating the Periodic Law and creating a farsighted version of the periodic table of elements.**', description = 'http://en.wikipedia.org/wiki/Dmitri_Mendeleev\nhttps://www.britannica.com/biography/Dmitri-Mendeleev\nhttps://www.biography.com/scientist/dmitri-mendeleyev', color = discord.Color.red())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806396194196029460.png?v=1')
  em.set_footer(text="That is one of the best beards I have seen no doubt")
  await ctx.send(embed = em)

@client.command()
async def invite(ctx):
  ctx.send('https://bit.ly/39O9N7t HOPING TO REACH 100 SERVERS :pray:')

@client.command(aliases = ['soc'])
async def socials(ctx):
  em = discord.Embed(title = '**QuackerDeezlesYT Socials**',description = '**YouTube Channel**\nhttps://www.youtube.com/channel/UC6PKOburRMFSjwTCQcL4wbQ?view_as=subscriber', color = discord.Color.orange())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
  em.set_footer(text="Like and subscribe!")
  await ctx.send(embed = em)

@client.command(aliases = ['site', 'website'])
async def botsite(ctx):
  em = discord.Embed(title = '**PERIODICCIA WEBSITE**', description ='https://periodiccia.squarespace.com - Password: periodiccia', color = discord.Color.green())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  em.set_footer(text="This video is sponsored by SquareSpace.")
  await ctx.send(embed = em)

@client.command(aliases = ['serv', 'guild'])
async def server(ctx):
  em = discord.Embed(title = '**Official Periodiccia Server**', description ='https://discord.gg/W6JHRPWvJd **STILL UNDER CONSTRUCTION**', color = discord.Color.purple())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806306254460420127.png?v=1')
  em.set_footer(text="JOIN JOIN JOIN")
  await ctx.send(embed = em)

@client.command(aliases = ['periodictable', 'periodic'])
async def table(ctx):
  await ctx.send(file = discord.File("periodictable2.jpg"))

@client.command(aliases = ['speak', 'talk', 'message'])
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@client.command()
async def like(ctx):
  await ctx.send('Juan or Rhino...')

@client.command(aliases = ['bio', 'dev'])
async def devbio(ctx, page = 1):
  if page == 1:

    em = discord.Embed(title = 'This is QuackerDeezlesYT', description = '**Page 1 of 3 - About Me**\n\n**I am a math fanatic, hardcore music lover, Geometry Dash and Fall Guys gamer, and puzzle enthusiast.**\n\n**More on the Music Aspect**\n\nI do everything; make music, listen to music, and learn music! My favorite music to listen is EDM (which covers Dubstep, Drum and Bass, and Trap) as well as Hiphop/R&B. I play the piano (for 10.5 years and counting) and percussion (for 4 years and counting). I make sure that with playing music and listening music, I keep learning more and more music theory. I also just started composing my own EDM music, and posting them on SoundCloud and YouTube.\n\n**More on the Video Games Aspect**\n\nI have been playing **Geometry Dash** for the past 6-7 years. I have actually spent 8 dollars on that game without in-app purchases; First few years on an iPad, then a year on my phone, and currently I play the game on my PC for the past 2 months and counting. My hardest level I have ever completed is 11 Demon EA, a hard demon. The game is so amazing, which is why I have played it for such a long time!\n\n**Fall Guys** is one, amazing feel-good game. I got the game right when I got my PC, and I have been playing it ever since. It is super fun, just hoping that there would be constant updates. Otherwise, 10/10.\n\nIf you have any good video game recommendations, DM Me!', color = discord.Color.purple())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
    em.set_footer(text="This is as long as an essay")
    await ctx.send(embed = em)
  elif page == 2:
    
    em = discord.Embed(title = 'This is QuackerDeezlesYT', description = '**Page 2 of 3 - Discord Experience**\n\n**Why did I decide to build Periodiccia?**\n\nTo be honest, I never liked programming. For who I want to be, writing random abbreviations was at the bottom of my priority list. A few months after I made a Discord account, I planned on making a Discord Bot. It felt fun seeing people type commands and in an instant my bot will respond, so why not try it out?\n\nIf you go to the URL of DiscordBotLists vote page (not top.gg) you will see quacc-ducc and not periodiccia. Quacc Ducc was 1.0, a bot with literally no purpose. It was not going well and was offline most of the time. I decided to take a stand. One of the commands of Quacc Ducc was `elem`, which would give out information about the Elements, similar to what Periodiccia is doing right now. I got a thought - why not make a bot just on this? I worked super hard on it, and it is paying off, with people constantly using it. I am realizing that me not trying out programming could have blocked a door that I have myself opened.\n\n**Moderation**\n\nI am an admin of 3 servers with member counts of 200, 260, 110, 70, and 40. Those servers are the ones I advertised on the third page of this bio, you can find them by typing `p devbio 3`. In addition to this, I am a Stream Moderator of 2 streamers with follower counts 200 and 350.\n\nI will be very happy if you make me a staff member in your server! Would be truly appreciated :grinning:', color = discord.Color.purple())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
    em.set_footer(text="I approve. He is a good moderator and yes, I was Quacc Ducc. Quacc Ducc will be remembered.")
    await ctx.send(embed = em)

  elif page == 3:
    
    em = discord.Embed(title = 'This is QuackerDeezlesYT', description = '**Page 3 of 3 - Recommended Servers**\n\nhttps://discord.gg/Xt8UQj2neY - 200 MEMBERS\n\n**__60hz Gang__** is a fun, inclusive community who loves all things Geometry Dash, a rhythm and music based game. The community that we hold is very friendly and loves to help people make levels, complete levels, collaborate with others, and to be there for any help. We would love you to join - and so would you!\n\nhttps://discord.com/invite/hDghRHmpnQ - 260 MEMBERS\n\nWelcome to **__Gumball Nation__**! A gaming, community server designed to have fun and no other reason. We also encourage Dank Memers to join to meet other Dank Memers!\n\nhttps://discord.gg/edQYThXvBt - 70 MEMBERS\n\nWe are __**TAL9988s Lounge**__, a server by the streamer and youtuber TAL9988.\n\nhttps://discord.gg/KwdnHrxBZf - 40 MEMBERS\n\nWe are __**Good Boi Kingdom**__, a Dank Memer and chill Server, brothers with Gumball Nation!', color = discord.Color.purple())
    em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/808451191779622972.png?v=1')
    em.set_footer(text="JOIN JOIN JOIN V2")
    await ctx.send(embed = em)


keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)
