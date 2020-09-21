# Python3 code to demonstrate  
# rotation of list  
# using slices

  
# initializing list 
test_list = [1, 4, 6, 7, 2, 11, 44, 66, 77, 22] 
  
# printing original list  
print ("Original list : " + str(test_list)) 
  
# using slicing to left rotate by 3 
test_list = test_list[3:] + test_list[:3] 
  
# Printing list after left rotate 
print ("List after left rotate from [3] in list : " + str(test_list)) 
  
# using slicing to right rotate by 3 
# back to Original 
test_list = test_list[-3:] + test_list[:-3] 
  
# Printing after right rotate 
print ("List after right rotate by 3(back to original) : "
                                         + str(test_list))


test_list = test_list[1-5]
print('REVERSE' + str(test_list))
                                        