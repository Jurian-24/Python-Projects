import sys
player_one = input('Voer je naam in speler 1:')
player_two = input('Voer je naam in speler 2:')
word = input(player_one + ', voer je woord in die ' + player_two + ' moet raden: ')

word_length = len(word)
good_letters = []
counter = 0
wordlist = []

for index in word:
    wordlist += '_'

while counter < 9:
    letter = input(player_two + ', geef een letter op: ')
    if(letter in word):
        for i in word:
            if(i == letter):
                for index in range(len(word)):
                    if word[index] == letter:
                        wordlist[index] = letter
                good_letters.append(letter) if letter not in good_letters else print('Deze letter zit er al in!')
        print(wordlist)
        if(len(good_letters) == word_length):
            print(player_two + ' heeft gewonnen!')
            sys.exit()
        else:
            print('Je hebt een letter goed! Je moet er nog', word_length - len(good_letters))
            guessed_word = ''.join(good_letters)
            
    else:
        counter = counter + 1
        print('Deze letter zit er niet in :(. Je hebt nu ' + str(counter) + ' fout(en)')
        
print(player_one + ' heeft gewonnen! Volgende keer beter :( ')