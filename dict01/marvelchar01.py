#!/usrbin/env python3

marvelchars = {
"Starlord":
    {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},
    "Mystique":
        {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},
"She-Hulk":{
  "real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
                }

char_name = input("Which character do you want to know about? (starlord, mystique, she-hulk)").title()
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)").lower()
#print(marvelchars, sep= ", ")
print(char_name,"s", char_stat, "is:", marvelchars[char_name][char_stat]) 
                                                    # notice that when you put the cursor over the last parens, it doesn't highlight the FIRST one next to print at the beginning of the line
                                                    # shows that you're missing an ending parenthesis at the end of line 21 :)
#would the get method give the current power of the chosen character?
# as written, no I don't believe so... the first argument is the key being "get"ted, the second argument is what gets returned if no key is found.
#Ok. I'll do some more digging . Ok cool! Let me know if you need any help!

