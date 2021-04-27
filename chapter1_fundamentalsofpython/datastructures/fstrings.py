## One of the most important python 3.6 additions were the so-called f-strings.
## It allows to format strings (previously done with %-formatting or str.format())

#a = 42
#print(f'The value of a is {a}.')

#an interesting example of this in action
from datetime import datetime
print(f'Current time is {datetime.now() :%H:%M}.')