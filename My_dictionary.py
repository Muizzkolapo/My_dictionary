import json
from difflib import get_close_matches


with open('data.json') as f:
  data = json.load(f)


def translate(my_input):
  my_input = my_input.lower()
  my_compare = get_close_matches(my_input, data, 1)
  if my_input in data:
      return data[my_input]
  elif my_input.upper() in data:
      return data[my_input.upper()]
  elif my_input.title() in data:
      return data[my_input.title()]
  elif len(my_compare)> 0:
      check = input("Did you mean %s instead? Enter Y if yes, or N if no: " % my_compare)
      check = check.upper()
      if check == 'Y':
          return data[my_compare[0]]
      elif check == 'N':
           return 'enter a valid word'
      else:
          return 'enter valid word'
my_input = input("Enter word: ")
translated = translate(my_input)

if type(translated) == list:
   for elem in translated:
    print (elem)
else:
    print(translated)




