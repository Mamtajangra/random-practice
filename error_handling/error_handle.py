# agar hmm koi file create krna chahte h to hme write mode main kholna hoga aur file automatically create ho jaayegi
# file ko write krne ke baad hmari responsibility h ki usko close bhi karein
# but inn methods ko handle krne ke liye ek hai jisse hmm file ko with mode main khole to close aur handle krne ki need nhi h

# file = open("test.py","w")
# try:
#     file.write("hello mamu")
# finally:
#     file.close    



    #  simple 
with open("mmu.py","w") as file:
    file.write("hiiii mamu")    