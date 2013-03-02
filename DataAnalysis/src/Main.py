#Reference:<<Oreilly.Data.Analysis.with.Open.Source.Tools.Nov.2010>>
import sys
import random as rnd
#Variables
first_choice = None
second_choice = None
#Main loop
#must be 'stick','choose',or 'switch'
strategy = sys.argv[1] 

wins = 0

for trail in range(1000) :
    #The prize is always in envelope #0... but we don't know that
    envelops = [0,1,2]
    ## Pre-choice
    first_choice = rnd.choice(envelops)
    
    if first_choice == 0:
        envelops = [0,rnd.choice([1,2])] # Randomly retain 1 or 2
    else:
        envelops = [0,first_choice] # Retain winner and first choice
    ## Strategy 
    if strategy == 'stick':
        second_choice = first_choice
    elif strategy == 'choose':
        second_choice = rnd.choice(envelops)
    elif strategy == 'switch':
        envelops.remove(first_choice)
        second_choice = envelops[0]
        
    ## Remember that the prize is in envelop#0
    if second_choice == 0:
        wins +=1
print("Total wins:",wins)