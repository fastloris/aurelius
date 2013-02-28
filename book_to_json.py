def roman_to_int(input):
   if type(input) != type(""):
      raise TypeError, "expected string, got %s" % type(input)
   input = input.upper()
   nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
   ints = [1000, 500, 100, 50,  10,  5,   1]
   places = []
   for c in input:
      if not c in nums:
         raise ValueError, "input is not a valid roman numeral: %s" % input
   for i in range(len(input)):
      c = input[i]
      value = ints[nums.index(c)]
      # If the next place holds a larger number, this value is negative.
      try:
         nextvalue = ints[nums.index(input[i +1])]
         if nextvalue > value:
            value *= -1
      except IndexError:
         # there is no next place.
         pass
      places.append(value)
   sum = 0
   for n in places: sum += n
   return sum

import re

book = open('pg2680.txt','r')
line_count = 0
para_count = 0
section_count = 0
book_count = 0
section_pattern = r'^([A-Z]*)\.'
content_dict = {}
ordered_keys = []
for line in book:
    line = line.rstrip()
    line_count += 1
    if line == "":
        para_count += 1
    if line == "THE FIRST BOOK":
        book_count = 1
        line = ""
    if line == "THE SECOND BOOK":
        book_count = 2
        line = ""
    if line == "THE THIRD BOOK":
        book_count = 3
        line = ""
    if line == "THE FOURTH BOOK":
        book_count = 4
        line = ""
    if line == "THE FIFTH BOOK":
        book_count = 5
        line = ""
    if line == "THE SIXTH BOOK":
        book_count = 6
        line = ""
    if line == "THE SEVENTH BOOK":
        book_count = 7
        line = ""
    if line == "THE EIGTH BOOK":
        book_count = 8
        line = ""
    if line == "THE NINTH BOOK":
        book_count = 9
        line = ""
    if line == "THE TENTH BOOK":
        book_count = 10
        line = ""
    if line == "THE ELEVENTH BOOK":
        book_count = 11
        line = ""
    if line == "THE TWELFTH BOOK":
        book_count = 12
        line = ""
    if line == "APPENDIX":
        book_count = 0
    if book_count != 0:
        if line != "":
             if re.match(section_pattern, line):
                 this_section = re.match(section_pattern, line)
                 roman = this_section.group(0).rstrip('.')
                 section_count = roman_to_int(roman)
             key = str(book_count) + '.' + str(section_count)
             if key in content_dict:
                 content_dict[key] += " " + line 
             else:
                 content_dict[key] = line
                 ordered_keys.append(key)


import json
print json.dumps(content_dict, sort_keys=True,indent=2)

#print "{"
#print "    \"book\": \"Meditations\"",
#print "    \"author\": \"Marcus Aurelius\"",
#print "    \"contents_\":"
#for key in ordered_keys:
#    curbook, cursect = key.split('.')
#    print "    {"
#    print "        \"book\": " + curbook + ","
#    print "        \"section\": " + cursect + ","
#    print "        \"text\": \"" + content_dict[key] + "\""
#    print "    },"
#print "}"     
