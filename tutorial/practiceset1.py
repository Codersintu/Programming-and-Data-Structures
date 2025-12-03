# problem 1.
# name=input("Enter your name: ")
# print(f"Good afternoon, {name}")

# problem 2.
letter=''' Dear <|Name|>,
        You are selected!
        <|Date|>'''

print(letter.replace("<|Name|>","sintu").replace("<|Date|>","2 September 2050"))

#problem 3
name="hello man  ther is "
print(name.find("  "))
print(name.replace("  "," ")) #string are immutable which means that you cannot change

#problem 5
letter="Dear Harry, \n\tthis python course is nice.\n Thnaks"
print(letter)
