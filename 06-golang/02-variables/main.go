package main

import "fmt"

func main() {
	const minhaConstanteString string = "Miguel Silva"
	const minhaConstanteInteiro int = 154
	var name string = "Miguel Muller"
	var firstName, lastName = "Miguel", "Muller"
	comAtalhoString := "variavel atribuida com atalho"
	comAtalhoInteiro := 1

	fmt.Println("var-name:", name, "const-inteiro:", minhaConstanteInteiro)
	fmt.Printf("Meu nome completo é: %s %s \n", firstName, lastName)
	fmt.Println(comAtalhoString)
	fmt.Println(comAtalhoInteiro)
}
