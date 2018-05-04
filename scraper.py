# scraper.py
"""Ibreviary scraper.

Scrapes ibreviary from www.hostname.com"""

# In each commented line you write one step of your program.
# create an ibreviariary settings url varible
# go to settings page
# ...
# ...
#... later you will add code below each line.




###
# coding: utf-8
import requests
import bs4
import datetime

def main():
	session = requests.Session()
	date = datetime.datetime.now()
	l = []
	while True:
		date = date - datetime.timedelta(days=1)
		print(date)
		day = str(date.day)
		year = str(date.year)
		month = str(date.month)
		response = set_date(session, year, month, day)
		morning_prayers = get_prayer(session, daytime='morning')
		evening_prayers = get_prayer(session, daytime='evening')
		l.append((date, morning_prayers, evening_prayers))
		if year == '2017':
			break
		if month == '2':
			print(l)
			break
		print(l)
		break

def set_date(session, year, month, day):
	payload = {'lang':'en', 'anno':year, 'mese':month, 'giorno':day, 'ok':'ok',}
	session.post('http://www.ibreviary.com/m/opzioni.php', data=payload)
	response = session.get('http://www.ibreviary.com/m/breviario.php')
	return response


def get_prayer(session, daytime):
	# mrning prayers
	d = {'morning':'lodi', 'evening':'vespri'}
	response = session.get('http://www.ibreviary.com/m/breviario.php', params={'s':d['morning']})
	soup = bs4.BeautifulSoup(response.text, 'lxml')
	l = []
	for row in soup.find_all('div'):
		l.append(row)
	return l

if __name__ == '__main__':
	main()
