with open("text.txt", "r+") as my_file:
  my_file.write("Adding to file")
  
  if my_file.closed == False:
    my_file.close()
    
   
print my_file.closed
