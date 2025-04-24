casos=int(input())
for i in range(1,casos+1):
   jugadas=input()
   b,h=jugadas.split(" ")
   if(b==h):
      print(f"Caso # {i}: ¡Otra vez!")
   elif(b=="tijeras" and h=="papel"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="papel" and h=="piedra"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="piedra" and h=="lagarto"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="Holk" and h=="tijeras"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="tijeras" and h=="lagarto"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="lagarto" and h=="papel"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="papel" and h=="Holk"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="Holk" and h=="piedra"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   elif(b=="piedra" and h=="tijeras"):
      print(f"Caso # {i}: ¡LaVidaEsdura!")
   else: 
      print(f"Caso # {i}: ¡No es suerte, es el árbitro!")                                         















