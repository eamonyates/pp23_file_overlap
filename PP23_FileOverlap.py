import requests
from bs4 import BeautifulSoup


def file_overlap(url1, url2):
	r1 = requests.get(url1)
	soup1 = BeautifulSoup(r1.text, 'html.parser')

	with open('test1.txt', 'w') as open_file:
		open_file.write(str(soup1))

	r2 = requests.get(url2)
	soup2 = str(BeautifulSoup(r2.text, 'html.parser'))

	with open('test2.txt', 'w') as open_file:
		open_file.write(str(soup2))

	list1 = []
	listOverlap = []

	with open('test1.txt', 'r') as open_file:	
		for line in open_file:
			number = line.strip()
			list1.append(int(number))

		with open('test2.txt', 'r') as open_file:	
			for line in open_file:
				number = int(line.strip())
				if number in list1:				
					listOverlap.append(number)
				else:
					pass

		print (listOverlap)


if __name__ == "__main__":
	file_overlap('http://www.practicepython.org/assets/primenumbers.txt','http://www.practicepython.org/assets/happynumbers.txt')
