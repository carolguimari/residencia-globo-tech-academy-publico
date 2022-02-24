package main

import (
	"fmt"
	"strings"
)

func main() {
	mensagem := ""
	heroi_pesquisa := ""
	lista_herois := make(map[string]int)

	fmt.Printf("Entrei com o nome do herói: ")
	fmt.Scanln(&heroi_pesquisa)

	lista_herois["capitaoamerica"] = 10
	lista_herois["homemdeferro"] = 8
	lista_herois["gaviaoarqueiro"] = 6
	lista_herois["hulk"] = 4
	lista_herois["homemaranha"] = 9

	if contains(lista_herois, heroi_pesquisa) {
		if lista_herois[heroi_pesquisa] >= 7 {
			mensagem = fmt.Sprintf("%s é  muito Forte", heroi_pesquisa)
		} else {
			mensagem = fmt.Sprintf("%s é  pouco Forte", heroi_pesquisa)
		}
	} else {
		mensagem = fmt.Sprintf("%s não está na lista", heroi_pesquisa)
	}

	fmt.Println(mensagem)
}

func contains(elements map[string]int, value string) bool {
	for i := range elements {
		if strings.ToUpper(i) == strings.ToUpper(value) {
			return true
		}
	}
	return false
}
