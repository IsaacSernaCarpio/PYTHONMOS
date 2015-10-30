# *-* coding: iso-8859-1 *-*
import re
import fileinput
import csv, operator, codecs, cStringIO
import time,sys
import StringIO


class clsProsaMainTlalpan:
	
	
	def clsProsaMainTlalpan(self):
		print 'metodo vacio'
	
	def ProcesaArchivo(self):
		try:
			listaDedatos = []
			lista_nueva = []
			listafinal = []
			
			actual = {}
			primera = {}
			ultima = {}
			serial = ''
			duracion = 0
			aux = 0
			
			contadorDeLineas = 1
			print contadorDeLineas
			
				
			Escribir = open('TlalpanProsa.csv','a')
			
			for line in fileinput.input():
				print '______________________________________'
				print 'contador de liena: ',contadorDeLineas
				
				line 	= re.sub('"','',line)   	
				line 	= re.sub(';',',',line)
				
				linealinea 	= ''	
				ID 			= ''
				NoMarcado 	= ''
				Extension 	= ''
				
				if "ANSWERED" in line:
					print 'Largo de linea   : ',len(line)
					campos					= line.strip().split(',')
					actual['Dies'] 			= campos[1]
					actual['cuatro'] 		= campos[2]
					actual['treintaYdos'] 	= campos[5]
					
					dies 		= actual['Dies']
					cuatro 		= actual['cuatro']
					treintaYdos = actual['treintaYdos']
					
					print 'dies'		,dies
					print 'cuatro'		, cuatro
					print 'treintaYdos'	,treintaYdos
				
					if dies.isdigit() and cuatro.isdigit() and len(dies) == 10 and len(cuatro) == 4:
						print 'si esta cumpliendo con esto'
						print line
						
					else:
						if "}-" in line:
							try:
								print "}-"
								#itemsFound = re.findall("}-(.*),Zap\/", line)
								itemsFound = re.findall("}-(.{32})", line)
								ID = itemsFound[0]
								print line
							except Exception, e:
								print 'Error en linea de clase 165: \n %s' % e
						if len(treintaYdos) == 32:
							try:
								ID = treintaYdos
								print line
							except Exception, e:
								print 'Error en linea de clase 165: \n %s' % e
					#Escribir.write(ID, noMarcado, Extension)
					
					print line
					print ID
					print Extension
					
					listaDedatos.append(ID)
					
					print line
					Escribir.write(ID)
					Escribir.write(line)
					noMarcado = ''
				contadorDeLineas += 1		
				
		except Exception, e:
			print line
			if "SyntaxError" in e: 
				print "Error de Sintaxis" 
				return
			elif "No such file or directory" in e:
				print 'la direcion(path) no es correcta'
				return
			print 'Error en Lectura de archivo: \n %s' % e	
			return
		

obj = clsProsaMainTlalpan()
obj.ProcesaArchivo();
