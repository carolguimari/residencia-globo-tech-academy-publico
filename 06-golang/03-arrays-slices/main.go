package main

import "fmt"

func main() {
	//ARRAYS
	var colors = [3]string{"Azul", "Vinho"}

	fmt.Println("o array tem", len(colors), "posições")
	fmt.Println("Os valores são", colors)
	fmt.Println("O 1º valor é", colors[0])

	colors[2] = "Vermelho"
	fmt.Println("Os valores são", colors)

	//SLICES
	var favoritesGames []string

	favoritesGames = append(favoritesGames, "Primeiro")
	favoritesGames = append(favoritesGames, "Segundo")
	favoritesGames = append(favoritesGames, "Terceiro")
	favoritesGames = append(favoritesGames, "Quarto")
	favoritesGames = append(favoritesGames, "Quinto")

	fmt.Println(favoritesGames)

	favoritesGames = append(favoritesGames[:2], favoritesGames[3:]...)
	// ... FUNÇÃO VARIADIC
}
