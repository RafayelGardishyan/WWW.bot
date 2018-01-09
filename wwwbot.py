import discord
import asyncio
import json, requests
import sys

urlstandard = 'https://codename-codeniacs.herokuapp.com/api/v1/9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b/'

def get_list(param):
	url = param
	params = dict(format = 'json')
	resp = requests.get(url=url, params=params)
#	print(resp, "\n")
	data = json.loads(resp.text)
#	print(data, "\n")
	return data

def parse_tasks1():
	raw = get_list(urlstandard + 'tasks')
	tasknames = []
	taskdeadlines = []
	taskusers = []
	for i in raw:
		name = i['name']
		deadline = i['date']
		user = get_list(i['user'])['name']
		tasknames.append(name)
		taskdeadlines.append(deadline)
		taskusers.append(user)
	k = 0
	
	embed = discord.Embed(color=0x9f6f0f, title='Tasks')
	for task in raw:
		embed.add_field(name=tasknames[k], value="User: " + taskusers[k] + "\nDeadline: " + taskdeadlines[k], inline=False)
		k += 1
	embeds = [embed]
	return embeds

def parse_people1():
	raw = get_list(urlstandard + 'users')
	peoplenames = []
	peopleranks = []
	peopleactive = []
	for i in raw:
		name = i['name']
		rank = i['rang']
		active = i['activated']
		peoplenames.append(name)
		peopleranks.append(rank)
		peopleactive.append(active)
	k = 0
	
	embed = discord.Embed(color=0x9f6f0f, title='People')
	for person in raw:
		if peopleactive[k] == True:
			embed.add_field(name="User:", value="Name: " + peoplenames[k] + "\nRank: " + peopleranks[k], inline=False)
		
		print(peoplenames[k])
		print(k)
		print('------')
		
		k += 1
	embeds = [embed]
	return embeds
	
	
def parse_tasks2():
	raw = get_list(urlstandard + 'tasks')
	tasknames = []
	taskdeadlines = []
	taskusers = []
	for i in raw:
		name = i['name']
		deadline = i['date']
		user = get_list(i['user'])['name']
		tasknames.append(name)
		taskdeadlines.append(deadline)
		taskusers.append(user)
	k = 0
	embeds = []
	for task in raw:
		embed = discord.Embed(color=0x9f6f0f, title=tasknames[k])
		embed.add_field(name="Deadline:", value=taskdeadlines[k], inline=False)
		embed.add_field(name="User:", value=taskusers[k], inline=False)
		embeds.append(embed)
		k += 1
	return embeds

def parse_people2():
	raw = get_list(urlstandard + 'users')
	peoplenames = []
	peopleranks = []
	peopleactive = []
	for i in raw:
		name = i['name']
		rank = i['rang']
		active = i['activated']
		peoplenames.append(name)
		peopleranks.append(rank)
		peopleactive.append(active)
	k = 0
	embeds = []
	for person in raw:
		if peopleactive[k] == True:
			embed = discord.Embed(color=0x9f6f0f, title="User")
			embed.add_field(name="Name:", value=peoplenames[k], inline=False)
			embed.add_field(name="Rank:", value=peopleranks[k], inline=False)
			embeds.append(embed)
		
		print(peoplenames[k])
		print(k)
		print('------')
		
		k += 1
	return embeds
	
parse_tasks1()
parse_tasks2()
parse_people1()
parse_people2()
client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('www.test'):
		await client.send_message(message.channel, '( ͡° ͜ʖ ͡°)')
	
	if message.content.startswith('www.tasks'):
		mes = await client.send_message(message.channel, 'loading tasks.')
		await asyncio.sleep(1)
		await client.edit_message(mes, 'loading tasks..')
		await asyncio.sleep(1)
		await client.edit_message(mes, 'loading tasks...')
		await asyncio.sleep(1)
		await client.edit_message(mes, 'loading tasks')
		await client.delete_message(mes)
		try:
			embeded = parse_tasks1()
			
			for embede in embeded:
				await client.send_message(message.channel, embed=embede)
		except Exception:
			embeded = parse_tasks2()
			for embede in embeded:
				await client.send_message(message.channel, embed=embede)
				
	if message.content.startswith('www.people'):
		mes = await client.send_message(message.channel, 'loading people.')
		await asyncio.sleep(1)
		await client.edit_message(mes, 'loading people..')
		await asyncio.sleep(1)
		await client.edit_message(mes, 'loading people...')
		await asyncio.sleep(1)
		await client.edit_message(mes, 'loading people')
		await client.delete_message(mes)
		try:
			embeded = parse_people1()
			
			for embede in embeded:
				await client.send_message(message.channel, embed=embede)
		except Exception:
			embeded = parse_people2()
			for embede in embeded:
				await client.send_message(message.channel, embed=embede)
		
	if message.content.startswith('!@#$%EXIT'):
		sys.exit()

client.run('Mzk5OTg4OTA4MzExNTc2NTc2.DTVGQQ.l5ZKaDnhCV96NVqeI697K7j1rNM')