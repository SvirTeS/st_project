import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['numbers of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    result = prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return " ".join(result.split())


testdata = [Contact(firstname='', middlename='', lastname='', nickname='',
                       title='', company='', address='', home_phone='', mobile_phone='',
                       work_phone='', fax='', email='', email2='', email3='', homepage='')] + [
    Contact(firstname=random_string('firstname', 6),
            middlename=random_string('middlename', 6),
            lastname=random_string('lastname', 8),
            nickname=random_string('nickname', 4),
            title=random_string('title', 5),
            company=random_string('company', 7),
            address=random_string('address', 15),
            home_phone=random_string('home_phone', 11),
            mobile_phone=random_string('mobile_phone', 11),
            work_phone=random_string('work_phone', 11),
            fax=random_string('fax', 7),
            email=random_string('email', 20),
            email2=random_string('email2', 20),
            email3=random_string('email3', 20)) for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
