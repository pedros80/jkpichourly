import twitter
import glob
import random

tweeter = twitter.Api(consumer_key='RbIQCGFG2DUeCMeByYnOqwQE3',
                  consumer_secret='AnN2klrw9HE628aDWAtPqZowgGD2Dr3s5EJgbUqzcH3VUNPeDN',
                  access_token_key='921528056841416706-pza5BXDuC3rAQhjA3M6fMnoCpsvSjjd',
                  access_token_secret='OQRA49dgEjL6R5rZJaNzzndY07XdEaBaT177pGA3b9D22')

# my_file = '/home/pedros/jkpic/spock.png'

# status = api.PostUpdate('', my_file)
# print(status)

files = glob.glob('img/*.jpg')
status = tweeter.PostUpdate('', random.choice(files))
