import discord
import keep_alive
import os
import random
import json
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = 'p ')
status = cycle([f'p help = Help Command', 'Made by QuackerDeezlesYT#3393', 'An original, informational element bot.'])
client.remove_command('help')

@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author

  embed = discord.Embed(
    color = discord.Color.purple()
  )

  embed.set_author(name='**Welcome to Periodiccia!**')
  embed.add_field(name='`p help`', value='Shows this!', inline=False)
  embed.add_field(name='To look up information about a specific element, type its symbol after the prefix.', value='For example, `p H` = Hydrogen, among its other information.', inline=False)
  embed.add_field(name='If you want to look at the list of Elements in the Periodic Table, type in `p list`.', value='**This is a built-in reference for most of the commands related to the elements here.**', inline=False)
  embed.add_field(name='`p mendeleev`', value='This command tells you a bit about who Mendeleev is, and some helpful resources to learn about him.', inline=False)
  embed.add_field(name='`p socials`', value='Use this command to see the social accounts of the developer!', inline=False)
  emb
  embed.add_field(name='It would be very appreciated if you could invite my bot to your server! :slight_smile:', value='https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot', inline=False)
  embed.add_field(name='There are some hidden commands in this bot. If you find a specific one, it will give you all the other ones! :smirk:', value='Hope you find them!', inline=False)
  embed.add_field(name='Made by QuackerDeezlesYT#3393', value='If you have any questions, feel free to DM him!', inline=False)

  await ctx.send(embed = embed)

@client.event
async def on_ready():
  change_status.start()
  print("The bot is ready!")

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def list(ctx):
  em = discord.Embed(title = '**List of the Elements**', description = 'Hydrogen (`H`), Helium (`He`), Lithium (`Li`), Beryllium (`Be`), Boron (`B`), Carbon (`C`) Nitrogen (`N`), Oxygen (`O`), Flourine (`F`), Neon (`Ne`), Sodium (`Na`), Magnesium (`Mg`), Aluminum (`Al`), Silicon (`Si`), Phosphorus (`P`), Sulfur (`S`), Chlorine (`Cl`), Argon (`Ar`), Potassium (`K`), Calcium (`Ca`), Scandium (`Sc`), Titanium (`Ti`), Vanadium (`V`), Chromium (`Cr`), Manganese (`Mn`), Iron (`Fe`), Cobalt (`Co`), Nickel (`Ni`), Copper (`Co`), Zinc (`Zn`), Gallium (`Ga`), Germanium (`Ge`), Arsenic (`As`), Selenium (`Se`), Bromine (`Br`), Kyrpton (`Kr`), Ribidium (`Rb`), Strontium (`Sr`), Yttrium (`Y`), Zirconium (`Zr`), Niobium (`Nb`), Molybdenum (`Mo`), Technetium (`Tc`), Ruthenium (`Ru`), Rhodium (`Rh`), Palladium (`Pd`), Silver (`Ag`), Candium (`Cd`), Indium (`In`), Tin (`Sn`), Antimony (`Sb`), Tellurium (`Te`), Iodine (`I`), Xenon (`Xe`), Caesium (`Cs`), Barium (`Ba`), Lanthanum (`La`), Cerium (`Ce`), Praseodymium (`Pr`), Neondymium (`Nd`), Prothemium (`Pm`), Samarium (`Sm`), Europium (`Eu`), Gadolinium (`Gd`), Terbium (`Tb`), Dysprosium (`Dy`), Holmium (`Ho`), Erbium (`Er`), Thulium (`Tm`), Ytterbium (`Yb`), Lutetium (`Lu`), Hafnium (`Hf`), Tantalum (`Ta`), Tungsten (`W`), Rhenium (`Re`), Osmium (`Os`), Iridium (`Ir`), Platinum (`Pt`), Gold (`Au`), Mercury (`Hg`), Thalium (`Ti`), Lead (`Pb`), Bismuth (`Bi`), Polonium (`Po`), Astatine (`At`), Radon (`Rn`), Francium (`Fr`), Radium (`Ra`), Actinium (`Ac`), Thorium (`Th`), Protactinium (`Pa`), Uranium (`U`), Neptunium (`Np`), Plutonium (`Pu`), Americium (`Am`), Curium (`Cm`), Berkelium (`Bk`), Californium (`Cf`), Einsteinium (`Es`), Fermium (`Fm`), Mendelevium (`Md`), Nobelium (`No`), Lawrencium (`Lr`), Rutherfordium (`Rf`), Dubnium (`Db`), Seaborgium (`Sg`), Bohrium (`Bh`), Hassium (`Hs`), Meitnerium (`Mt`), Darmstadtium (`Ds`), Roentgenium (`Rg`), Copernicium (`Cn`), Nihonium (`Nh`), Flerovium (`Fl`), Moscovium (`Mc`), Livermorium (`Lv`), Tennessine (`Ts`), Oganesson (`Og`)')
  await ctx.send(embed = em)
  
@client.command()
async def H(ctx):
  em = discord.Embed(title = '**Hydrogen**', description = '1st Element, Mass of 1.008', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def He(ctx):
  em = discord.Embed(title = '**Helium**', description = '2nd Element, Mass of 4.0026, **Noble Gas**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Li(ctx):
  em = discord.Embed(title = '**Lithium**', description = '3rd Element ,Mass of 6.94, **Alkali Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Be(ctx):
  em = discord.Embed(title = '**Beryllium**', description = '4th Element, Mass of 9.0122, **Alkaline Earth Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def B(ctx):
  em = discord.Embed(title = '**Boron**', description = '5th Element, Mass of 10.81, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def C(ctx):
  em = discord.Embed(title = '**Carbon**', description = '6th Element, Mass of 12.011, **Nonmetal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def N(ctx):
  em = discord.Embed(title = '**Nitrogen**', description = '7th Element, Mass of 14.077, **Nonmetal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def O(ctx):
  em = discord.Embed(title = '**Oxygen**', description = '8th Element, Mass of 15.999, **Nonmetal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def F(ctx):
  em = discord.Embed(title = '**Flourine**', description = '9th Element, Mass of 18.998, **Halogen**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ne(ctx):
  em = discord.Embed(title = '**Neon**', description = '10th Element, Mass of 20.180, **Noble Gas**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Na(ctx):
  em = discord.Embed(title = '**Sodium**', description = '11th Element, Mass of 22.990, **Alkali Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Mg(ctx):
  em = discord.Embed(title = '**Magnesium**', description = '12th Element, Mass of 23.405, **Alkaline Earth Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Al(ctx):
  em = discord.Embed(title = '**Aluminum**', description = '13th Element, Mass of 26.982, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Si(ctx):
  em = discord.Embed(title = '**Silicon**', description = '14th Element, Mass of 28.085, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def P(ctx):
  em = discord.Embed(title = '**Phosphorus**', description = '15th Element, Mass of 30.974, **Nonmetal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def S(ctx):
  em = discord.Embed(title = '**Sulfur**', description = '16th Element, Mass of 32.06, **Nonmetal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Cl(ctx):
  em = discord.Embed(title = '**Chlorine**', description = '17th Element, Mass of 32.06, **Halogen**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ar(ctx):
  em = discord.Embed(title = '**Argon**', description = '18th Element, Mass of 39.948, **Noble Gas**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def K(ctx):
  em = discord.Embed(title = '**Potassium**', description = '19th Element, Mass of 39.098, **Alkali Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ca(ctx):
  em = discord.Embed(title = '**Calcium**', description = '20th Element, Mass of 40.078, **Alkaline Earth Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Sc(ctx):
  em = discord.Embed(title = '**Scandium**', description = '21th Element, Mass of 44.956, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ti(ctx):
  em = discord.Embed(title = '**Titanium**', description = '22th Element, Mass of 47.867, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def V(ctx):
  em = discord.Embed(title = '**Vanadium**', description = '23th Element, Mass of 50.942, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Cr(ctx):
  em = discord.Embed(title = '**Chromium**', description = '24th Element, Mass of 51.996, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Mn(ctx):
  em = discord.Embed(title = '**Manganese**', description = '25th Element, Mass of 54.938, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Fe(ctx):
  em = discord.Embed(title = '**Iron**', description = '26th Element, Mass of 55.845, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Co(ctx):
  em = discord.Embed(title = '**Cobalt**', description = '27th Element, Mass of 58.933, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ni(ctx):
  em = discord.Embed(title = '**Nickel**', description = '28th Element, Mass of 58.693, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Cu(ctx):
  em = discord.Embed(title = '**Copper**', description = '29th Element, Mass of 63.546, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Zn(ctx):
  em = discord.Embed(title = '**Zinc**', description = '30th Element, Mass of 65.38, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ga(ctx):
  em = discord.Embed(title = '**Gallium**', description = '31th Element, Mass of 69.723, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ge(ctx):
  em = discord.Embed(title = '**Germanium**', description = '32th Element, Mass of 72.63, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def As(ctx):
  em = discord.Embed(title = '**Arsenic**', description = '33th Element, Mass of 74.922, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Se(ctx):
  em = discord.Embed(title = '**Selenium**', description = '34th Element, Mass of 78.97, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Br(ctx):
  em = discord.Embed(title = '**Bromine**', description = '35th Element, Mass of 79.004, **Halogen**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Kr(ctx):
  em = discord.Embed(title = '**Krypton**', description = '36th Element, Mass of 83.80, **Noble Gas**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Rb(ctx):
  em = discord.Embed(title = '**Rubidium**', description = '37th Element, Mass of 85.468, **Alkali Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)
  
@client.command()
async def Sr(ctx):
  em = discord.Embed(title = '**Strontium**', description = '38th Element, Mass of 87.62, **Alkaline Earth Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Y(ctx):
  em = discord.Embed(title = '**Yttrium**', description = '39th Element, Mass of 88.906, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Zr(ctx):
  em = discord.Embed(title = '**Zirconium**', description = '40th Element, Mass of 91.224, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Nb(ctx):
  em = discord.Embed(title = '**Niobium**', description = '41th Element, Mass of 92.906, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Mo(ctx):
  em = discord.Embed(title = '**Molybdenum**', description = '42th Element, Mass of 95.95, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Tc(ctx):
  em = discord.Embed(title = '**Technetium**', description = '43th Element, Mass of 98, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ru(ctx):
  em = discord.Embed(title = '**Ruthenium**', description = '44th Element, Mass of 101.07, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Rh(ctx):
  em = discord.Embed(title = '**Rhodium**', description = '45th Element, Mass of 102.91, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Pd(ctx):
  em = discord.Embed(title = '**Palladium**', description = '46th Element, Mass of 106.42, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ag(ctx):
  em = discord.Embed(title = '**Silver**', description = '47th Element, Mass of 107.87, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)
  
@client.command()
async def Cd(ctx):
  em = discord.Embed(title = '**Cadmium**', description = '48th Element, Mass of 112.41, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def In(ctx):
  em = discord.Embed(title = '**Iodine**', description = '49th Element, Mass of 114.52, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Sn(ctx):
  em = discord.Embed(title = '**Tin**', description = '50th Element, Mass of 118.71, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Sb(ctx):
  em = discord.Embed(title = '**Antimony??????**', description = '51th Element, Mass of 121.76, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Te(ctx):
  em = discord.Embed(title = '**Tellerium**', description = '52th Element, Mass of 127.60, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def I(ctx):
  em = discord.Embed(title = '**Iodine**', description = '53th Element, Mass of 126.90, **Halogen**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Xe(ctx):
  em = discord.Embed(title = '**Xenon**', description = '54th Element, Mass of 131.29, **Noble Gases**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Cs(ctx):
  em = discord.Embed(title = '**Caesium**', description = '55th Element, Mass of 132.91, **Alkali Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ba(ctx):
  em = discord.Embed(title = '**Barium**', description = '56th Element, Mass of 137.33, **Alkaline Earth Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def La(ctx):
  em = discord.Embed(title = '**Lanthanium**', description = '57th Element, Mass of 138.91, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ce(ctx):
  em = discord.Embed(title = '**Cerium**', description = '58th Element, Mass of 140.12, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Pr(ctx):
  em = discord.Embed(title = '**Praseodymium**', description = '59th Element, Mass of 140.91, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Nd(ctx):
  em = discord.Embed(title = '**Neodynium**', description = '60th Element, Mass of 144.25, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Pm(ctx):
  em = discord.Embed(title = '**Promethium**', description = '61th Element, Mass of 145, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Sm(ctx):
  em = discord.Embed(title = '**Samarium**', description = '62th Element, Mass of 150.36, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Eu(ctx):
  em = discord.Embed(title = '**Europium**', description = '63th Element, Mass of 151.96, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Gd(ctx):
  em = discord.Embed(title = '**Gadolinium**', description = '64th Element, Mass of 157.25, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Tb(ctx):
  em = discord.Embed(title = '**Terbium**', description = '65th Element, Mass of 158.93, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Dy(ctx):
  em = discord.Embed(title = '**Dysprosium**', description = '66th Element, Mass of 162.50, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ho(ctx):
  em = discord.Embed(title = '**Holmium**', description = '67th Element, Mass of 164.93, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Er(ctx):
  em = discord.Embed(title = '**Erbium**', description = '68th Element, Mass of 167.26, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Tm(ctx):
  em = discord.Embed(title = '**Thulium**', description = '**69**th Element :smirk:, Mass of 168.93, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Yb(ctx):
  em = discord.Embed(title = '**Ytterbium**', description = '70th Element, Mass of 173.05, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Lu(ctx):
  em = discord.Embed(title = '**Lutetium**', description = '71th Element, Mass of 174.94, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Hf(ctx):
  em = discord.Embed(title = '**Hafnium**', description = '72th Element, Mass of 178.49, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ta(ctx):
  em = discord.Embed(title = '**Tantalum**', description = '73th Element, Mass of 180.95, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def W(ctx):
  em = discord.Embed(title = '**Tungsten BIG W POG**', description = '74th Element, Mass of 183.84, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Re(ctx):
  em = discord.Embed(title = '**Rhenium**', description = '75th Element, Mass of 186.21, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Os(ctx):
  em = discord.Embed(title = '**Osmium**', description = '76th Element, Mass of 190.23, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ir(ctx):
  em = discord.Embed(title = '**Iridium**', description = '77th Element, Mass of 192.22, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Pt(ctx):
  em = discord.Embed(title = '**Platinum**', description = '78th Element, Mass of 195.08, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Au(ctx):
  em = discord.Embed(title = '**Gold**', description = '79th Element, Mass of 196.97, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)
  
@client.command()
async def Hg(ctx):
  em = discord.Embed(title = '**Mercury**', description = '80th Element, Mass of 200.59, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Tl(ctx):
  em = discord.Embed(title = '**Thallium**', description = '81th Element, Mass of 204.38, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Pb(ctx):
  em = discord.Embed(title = '**Lead**', description = '82th Element, Mass of 207.2, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Bi(ctx):
  em = discord.Embed(title = '**Bismuth**', description = '83th Element, Mass of 208.98, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Po(ctx):
  em = discord.Embed(title = '**Polonium**', description = '84th Element, Mass of 209, **Metalloid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def At(ctx):
  em = discord.Embed(title = '**Astatine**', description = '85th Element, Mass of 210, **Halogen**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Rn(ctx):
  em = discord.Embed(title = '**Radon**', description = '86th Element, Mass of 222, **Noble Gas**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Fr(ctx):
  em = discord.Embed(title = '**Francium**', description = '87th Element, Mass of 223, **Alkali Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ra(ctx):
  em = discord.Embed(title = '**Radium**', description = '88th Element, Mass of 226, **Alkaline Earth Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ac(ctx):
  em = discord.Embed(title = '**Actinium**', description = '89th Element, Mass of 227, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Th(ctx):
  em = discord.Embed(title = '**Thorium**', description = '90th Element, Mass of 232.04, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Pa(ctx):
  em = discord.Embed(title = '**Protactinium**', description = '91th Element, Mass of 231.04, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def U(ctx):
  em = discord.Embed(title = '**Uranium**', description = '92th Element, Mass of 238.03, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Np(ctx):
  em = discord.Embed(title = '**Neptunium**', description = '93th Element, Mass of 237, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Pu(ctx):
  em = discord.Embed(title = '**Plotunium**', description = '94th Element, Mass of 244, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Am(ctx):
  em = discord.Embed(title = '**Americium**', description = '95th Element, Mass of 243, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Cm(ctx):
  em = discord.Embed(title = '**Curium**', description = '96th Element, Mass of 247, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Bk(ctx):
  em = discord.Embed(title = '**Berlekium**', description = '97th Element, Mass of 247, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Cf(ctx):
  em = discord.Embed(title = '**Californium**', description = '98th Element, Mass of 251, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Es(ctx):
  em = discord.Embed(title = '**Einsteinium**', description = '99th Element, Mass of 252, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Fm(ctx):
  em = discord.Embed(title = '**Fermium**', description = '100th Element!!, Mass of 257, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Md(ctx):
  em = discord.Embed(title = '**Mendelevium**', description = '101th Element, Mass of 258, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def No(ctx):
  em = discord.Embed(title = '**Nobelium**', description = '102th Element, Mass of 259, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Lr(ctx):
  em = discord.Embed(title = '**Lawrencium**', description = '103th Element, Mass of 262, **Lanthanoid**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Rf(ctx):
  em = discord.Embed(title = '**Rutherfordium**', description = '104th Element, Mass of 267, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Db(ctx):
  em = discord.Embed(title = '**Dubnium**', description = '105th Element, Mass of 268, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Sg(ctx):
  em = discord.Embed(title = '**Seaborgium**', description = '106th Element, Mass of 269, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Bh(ctx):
  em = discord.Embed(title = '**Bohrium**', description = '107th Element, Mass of 270, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Hs(ctx):
  em = discord.Embed(title = '**Hassium**', description = '108th Element, Mass of 277, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Mt(ctx):
  em = discord.Embed(title = '**Meitherium**', description = '109th Element, Mass of 278, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ds(ctx):
  em = discord.Embed(title = '**Darmstadtium**', description = '110th Element, Mass of 281, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Rg(ctx):
  em = discord.Embed(title = '**Roentgenium**', description = '111th Element, Mass of 282, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Cn(ctx):
  em = discord.Embed(title = '**Copernicium**', description = '112th Element, Mass of 285, **Transition Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Nh(ctx):
  em = discord.Embed(title = '**Nihonium**', description = '113th Element, Mass of 286, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Fl(ctx):
  em = discord.Embed(title = '**Flerovium**', description = '114th Element, Mass of 289, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Mc(ctx):
  em = discord.Embed(title = '**Moscovium**', description = '115th Element, Mass of 289, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Lv(ctx):
  em = discord.Embed(title = '**Livermorium**', description = '116th Element, Mass of 293, **Other Metal**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Ts(ctx):
  em = discord.Embed(title = '**Tennessine**', description = '117th Element, Mass of 294, **Halogen**', color = discord.Color.blue())
  await ctx.send(embed = em)

@client.command()
async def Og(ctx):
  em = discord.Embed(title = '**Oganesson**', description = '118th Element (finally we are done!), Mass of 294, **Noble Gas**', color = discord.Color.blue())
  await ctx.send(embed = em)

#hidden command
@client.command()
async def dm(ctx):
  await ctx.author.send(':rage: aw shit you found me :rage:\nI guess you want to know the secret commands right?\nFine.\n`clear` would clear messages and is **not** a moderation command. For example, `p clear 3` would clear 3 messages.\nWho doesn not want free hugs? Do `p freehugs` for free hugs. This was a fanmade command!\n`p gif` = Science gif\n`p billnye` is a randomized gif with the one and only Bill Nye!\n`p rsl` gives the entire script of the Raid Shadow Legends! This command was also fanmade :slight_smile:\n\nYou happy now? Also do not tell about this command to anyone - not even your best friend. Developer would be :face_with_symbols_over_mouth: lmao')

#hidden command
@client.command()
async def clear(ctx, amount=0):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

#hidden command
@client.command()
async def rsl(ctx):
  await ctx.author.send('This message is sponsored by Raid Shadow Legends, one of the biggest mobile role-playing games of 2021 and it is totally free! Currently almost 10 million users have joined Raid over the last six months, and it is one of the most impressive games in its class with detailed models, environments and smooth 60 frames per second animations! All the champions in the game can be customized with unique gear that changes your strategic buffs and abilities! The dungeon bosses have some ridiculous skills of their own and figuring out the perfect party and strategy to overtake them is a lot of fun! Currently with over 300,000 reviews, Raid has almost a perfect score on the Play Store! The community is growing fast and the highly anticipated new faction wars feature is now live, you might even find my squad out there in the arena! It is easier to start now than ever with rates program for new players you get a new daily login reward for the first 90 days that you play in the game! So what are you waiting for? Go to the video description, click on the special links and you will get 50,000 silver and a free epic champion as part of the new player program to start your journey! Good luck and I will see you there!')
  
#hidden command
@client.command()
async def freehugs(ctx):
  await ctx.author.send("https://tenor.com/view/running-hug-embrace-imiss-you-good-to-see-you-again-gif-15965620")

#hidden command
@client.command()
async def gif(ctx):
  gifs = ['https://tenor.com/view/carbon-is-highly-reactive-with-other-elements-sensitive-responsive-active-neil-degrasse-tyson-gif-15827677', 'https://tenor.com/view/massiveunregulatednitrogendioxide-gif-19415452', 'https://tenor.com/view/drinks-margarita-liquid-nitrogen-dry-ice-gif-3384966', 'https://tenor.com/view/mundschutz-mask-breathe-gif-17200590','https://tenor.com/view/gold-rich-daffy-duck-money-gif-10195329',]
  await ctx.send(f'For the love of science and elements {random.choice(gifs)}')

#hidden command
@client.command()
async def billnye(ctx):
  billnye_gifs = ['https://tenor.com/view/bill-nye-billnye-sciencerules-science-gif-5866727',  'https://tenor.com/view/bill-nye-party-horn-confetti-sarcastic-like-child-gif-5499505', 'https://tenor.com/view/bill-nye-head-explode-mindblown-gif-4903176', 'https://tenor.com/view/tongue-out-crazy-gif-11927272', 'https://tenor.com/view/memes-bill-nye-the-science-gif-5930649', 'https://tenor.com/view/mic-drop-drop-the-mic-serious-boss-bill-nye-gif-8166361', 'https://tenor.com/view/bill-nye-bill-nye-the-science-guy-scienceguy-consider-gif-7391226', 'https://tenor.com/view/dance-bill-nye-bill-nye-the-science-guy-bill-nye-dance-dancing-gif-5603636']
  await ctx.send(f'You cannot have enough Bill Nye {random.choice(billnye_gifs)}')

@client.command()
async def mendeleev(ctx):
  em = discord.Embed(title = '**Dmitri Ivanovich Mendeleev was a Russian chemist and inventor. He is best remembered for formulating the Periodic Law and creating a farsighted version of the periodic table of elements.**', description = 'http://en.wikipedia.org/wiki/Dmitri_Mendeleev\nhttps://www.britannica.com/biography/Dmitri-Mendeleev\nhttps://www.biography.com/scientist/dmitri-mendeleyev', color = discord.Color.red())
  await ctx.send(embed = em)

@client.command()
async def socials(ctx):
  em = discord.Embed(title = '**Developer socials**',description = '**Discord Server**: https://discord.gg/Xt8UQj2neY\n**Youtube Channel**: https://www.youtube.com/channel/UC6PKOburRMFSjwTCQcL4wbQ?view_as=subscriber', color = discord.Color.orange())
  await ctx.send(embed = em)

keep_alive.keep_alive()
client.run(key")
