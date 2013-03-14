##
##                               <\              _                
##                                \\          _/{                  
##                         _       \\       _-   -_                
##                       /{        / `\   _-     - -_              
##                     _~  =      ( @  \ -        -  -_            
##                   _- -   ~-_   \( =\ \           -  -_          
##                 _~  -       ~_ | 1 :\ \      _-~-_ -  -_        
##               _-   -          ~  |V: \ \  _-~     ~-_-  -_      
##            _-~   -            /  | :  \ \            ~-_- -_    
##         _-~    -   _.._      {   | : _-``               ~- _-_  
##      _-~   -__..--~    ~-_  {   : \:}                           
##    =~__.--~~              ~-_\  :  /                            
##                               \ : /__                           
##                              //`*'--\\                          
##                             <+       \\                         
##                              \\      WWW                       
##                              MMM
##
##  This Pterror will eat all of the bugs in this code!
##  Some things that we have to look into:
##  How do we make a random integer?

import random

guess_counter = 0
guess = 0
magic_number = random.randint(1, 100)

#The first thing, get this to ask our names. Let's use the raw_int function.

name = raw_input('What is your name?')
print('Nice to meet you, '+name)

print('Well, ' +name +', I am thinking of a number between 1 and 100')

while guess !=magic_number or guess_counter < 6:
    # print magic_number
    guess = int(raw_input('Take a guess: '))

    if guess > 100 or guess < 1:
        guess_counter +=1
        print 'That\'s not a number between 1 and 100!'

    elif guess < magic_number:
        guess_counter +=1
        print 'Take another guess, dingus! \n (because it\'s too small, you big dummy!)'

    elif guess > magic_number:
        print 'take another guess, shithead!\noh yea, it\'s too big'
        guess_counter +=1

    else:
        print 'Why not blast your own butthole?'
        guess_counter +=1
        break
print 'Congrats, ' +name +', it took you, ' +str(guess_counter) +' tries to get it right.'
