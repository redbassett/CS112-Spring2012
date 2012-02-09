#!/user/bin/env/ python


slices = 3

while True:
    input = raw_input("Cake or death? ").lower()
    if input == 'cake' and slices > 0:
        slices -= 1
        print "Very well!  Give him cake."
    elif input == 'death':
        print "You vividly die."
        break
