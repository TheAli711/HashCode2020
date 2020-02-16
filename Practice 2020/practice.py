
x = input("Enter file name")

file = open(x,"r")
first = file.readline()
second = file.readline()
first_list=first.split()
second_list =second.split()
first_list_mod=[int(i) for i in first_list]
second_list_mod=[int(i) for i in second_list]

output=[]
trueoutput=[]

for i in second_list_mod[::-1]:
	output.append(i)
	if sum(output)<=first_list_mod[0]:
		continue
	else:
		output.remove(i)

for i in output[::-1]:
	trueoutput.append(str(second_list_mod.index(i,second_list_mod.index(i))))

x_out = x.split(".")
out_file = open(x_out[0]+".out","w")
out_file.write(str(len(trueoutput))+"\n")
for i in trueoutput:
	out_file.write(i+" ")

