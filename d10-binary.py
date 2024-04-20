my_file = str(open("d10", r))

my_binary_output = ""
  
for my_char in my_file:
    if(int(my_char) % 2 = 0):
        my_binary_output.append("0")
    else:
        my_binary_outpud.append("1")

print(my_binary_output)
