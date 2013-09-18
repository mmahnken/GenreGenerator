import requests, requests.exceptions
import lxml
from lxml import html

def getInfoBox(url):
	link = url
	#Handle 404 error
	try:
 		r = requests.get(link)
	except (requests.exceptions.MissingSchema) as e:
		return ['404 error' ]
	except (requests.exceptions.ConnectionError) as e:
		return ['Connection Error, invalid url']
	tree = html.fromstring(r.text)
	list_of_rows = tree.xpath('//table[@class="infobox vevent"]//tr//text()')
	#Handle when 'Genre' not in list of rows from info box (ie incorrect wikipedia page or genre not listed).
	if 'Genre' not in list_of_rows:
		if 'Format' in list_of_rows:
			jackpot = list_of_rows.index('Format') +2
			current = jackpot
			formats = ["No Genre information in XML tree, but there are formats listed:"]
			while list_of_rows[current] != '\n':
				formats.append(list_of_rows[current])
				current += 1
				return formats
		else:
			return ["No genre or format listed. Invalid wikipedia url."]
	#Clean out superscripts from the genre section.
	if '[' in list_of_rows:
		beg_delete = list_of_rows.index('[')
		list_of_rows.pop(beg_delete)
		list_of_rows.pop(beg_delete)
		list_of_rows.pop(beg_delete)
	#Clean out slashes from genre section.
	if ' / ' in list_of_rows:
		to_delete = list_of_rows.index(' / ')
		list_of_rows.pop(to_delete)
	jackpot = list_of_rows.index('Genre') + 2
	current = jackpot
	genres = []
	while list_of_rows[current] != '\n':
		genres.append(list_of_rows[current])
		current += 1
	return genres



	


