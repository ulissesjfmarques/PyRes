# 0 = Green Square
# 1 = Red Triangle
# 2 = Yellow Circle
# 3 = Blue Star

pattern = [ [1,0,0,1,2,1,3,2],
            [2,1,3,0,2,3,0,0],
            [2,3,1,2,2,0,3,1],
            [0,3,2,3,1,3,0,2],
            [1,1,0,2,3,0,1,3],
            [3,2,1,3,2,3,1,3],
            [0,1,3,0,0,1,2,1]]

print("-------")
print("PATTERN:")
for row in pattern:
    print(row)
print("-------")

