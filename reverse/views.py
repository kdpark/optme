from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, Template, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from BeautifulSoup import BeautifulSoup
import urllib2, urllib, mechanize, datetime, random

def calculateAge(month, day, year):
	today=datetime.date.today()
	age = today.year - year
	# unpassed more minus 1
	if month >= today.month:
		if day > today.day:
			age = age-1
		
	return age

def main(request):
	br = mechanize.Browser()

	url = 'https://livingto100.com/'

	# receive user's data
	dateMonth = ['6']
	dateDay = ['10']
	dateYear = ['1987']
	gender = ['M']
	country_id = ['230']
	zipcode = '02215'
	accept= ['1']

	# user's answer
	# At the moment, Random variable!!



	# check all data are received successfully.

	# calculate the User Age
	age = calculateAge(int(dateMonth[0]), int(dateDay[0]), int(dateYear[0]))
	# external
	if age < 13 or age > 99:
		assert "unsupported age"

	br.open(url+'calculator')
	br.form = list(br.forms())[0]
	br.form['date[month]'] = dateMonth
	br.form['date[day]'] = dateDay
	br.form['date[year]'] = dateYear
	br.form['gender'] = gender
	br.form['country_id'] = country_id
	br.form['zipcode'] = zipcode
	br.form['accept'] = accept
	br.submit()

	flag=0
	br.form = list(br.forms())[0]
	# branch 4 - way
	if age > 38:
		if gender[0] == 'M':
			# start/1
			flag = 1
		else:
			# start/2
			flag = 2
	else:
		if gender[0] =='M':
			# start/3 (99~205)
			for x in range(99,206,2):
				if x == 161:
					br.form['161[1004]'] = ['B']
				else:
					ran = random.sample(br.form.find_control(str(x)).items, 1)
					br.form[str(x)] = [ran[0].name] # warning of list
		else:
			# start/4
			flag = 4

	br.submit()
	# len(br.form.find_control('190').items)
	# br.form.find_control('190').items[0].name
	# a = random.sample(br.form.find_control('190').items, 1)
	# a[0].name
	br.open(url+'users/sign_in')
	br.form = list(br.forms())[0]
	br.form['user[email]'] = 'lvnknlan@naver.com'
	br.form['user[password]'] = '1121rbeh'
	submitLogin = br.submit()
	# form value dictionary loading
	soup = BeautifulSoup(submitLogin)
	image_tags = soup.findAll('img')

	resultAge = image_tags[2]['alt']
	

	""" login module for result
	
	"""
	return HttpResponse("Your calculated life expectancy is "+ resultAge)

"""
def login(request):
	param = {'user[email]':'lvnknlan@naver.com',
	'user[password]' : '1121rbeh',
	#('user[password_confirmation]', '123'),
	'authenticity_token' : 'gWG7mqX3XzqnkaR1gJO9Fes9mbVZzEyYHWF8M1kW/ho='}
	data = urllib.urlencode(param)
	req = urllib2.Request('https://livingto100.com/users/sign_in', data)
	req.add_header('Content-type', 'application/x-www-form-urlencoded')
	result = urllib2.urlopen(req)
	#result = urllib2.urlopen('https://livingto100.com/users/sign_in', data)
	content = result.read()
	return HttpResponse(content)
	"""