Old_list = [1,2,3,4,5,6,7,8,9,10]

New_list = list(map(lambda x: x + 5 , Old_list))
print(New_list)

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))