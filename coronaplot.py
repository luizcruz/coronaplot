import datetime, googletrans
import pandas as pd
from matplotlib import pyplot
import numpy as np
from datetime import datetime, timedelta
from googletrans import Translator


# pomber series from JHU CSSE
url = 'https://pomber.github.io/covid19/timeseries.json'
df = pd.read_json(url, orient='columns')




def per_country_cases(log=False):

	translator = Translator()
	for country in df:
		print ("Generating graph "+country)
		qty = 0
		dayzero = ""
		dates = []
		confirmed = []
		deaths = []
		recover = []

		for item in df[country]:
			if dayzero == "":
				dayzero = item['date']
			lastday = str(item['date'])
			dates.append(qty)
			qty = qty + 1
			
			confirmed.append(item['confirmed'])
			deaths.append(item['deaths'])
			recover.append(item['recovered'])


		x = np.array(dates)
		c = np.array(confirmed)
		d = np.array(deaths)
		r = np.array(recover)

		pyplot.figure(figsize=(6,5),facecolor = 'black', dpi=100)
		pyplot.plot(x,c,color="black", label="Confirmados",linewidth=2)
		pyplot.plot(x,d,color="red", label="Mortes",linewidth=2)
		pyplot.plot(x,r,color="green", label="Recuperados",linewidth=2)
		if log == True: 
			pyplot.yscale('log')
			suffix = "_log"
		else:
			suffix = ""
		for var in (c, d, r):
			pyplot.annotate(var.max(), xy=(1, var.max()), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

		pyplot.legend(loc="upper left")
		pyplot.xticks(rotation=45)
		pyplot.grid()
		#translated_country = translator.translate(country, dest='pt')
		pyplot.title(country+ ' - Casos de COVID-19 ('+lastday+')')
		pyplot.xlabel('Dias')
		pyplot.ylabel('Pessoas')
		pyplot.annotate('Fonte: JHU CSSE, desde '+dayzero, (0,0), (0,-25), fontsize=6, xycoords='axes fraction', textcoords='offset points', va='top')
		pyplot.savefig(country+suffix+'.png', dpi=100)
		pyplot.close()



def overall_cases(log=False):

	translator = Translator()
	# Superior limit of cases to plot
	limit = 1500
	print ("Generating graph Overall Deaths")

	pyplot.figure(figsize=(8,6),facecolor = 'black', dpi=100)

	for country in df:
		qty = 0
		dayzero = ""
		dates = []
		deaths = []

		for item in df[country]:
			if dayzero == "":
				dayzero = item['date']
			lastday = str(item['date'])	
			dates.append(qty)
			qty = qty + 1
			deaths.append(item['deaths'])

		x = np.array(dates)
		d = np.array(deaths)
		
	

		#translated_country = translator.translate(country, dest='pt')
	
		if d.max()>limit:
			pyplot.plot(x,d,label=country,linewidth=2)
			pyplot.annotate(d.max(), xy=(1, d.max()), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

	
	
	pyplot.legend(loc="upper left")
	pyplot.xticks(rotation=45)
	pyplot.grid(True)
	if log == True: 
		pyplot.yscale('log')
		suffix = "_log"
	else:
		suffix = ""
	pyplot.title('Total de mortes COVID-19 acima de 1.500 ('+lastday+')')
	pyplot.xlabel('Dias')
	pyplot.ylabel('Pessoas')
	pyplot.annotate('Fonte: JHU CSSE, desde '+dayzero, (0,0), (0,-25), fontsize=6, xycoords='axes fraction', textcoords='offset points', va='top')
	pyplot.savefig('OverallDeaths'+suffix+'.png', dpi=100)
	pyplot.close()




	# Superior limit of cases to plot
	limit = 25000
	print ("Generating graph Overall Confirmed")

	pyplot.figure(figsize=(8,6),facecolor = 'black', dpi=100)

	for country in df:
		qty = 0
		dayzero = ""
		dates = []
		confirmed = []

		for item in df[country]:
			if dayzero == "":
				dayzero = item['date']
			lastday = str(item['date'])
			dates.append(qty)
			qty = qty + 1
			confirmed.append(item['confirmed'])

		x = np.array(dates)
		c = np.array(confirmed)
		
	

		#translated_country = translator.translate(country, dest='pt')
	
		if c.max()>limit:
			pyplot.plot(x,c,label=country,linewidth=2)
			pyplot.annotate(c.max(), xy=(1, c.max()), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')

	
	
	pyplot.legend(loc="upper left")
	pyplot.xticks(rotation=45)
	pyplot.grid(True)
	if log == True: 
		pyplot.yscale('log')
		suffix = "_log"
	else:
		suffix = ""
	pyplot.title('Total de confirmados COVID-19 acima de 25.000 ('+lastday+')')
	pyplot.xlabel('Dias')
	pyplot.ylabel('Pessoas')
	pyplot.annotate('Fonte: JHU CSSE, desde '+dayzero, (0,0), (0,-25), fontsize=6, xycoords='axes fraction', textcoords='offset points', va='top')

	pyplot.savefig('OverallConfirmed'+suffix+'.png', dpi=100)
	pyplot.close()





def main():
	per_country_cases(True)
	overall_cases(True)        
	per_country_cases(False)
	overall_cases(False)       

if __name__== "__main__":
   main()





