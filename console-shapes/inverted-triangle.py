empty = 5;
string = '';

for k in range(5):
    string = ''
    string += ' ' * empty
    string += ' *' * (k + 1)
    empty -= 1  
      
    print(string)
