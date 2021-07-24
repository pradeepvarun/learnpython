#List
l = ["bob", "pradeep", "Santu", "bob"]
print(l)
print(l[1])  # subscript notation can be userd to access element of list
l[0] = "smith"  # modifying the list element
l.append("Ajay") # Appending the list
l.remove("bob")
print(l)
print(type (l))
print(dir (l))
t = ("bob", "pradeep", "Santu", "bob")
print(t)
print(type(t))
print(dir(t))
s = {"bob", "pradeep", "Santu", "bob"}
s.add("anita")
s.pop()
print(s)  # Note that the duplicate set element is shown once

print(type(s))
print(dir(s))

# List comprehension

numbers = [1, 2, 3, 4, 5]
double = [num*num for num in numbers]
print (double)

#Alternatve
new_double=[]
for i in numbers:
    new_double.append(i*i)
print(new_double)
# Clearly the list comprehender is efficient.





















