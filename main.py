import discord
import keep_alive
import os
import random
from discord.ext import commands

client = commands.Bot(commands.when_mentioned_or("p "), case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("p help | I am back up and running"))
    for x in client.guilds:
      print(x.name)

@client.event
async def on_guild_join(guild):
	try:
		if guild.system_channel:
			await guild.system_channel.send(f'Hey! My name is Periodiccia! I am a Periodic Table of Elements discord bot. `p help` opens up the help page, and I will guide you through the modules I have! :sunglasses:\nMade by <@704506180273438721>')
	except:
		pass
	print("yo hopped in a new server less go")

@client.command(aliases = ['huh', 'what'])
async def help(ctx, args = None):
 if not args:
  em = discord.Embed(title = 'Welcome to Periodiccia! :D', url = "https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot", description = '**Here are my modules (chem, utility, rand, websearch).**',  color = discord.Color.purple())
  em.add_field(name = ':microscope: Chemistry Command List', value = '`p help chem`', inline = False)
  em.add_field(name = '<:settings:585767366743293952> Utility Command List', value = '`p help utility`', inline = False)
  em.add_field(name = ':game_die: Random Command List', value = '`p help rand`', inline = False)
  em.add_field(name = ':globe_with_meridians: Web Search Command List', value = '`p help websearch`', inline = False)
  em.add_field(name = 'Need help?', value = 'DM the head developer, <@704506180273438721>', inline = False)
  em.add_field(name = 'Invite me!', value = '[Click here](https://bit.ly/39O9N7t)', inline = False)
  em.add_field(name = 'Join my official server!', value = '[Click here](https://bit.ly/3b4JbPd)', inline = False)
  em.add_field(name = 'Vote me on top.gg!', value = '[Click here](https://top.gg/bot/767190721534361631/vote)', inline = False)
  em.add_field(name = 'Fun Fact:', value = 'My pronouns are she/her!', inline = False)
  em.set_footer(text = 'None of the links are rickrolls.')
  em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
  await ctx.send(embed = em)
 else:
  if args == 'chem':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', url = "https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot", description = '**:microscope: __Chemistry Commands__**\n\n - `p <element_symbol>` or `p <atomic_number>` - Gives information about an element\n - `p elements <page_number>` - Reference to symbols to use for the element commands. **12 pages**\n - `p bonds` - Explains the four types of bonds between molecules.\n - `p valence` (aliases = `val`, `electron`) - Explains what valence electrons are.\n - `p elemgroup` - Gives information about the groups of elements found in the Periodic Table (example: Transition Metal)!\n - `p mendeleev` (aliases = `dmitri`) - This command tells you a bit about who Mendeleev is, and some helpful resources to learn more about him.\n - `p lightningmyth` - A random lightning myth and a fact to go along with it.\n - `p table` - The Periodic Table of Elements as an image.', color = discord.Color.purple())
    em.set_image(url="https://cdn.discordapp.com/attachments/831783191198957613/833831137809006663/periodiccia-High-Quality.jpg")
    await ctx.send(embed = em)
  elif args == 'utility':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', url = "https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot", description = '<:settings:585767366743293952> **__Utility Commands__**\n\n - `p about` - See who I am!\n - `p yt` (aliases = `p quacker`) - His YouTube!\n - `p ping` - Check out the latency!\n - `p invite` - My invite link!\n - `p servcount` - Find how many servers I am in!\n - `p readdocs` (aliases = `docs`) - View the Discord documentation of popular programming Discord API languages\n - `p gitrepo` (aliases = `repo`, `repository`) - View my official GitHub Repository\n - `p vote` - Please vote me on top.gg!\n - `p server` (aliases = `serv`, `guild`) - My Official Server! :D\n\n<:pin_unread:658538492548218890> A Helpful Video made by my Dev: https://www.youtube.com/watch?v=yaaj5PkE290', color = discord.Color.purple())
    em.set_image(url="https://cdn.discordapp.com/attachments/831783191198957613/833831123431849994/periodiccia-High-Quality_1.jpg")
    await ctx.send(embed = em)
  elif args == 'rand':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', url = "https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot", description = '**:game_die: __Random Commands__**\n\n - `p simprate` (aliases = `simp`) - Rate how much of a simp are you\n - `p waifurate` (aliases = `waifu`) - Rate how much of a waifu are you\n - `p progamer` (aliases = `gamer`, `gamerrate`, `progamerrate`) - Rate how much of a gamer are you\n - `p randyt` (aliases = `randomyoutube`) - Gives a random popular YouTuber\'s channel link for you to check out\n - `p randtwitch` (aliases = `randomtwitch`) - Gives a random popular Twitch streamer\'s channel for you to check out\n - `p randletter <letter_count>` (aliases = `letter`, `randomletter`) - Sends a random string of letters (up to 10) at once.\n\n - `p coinflip` (aliases = `coin`, `flip`) - What side?\n - `p die` (aliases = `roll`) - Roll the die!\n - `p rng <any_integer>` - RNG from 1 to your number', color = discord.Color.purple())
    em.set_image(url="https://cdn.discordapp.com/attachments/778322617211289653/837876280707383346/periodiccia-High-Quality_4.jpg")
    await ctx.send(embed = em)
  elif args == 'websearch':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', url = "https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot", description = '**:globe_with_meridians: __Web Search Commands__**\n\nSearch popular websites without any hassle!\n**Syntax:** `p <command_name> <search_text>`\n\n`topgg`, `youtube`, `urban`, `wiki`, `twitch`, `tiktok`, `insta`, `twitter`, `soundcloud`, `amazon`, `wired`, `fortune`, `nytimes`, `espn`, `msft`, `github`, `forbes`, `stackoverflow`, `quora`, `theverge`, `history`, `natgeo`, `mrktwatch`, `reddit`, `medium`\n\nPlease do not misuse the commands!', color = discord.Color.purple())
    em.set_image(url="https://cdn.discordapp.com/attachments/841743778347614249/842990566836666388/periodiccia-High-Quality_5.jpg")
    em.set_footer(text="If you have any popular websites you want me to feature in this module, let my developer know through DMs or the support server!")
    await ctx.send(embed = em)
  elif args == 'web':
    em = discord.Embed(title = '__Welcome to Periodiccia!__', url = "https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot", description = '**:globe_with_meridians: __Web Search Commands__**\n\nSearch popular websites without any hassle!\n**Syntax:** `p <command_name> <search_text>`\n\n`topgg`, `youtube`, `urban`, `wiki`, `twitch`, `tiktok`, `insta`, `twitter`, `soundcloud`, `amazon`, `wired`, `fortune`, `nytimes`, `espn`, `msft`, `github`, `forbes`, `stackoverflow`, `quora`, `theverge`, `history`, `natgeo`, `mrktwatch`, `reddit`, `medium`\n\nPlease do not misuse the commands!', color = discord.Color.purple())
    em.set_image(url="https://cdn.discordapp.com/attachments/841743778347614249/842990566836666388/periodiccia-High-Quality_5.jpg")
    em.set_footer(text="If you have any popular websites you want me to feature in this module, let my developer know through DMs or the support server!")
    await ctx.send(embed = em)
  else:
    pass

@client.command(aliases = ['1'])
async def H(ctx):
  em = discord.Embed(title = '**Hydrogen**', description = '1st Element, Mass of 1.008\n**Henry Cavendish FRS** was an English natural philosopher, scientist, and an important experimental and theoretical chemist and physicist. He is noted for his **discovery of hydrogen**, which he termed "inflammable air".', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806237831613775885.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['2'])
async def He(ctx):
  em = discord.Embed(title = '**Helium**', description = '2nd Element, Mass of 4.0026, **Noble Gas**\nThe first **evidence of helium** was obtained on August 18th, 1868 by French **astronomer Jules Janssen.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806566745980665926.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['3'])
async def Li(ctx):
  em = discord.Embed(title = '**Lithium**', description = '3rd Element, Mass of 6.94, **Alkali Metal**\n**Johan August Arfwedson** was a **Swedish chemist** who discovered the **chemical element lithium** in 1817 by **isolating it as a salt.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806567984415768678.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['4'])
async def Be(ctx):
  em = discord.Embed(title = '**Beryllium**', description = '4th Element, Mass of 9.0122, **Alkaline Earth Metal**\nBeryllium was discovered by French **pharmacist Louis Nicolas Vanquelin** in 1798. He determined that this new metal was a **component of beryl and emeralds.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806569567593168906.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['5'])
async def B(ctx):
  em = discord.Embed(title = '**Boron**', description = '5th Element, Mass of 10.81, **Metalloid**\n**Boron** was discovered by **Joseph-Louis Gay-Lussac and Louis-Jaques Thénard**, French chemists, and **independently by Sir Humphry Davy**, an English chemist, in 1808. They all **isolated boron by combining boric acid with potassium.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806572191826968656.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['6'])
async def C(ctx):
  em = discord.Embed(title = '**Carbon**', description = '6th Element, Mass of 12.011, **Nonmetal**\nUnfortunately, **no one knows who discovered carbon.** It is one of the few elements that was known since ancient times. The **earliest use of carbon** was sometime around **3750 BC.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806609579890835466.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['7'])
async def N(ctx):
  em = discord.Embed(title = '**Nitrogen**', description = '7th Element, Mass of 14.077, **Nonmetal**\n**Daniel Rutherford** was a Scottish **physician, chemist and botanist** who is known for the isolation of **nitrogen in 1772.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610043762901042.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['8'])
async def O(ctx):
  em = discord.Embed(title = '**Oxygen**', description = '8th Element, Mass of 15.999, **Nonmetal**\n**Oxygen was discovered about 1772** by a Swedish chemist, **Carl Wilhelm Scheele**, who obtained it by **heating potassium nitrate, mercuric oxide, and many other substances.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610357668937748.png?v=1' )
  await ctx.send(embed = em)

@client.command(aliases = ['9'])
async def F(ctx):
  em = discord.Embed(title = '**Flourine**', description = '9th Element, Mass of 18.998, **Halogen**\n**Ferdinand Frédéric Henri Moissan** was a French chemist and pharmacist who **won the 1906 Nobel Prize** in Chemistry for his work in **isolating fluorine from its compounds**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806610601761570836.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['10'])
async def Ne(ctx):
  em = discord.Embed(title = '**Neon**', description = '10th Element, Mass of 20.180, **Noble Gas**.\nWho discovered **neon**? In 1898, English chemist **Morris W. Travers** and Scottish chemist **William Ramsay** discovered this all-important chemical element in the City of London in England.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806611638672949269.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['11'])
async def Na(ctx):
  em = discord.Embed(title = '**Sodium**', description = '11th Element, Mass of 22.990, **Alkali Metal**\n**Sir Humphry Davy**, a British chemist, discovered **sodium in 1807**. He found the element by **isolating it from caustic soda using electrolysis.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806611195548794912.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['12'])
async def Mg(ctx):
  em = discord.Embed(title = '**Magnesium**', description = '12th Element, Mass of 23.405, **Alkaline Earth Metal**\n**Joseph Black** was a Scottish **physicist and chemist**, known for his discoveries of magnesium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612129914159114.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['13'])
async def Al(ctx):
  em = discord.Embed(title = '**Aluminum**', description = '13th Element, Mass of 26.982, **Other Metal**\n**Hans Christian Ørsted was a Danish physicist and chemist who discovered that electric currents create magnetic fields, which was the first connection found between electricity and magnetism. Oersteds law and the Oersted are named after him.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612299808636948.png?v=1')
  em.set_footer(text="Ø is the Twenty One Pilots O, that's pretty swag")
  await ctx.send(embed = em)

@client.command(aliases = ['14'])
async def Si(ctx):
  em = discord.Embed(title = '**Silicon**', description = '14th Element, Mass of 28.085, **Metalloid**\n**Silicon** was discovered by **Jöns Jacob Berzelius**, a Swedish chemist, in 1824 by **heating chips of potassium in a silica container** and then carefully **washing away the residual by-products.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612488745386004.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['15'])
async def P(ctx):
  em = discord.Embed(title = '**Phosphorus**', description = '15th Element, Mass of 30.974, **Nonmetal**\n**Hennig Brand** was a German **merchant, pharmacist and alchemist**, who lived and worked in Hamburg. He is the **discoverer of** the chemical element **phosphorus.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612670932975646.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['16'])
async def S(ctx):
  em = discord.Embed(title = '**Sulfur**', description = '16th Element, Mass of 32.06, **Nonmetal**\nThe credit for discovering sulfur is given to **Hennig Brand** (1669), however it was **identified by Antoine Lavoisier in 1777**. But scholars believe that no single person was responsible for discovering this non-metallic element because it has **been in usage since ancient times for alchemy and other purposes.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806612864936181811.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['17'])
async def Cl(ctx):
  em = discord.Embed(title = '**Chlorine**', description = '17th Element, Mass of 35.45, **Halogen**\n**Carl Wilhelm Scheele** is a German Swedish chemist who **independently discovered** oxygen, **chlorine**, and manganese.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806613436347187250.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['18'])
async def Ar(ctx):
  em = discord.Embed(title = '**Argon**', description = '18th Element, Mass of 39.948, **Noble Gas**\n**Sir John Rayleigh**, a peer by inheritance, was a British physicist. He **discovered argon, an inert gas**, that **earned him the 1904 Nobel Prize** in physics award. He is also known for “Rayleigh Scattering.”', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806613620657750086.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['19'])
async def K(ctx):
  em = discord.Embed(title = '**Potassium**', description = '19th Element, Mass of 39.098, **Alkali Metal**\n**Potassium** was discovered in 1807 by British scientist **Sir Humphry Davy**, who derived it from caustic potash where was it discovered and when his first successes came in 1807 with the **separation of potassium from molten potash and of sodium from common salt.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628580200939551.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['20'])
async def Ca(ctx):
  em = discord.Embed(title = '**Calcium**', description = '20th Element, Mass of 40.078, **Alkaline Earth Metal**\nIt was only during the year of 1808 did calcium get isolated and taken as a particular element in itself. And the person who discovered calcium was Englishman **Sir Humphrey Davy.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628602259046480.png?v=1')
  em.set_footer(text="Ayyyy him again")
  await ctx.send(embed = em)

@client.command(aliases = ['21'])
async def Sc(ctx):
  em = discord.Embed(title = '**Scandium**', description = '21th Element, Mass of 44.956, **Transition Metal**\n**Lars Fredrik Nilson** was the discoverer. He discovered scandium in 1879. The name **scandium came from the place it was discovered - Scandinavia**. Lars Fredrik Nilson created 2 grams of high purity scandium oxide.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628627847708683.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['22'])
async def Ti(ctx):
  em = discord.Embed(title = '**Titanium**', description = '22th Element, Mass of 47.867, **Transition Metal**\n**William Gregor** was the British **clergyman and mineralogist** who discovered the elemental metal titanium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628650354475089.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['23'])
async def V(ctx):
  em = discord.Embed(title = '**Vanadium**', description = '23th Element, Mass of 50.942, **Transition Metal**\n**Andrés Manuel del Río y Fernández** was a Spanish–Mexican **scientist, naturalist and engineer** who discovered **compounds of vanadium in 1801.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806628668347777024.png?v=1')
  em.set_footer(text = "That's a pretty long name")
  await ctx.send(embed = em)

@client.command(aliases = ['24'])
async def Cr(ctx):
  em = discord.Embed(title = '**Chromium**', description = '24th Element, Mass of 51.996, **Transition Metal**\n**Chromium was discovered by Louis-Nicholas Vauquelin** while experimenting with a material known as **Siberian red lead**, also known as the mineral **crocoite (PbCrO 4)**, in 1797.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630723296952330.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['25'])
async def Mn(ctx):
  em = discord.Embed(title = '**Manganese**', description = '25th Element, Mass of 54.938, **Transition Metal**\nProposed to be an **element by Carl Wilhelm Scheele in 1774**, manganese was **discovered by Johan Gottlieb Gahn**, a Swedish chemist, by **heating the mineral pyrolusite (MnO 2) in the presence of charcoal** later that year.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630771581779988.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['26'])
async def Fe(ctx):
  em = discord.Embed(title = '**Iron**', description = '26th Element, Mass of 55.845, **Transition Metal**\nUnfortunately, **no one knows who was the first person to discover iron.** Iron has been **used since prehistory.** The Ancient Egyptians and Sumerians began using **iron on the tips of spears and in some ornaments around 4000 BC.** They obtained the **iron from meteorites** that hit the earth.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630803467141151.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['27'])
async def Co(ctx):
  em = discord.Embed(title = '**Cobalt**', description = '27th Element, Mass of 58.933, **Transition Metal**\n**Georg Brandt** was a **Swedish chemist and mineralogist who discovered cobalt.** He was the **first person to discover a metal unknown in ancient times.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630849117814845.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['28'])
async def Ni(ctx):
  em = discord.Embed(title = '**Nickel**', description = '28th Element, Mass of 58.693, **Transition Metal**\n**Axel Fredrik Cronstedt** was a **Swedish mineralogist and chemist** who discovered the **element nickel in 1751** as a **mining expert with the Bureau of Mines.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806630871225860106.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['29'])
async def Cu(ctx):
  em = discord.Embed(title = '**Copper**', description = '29th Element, Mass of 63.546, **Transition Metal**\nUnfortunately, **no one knows who discovered copper.** Copper **occurs in nature uncombined with any other things.** Therefore, it has been recognized and **used by civilizations for thousands of years.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639082914054184.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['30'])
async def Zn(ctx):
  em = discord.Embed(title = '**Zinc**', description = '30th Element, Mass of 65.38, **Transition Metal**\nIn 1746, **German chemist Andreas Marggraf** figured out how to **isolate zinc by heating carbon and calamine** (the stuff in calamine lotion).', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639415828938802.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['31'])
async def Ga(ctx):
  em = discord.Embed(title = '**Gallium**', description = '31th Element, Mass of 69.732, **Other Metal**\n**Paul-Émile Lecoq de Boisbaudran, also called François Lecoq de Boisbaudran**, was a French **chemist known for his discovery of gallium**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639435323539496.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['32'])
async def Ge(ctx):
  em = discord.Embed(title = '**Germanium**', description = '32th Element, Mass of 72.61, **Metalloid**\n**Clemens Alexander Winkler** was a **German chemist** who discovered the **element germanium in 1886**, solidifying Dmitri Mendeleevs theory of periodicity.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639480726880268.png?v=1')
  em.set_footer(text="Mendeleev shoutout woohoo")
  await ctx.send(embed = em)

@client.command(aliases = ['33'])
async def As(ctx):
  em = discord.Embed(title = '**Arsenic**', description = '33th Element, Mass of 74.922, **Metalloid**\nArsenic was discovered by **Albertus Magnus in 1250.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806639501648330765.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['34'])
async def Se(ctx):
  em = discord.Embed(title = '**Selenium**', description = '34th Element, Mass of 78.96, **Metalloid**\n**Selenium was discovered by Jöns Jakob Berzelius** in 1817 as a **byproduct of the production of sulfuric acid.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806736485788287027.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['35'])
async def Br(ctx):
  em = discord.Embed(title = '**Bromine**', description = '35th Element, Mass of 79.004, **Halogen**\nBromine was discovered in 1826 by the **French chemist Antoine-Jérôme Balard** in the **residues from the manufacture of sea salt at Montpellier.** He liberated the element by **passing chlorine through an aqueous solution of the residues, which contained magnesium bromide.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806737203832160336.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['36'])
async def Kr(ctx):
  em = discord.Embed(title = '**Krypton**', description = '36th Element, Mass of 83.80, **Noble Gas**\nKrypton was discovered on May 30, 1898 by **Sir William Ramsay, a Scottish chemist, and Morris M. Travers, an English chemist**, while studying liquefied air.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806737863960952862.png?v=1')
  em.set_footer(text = "SUPERMAN OMGGGG")
  await ctx.send(embed = em)

@client.command(aliases = ['37'])
async def Rb(ctx):
  em = discord.Embed(title = '**Rubidium**', description = '37th Element, Mass of 85.468, **Alkali Metal**\nRubidium was discovered in 1861 by **Robert Bunsen and Gustav Kirchhoff, in Heidelberg, Germany**, in the mineral **lepidolite through flame spectroscopy.** Because of the bright red lines in its emission spectrum, they chose a name derived from the **Latin word rubidus, meaning "deep red".**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738015644418078.png?v=1')
  await ctx.send(embed = em)
  
@client.command(aliases = ['38'])
async def Sr(ctx):
  em = discord.Embed(title = '**Strontium**', description = '38th Element, Mass of 87.62, **Alkaline Earth Metal**\n**Humphry Davy** in London **isolated the soft, silvery metal** of the new element **using electrolysis.** The Scottish village was called Strontian, the mineral found there, strontianite and the **new element strontium.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738197517959169.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['39'])
async def Y(ctx):
  em = discord.Embed(title = '**Yttrium**', description = '39th Element, Mass of 88.906, **Transition Metal**\nYttrium was discovered by **Johan Gadolin, a Finnish chemist**, while **analyzing the composition of the mineral gadolinite** in 1789.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738408671019018.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['40'])
async def Zr(ctx):
  em = discord.Embed(title = '**Zirconium**', description = '40th Element, Mass of 91.224, **Transition Metal**\nIn the Middle Ages colourless **gemstones of zircon were thought to be an inferior kind of diamond**, but that was **shown to be wrong** when a German chemist, **Martin Klaproth (1743-1817), analysed one in 1789** and discovered zirconium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806738696300527656.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['41'])
async def Nb(ctx):
  em = discord.Embed(title = '**Niobium**', description = '41th Element, Mass of 92.906, **Transition Metal**\nNiobium was **discovered in 1801 by Charles Hatchett** in an ore called **columbite** sent to England in the 1750s by John Winthrop the Younger, the first goveror of Connecticut, USA. The metal niobium was **first prepared in 1864** by Blomstrand, who reduced the chloride by **heating it in a hydrogen atmosphere.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814906461720805376.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['42'])
async def Mo(ctx):
  em = discord.Embed(title = '**Molybdenum**', description = '42th Element, Mass of 95.95, **Transition Metal**\nIn 1768, the Swedish scientist **Carl Wilhelm Scheele** determined that **molybdenite was a sulfide compound of an as-yet unidentified element**, by decomposing it in **hot nitric acid** and heating the product in air to yield a **white oxide powder.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806739137947369502.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['43'])
async def Tc(ctx):
  em = discord.Embed(title = '**Technetium**', description = '43th Element, Mass of 98.907, **Transition Metal\nTechnetium was the first **artificially produced element.** It was isolated by **Carlo Perrier and Emilio Segrè in 1937**. Technetium was created by bombarding molybdenum atoms with deuterons that had been accelerated by a device called a **cyclotron.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806739458296381500.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['44'])
async def Ru(ctx):
  em = discord.Embed(title = '**Ruthenium**', description = '44th Element, Mass of 101.07, **Transition Metal**\nRuthenium was discovered by **Karl Karlovich Klaus**, a Russian chemist, in 1844 while analyzing the **residue of a sample of platinum ore** obtained from the Ural mountains.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806740984279859220.png?v=1')
  em.set_footer(text="Triple K: Karl Karlovich Klaus")
  await ctx.send(embed = em)

@client.command(aliases = ['45'])
async def Rh(ctx):
  em = discord.Embed(title = '**Rhodium**', description = '45th Element, Mass of 102.91, **Transition Metal**\nRhodium was discovered by **William Hyde Wollaston**, an English chemist, in 1803 shortly after his discovery of the element palladium. He obtained rhodium from a **sample of platinum ore that was obtained from South America.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806741372124004372.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['46'])
async def Pd(ctx):
  em = discord.Embed(title = '**Palladium**', description = '46th Element, Mass of 106.42, **Transition Metal**\n**William Hyde Wollaston** was an English chemist and physicist who is famous for discovering the chemical elements palladium and rhodium. He also developed a way to process platinum ore into malleable ingots.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806741800853307392.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['47'])
async def Ag(ctx):
  em = discord.Embed(title = '**Silver**', description = '47th Element, Mass of 107.87, **Transition Metal**\nNo one knows who discovered silver, but it was German physicist **Johann Heinrich Schultze** who used **silver nitrate to invent photography in 1727.** Since then, the lustrous Silver element has become **even more precious** as science and technology have discovered more and more uses.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742042054099025.png?v=1')
  await ctx.send(embed = em)
  
@client.command(aliases = ['48'])
async def Cd(ctx):
  em = discord.Embed(title = '**Cadmium**', description = '48th Element, Mass of 112.41, **Transition Metal**\nCadmium was discovered by **Friedrich Strohmeyer**, a German chemist, in 1817 while **studying samples of calamine (ZnCO 3)**. When heated, Strohmeyer noticed that some **samples of calamine glowed with a yellow color while other samples did not.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742338411298887.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['49'])
async def In(ctx):
  em = discord.Embed(title = '**Indium**', description = '49th Element, Mass of 114.82, **Other Metal**\nIndium was discovered in 1863 when **German Chemists Ferdinand Reich and Hieronymous Theodor Richter tested ores from Saxony**,where they worked. They made the discovery after **dissolving the minerals from these ores and testing for thallium**, which was already known at the time, **with spectroscopy.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806745134343520317.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['50'])
async def Sn(ctx):
  em = discord.Embed(title = '**Tin**', description = '50th Element, Mass of 118.71, **Other Metal**\nJames Smith found the **rich deposit of tin at Mount Bischoff.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806743088475144213.png?v=1')
  em.set_footer(text="That's it?")
  await ctx.send(embed = em)

@client.command(aliases = ['51'])
async def Sb(ctx):
  em = discord.Embed(title = '**Antimony??????**', description = '51th Element, Mass of 121.76, **Metalloid**\nNicolas Lémery, a French chemist, was the **first person to scientifically study antimony and its compounds.** He published his findings in 1707. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806743967370182689.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['52'])
async def Te(ctx):
  em = discord.Embed(title = '**Tellerium**', description = '52th Element, Mass of 127.60, **Metalloid**\nTellurium was discovered by **Franz Joseph Müller von Reichenstein**, a Romanian mining official.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806744271704031242.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['53'])
async def I(ctx):
  em = discord.Embed(title = '**Iodine**', description = '53th Element, Mass of 126.90, **Halogen**\nIt was discovered by French chemist **Bernard Courtois in 1811** whereby Gay-Lussac subsequently suggested the name "iode", from the Greek word ιώδες (iodes) for violet, **because of the color of iodine vapor.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806742859163631626.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['54'])
async def Xe(ctx):
  em = discord.Embed(title = '**Xenon**', description = '54th Element, Mass of 131.29, **Noble Gases**\nXenon was discovered in England by the **Scottish chemist William Ramsay and English chemist Morris Travers** in September 1898, shortly after their discovery of the elements krypton and neon. **They found xenon in the residue left over from evaporating components of liquid air.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806745520797384764.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['55'])
async def Cs(ctx):
  em = discord.Embed(title = '**Cesium**', description = '55th Element, Mass of 132.91, **Alkali Metal**\nCesium was discovered by **Robert Wilhelm Bunsen and Gustav Robert Kirchhoff**, German chemists, in 1860 through the **spectroscopic analysis of Durkheim mineral water.** They named cesium after the **blue lines** they observed in its **spectrum.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746036362149939.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['56'])
async def Ba(ctx):
  em = discord.Embed(title = '**Barium**', description = '56th Element, Mass of 137.33, **Alkaline Earth Metal**\n**Vincenzo Casciarolo, a 17th-century Italian alchemist,** first noticed barium in the form of **unusual pebbles that glowed** for years after exposure to heat.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746477622722610.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['57'])
async def La(ctx):
  em = discord.Embed(title = '**Lanthanium**', description = '57th Element, Mass of 138.91, **Lanthanoid**\nLanthanum was discovered by **Carl Gustaf Mosander, a Swedish chemist**, in 1839. Mosander was searching for **impurities** he believed existed within **samples of cerium**. He treated **cerium nitrate with dilute nitric acid** and found a new substance he **named lanthana.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806746907807318016.png?v=1')
  em.set_footer(text = "Lanthanium is a lanthanoid. Pretty simple fact.")
  await ctx.send(embed = em)

@client.command(aliases = ['58'])
async def Ce(ctx):
  em = discord.Embed(title = '**Cerium**', description = '58th Element, Mass of 140.12, **Lanthanoid**\nCerium was discovered in 1803 by **Jacob Berzelius and Wilhelm von Hisinger in Sweden**. They discovered the new element in a **rare reddish-brown mineral** now known as cerite, a cerium-lanthanide silicate.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747109360795649.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['59'])
async def Pr(ctx):
  em = discord.Embed(title = '**Praseodymium**', description = '59th Element, Mass of 140.91, **Lanthanoid**\n**Carl Auer von Welsbach** (1858–1929), discovered praseodymium in 1885.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747420624027718.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['60'])
async def Nd(ctx):
  em = discord.Embed(title = '**Neodynium**', description = '60th Element, Mass of 144.25, **Lanthanoid**\nAustrian chemist **Carl Auer von Welsbach** discovered neodymium in 1885 by separating **ammonium didymium nitrate prepared from didymia** (a mixture of rare-earth oxides) into a **neodymium fraction and a praseodymium fraction by repeated crystallization.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806747639017766922.png?v=1')
  em.set_footer(text="That sounds very complex to me.")
  await ctx.send(embed = em)

@client.command(aliases = ['61'])
async def Pm(ctx):
  em = discord.Embed(title = '**Promethium**', description = '61th Element, Mass of 145, **Lanthanoid**\nPromethium was the **last rare earth element of the lanthanide series** to be discovered. It was discovered in 1945 by **Jacob A. Marinsky, Lawrence E. Glendenin, and Charles D. Coryell**, although its existence had been predicted in 1902 by Czech chemist Bohuslav Brauner.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954923534712854.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['62'])
async def Sm(ctx):
  em = discord.Embed(title = '**Samarium**', description = '62th Element, Mass of 150.36, **Lanthanoid**\nSamarium was discovered in 1879 by the **French chemist Paul-Émile Lecoq de Boisbaudran** and named after the mineral samarskite from which it was isolated.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954959626567710.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['63'])
async def Eu(ctx):
  em = discord.Embed(title = '**Europium**', description = '63th Element, Mass of 151.96, **Lanthanoid**\nEuropium was first **found in 1892 by Paul Émile Lecoq de Boisbaudran**, who obtained basic fractions from samarium-gadolinium concentrates which had **spectral lines not accounted** for by samarium or gadolinium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806954988865585172.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['64'])
async def Gd(ctx):
  em = discord.Embed(title = '**Gadolinium**', description = '64th Element, Mass of 157.25, **Lanthanoid**\nGadolinium was **discovered in 1880 by Jean Charles de Marignac**, who detected its oxide by using **spectroscopy**. It is named after the mineral gadolinite, one of the **minerals in which gadolinium is found.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806955066371473459.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['65'])
async def Tb(ctx):
  em = discord.Embed(title = '**Terbium**', description = '65th Element, Mass of 158.93, **Lanthanoid**\n**Swedish chemist Carl Gustaf Mosander discovered terbium** in 1843. He detected it as an **impurity in yttrium oxide**. Yttrium is **named after the village of Ytterby** in Sweden. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806955083731828737.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['66'])
async def Dy(ctx):
  em = discord.Embed(title = '**Dysprosium**', description = '66th Element, Mass of 162.50, **Lanthanoid**\nDysprosium was first **identified in 1886 by Paul Émile Lecoq de Boisbaudran**, but it was **not isolated** in pure form until the **development of ion-exchange techniques** in the 1950s.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814920279892951070.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['67'])
async def Ho(ctx):
  em = discord.Embed(title = '**Holmium**', description = '67th Element, Mass of 164.93, **Lanthanoid**\nHolmium was discovered through isolation by **Swedish chemist Per Theodor Cleve and independently by Jacques-Louis Soret and Marc Delafontaine** who observed it **spectroscopically** in 1878.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956660878082139.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['68'])
async def Er(ctx):
  em = discord.Embed(title = '**Erbium**', description = '68th Element, Mass of 167.26, **Lanthanoid**\nErbium was **discovered by Carl Gustaf Mosander** in 1843. Mosander was working with a sample of what was thought to be the **single metal oxide yttria, derived from the mineral gadolinite.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956695682809897.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['69'])
async def Tm(ctx):
  em = discord.Embed(title = '**Thulium**', description = '69th Element, Mass of 168.93, **Lanthanoid**\nThulium was **discovered in 1879 by Per Teodor Cleve**, who named the oxide thulia after an ancient name for Scandinavia.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956747393597441.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['70'])
async def Yb(ctx):
  em = discord.Embed(title = '**Ytterbium**', description = '70th Element, Mass of 173.05, **Lanthanoid**\nYtterbium was discovered by the **Swiss chemist Jean Charles Galissard de Marignac** in the year 1878. While examining samples of gadolinite, Marignac found a new component in the earth then known as erbia, and **he named it ytterbia, for Ytterby, the Swedish village near where he found the new component of erbium.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806956775248101387.png?v=1')
  em.set_footer(text = "When Ytterby gets all the recognition")
  await ctx.send(embed = em)

@client.command(aliases = ['71'])
async def Lu(ctx):
  em = discord.Embed(title = '**Lutetium**', description = '71th Element, Mass of 174.97, **Lanthanoid**\nLutetium was independently discovered in 1907 by French scientist **Georges Urbain**, Austrian mineralogist **Baron Carl Auer von Welsbach**, and American chemist **Charles James**. All of these researchers found lutetium as an **impurity** in the mineral ytterbia.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814924472015519754.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['72'])
async def Hf(ctx):
  em = discord.Embed(title = '**Hafnium**', description = '72th Element, Mass of 178.49, **Transition Metal**\nHafnium was **discovered by Dirk Coster**, a Danish chemist, and **George Charles de Hevesy**, a Hungarian chemist, in 1923. They used a method known as **X-ray spectroscopy** to study the arrangement of the **outer electrons of atoms** in samples of **zirconium ore.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959523256336425.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['73'])
async def Ta(ctx):
  em = discord.Embed(title = '**Tantalum**', description = '73th Element, Mass of 180.95, **Transition Metal**\nTantalum was discovered by **Anders Gustaf Ekenberg**, a Swedish chemist, in 1802 in **minerals obtained from Ytterby, Sweden.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959549986635807.png?v=1')
  em.set_footer(text="Ah yes, another Ytterby shoutout")
  await ctx.send(embed = em)

@client.command(aliases = ['74'])
async def W(ctx):
  em = discord.Embed(title = '**Tungsten**', description = '74th Element, Mass of 183.84, **Transition Metal**\nTungsten was discovered in 1783 by **Juan José and Fausto Elhuyar**, Spanish chemists and brothers.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959566642085888.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['75'])
async def Re(ctx):
  em = discord.Embed(title = '**Rhenium**', description = '75th Element, Mass of 186.21, **Transition Metal**\nIn 1925 the discovery of rhenium was announced by **German chemists Walter Noddack, Ida Tacke, and Otto Berg.** They detected the element in the minerals columbite, gadolinite, molybdenite, and in platinum ore.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806959608748441620.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['76'])
async def Os(ctx):
  em = discord.Embed(title = '**Osmium**', description = '76th Element, Mass of 190.23, **Transition Metal**\nOsmium was **discovered in 1803 by English chemist Smithson Tennant.** This discovery came about through research into platinum ore that was **first discovered in Columbia in the 17th century.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962799565340692.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['77'])
async def Ir(ctx):
  em = discord.Embed(title = '**Iridium**', description = '77th Element, Mass of 192.22, **Transition Metal**\nIridium was discovered in 1803 among **insoluble impurities** in natural platinum. **Smithson Tennant**, the primary discoverer, named iridium after the **Greek goddess Iris**, personification of the **rainbow**, because of the **striking and diverse colors** of its salts.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962871555850352.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['78'])
async def Pt(ctx):
  em = discord.Embed(title = '**Platinum**', description = '78th Element, Mass of 195.08, **Transition Metal**\nPlatinum was discovered in South America independently by **Antonio de Ulloa in 1735** and by **N. Wood in 1741**, but it had been in use by pre-Columbian Indians.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962912220151829.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['79'])
async def Au(ctx):
  em = discord.Embed(title = '**Gold**', description = '79th Element, Mass of 196.97, **Transition Metal**\n**No single person discovered gold** but there are many **traces** of its use by ancient peoples. One early reference to it was made by Tushratta, a king of Mitanni (now northern Syria) in 2600 BC. He remarked that **there was more gold than dust in Egypt.** Such **abundance** of gold especially in Nubia **made Egypt a rich country.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962930531696650.png?v=1')
  await ctx.send(embed = em)
  
@client.command(aliases = ['80'])
async def Hg(ctx):
  em = discord.Embed(title = '**Mercury**', description = '80th Element, Mass of 200.59, **Transition Metal**\nIt is **not known who discovered mercury**, but it has been **found in Egyptian tombs** dating back over 3,500 years. Mercury was also known to the ancient Chinese and Hindus.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806962950479806577.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['81'])
async def Tl(ctx):
  em = discord.Embed(title = '**Thallium**', description = '81th Element, Mass of 204.38, **Other Metal**\nThallium was discovered by **Sir William Crookes** in 1861. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994333910827028.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['82'])
async def Pb(ctx):
  em = discord.Embed(title = '**Lead**', description = '82th Element, Mass of 207.2, **Other Metal**\nEarly evidence of lead include **lead beads from 6400 BC in Turkey**, and verse 15:10 of the Book of Exodus. Lead was also discovered **independently by the Egyptians, Babylonians, Assyrians and Chinese.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994370648735784.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['83'])
async def Bi(ctx):
  em = discord.Embed(title = '**Bismuth**', description = '83th Element, Mass of 208.98, **Other Metal**\n**Claude François Geoffroy** was a French chemist. In 1753 he **proved the chemical element bismuth to be distinct from lead**, becoming the official discoverer of the element.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/814927082051338280.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['84'])
async def Po(ctx):
  em = discord.Embed(title = '**Polonium**', description = '84th Element, Mass of 209, **Metalloid**\nPolonium was discovered in 1898 by **Marie and Pierre Curie**, when it was extracted from the uranium ore pitchblende and **identified solely by its strong radioactivity.** Polonium was **named after Marie Curies homeland of Poland.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994440916697128.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['85'])
async def At(ctx):
  em = discord.Embed(title = '**Astatine**', description = '85th Element, Mass of 210, **Halogen**\nAstatine was discovered in 1940 by **Dale Corson, Kenneth McKenzie, and Emilio Segre at Berkley**. It was not until three years later, however, that **astatine was found in nature.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806994457672417310.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['86'])
async def Rn(ctx):
  em = discord.Embed(title = '**Radon**', description = '86th Element, Mass of 222, **Noble Gas**\nRadon was discovered by **Friedrich Ernst Dorn, a German chemist**, in 1900 while studying **radium’s decay chain.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996687691579444.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['87'])
async def Fr(ctx):
  em = discord.Embed(title = '**Francium**', description = '87th Element, Mass of 223, **Alkali Metal**\nFrancium was discovered by **Marguerite Perey in France** (from which the element takes its name) in 1939. It was the **last element first discovered in nature, rather than by synthesis.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996743065305121.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['88'])
async def Ra(ctx):
  em = discord.Embed(title = '**Radium**', description = '88th Element, Mass of 226, **Alkaline Earth Metal**\nRadium was discovered by **Marie Sklodowska-Curie and her husband Pierre Curie on 21 December 1898**, in a **uraninite (pitchblende) sample** from Jáchymov.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996771599024128.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['89'])
async def Ac(ctx):
  em = discord.Embed(title = '**Actinium**', description = '89th Element, Mass of 227, **Lanthanoid**\nActinium was discovered in 1899 by **André-Louis Debierne**, a French chemist, while experimenting with **new methods of separating rare earth oxides.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996804897341520.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['90'])
async def Th(ctx):
  em = discord.Embed(title = '**Thorium**', description = '90th Element, Mass of 232.04, **Lanthanoid**\nThorium was discovered by **Jöns Jacob Berzelius in 1828, in Stockholm, Sweden**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806996833288716328.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['91'])
async def Pa(ctx):
  em = discord.Embed(title = '**Protactinium**', description = '91th Element, Mass of 231.04, **Lanthanoid**\nProtactinium was first identified in 1913 by **Kazimierz Fajans and Oswald Helmuth Göhring.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998911327272983.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['92'])
async def U(ctx):
  em = discord.Embed(title = '**Uranium**', description = '92th Element, Mass of 238.03, **Lanthanoid**\n**Martin Heinrich Klaproth** was a German chemist who discovered uranium.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998950375587881.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['93'])
async def Np(ctx):
  em = discord.Embed(title = '**Neptunium**', description = '93th Element, Mass of 237, **Lanthanoid**\nNeptunium was discovered by **Edwin McMillan and Philip Abelson** in 1940.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998967928750184.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['94'])
async def Pu(ctx):
  em = discord.Embed(title = '**Plotunium**', description = '94th Element, Mass of 244, **Lanthanoid**\nPlutonium was discovered in 1941 by scientists **Joseph W. Kennedy, Glenn T. Seaborg, Edward M. McMillan and Arthur C. Wohl** at the University of California, Berkeley. The discovery occurred when the team **bombarded uranium-238 with deuterons** that had been accelerated in a **cyclotron device**, which created **neptunium-238 and two free neutrons**. The neptunium-238 then **decayed into plutonium-238** through beta decay. ', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806998986611228673.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['95'])
async def Am(ctx):
  em = discord.Embed(title = '**Americium**', description = '95th Element, Mass of 243, **Lanthanoid**\nAmericium was first **produced in 1944 by the group of Glenn T. Seaborg from Berkeley, California,** at the Metallurgical Laboratory of the University of Chicago, a part of the Manhattan Project.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806999002138279938.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['96'])
async def Cm(ctx):
  em = discord.Embed(title = '**Curium**', description = '96th Element, Mass of 247, **Lanthanoid**\nCurium was first intentionally produced and identified in July 1944 by the **group of Glenn T. Seaborg at the University of California, Berkeley.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293411362209812.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['97'])
async def Bk(ctx):
  em = discord.Embed(title = '**Berkelium**', description = '97th Element, Mass of 247, **Lanthanoid**\nAlthough very small amounts of berkelium were possibly produced in previous nuclear experiments, it was first intentionally synthesized, isolated and identified in December 1949 by Glenn T. Seaborg, Albert Ghiorso, Stanley G. Thompson, and Kenneth Street, Jr.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293439963430953.png?v=1')
  em.set_footer(text="Berkeley and Seaborg now")
  await ctx.send(embed = em)

@client.command(aliases = ['98'])
async def Cf(ctx):
  em = discord.Embed(title = '**Californium**', description = '98th Element, Mass of 251, **Lanthanoid**\n It was discovered in 1950 by the **researchers of University of California, Berkeley.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293504198934552.png?v=1')
  em.set_footer(text = "Berkeley shoutouts galore")
  await ctx.send(embed = em)

@client.command(aliases = ['99'])
async def Es(ctx):
  em = discord.Embed(title = '**Einsteinium**', description = '99th Element, Mass of 252/254, **Lanthanoid**\nEinsteinium was **discovered as a component of the debris** of the first hydrogen bomb explosion in 1952, and **named after Albert Einstein.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293534545379338.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['100'])
async def Fm(ctx):
  em = discord.Embed(title = '**Fermium**', description = '100th Element!!, Mass of 257, **Lanthanoid**\nFermium was first observed in the fallout from the Ivy Mike nuclear test. The element was **named after Enrico Fermi.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807293586600624148.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['101'])
async def Md(ctx):
  em = discord.Embed(title = '**Mendelevium**', description = '101th Element, Mass of 258, **Lanthanoid**\nMendelevium, the **ninth transuranium element of the actinide series** to be discovered, was **first identified by Seaborg** and others in 1955 as a product of the bombardment of the einsteinium isotope 253 Es with helium ions.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295147468390470.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['102'])
async def No(ctx):
  em = discord.Embed(title = '**Nobelium**', description = '102th Element, Mass of 259, **Lanthanoid**\nNobelium is named after Alfred Nobel, the inventor of dynamite. The element was officially discovered in April 1958 in Berkeley, California, by Albert Ghiorso, Glenn Seaborg, Torbørn Sikkeland and John R. Walton.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295176645017640.png?v=1')
  em.set_thumbnail(text = "Seaborg is a madman")
  await ctx.send(embed = em)

@client.command(aliases = ['103'])
async def Lr(ctx):
  em = discord.Embed(title = '**Lawrencium**', description = '103th Element, Mass of 262, **Lanthanoid**\n Lawrencium was discovered at the University of California, Berkeley, by **Albert Ghiorso, Torbjørn Sikkeland, Almon E. Larsh and Robert M. Latimer in 1961.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295198635098124.png?v=1')
  em.set_footer(text = "berkeley madness")
  await ctx.send(embed = em)

@client.command(aliases = ['104'])
async def Rf(ctx):
  em = discord.Embed(title = '**Rutherfordium**', description = '104th Element, Mass of 261/267, **Transition Metal**\nRutherfordium was the first transactinide or super-heavy element to be discovered. Rutherfordium **may first have been synthesized in 1964** when a team of scientists at Dubna, Russia, led by Georgy Flerov, **bombarded a plutonium target** with neon ions.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295217425317889.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['105'])
async def Db(ctx):
  em = discord.Embed(title = '**Dubnium**', description = '105th Element, Mass of 268, **Transition Metal**\nDubnium does not occur naturally on Earth and is **produced artificially.** The Soviet Joint Institute for Nuclear Research **(JINR) claimed the first discovery of the element in 1968**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807295240201437186.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['106'])
async def Sg(ctx):
  em = discord.Embed(title = '**Seaborgium**', description = '106th Element, Mass of 266, **Transition Metal**\nSeaborgium was **discovered by Albert Ghiorso and others** in 1974 at The Lawrence Berkeley Laboratory in California', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298519945838603.png?v=1')
  em.set_footer(text="He has his own element...")
  await ctx.send(embed = em)

@client.command(aliases = ['107'])
async def Bh(ctx):
  em = discord.Embed(title = '**Bohrium**', description = '107th Element, Mass of 264, **Transition Metal**\nBohrium was first **discovered by a team of scientists in Dubna, Russia, in 1976.** The discovery was **confirmed by Peter Armbruster, Gottfried Münzenber and their team** working in Darmstadt, Germany, in 1981.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298541457244290.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['108'])
async def Hs(ctx):
  em = discord.Embed(title = '**Hassium**', description = '108th Element, Mass of 269, **Transition Metal**\nIt was discovered in 1984 by two famous German physicists **Peter Armbruster and Gottfried Munzenber.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298715798470699.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['109'])
async def Mt(ctx):
  em = discord.Embed(title = '**Meitnerium**', description = '109th Element, Mass of 268, **Transition Metal**\nMeitnerium was **first synthesized on August 29, 1982** by a German research team led by **Peter Armbruster and Gottfried Münzenberg.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298735620882482.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['110'])
async def Ds(ctx):
  em = discord.Embed(title = '**Darmstadtium**', description = '110th Element, Mass of 281, **Transition Metal**\nDarmstadtium was first **created on November 9, 1994**, at the Institute for Heavy Ion Research in Darmstadt, Germany, by **Peter Armbruster and Gottfried Münzenberg**, under the direction of Sigurd Hofmann.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807298754495381595.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['111'])
async def Rg(ctx):
  em = discord.Embed(title = '**Roentgenium**', description = '111th Element, Mass of 282, **Transition Metal**\n: Roentgenium is named for **scientist Wilhelm Conrad Röentgen, who discovered X-rays.** It is discovered by the **Gesellschaft fur Schwerionenforschung team** led by Peter Armbruster and Gottfried Münzenber in late 1994.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319083724832769.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['112'])
async def Cn(ctx):
  em = discord.Embed(title = '**Copernicium**', description = '112th Element, Mass of 285, **Transition Metal**\nCopernicium was first **made by research scientists led by Sigurd Hofmann at the Heavy Ion Research Laboratory** in Darmstadt, Germany in 1996.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319128355766322.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['113'])
async def Nh(ctx):
  em = discord.Embed(title = '**Nihonium**', description = '113th Element, Mass of 286, **Other Metal**\nNihonium was discovered on **August 12, 2012 by Kosuke Morita’s RIKEN collaborative team** in Japan. It was the first chemical **element ever discovered in Asia.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319155892158544.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['114'])
async def Fl(ctx):
  em = discord.Embed(title = '**Flerovium**', description = '114th Element, Mass of 289, **Other Metal**\nThe element is **Named after the Flerov Laboratory of Nuclear Reactions of the Joint Institute for Nuclear Research in Dubna, Russia**, where the element was **discovered in 1998.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319188757676072.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['115'])
async def Mc(ctx):
  em = discord.Embed(title = '**Moscovium**', description = '115th Element, Mass of 288, **Other Metal**\nIt was created and **announced by scientists at the Joint Institute for Nuclear Research** in Dubna, Russia, and scientists at the Lawrence **Livermore National Laboratory** in the United States.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319204868128768.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['116'])
async def Lv(ctx):
  em = discord.Embed(title = '**Livermorium**', description = '116th Element, Mass of 293, **Other Metal**\nIt was discovered in 2000 by by science **teams led by Yuri Oganessian and Ken Moody.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319250514739220.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['117'])
async def Ts(ctx):
  em = discord.Embed(title = '**Tennessine**', description = '117th Element, Mass of 294, **Halogen**\nTennessine was discovered by **scientists at Vanderbilt, the University of Tennessee and Oak Ridge National Laboratory.**', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319266311012413.png?v=1')
  await ctx.send(embed = em)

@client.command(aliases = ['118'])
async def Og(ctx):
  em = discord.Embed(title = '**Oganesson**', description = '118th Element (finally we are done!), Mass of 294, **Noble Gas**\nThe first to claim the discovery of oganesson was **Polish physicist Robert Smolańczuk**, who published a report of his discovery in 1998. According to the physicist, **he discovered oganesson during the fusion of atomic nuclei** that form the synthesis of superheavy atoms.', color = discord.Color.blue())
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/807319288561008711.png?v=1')
  await ctx.send(embed = em)

@client.command()
async def elements(ctx, page = 1):
  if page == 1:
    em = discord.Embed(title = 'List of the Elements 1', description = 'Hydrogen (`H`)\nHelium (`He`)\nLithium (`Li`)\nBeryllium (`Be`)\nBoron (`B`)\nCarbon (`C`)\nNitrogen (`N`)\nOxygen (`O`)\nFlourine (`F`)\nNeon (`Ne`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 2:
    em = discord.Embed(title = 'List of the Elements 2', description = 'Sodium (`Na`)\nMagnesium (`Mg`)\nAluminum (`Al`)\nSilicon (`Si`)\nPhosphorus (`P`)\nSulfur (`S`)\nChlorine (`Cl`)\nArgon (`Ar`)\nPotassium (`K`)\nCalcium (`Ca`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 3:
    em = discord.Embed(title = 'List of the Elements 3', description = 'Scandium (`Sc`)\nTitanium (`Ti`)\nVanadium (`V`)\nChromium (`Cr`)\nManganese (`Mn`)\nIron (`Fe`)\nCobalt (`Co`)\nNickel (`Ni`)\nCopper (`Cu`)\nZinc (`Zn`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 4:
    em = discord.Embed(title = 'List of the Elements 4', description = 'Gallium (`Ga`)\nGermanium (`Ge`)\nArsenic (`As`)\nSelenium (`Se`)\nBromine (`Br`)\nKyrpton (`Kr`)\nRibidium (`Rb`)\nStrontium (`Sr`)\nYttrium (`Y`)\nZirconium (`Zr`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 5:
    em = discord.Embed(title = 'List of the Elements 5', description = 'Niobium (`Nb`)\nMolybdenum (`Mo`)\nTechnetium (`Tc`)\nRuthenium (`Ru`)\nRhodium (`Rh`)\nPalladium (`Pd`)\nSilver (`Ag`)\nCandium (`Cd`)\nIndium (`In`)\nTin (`Sn`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    em.set_footer(text="Do people still like cat videos?")
    await ctx.send(embed = em)
  elif page == 6:
    em = discord.Embed(title = 'List of the Elements 6', description = 'Antimony (`Sb`)\nTellurium (`Te`)\nIodine (`I`)\nXenon (`Xe`)\nCaesium (`Cs`)\nBarium (`Ba`)\nLanthanum (`La`)\nCerium (`Ce`)\nPraseodymium (`Pr`)\nNeondymium (`Nd`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 7:   
    em = discord.Embed(title = 'List of the Elements 7', description = 'Prothemium (`Pm`)\nSamarium (`Sm`)\nEuropium (`Eu`)\nGadolinium (`Gd`)\nTerbium (`Tb`)\nDysprosium (`Dy`)\nHolmium (`Ho`)\nErbium (`Er`)\nThulium (`Tm`)\nYtterbium (`Yb`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 8:   
    em = discord.Embed(title = 'List of the Elements 8', description = 'Lutetium (`Lu`)\nHafnium (`Hf`)\nTantalum (`Ta`)\nTungsten (`W`)\nRhenium (`Re`)\nOsmium (`Os`)\nIridium (`Ir`)\nPlatinum (`Pt`)\nGold (`Au`)\nMercury (`Hg`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 9:  
    em = discord.Embed(title = 'List of the Elements 9', description = 'Thallium (`Tl`)\nLead (`Pb`)\nBismuth (`Bi`)\nPolonium (`Po`)\nAstatine (`At`)\nRadon (`Rn`)\nFrancium (`Fr`)\nRadium (`Ra`)\nActinium (`Ac`)\nThorium (`Th`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 10:  
    em = discord.Embed(title = 'List of the Elements 10', description = 'Protactinium (`Pa`)\nUranium (`U`)\nNeptunium (`Np`)\nPlutonium (`Pu`)\nAmericium (`Am`)\nCurium (`Cm`)\nBerkelium (`Bk`)\nCalifornium (`Cf`)\nEinsteinium (`Es`)\nFermium (`Fm`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 11:   
    em = discord.Embed(title = 'List of the Elements 11', description = 'Mendelevium (`Md`)\nNobelium (`No`)\nLawrencium (`Lr`)\nRutherfordium (`Rf`)\nDubnium (`Db`)\nSeaborgium (`Sg`)\nBohrium (`Bh`)\nHassium (`Hs`)\nMeitnerium (`Mt`)\nDarmstadtium (`Ds`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page == 12:
    em = discord.Embed(title = 'List of the Elements 12', description = 'Roentgenium (`Rg`)\nCopernicium (`Cn`)\nNihonium (`Nh`)\nFlerovium (`Fl`)\nMoscovium (`Mc`)\nLivermorium (`Lv`)\nTennessine (`Ts`)\nOganesson (`Og`)')
    em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/817876187023015960/818955057197613106/periodiccia.gif')
    await ctx.send(embed = em)
  elif page >= 12:
				return await ctx.send("There are only 12 list sectors you idiot lmao")

@client.command()
async def elemgroup(ctx, *, page: int = None):
		groupname = ''
		groupdesc = ''
		yeetus = 'Use `p elemgroup <number>` to find the group you want to view.\n\n**1.**  Alkali Metals\n**2.** Alkaline Earth Metals\n**3.** Transition Metals\n**4.** Non-Metals\n**5.** Noble Gases\n**6.** Halogens\n**7.** Metalloids\n**8.** Lanthanoids'
		if not page:
				em = discord.Embed(title='Groups of the Periodic Table of Elements', description=yeetus)
				await ctx.send(embed=em)
		else:
			if page == 1:
						groupname = 'Alkali Metals'
						groupdesc = 'All alkali metals have their outermost electron in an s-orbital (hence are group 1): this shared electron configuration results in their having very similar characteristic properties. Tthe alkali metals provide the best example of group trends in properties in the periodic table, with elements exhibiting well-characterised homologous behaviour. Upon reacting with oxygen, alkali metals form oxides, peroxides, superoxides and suboxides.'
			elif page == 2:
						groupname = 'Alkaline Earth Metals'
						groupdesc = 'The alkaline earth metals are six chemical elements in group 2 of the periodic table. The elements have very similar properties: they are all shiny, silvery-white, somewhat reactive metals at standard temperature and pressure.'
			elif page == 3:
						groupname = 'Transition Metals'
						groupdesc = 'Most scientists describe a "transition metal" as any element in the d-block of the periodic table, which includes groups 3 to 12 on the periodic table. The word transition was first used to describe the elements now known as the d-block by the English chemist Charles Bury in 1921, who referred to a transition series of elements during the change of an inner layer of electrons from a stable group of 8 to one of 18, or from 18 to 32.'
			elif page == 4:
						groupname = 'Non-Metals'
						groupdesc = 'In chemistry, a nonmetal (or non-metal) is a chemical element that mostly lacks the characteristics of a metal. Physically, a nonmetal tends to have a relatively low melting point, boiling point, and density. A nonmetal is typically brittle when solid and usually has poor thermal conductivity and electrical conductivity. Chemically, nonmetals tend to have relatively high ionization energy, electron affinity, and electronegativity. They gain or share electrons when they react with other elements and chemical compounds.'
			elif page == 5:
						groupname = 'Noble Gases'
						groupdesc = 'The noble gases (historically also the inert gases; sometimes referred to as aerogens) make up a class of chemical elements with similar properties; under standard conditions, they are all odorless, colorless, monatomic gases with very low chemical reactivity.'
			elif page == 6:
						groupname = 'Halogens'
						groupdesc = 'The halogens are a group in the periodic table consisting of five chemically related elements: fluorine (F), chlorine (Cl), bromine (Br), iodine (I), and astatine (At). When halogens react with metals, they produce a wide range of salts, including calcium fluoride, sodium chloride (common table salt), silver bromide and potassium iodide. All of the halogens form acids when bonded to hydrogen. Most halogens are typically produced from minerals or salts.'
			elif page == 7:
						groupname = 'Metalloids'
						groupdesc = 'Metalloids are a small group of elements founds in the periodic table of elements along the zigzag line that distinguishes metals from non-metals and is drawn from between boron and aluminium to the border polonium and astatine.'
			elif page == 8:
						groupname = 'Lanthanoids'
						groupdesc = 'The lanthanide or lanthanoid series of chemical elements comprises the 15 metallic chemical elements with atomic numbers 57–71, from lanthanum through lutetium. These elements, along with the chemically similar elements scandium and yttrium, are often collectively known as the rare earth elements.'
			elif page >= 8:
					return await ctx.send("bro there are only 8 sections")			
			em = discord.Embed(title=f'Page {page} | {groupname}', description = f'{groupdesc}')
			await ctx.send(embed=em)

@client.command()
async def bonds(ctx):
  em = discord.Embed(title = 'Types of Bonds', description = 'Ionic - Covalent - Polar - Hydrogen')
  em.add_field(name = 'Ionic Bond', value = 'Ionic bonding involves a transfer of an electron, so one atom gains an electron while one atom loses an electron. One of the resulting ions carries a negative charge (anion), and the other ion carries a positive charge (cation). Because opposite charges attract, the atoms bond together to form a molecule.', inline = False)
  em.add_field(name = 'Covalent Bond', value = 'The most common bond in organic molecules, a covalent bond involves the sharing of electrons between two atoms. The pair of shared electrons forms a new orbit that extends around the nuclei of both atoms, producing a molecule. There are two secondary types of covalent bonds that are relevant to biology — polar bonds and hydrogen bonds.', inline = False)
  em.add_field(name = 'Polar Bond', value = 'Two atoms connected by a covalent bond may exert different attractions for the electrons in the bond, producing an unevenly distributed charge. The result is known as a polar bond, an intermediate case between ionic and covalent bonding, with one end of the molecule slightly negatively charged and the other end slightly positively charged.', inline = False)
  em.add_field(name = 'Hydrogen Bond', value = 'Because they’re polarized, two adjacent H2O (water) molecules can form a linkage known as a hydrogen bond, where the (electronegative) hydrogen atom of one H2O molecule is electrostatically attracted to the (electropositive) oxygen atom of an adjacent water molecule.', inline = False)
  em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/778322617211289653/834648220046458920/bonds.jpg')
  em.set_footer(text="Quacker learned bonds thru Khan Academy but was too lazy to use his notes so he copied from dummies.com lmao")
  await ctx.send(embed = em)
    
@client.command()
async def lightningmyth(ctx, *, page: int = None):
  lightningmyths = 'Lightning never strikes twice in the same place.\n\nFact: Lightning often strikes the same place repeatedly, especially if it’s a tall, pointy, isolated object. The Empire State Building was once used as a lightning laboratory because it is hit nearly 25 times per year, and has been known to have been hit up to a dozen times during a single storm.', 'Lightning only strikes the tallest objects.\n\nFact: Lightning is indiscriminate and it can find you anywhere. Lightning may hit the ground instead of a tree, cars instead of nearby telephone poles, and parking lots instead of buildings.', 'If you are stuck in a thunderstorm, being under a tree is better than no shelter at all.\n\nFact: Sheltering under a tree is just about the worst thing you can do. If lightning does hit the tree, there is the chance that a “ground charge” will spread out from the tree in all directions. Being underneath a tree is the second leading cause of lightning casualties.', 'If you do not see rain or clouds, you are safe.\n\nFact: Lightning often strikes more than three miles from the thunderstorm, far outside the rain or even the thunderstorm cloud. Though infrequent, “bolts from the blue” have been known to strike areas as distant as 10 miles from their thunderstorm origins, where the skies appear clear.', 'A car\'s rubber tires will protect you from lightning.\n\nFact: True, being in a car will likely protect you. But most vehicles are actually safe because the metal roof and sides divert lightning around you—the rubber tires have little to do with keeping you safe. Convertibles, motorcycles, bikes, open shelled outdoor recreation vehicles and cars with plastic or fiberglass shells offer no lightning protection at all.', 'If you are outside in a storm, lie flat on the ground.\n\nFact: Lying flat on the ground makes you more vulnerable to electrocution, not less. Lightning generates potentially deadly electrical currents along the ground in all directions — by lying down, you are providing more potential points on your body to hit.', 'If you touch a lightning victim, you will be electrocuted.\n\nFact: The human body doesn’t store electricity. It is perfectly safe to touch a lightning victim to give them first aid.', 'Wearing metal on your body attracts lightning.\n\nFact: The presence of metal makes very little difference in determining where lightning will strike. Height, pointy shape and isolation are the dominant factors in whether lightning will strike an object (including you). However, touching or being near metal objects, such as a fence, can be unsafe when thunderstorms are nearby. If lightning does happen to hit one area of the fence—even a long distance away - the metal can conduct the electricity and electrocute you.', 'A house will always keep you safe from lightning.\n\nFact: While a house is the safest place you can be during a storm, just going inside is not enough. You must avoid any conducting path leading outside, such as electrical appliances, wires, TV cables, plumbing, metal doors or metal window frames. Do not stand near a window to watch the lightning. An inside room is generally safe, but a home equipped with a professionally installed lightning protection system is the safest shelter available.', 'Surge suppressors can protect a home against lightning.\n\nFact: Surge arresters and suppressors are important components of a complete lightning protection system, but can do nothing to protect a structure against a direct lightning strike. These items must be installed in conjunction with a lightning protection system to provide whole house protection.'
  em = discord.Embed(title = 'Lightning Myths', description = f'{random.choice(lightningmyths)}')
  em.set_image(url ='https://cdn.discordapp.com/attachments/817876187023015960/827303919612854350/lightning.png')
  em.set_footer(text="Info from iii.org")
  await ctx.send(embed = em)
  
@client.command(aliases = ['val', 'electron'])
async def valence(ctx):
  em = discord.Embed(title = 'What are valence electrons?', description = 'The electrons in the outermost shell are the valence electrons--the electrons on an atom that can be gained or lost in a chemical reaction. Since filled d or f subshells are seldom disturbed in a chemical reaction, we can define valence electrons as follows: The electrons on an atom that are not present in the previous rare gas, ignoring filled d or f subshells.\n\nGallium has the following electron configuration: **Ga: [Ar] 4s2 3d10 4p1**\n\nThe 4s and 4p electrons can be lost in a chemical reaction, but not the electrons in the filled 3d subshell. Gallium therefore has three valence electrons.')
  em.set_image(url ='https://cdn.discordapp.com/emojis/825941003281760306.png?v=1')
  em.set_footer(text="Info from chemed.chem.purdue.edu")
  await ctx.send(embed = em)

@client.command(aliases = ['dmitri'])
async def mendeleev(ctx):
  em = discord.Embed(title = '**Who is Mendeleev?**', description = 'Dmitri Ivanovich Mendeleev was a Russian chemist and inventor. He is best remembered for formulating the Periodic Law and creating a farsighted version of the periodic table of elements.', url = 'https://www.biography.com/scientist/dmitri-mendeleyev')
  em.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/806396194196029460.png?v=1')
  em.set_footer(text="That is one of the best beards I have seen no doubt")
  await ctx.send(embed = em)

@client.command()
async def table(ctx):
  await ctx.send(file = discord.File("table.jpg"))

@client.command(aliases = ['vote'])
async def upvote(ctx):
  await ctx.send('https://top.gg/bot/767190721534361631/vote')

@client.command()
async def ping(ctx):
  await ctx.send(f'The latency is {round(client.latency * 1000)} ms!')

@client.command(aliases = ['quacker'])
async def yt(ctx):
  await ctx.send(f'https://www.youtube.com/channel/UC6PKOburRMFSjwTCQcL4wbQ https://www.youtube.com/watch?v=eOJONIkB6iI')

@client.command(aliases = ['docs'])
async def readdocs(ctx):
  em = discord.Embed(title = 'Popular Discord Wrapper Documentations for Discord Bots!', url = "https://discord.gg/discord-api", description = '**discord.py, discord.js, and discordUnity**')
  em.add_field(name = 'discord.py documentation', value = '[Click here](https://discordpy.readthedocs.io/en/stable/index.html)', inline = False)
  em.add_field(name = 'discord.js documentation', value = '[Click here](https://discordjs-fork.readthedocs.io/en/latest/)', inline = False)
  em.add_field(name = 'discordUnity documentation', value = '[Click here](https://discordunity.readthedocs.io/en/latest/)', inline = False)
  em.set_footer(text = 'Again, none of the links are rickrolls.')
  await ctx.send(embed = em)

@client.command(aliases = ['serv', 'guild'])
async def server(ctx):
  await ctx.send(f'https://discord.gg/W6JHRPWvJd')

@client.command()
async def servcount(ctx):
  await ctx.send(f'I am currently operating in {len(client.guilds)} servers!')

@client.command()
async def invite(ctx):
  await ctx.send(f'https://dsc.gg/perio I reached max servers so it would not work :( Waiting for Discord to approve my verification')

@client.command(aliases = ['repo', 'repository'])
async def gitrepo(ctx):
  await ctx.send(f'https://github.com/QuackerDeezles/Periodiccia')
  
@client.command()
async def about(ctx):
  await ctx.send(f'Hey! I am **Periodiccia**, a Discord bot designed to provide information about Chemistry and the Periodic Table of Elements. I house the basic element commands (hydrogen, tungsten, etc.), a helpful element list, an element group definition finder, and much more. Just type in `p help elements` to view the element commands, and `p help` to view the other modules and information. Developed by <@704506180273438721> \n\nIf you want to invite me to your server, use the following authorization hyperlink: https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot -  All of my code can be viewed on GitHub. To view the repository, type `p gitrepo`.\n\nIf you have a suggestion, want to report a bug, or anything else, join my official server! https://discord.gg/W6JHRPWvJd\n\n')

@client.command(aliases = ['simp'])
async def simprate(ctx):
  simp = ['2', '5', '9', '11', '14', '18', '23', '26', '27', '34', '36', '37', '40', '45', '48', '52', '54', '57', '61', '67', '69', '72', '75', '78', '80', '84', '86', '91', '93', '97', '100']
  em = discord.Embed(title = '**SimpRate Percentage**', description = f'You are {random.choice(simp)}% a simp', color = discord.Color.green())
  em.set_footer(text = "are you proud of that?")
  await ctx.send(embed = em)

@client.command(aliases = ['waifu'])
async def waifurate(ctx):
  waifu = ['2', '5', '9', '11', '14', '18', '23', '26', '27', '34', '36', '37', '40', '45', '48', '52', '54', '57', '61', '67', '69', '72', '75', '78', '80', '84', '86', '91', '93', '97', '100']
  em = discord.Embed(title = '**WaifuRate Percentage**', description = f'You are {random.choice(waifu)}% a waifu uwu', color = discord.Color.green())
  await ctx.send(embed = em)

@client.command(aliases = ['gamer', 'gamerrate', 'progamerrate'])
async def progamer(ctx):
  game = ['2', '5', '9', '11', '14', '18', '23', '26', '27', '34', '36', '37', '40', '45', '48', '52', '54', '57', '61', '67', '69', '72', '75', '78', '80', '84', '86', '91', '93', '97', '100']
  em = discord.Embed(title = '**ProGamerRate Percentage**', description = f'You are {random.choice(game)}% a pro gamer :video_game:', color = discord.Color.green())
  em.set_footer(text = "Number one victory royale")
  await ctx.send(embed = em)

@client.command(aliases = ['coin', 'flip'])
async def coinflip(ctx):
  coin = ['Heads', 'Tails']
  await ctx.send(f'The coin flipped {random.choice(coin)}.')

@client.command(aliases = ['roll'])
async def die(ctx):
  await ctx.send(f':game_die: You rolled a {random.randint(1,6)}!')

@client.command()
async def rng(ctx, num : int):
  await ctx.send(f'You rolled a {random.randint(1,num)} out of {num} possiblities!')

@client.command(aliases = ['letter', 'randomletter'])
async def randletter(ctx, *, page = 1):
  letters = [':regional_indicator_a:', ':regional_indicator_b:', ':regional_indicator_c:', ':regional_indicator_d:', ':regional_indicator_e:', ':regional_indicator_f:', ':regional_indicator_g:', ':regional_indicator_h:', ':regional_indicator_i:', ':regional_indicator_j:', ':regional_indicator_k:', ':regional_indicator_l:', ':regional_indicator_m:', ':regional_indicator_n:', ':regional_indicator_o:', ':regional_indicator_p:', ':regional_indicator_q:', ':regional_indicator_r:', ':regional_indicator_s:', ':regional_indicator_t:', ':regional_indicator_u:', ':regional_indicator_v:', ':regional_indicator_w:', ':regional_indicator_x:', ':regional_indicator_y:', ':regional_indicator_z:']
  if page == 1:
      await ctx.send(f'{random.choice(letters)}')
  elif page == 2:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)}')
  elif page == 3:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page == 4:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page == 5:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page == 6:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page == 7:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page == 8:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page == 9:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page == 10:
      await ctx.send(f'{random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)} {random.choice(letters)}')
  elif page >= 10:
				return await ctx.send("The max is 10 letters, what were you thinking?")

@client.command(aliases = ['randomyoutube'])
async def randyt(ctx):
  yt = ['James Charles https://www.youtube.com/channel/UCucot-Zp428OwkyRm2I7v2Q', 'MrBeast https://www.youtube.com/user/MrBeast6000', 'Karl https://www.youtube.com/channel/UCrYrcFGGs_nke1MggS8Jvqg', 'npesta https://www.youtube.com/channel/UC9cqZITak5v02ciYEP1Lj-w', 'Marques Brownlee https://www.youtube.com/c/mkbhd', 'ImranSAVAGE https://www.youtube.com/channel/UCQlVUVsJrEK9BPZlGNob3Yw', 'Mark Rober https://www.youtube.com/c/MarkRober', 'Lessons In Meme Culture https://www.youtube.com/c/LessonsinMemeCulture', 'Nathan Doan Comedy https://www.youtube.com/channel/UCdyMFblTjr-C2N-T5TGftQQ', 'Steven He https://www.youtube.com/channel/UCP0_k4INXrwPS6HhIyYqsTg', 'Dude Perfect https://www.youtube.com/user/corycotton', 'MindYourDecisions https://www.youtube.com/user/MindYourDecisions', 'Sheet Music Boss https://www.youtube.com/channel/UCzTR9iSH-TFC4-ocDS_ll4A', 'https://tenor.com/view/rickroll-dance-funny-you-music-gif-7755460 ha', 'Timeworks https://www.youtube.com/c/Timeworks', 'Technoblade https://www.youtube.com/user/technothepig', 'Colin and Samir https://www.youtube.com/channel/UCamLstJyCa-t5gfZegxsFMw', 'EricVanWilderman https://www.youtube.com/user/EricVanWilderman', 'orangepeanut https://www.youtube.com/channel/UC4UnIP8UhglLQZgGrR1zv-w', 'Tom Scott https://www.youtube.com/c/TomScottGo', 'Kurzgesagt https://www.youtube.com/user/Kurzgesagt', 'Veritasium https://www.youtube.com/c/veritasium', 'Vox https://www.youtube.com/user/voxdotcom', 'GeorgeNotFound https://www.youtube.com/user/GeorgeeeHDPlays', 'fnm04 https://www.youtube.com/channel/UCw00BI5Nm1nXxxbTsXHNaLg', 'Karl Jobst https://www.youtube.com/user/karljobst', 'Milad Mirg https://www.youtube.com/channel/UCWLu3q9FEmPPYKcUAxKZb2A', 'Bosh https://www.youtube.com/user/SuperMore101', 'Flamingo https://www.youtube.com/channel/UCm-X6o81nRsXQTmqpyArkBQ', 'Sechi https://www.youtube.com/channel/UCEBN79bwwYNfRWcYYUzrkcw', 'Exyl https://www.youtube.com/channel/UCNgchdiFrWvmjXKOKX5Vfsg', 'RØB https://www.youtube.com/user/RobertEntertains', 'Daylight Gaming https://www.youtube.com/channel/UCjoJJnvfTQ2AM5qbEDEqY6A', 'LazarBeam https://www.youtube.com/channel/UCw1SQ6QRRtfAhrN_cjkrOgA', 'ian kung https://www.youtube.com/c/IanKung', 'jacksfilms https://www.youtube.com/user/jacksfilms', 'Sapnap https://www.youtube.com/channel/UCqynl7rdtktKMQESdSBmE-g', 'OmicronGaming https://www.youtube.com/channel/UCryKACitFpPVPiqvYH6pQBQ', 'Parashockx https://www.youtube.com/channel/UCKUnB5P0cdfnufPCKkGecqQ', 'DGR https://www.youtube.com/channel/UCzg5UMJ62uoKHTkq5bgkp5g', '- LeKukie - https://www.youtube.com/channel/UCG0J5pTtRZtGk_45nOAebfA', 'Niftski https://www.youtube.com/channel/UCWdQCuLMf45n-_PHWu4sJNw', 'bill wurtz https://www.youtube.com/user/billwurtz', 'BadBoyHalo https://www.youtube.com/user/thesaintsofgames', 'ProZD https://www.youtube.com/user/ProZD', 'SethEverman https://www.youtube.com/user/SethEverman', 'Davie504 https://www.youtube.com/user/Davie504', 'PangaeaPanga https://www.youtube.com/user/PangaTAS', 'Summoning Salt https://www.youtube.com/channel/UCtUbO6rBht0daVIOGML3c8w', 'NoThisIsJohn https://www.youtube.com/channel/UC2xw-F0lBbPX0MV2Ezp833A', 'Ben Awad https://www.youtube.com/user/99baddawg', 'Johnny Harris https://www.youtube.com/user/johnnymangosteen', 'TheTekkitRealm https://www.youtube.com/channel/UCHOgE8XeaCjlgvH0t01fVZg', 'Markiplier https://www.youtube.com/user/markiplierGAME', 'Discord https://www.youtube.com/c/discord']
  await ctx.send(f'You should watch {random.choice(yt)}')

@client.command(aliases = ['randomtwitch'])
async def randtwitch(ctx):
  twit = ['Im_Dontai https://www.twitch.tv/im_dontai', 'actingliketommy https://www.twitch.tv/actingliketommy', 'Sommerset https://www.twitch.tv/sommerset', 'Clix https://www.twitch.tv/clix', 'BagBagBagBagBagBagBagBag https://www.twitch.tv/bagbagbagbagbagbagbagbag', 'DudePerfectGaming https://www.twitch.tv/dudeperfectgaming', 'pokimane https://www.twitch.tv/pokimane', 'TheFatRatTV https://www.twitch.tv/thefatrattv', 'NoThisIsJohn https://www.twitch.tv/nothisisjohn', 'Quackity https://www.twitch.tv/quackity', 'WilburSoot https://www.twitch.tv/wilbursoot', 'karljacobs https://www.twitch.tv/karljacobs', ' Sykkuno https://www.twitch.tv/sykkuno', 'strawbys_ https://www.twitch.tv/strawbys_', 'Kaydop https://www.twitch.tv/kaydop', 'SypherPK https://www.twitch.tv/sypherpk', 'xQcOW https://www.twitch.tv/xqcow', 'tommyinnit https://www.twitch.tv/tommyinnit', 'CaptainPuffy https://www.twitch.tv/captainpuffy', 'Tubbo https://twitch.tv/tubbo', 'Alixxa https://www.twitch.tv/alixxa']
  await ctx.send(f'You should watch {random.choice(twit)}')

@client.command()
async def topgg(ctx, *args):
  topgg = "Open this to view search results in the website top.gg: https://top.gg/search?q=" + ("%20".join(args[:]))
  await ctx.send(topgg)

@client.command()
async def youtube(ctx, *args):
  youtube = "Open this to view search results in the website youtube.com: https://www.youtube.com/results?search_query=" + ("+".join(args[:]))
  await ctx.send(youtube)

@client.command()
async def urban(ctx, *args):
  urbandictionary = "Open this to view search results in the website urbandictionary.com - If it doesn't show the embed, that means what you wrote isn't a word listed in Urban Dictionary: https://www.urbandictionary.com/define.php?term=" + ("%20".join(args[:]))
  await ctx.send(urbandictionary)

@client.command()
async def wiki(ctx, *args):
  wiki = "Open this to view search results in the website wikipedia.org - If it doesn't show the embed, that means what you wrote isn't a word listed in Wikipedia: https://en.wikipedia.org/wiki/" + ("_".join(args[:]))
  await ctx.send(wiki)

@client.command()
async def twitch(ctx, *args):
  twitch = "Open this to view search results in the website twitch.tv: https://www.twitch.tv/search?term=" + ("%20".join(args[:]))
  await ctx.send(twitch)

@client.command()
async def tiktok(ctx, *args):
  tiktok = "Open this to view search results in the website tiktok.com: https://www.tiktok.com/search?q=" + ("%20".join(args[:])) + "&lang=en"
  await ctx.send(tiktok)

@client.command()
async def insta(ctx, *, msg):
  insta = "Open this to view search results in the website instagram.com: https://www.instagram.com/explore/tags/" + msg + "/"
  await ctx.send(insta)

@client.command()
async def twitter(ctx, *args):
  twitter = "Open this to view search results in the website twitter.com: https://twitter.com/search?q=" + ("%20".join(args[:])) + "&src=typed_query"
  await ctx.send(twitter)

@client.command()
async def soundcloud(ctx, *args):
  twitter = "Open this to view search results in the website soundcloud.com: https://soundcloud.com/search?q=" + ("%20".join(args[:]))
  await ctx.send(twitter)

@client.command()
async def amazon(ctx, *args):
  amazon = "Open this to view search results in the website amazon.com: https://www.amazon.com/s?k=" + ("%20".join(args[:])) + "&ref=nb_sb_noss_2"
  await ctx.send(amazon)

@client.command()
async def wired(ctx, *args):
  wired = "Open this to view search results in the website wired.com: https://www.wired.com/search/?q=" + ("%20".join(args[:])) + "&page=1&sort=score"
  await ctx.send(wired)

@client.command()
async def fortune(ctx, *args):
  fortune = "Open this to view search results in the website fortune.com: https://fortune.com/advanced-search/?query=" + ("%20".join(args[:]))
  await ctx.send(fortune)

@client.command()
async def nytimes(ctx, *args):
  nytimes = "Open this to view search results in the website nytimes.com: https://www.nytimes.com/search?query=" + ("+".join(args[:]))
  await ctx.send(nytimes)

@client.command()
async def espn(ctx, *args):
  espn = "Open this to view search results in the website espn.com: https://www.espn.com/search/_/q/" + ("%20".join(args[:]))
  await ctx.send(espn)

@client.command()
async def msft(ctx, *args):
  msft = "Open this to view search results in the website microsoft.com: https://www.microsoft.com/en-us/search?q=" + ("+".join(args[:]))
  await ctx.send(msft)

@client.command()
async def github(ctx, *args):
  github = "Open this to view search results in the website microsoft.com: https://github.com/search?q=" + ("+".join(args[:]))
  await ctx.send(github)

@client.command()
async def forbes(ctx, *args):
  forbes = "Open this to view search results in the website forbes.com: https://www.forbes.com/search/?q=" + ("+".join(args[:])) + "&sh=64a56bfa279f"
  await ctx.send(forbes)

@client.command()
async def stackoverflow(ctx, *args):
  stackoverflow = "Open this to view search results in the website stackoverflow.com: https://stackoverflow.com/search?q=" + ("+".join(args[:]))
  await ctx.send(stackoverflow)

@client.command()
async def quora(ctx, *args):
  quora = "Open this to view search results in the website quora.com: https://www.quora.com/search?q=" + ("%20".join(args[:]))
  await ctx.send(quora)

@client.command()
async def theverge(ctx, *args):
  theverge = "Open this to view search results in the website theverge.com: https://www.theverge.com/search?q=" + ("+".join(args[:]))
  await ctx.send(theverge)

@client.command()
async def history(ctx, *args):
  history = "Open this to view search results in the website history.com: https://www.history.com/search?q=" + ("%20".join(args[:]))
  await ctx.send(history)

@client.command()
async def natgeo(ctx, *args):
  natgeo = "Open this to view search results in the website nationalgeographic.com: https://www.nationalgeographic.com/search?q=" + ("%20".join(args[:])) + "&location=srp&type=manual"
  await ctx.send(natgeo)

@client.command()
async def mrktwatch(ctx, *args):
  mrktwatch = "Open this to view search results in the website marketwatch.com: https://www.marketwatch.com/tools/quotes/lookup.asp?lookup=" + ("%20".join(args[:]))
  await ctx.send(mrktwatch)

@client.command()
async def reddit(ctx, *args):
  reddit = "Open this to view search results in the website reddit.com: https://www.reddit.com/search/?q=" + ("%20".join(args[:]))
  await ctx.send(reddit)

@client.command()
async def medium(ctx, *args):
  medium = "Open this to view search results in the website medium.com: https://medium.com/search?q=" + ("%20".join(args[:]))
  await ctx.send(medium)

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)

@client.command()
async def talk(ctx, *, msg):
  await ctx.message.delete()
  await ctx.send(msg)
