round
#promedio de duraciones 
otros_cursos_min = 2.5
otros_cursos_max = 7 
otros_cursos_promedio = 4 
dalto_curso = 1.5 
#duracion de crudos 
crudo_promedio= 5
crudo_dalto= 3.5
#diferencia de duraccion 
diferencia_con_max =  round (100 - dalto_curso  / otros_cursos_max *100)
diferencia_con_promedio = 100 - dalto_curso /otros_cursos_promedio *100
diferencia_con_min = 100 - dalto_curso /otros_cursos_min *100

print(f"ver 10 horas de este curso equivale a ver { otros_cursos_promedio *1000 //dalto_curso / 10 }")
print(f"ver 10 horas de este curso equivale a ver { dalto_curso *1000 // otros_cursos_promedio / 10 }")
print("---------------------")


print("---------------------")
print(f"el cuso de dalto duro un {diferencia_con_min}% menos que el mas rapido")
print(f"el cuso de dalto duro un {diferencia_con_promedio}% menos que el promedio")
print(f"el cuso de dalto duro un {diferencia_con_max}% menos que el mas lento")
print("---------------------")
