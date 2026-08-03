student_data={
    "id1":{'name':"pujit","class":"9"},
    "id2":{'name':"sarah",'class':'8'},
    "id3":{'name':"pujit","class":"9"},
}
result={}
seen=[]
for student_id,details in student_data.items():
    unique_key=(details['name'],details["class"])
    if unique_key not in seen:
        seen.append(unique_key)
        result[student_id]=details
for k,v in result.items():
    print(k,":",v)