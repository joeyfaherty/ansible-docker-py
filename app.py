import os, sys

def anogram_check(s1, s2):
  # Strings are sorted, transformed to lower case and verified
  if(sorted(s1.lower())== sorted(s2.lower())):
    print("Both strings form an anogram.")
  else:
    print("Both strings do not form an anogram.")
  
s1 =  sys.argv[1]
s2 =  sys.argv[2]
print("String input s1: ", s1 )
print("String input s2: ", s2 )
anogram_check(s1, s2)


