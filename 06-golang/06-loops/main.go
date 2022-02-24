package main

import "fmt"

func main() {
	favoriteFoods := [3]string{"Comida 1", "Comida 2", "Comida 3"}

	fmt.Println("MINHA COMIDAS FAVORITAS SÃO")

	for index, food := range favoriteFoods {
		fmt.Println(index, "-", food)
	}

	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
			//break
		}
		fmt.Println(n)
	}

	//WHILE
	count := 1
	for count <= 5 {
		fmt.Println("O contador é", count)
		count++
	}

	// LOOP INFINITO
	// for {
	// }
}
