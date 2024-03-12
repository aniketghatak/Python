dict1={
  "name":"John",
  "color":"blue",
  "fruit":"grapes"
}

print(dict1["name"])
print(dict1["fruit"])

print(list(dict1.keys())) 
print(dict1.values()) 
print(dict1.items())

updatedict1={
  "sport":"football"
}

dict1.update(updatedict1)
print(dict1)
print(list(dict1.keys())) 