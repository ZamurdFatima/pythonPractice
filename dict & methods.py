a={}
b=set()
print(a, type(a))
print(b, type(b))
classStrength={"Class1" :22, "Class3":32}
marks={"ZARA":34, "Zain":21, "Zamurd":43}
print(marks["ZARA"])
print(marks.get("Zara"))                  #by using get there would'nt be any error for wrong name
print(marks.keys())
print(marks.values())
print(marks.items())
print(marks.__ior__(classStrength))       #modifies the object in place

