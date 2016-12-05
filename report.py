import sys

def sep(filename,protocol):
	if(len(filename) == 0):
		print("len(filename) == 0")
		classify(filename,protocol)
	else:
		for i in range(len(filename)):
			filename[i] = filename[i].split(".")
		classify(filename,protocol)
	#print(filename)
		
def classify(filename,protocol):
	count = []
	compression_type = ["zip","tar","bz2","gz"]
	file_type = ["doc","docx","xls","xlsx","csv","txt"]
	
	if(len(filename) == 0):
		count.append(0)
	else:
		for i in range(len(filename)):
			for k in range(len(filename[i])):
				#print(filename[i][k])
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
	total = 1
	success = 1
	#print(count)
	#for i in count:
		#if(i == 0):
			#total += 1
			#success += 1
		#else:
			#total += 1

	rep.write(protocol + ": " + str(success) + " success out of " + str(total) + "\n")
	rep.close()

def main(arg1, arg2):
	filename = []
	filename.append(str(arg1))
	protocol = str(arg2)
	sep(filename, protocol)

def print_(filename):
	for i in range(len(filename)):
		for l in range(len(filename[i])):
			print filename[i][l] + "\n"

if __name__ == '__main__':
	sys.exit(main(sys.argv[1], sys.argv[2]))
