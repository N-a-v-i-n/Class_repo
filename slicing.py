# we can return a range of characters by using slicing concept
# syntax :- 1. string_name[start_with:Stop-1:Step]
#           2. slice(start,stop-1,step)
# here, start_with --> starting index value of a string
# here, stop_with --> ending index value of a string, but this could be stop-1
# here, Step --> number of difference b/w each index_value of a sting
string = "P C Naveen"
#10987654321(-neg)  --> Negative Index value
# ||||||||||
# P C Naveen 
# ||||||||||
# 0123456789  --> Positve index value 

print(string[0:5:1])     # o/p --> P C N
print(string[2:6])       # o/p --> C Na
print(string[-1:-7:-1])  # o/p --> neevaN   Note:- step = -1 will be start printing reversal 
print(string[::])        # o/p --> By default start_with == '0', Stop is == 'len(string)' and Step == '1' 

