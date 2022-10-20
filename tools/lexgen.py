#!/usr/bin/env python3

import numpy as np

onset_probs     = 0.87
has_coda_probs  = 0.15

syllable_probs = {1: 0.13, 2: 0.80, 3: 0.07}

vowel_probs = {"a"  : 0.23, 
               "i"  : 0.17,
               "u"  : 0.26,
               "e"  : 0.16,
               "o"  : 0.18,
}

initial_probs = {"p"   : 0.044164389776260825,
                 "b"   : 0.10810835267630536 ,
                 "t"   : 0.07135828329322066 ,
                 "d"   : 0.07480676427712657,
                 "k"   : 0.024007299121923467 ,
                 "g"   : 0.015125958418424922,
                 "q"   : 0.08132845722873172 ,
                 "f"   : 0.06754721406458522 ,
                 "s"   : 0.1026574550068403  ,
                 "z"   : 0.029092302537119457,
                 "x"   : 0.08543717708662542 ,
                 "y"   : 0.056131972780616816,
                 "m"   : 0.05128228639123888 ,
                 "n"   : 0.09021167261822362 ,
                 "l"   : 0.02511646234737029 ,
                 "j"   : 0.041223229372901876,
                 "w"   : 0.032400723002484574,
}

coda_probs = {"n": 0.7 ,
              "k": 0.3 ,
}

## Make dictionaries with prob ranges assoc phonemes

def dict_make(raw):
  choices = {}
  low    = 0.0

  for choice, percent in raw.items():
    high = low + percent
    choices[choice] = (low, high)
    low = high

  return choices

## given a random val [0,1] extract the sound

def dict_access(choices, prob):
  for choice, (low, high) in choices.items():
    if (low <= prob) and (prob <= high):
      return choice

def rand_get():
  return np.random.uniform(low = 0.0, high = 1.0001)

## main

if __name__ == "__main__":

  vowels    = dict_make(vowel_probs)
  initials  = dict_make(initial_probs)
  codas     = dict_make(coda_probs)
  syllables = dict_make(syllable_probs) 

  for _ in range(0, 250):
    word = []
    coda = "#"

    for syls in range(np.random.randint(low = 2, high = 4)):
      if (rand_get() < onset_probs) or (coda == "_") or (syls == 1):
        onset = dict_access(initials, rand_get())
        while (coda == "k") and (onset in ["k", "g", "x", "y", "q"]):
          onset = dict_access(initials, rand_get())
        word.append(onset)
  
      vowel = dict_access(vowels, rand_get())
      word.append(vowel)
  
      if rand_get() < has_coda_probs:
        coda = dict_access(codas, rand_get())
        word.append(coda)
      else:
        coda = "_"
  
    print("".join(word)) 
