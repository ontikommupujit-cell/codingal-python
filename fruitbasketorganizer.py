basket1={"apple","banana","watermelon","tamato","apple","watermelon"}
basket2={'apple',"kiwi","orange","pineapple","pineapple"}
print('basket1',basket1)
print('basket2',basket2)
#adding orange to basket 1
basket1.add("orange")
print('basket1 after adding orange',basket1)
#finding the common fruits in both baskets
common_fruit=basket1.intersection(basket2)
print(common_fruit)
#import array of fruit count
import array as arr
fruit_count=arr.array('i',[3,2,5,4])
print(fruit_count)
#adding a new fruit count
fruit_count.insert(0,1)
fruit_count.append(6)
print(fruit_count)
#checking how many times number 2 appears
count_of_2=fruit_count.count(2)
print("the number of times number 2 is there is",count_of_2)
#we are going to reverse the array
fruit_count.reverse()
print(fruit_count)
#class fruit summery
print('')
print('================Class Fruits================')
print('basket1 is',basket1)
print('basket2 is',basket2)
print('the amount of reverse fruits is',fruit_count)
print('the amount of common fruits is',common_fruit)
print('=============================================')