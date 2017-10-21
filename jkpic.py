import twitter
import glob
import random

tweeter = twitter.Api(consumer_key='RbIQCGFG2DUeCMeByYnOqwQE3',
                  consumer_secret='AnN2klrw9HE628aDWAtPqZowgGD2Dr3s5EJgbUqzcH3VUNPeDN',
                  access_token_key='921528056841416706-pza5BXDuC3rAQhjA3M6fMnoCpsvSjjd',
                  access_token_secret='OQRA49dgEjL6R5rZJaNzzndY07XdEaBaT177pGA3b9D22')

zero_quotes = ['zero drops given', 'why does it never rain on jason?']

files = glob.glob('/home/ubuntu/jkpichourly/img/*.jpg')
with open('/home/ubuntu/jkpichourly/data/data.txt', 'r') as f:
	num_raindrops = int(f.read())
	if num_raindrops == 1:
		s = ''
	else:
		s = 's'
	out = '{} raindrop{} counted'.format(num_raindrops, s)
	counted = random.randint(0, 100)
	if (counted % 5 == 0):
		counted = 0
	num_raindrops += counted
	if counted == 0:
		out += ' ({})'.format(random.choice(zero_quotes))
	#status = tweeter.PostUpdate(out, random.choice(files))
	print out

with open('/home/ubuntu/jkpichourly/data/data.txt', 'w') as f:
	f.write(str(num_raindrops))