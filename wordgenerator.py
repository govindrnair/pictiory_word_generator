#!/opt/homebrew/bin/python3

import random

main_list = None
done_list = None

with open ('word_list','r') as f:
    main_list = f.read().splitlines()

with open ('done_list','r') as f:
    done_list = f.read().splitlines()

not_found = True
word = ""
while not_found:
    word = random.choice(main_list)
    if word not in done_list:
        not_found = False
        with open ('done_list','a') as f:
            f.write('\n')
            f.write(word)

print (word)
