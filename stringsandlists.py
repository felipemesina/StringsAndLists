words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")

newwords = "It's thanksgiving day. It's my birthday, too!"
print newwords.replace("day", "month")

x = [2, 6, 8, 1, 20, 11, 3, 7]
print (min(x))
print (max(x))

y = ["name", 20, "hi", "bye", 7, "hello", 1, 4]
print y[0]
print y[-1]
z=[y[0], y[-1]]
print z

i = [19,2,54,-2,7,12,98,32,10,-3,6]
i.sort()
print i
first_list = i[:len(i)/2] 
second_list = i[len(i)/2:] 
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
