#collection data types in Python
#1.1 set..
print({2,0,3})
print({-2,0,4,5})
print(len({2,-3,1,2,3,23,3,1,1,4,3,1,2,2}))
print(sum({2,-3,1,}))
print(sum({2,-3,1,},4))

s1={0,9,-19,10,"kuch bi...","x","y","z"}
print({2,3,"abc"}|{2,-3,2})#UNION
print({2,3,"abc"}&{2,-3,2})#INTERSECTION

s2={"data",12,"ali",2,3,5,9,1,8,38,4,2,854,75,25}
s2.add("New value")
print(s2)

s2.remove("data")
print(s2)

s2.update(3,"Iqra")
print(s2)

s3={1,2,3,4,5,6,7}
s4={8,9,10,11,12,13,14}

print({x*x for x in s3|s4})
print({x*x for x in s3&s4})

print({x*y for x in s3 for y in s4})
print({x*y for x in {2,3} for y in {1,4}})

l1=[1,2,3,45,s3,"anything",2+9]
print(len(l1))

# print(sum([]))