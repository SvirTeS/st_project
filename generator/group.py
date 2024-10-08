import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.group import Group


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['numbers of groups', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    result = prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return " ".join(result.split())


testdata = [Group(group_name='', group_header='', group_footer='')] + [
    Group(group_name=random_string('name', 10), group_header=random_string('header', 20),
          group_footer=random_string('footer', 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
