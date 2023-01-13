# file handleing :- Through this we can do --> 1. Storing particular data Results in a sheets, text, etc..  2. Taking any inputs from CSV, TXT, ZIP_File.
#------------------
# syntax :- f=open("file_name","mode")  Note:- always file_name & Mode should enclosed with string !!

# 1. Modes :- read (r), write(w), append(a)
# 2. open :- to open any file and in what mode it should be i.e read/write/append
# 3. close :- Once file is open, it must should be closed due to data sensitivity
# 4. readable() :- this is a method which will return bool value, indicates that file is readable or Not
# 5. writeable():- this is a method which will return bool value, indicates that file is writable or Not
# 6. closed :-  this is a attribute or like any properties/property, which will return bool value, indicates that file is closed or Not


#Case 1:-  (read_mode)
#---------------
#f=open("abc.txt","r")  #Note:- to reading the file it must should exist in local_drive
#data=f.read()
#print(data) 
#f.close()

#o/p:- 1. it will check for file abc.txt is exist, if not exist it will give error about no such directory/file found
#      2. if file exist, it will read_data and store in data_variable and print data
#      3. close that file


#Case 2:-   (write_mode)
#---------------
#f=open("abc.txt","w")  # for write mode, if file is not exist, then it will create a new empty file with 'txt' extension in the pyth_current directory
#f.close()

#o/p:- 1. it will check for file abc.txt is exist, if not exist it will create new file with name abc.txt.
#      2. close that file


#Case 3:-   (write_mode)
#---------------
#f=open("ecom_project.txt","w")
#print("file Name : ",f.name)
#print("file Mode : ",f.mode)
#print("Is file readable : ",f.readable())
#print("Is file Writable : ",f.writable())
#print("Is file Closed : ",f.closed)
#f.close()
#print("Is file Closed : ",f.closed)

#O/p:-
# file Name :  ecom_project.txt
# file Mode :  w
# Is file readable :  False
# Is file Writable :  True
# Is file Closed :  False
# Is file Closed :  True


# Case 4:-  (write operations On TxT_file)
#---------------------------
#f=open("besant_data.txt","w")  
#f.write("Besant\n")
#f.write("Technology\n")
#f.write("HSR\n")
#print("Data Written to the file successfully ")
#f.close()

#O/p:- 1. file is create
#      2. write data "Besant "
#      3. write data "Technology"
#      4. write data "HSR"'
#      5. Print f
#      6. close 

# Case 5:-   (read operations on TXT_file)
#-------------------------
#f=open("besant_data.txt","r")   #Note:- we are reading that same file which is created in previous steps
#data=f.read()
#print(data)
#f.close()


#Note : - When ever we open any existing file in write mode.. it will clear that existing file data, and then it will write all new data

# Case 6:-   (Write, append, & read   example)
#-------------------------
f=open("besant.txt","w")
f.write("Besant\n")
f.write("Technology\n")
f.write("HSR\n")
f.close()

f=open("besant.txt","a")
f.write("Besant111\n")
f.write("Technology11\n")
f.write("HSR111\n")
f.close()


f=open("besant.txt","r")
data=f.read()
print(data)
f.close()




