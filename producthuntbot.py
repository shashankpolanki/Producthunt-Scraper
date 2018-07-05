#Create a bot, maybe deploy to heroku, that downloads producthunt's homepage
#Writes to file all of the tools with more than 250 likes for the day

#First: start off by returning 1 or 2 tools in the terminal

#Second: Get all tools above 150 likes

import bs4, requests

res = requests.get('https://www.producthunt.com')
res.raise_for_status()

content = bs4.BeautifulSoup(res.text, "html.parser")

#allTools = content.find_all('.PostsList_b2208 li')

#for i in allTools:

ToolName = content.select('.item_54fdd h2')

ToolTag =  content.select('.item_54fdd h3')

linkElem = content.select('.item_54fdd a')[0]

print(ToolName[0].getText())

print(ToolTag[0].getText())

res2 = requests.get('https://www.producthunt.com' + str(linkElem.get('href')))

res2.raise_for_status()

content2 = bs4.BeautifulSoup(res2.text, "html.parser")

linkElem2 = content2.select('.side_c0705 span')

print('https://' + str(linkElem2[0].getText()))
