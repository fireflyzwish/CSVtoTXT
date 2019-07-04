import csv,re
prefix="+39"
sms=open("smspro.txt","w")
with open("appuntamentiorario.csv") as csvfile:
    numreader=csv.reader(csvfile, delimiter=';')
    str_list = []
    for row in numreader:
        nmb=re.sub(r'\D', '',row[11]).split()
        for i in nmb:
            i=re.sub(r'\D', '',i)
            if i not in str_list:
                str_list.append(i)
                sms.write(prefix+i+"\n")
