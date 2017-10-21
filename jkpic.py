import twitter
import glob
import random

tweeter = twitter.Api(consumer_key='RbIQCGFG2DUeCMeByYnOqwQE3',
                  consumer_secret='AnN2klrw9HE628aDWAtPqZowgGD2Dr3s5EJgbUqzcH3VUNPeDN',
                  access_token_key='921528056841416706-pza5BXDuC3rAQhjA3M6fMnoCpsvSjjd',
                  access_token_secret='OQRA49dgEjL6R5rZJaNzzndY07XdEaBaT177pGA3b9D22')

files = glob.glob('img/*.jpg')
with open('data/data.txt', 'rw') as f:
	num_raindrops = int(f.read())
	if num_raindrops == 1:
		s = ''
	else:
		s = 's'
	out = '{} raindrop{} counted'.format(num_raindrops, s)
	#status = tweeter.PostUpdate(out, random.choice(files))
	print out
	num_raindrops +=1

with open('data/data.txt', 'w') as f:
	f.write(str(num_raindrops))