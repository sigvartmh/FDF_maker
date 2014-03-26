#!/usr/bin/python
# -*- coding: utf-8 -*-

#import os
#import subprocess

"""
	Todo:
		1. Do a check with os if the previous file exist and do something to avoid crash if 2 people compile their list at the same time.
		2. Improve api
		3. Clean code
		4. Uncomment subprocess and subprocess.call(f(x)) when on server to do pdf+fdf merge.
"""

def fdf_txt_object(field_name, field_value):
	fdf_obj = "<</T("+str(field_name)+")/V("+str(field_value)+")>>"
	return fdf_obj

#filename = "output.pdf"
#filename should be the same as the pdf you are going to merge the data with

def fdf_make(filename, fdf_list,lonns_trinn):
#Meta header for FDF	
	fdf = ['%FDF-1.2\n']
	fdf.append('%âãÏÓ\n')
	fdf.append('1 0 obj\n')
	fdf.append('<</FDF<</F('+filename+')/Fields[')
	
#initialize values
	i=1
	j=1
	sum = 0
	
	for x in range(0,len(fdf_list)):
		if fdf_list[x][0] == "uke":
			name  = "Uke nrRow"+str(i)
			value = fdf_list[x][1]
			fdf.append(fdf_txt_object(name,value))
			i=i+1
		elif fdf_list[x][0] == "time":
			name  = "pr ukeRow"+str(j)
			value = fdf_list[x][1]
			sum = sum + value
			fdf.append(fdf_txt_object(name,value))
			j=j+1
	fdf.append(fdf_txt_object("Sum",sum))
	fdf.append(fdf_txt_object("Antall timer",sum))
	fdf.append(fdf_txt_object("Sats",lonns_trinn[1]))
	fdf.append(fdf_txt_object("Trinn",lonns_trinn[0]))
	fdf.append(fdf_txt_object("Belop",lonns_trinn[1]*sum))
	
#Meta end of file for FDF
	fdf.append(']/UF('+filename+')>>/Type/Catalog>>')
	fdf.append('endobj\n')
	fdf.append('trailer\n')
	fdf.append('<</Root 1 0 R>>\n')
	fdf.append('%%EOF\n')

	new_file = file('output.fdf','w')

	for i in range(0, len(fdf)):
		new_file.write(fdf[i])
	new_file.close()

	proccess_string='pdftk '+filename+' fill_form output.fdf output output.pdf'

	#Danger shell=True is a security hazard try shell=false
	#subprocess.call(proccess_string, shell=True)

valid_strings=["Sats","Antall timer","time","uke","Trinn"]
#if in valid strings do fdf.append(fdf_txt_object(name,value))

mylist=[("uke",3),("time",12),("time",14),("time",13),("uke",4),("uke",5)]
lonns_trinn=["C23",154.73]

fdf_make("P_6_web.pdf",mylist, lonns_trinn)

"""
filename = "P_6_web.pdf"

fdf = [b'%FDF-1.2\n']
fdf.append('%âãÏÓ\n')
fdf.append('1 0 obj\n')
fdf.append('<</FDF<</F('+filename+')/Fields[')

for i in range(1,10):
	name  = "Uke nrRow"+str(i)
	value = i
	fdf.append(fdf_txt_object(name,value))

for i in range(1,10):
	name  = "pr ukeRow"+str(i)
	value = i*2
	fdf.append(fdf_txt_object(name,value))

#time_felt=[(8,12]
#timer = "<</T(timer)/V("+ str(time_felt[0]) + ")>><</T(timer2)/V(" + str(time_felt[1]) +")>>"

#uker_felt=[2,7]
#uker = "<</T(uke)/V(" + str(uker_felt[0]) + ")>><</T(uke2)/V(" + str(uker_felt[1]) + ")>>"

#fdf.append(timer)
#fdf.append(uker)
	
#fdf.append('<</T(uke)/V(8)>><</T(uke2)/V(9)>>')

fdf.append(']/UF('+filename+')>>/Type/Catalog>>')
fdf.append('endobj\n')
fdf.append('trailer\n')
fdf.append('<</Root 1 0 R>>\n')
fdf.append('%%EOF\n')

new_file = file('new.fdf','w')

for i in range(0, len(fdf)):
	new_file.write(fdf[i])
new_file.close()

print(fdf);

"""
