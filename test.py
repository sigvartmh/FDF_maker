#!/usr/bin/python
# -*- coding: utf-8 -*-

#import os
def fdf_txt_object(field_name, field_value):
	fdf_obj = "<</T("+str(field_name)+")/V("+str(field_value)+")>>"
	return fdf_obj

#filename = "output.pdf"
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


