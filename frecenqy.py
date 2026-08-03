text_dict={"codingal":2,"john":2,"naithik":2,"sarah":2,"cameron":2}
print(str(text_dict))
k=2
result=0
for key in text_dict:
    if text_dict[key]==k:
     result=result+1
print(str(result))