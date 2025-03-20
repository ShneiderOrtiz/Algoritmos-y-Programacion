Algoritmo Ejercicio_7
	Escribir "Ingrese un número:"
	Leer num
	esPrimo <- Verdadero
	
	Si num <= 1 Entonces
		esPrimo <- Falso
	Sino
		i <- 2
		Mientras i <= num / 2 Y esPrimo Hacer
			Si num MOD i = 0 Entonces
				esPrimo <- Falso
			FinSi
			i <- i + 1
		FinMientras
	FinSi
	
	Si esPrimo Entonces
		Escribir "Es primo"
	Sino
		Escribir "No es primo"
	FinSi

	
FinAlgoritmo
