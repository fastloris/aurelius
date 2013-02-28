import django
from meditations.models import BookSection
import json

json_data=open('meditations.json').read()
meditations = json.loads(json_data)
print meditations.keys()
for key in meditations.keys():
    book, chapter = key.split('.')
    print "book: " + book
    print "chapter: " + chapter
    print "content: " + meditations[key]
    bs = BookSection()
    bs.book = book
    bs.section = chapter
    bs.content = meditations[key]
    bs.save()
