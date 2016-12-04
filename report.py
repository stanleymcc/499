def sep(filename,protocol):
    if(len(filename) == 0):
        classify(filename,protocol)
    else:
        for i in range(len(filename)):
            filename[i] = filename[i].split(".")
        classify(filename,protocol)
def classify(filename,protocol):
    count = []
    compression_type = ["zip","tar","bz2","gz"]
    file_type = ["doc","docx","xls","xlsx","csv","txt"]
    
    if(len(filename) == 0):
        count.append(0)
    else:
        for i in range(len(filename)):
            for k in range(len(filename[i])):
                print(filename[i][k])
                if(filename[i][k] == "encrypted"):
                    count.append(2)
                    
                elif(filename[i][k] == "unencrypted" and len(filename[i][k]) < 2):
                    count.append(1)                
                
                elif(filename[i][k] == "unencrypted" and len(filename[i][k]) > 2):
                    count.append(1)
               
                elif(len(filename[i][k]) <= 0):
                    count.append(0)
                
            
    file_generate(count,protocol)
                    
def file_generate(count,protocol):
    rep = open("report.txt","w")
    total = 0
    success = 0
    print(count)
    for i in count:
        if(i == 0):
            total += 1
            success += 1
        else:
            total += 1
    rep.write(protocol + " " + str(success) + " out of " + str(total))
    rep.close()
def main():
    filename = ["encrypted.csv","unencrypted.docx.zip","encrypted.docx.tar.gz","unencrypted.docx",""]
    protocol = "HTTP"
    sep(filename,protocol)
    
def print_(filename):
    for i in range(len(filename)):
        for l in range(len(filename[i])):
            print filename[i][l] + "\n"
main()