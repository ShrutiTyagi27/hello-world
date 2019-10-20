import pdfquery
import re
import os,shutil
 

value_ch = re.search(r"Electricity Charges.{500}", text)
    value1_ch=value_ch.group().split()
    value1_ch=value1_ch[31]
    value1_ch=value1_ch.replace(r"Amount(`)","Electricity charges : ")
    value1_ch= value1_ch[:30]    
    print(value1_ch) 



 value_ch1= str(value_ch1)   
    if re.search("\d", value_ch1) :
        print(re.search("\d.{30}", value_ch1)) 