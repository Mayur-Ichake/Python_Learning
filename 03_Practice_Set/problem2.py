# write a program to fill in a letter template given below with name and date   

letter ='''Dear <|Name|>,
You are selected!
<|Date|>'''

# question is replace 
"""print("Dear Mayur,\nYou are selected!\n15-07-2025")"""


print(letter.replace("<|Name|>", "Mayur").replace("<|Date|>", "15-07-2025"))