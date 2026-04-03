thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict["year"] = thisdict["year"] +1
print(thisdict["year"])

if "model" in thisdict:
    print(thisdict["model"])