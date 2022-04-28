a={}

a ["이름"] = "지혜민"
a ["나이"] ="24살"
a ["학번"] ="2019144002"
a ["학과"] ="건설환경공학과"
a ["생일"] = "19990721"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학과"]
del a["학번"]
del a["생일"]

print(a)
print(len(a))
print()

a = dict(이름="김수현", 나이 ="22살", 학번 ="2019144002", 학과="건설환경공학과", 생일="990721")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))





