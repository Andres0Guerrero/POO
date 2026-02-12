# la mama de juan tiene 3 hijos #preguntarle la edad a juan
#Alberto tendrá 2/3 de la edad de juan #Ana debe tener 3/4 de la edad de juan
# la edad de la mama es la suma de las tres edades
edad_juan = int(input(" Hola Juan, ¿cuantos años tienes? : "))
edad_alberto = int(edad_juan*2/3) 
edad_ana = int(edad_juan*4/3)
edad_mamá = int(edad_juan + edad_alberto + edad_ana)
print (f"la edad de juan es : {edad_juan} años"); print (f"la edad de alberto es : {edad_alberto} años"); print (f"la edad de ana es : {edad_ana} años");
print (f"la edad de la mamá es : {edad_mamá} años");
