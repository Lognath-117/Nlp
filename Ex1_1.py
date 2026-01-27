import re
patterns=[("[0-9]+","The fav movies for me is almost 0 but i watched more than 100 movies."),
           ("[A-Z][a-z]+"," Campa kudinga themba erunga "),
          ("[aeiou]+"," Kcet consert gang"),
          ("[a-z]+@[a-z]+\.com","Gmail id for putin is gmail@putin.com")]
for pattern, text in patterns:
    print("Pattern:",pattern)
    print("Text:",text)
    matches=re.findall(pattern,text)
    if matches:
        print("Matches found:",matches)
    else:
        print("No matches found")
        
