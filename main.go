package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli/v3"
)

/*
paths := [
        "~/.config/nvim/*",
        "~/.config/alacritty/alacritty.toml",
        "~/.zshrc"
    ];
*/


func main() {
	createConfigFile()
	fmt.Println("Hello, World!")
	(&cli.Command{}).Run(context.Background(), os.Args)
}

func createConfigFile() {
	file, err := os.Create("castle.yml")

	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
}

func copyFiles() {
    /*
     * Read in paths from config file
     * For path in paths, copy the files at designated locations into current directory
     * Preserve directory structure
     * Create hash of files and store in like .castle or something
    */
}

func sync() {
    /*
     * Read in paths from config file 
     * Check their contents and get hash
     * If hash doesn't match file in current directory, recopy
     * Print success/ failure message
    */
}
