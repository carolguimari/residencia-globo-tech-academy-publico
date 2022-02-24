package main

import "fmt"

// MAPA É SIMILAR AO DICIONÁRIO DO PYTHON
// MAKE É O NEW DO JAVA
func main() {
	languageLevel := make(map[string]int)

	languageLevel["Java"] = 10
	languageLevel["PHP"] = 8
	languageLevel["JavaScript"] = 6
	languageLevel["GoLang"] = 4
	languageLevel["Dart"] = 2

	fmt.Println(languageLevel)

	languageLevel["Dart"] = 7

	fmt.Println(languageLevel)

	delete(languageLevel, "Dart")

	// -- //

	consoleAndGames := make(map[string][]string)

	consoleAndGames["Super Nintendo"] = append(consoleAndGames["Super Nintendo"], "Donkey Kong")

	var superNintendo = consoleAndGames["Super Nintendo"]

	consoleAndGames["Super Nintendo"] = append(superNintendo, "Super mario world")
	consoleAndGames["Super Nintendo"] = append(superNintendo, "Star Fox")

	consoleAndGames["Mega drive"] = append(consoleAndGames["Mega drive"], "Sonic")
	consoleAndGames["Mega drive"] = append(consoleAndGames["Mega drive"], "Streets of rage")
	consoleAndGames["Mega drive"] = append(consoleAndGames["Mega drive"], "Shinobi")

	fmt.Println(consoleAndGames)
	fmt.Println(consoleAndGames["Super Nintendo"])
	fmt.Println(consoleAndGames["Super Nintendo"][1])

	// delete
	consoleAndGames["Super Nintendo"] = append(consoleAndGames["Super Nintendo"][:1], consoleAndGames["Super Nintendo"][2:3]...)

	fmt.Println(consoleAndGames["Super Nintendo"])

}
