package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

// Load input file into two lists of integers
func loadInputFile(filename string) ([]int, []int) {
	var l1, l2 []int

	// Open file
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		os.Exit(1)
	}
	defer file.Close()

	// Iterate for each line and grab the two list values
	scanner := bufio.NewScanner(file)
	for {
		if !scanner.Scan() {
			break
		}
		line := scanner.Text()
		parts := strings.Fields(line)
		v1, _ := strconv.Atoi(parts[0])
		v2, _ := strconv.Atoi(parts[1])
		l1 = append(l1, v1)
		l2 = append(l2, v2)
	}

	return l1, l2
}

// Make unique element slice - NOT USED IN THIS TASK THO
// Keep in case we need a reference to template/generic
// and unique element slice later.
// func uniqueElements[T comparable](inputSlice []T) []T {
// 	uniqueSlice := []T{}
// 	lookup := make(map[T]bool)
// 	for _, entry := range inputSlice {
// 		if _, value := lookup[entry]; !value {
// 			lookup[entry] = true
// 			uniqueSlice = append(uniqueSlice, entry)
// 		}
// 	}
// 	return uniqueSlice
// }

// Calculate the distance between two lists (STAGE 1)
// Sort the lists and compare lowest to lowest, second
// lowest to second lowest, etc. and sum the differences
func calculateListDistanceStage1(list1 []int, list2 []int) int {
	distance := 0
	for i := 0; i < len(list1); i++ {
		tmp := (list1[i] - list2[i])
		distance += int(math.Abs(float64(tmp)))
	}
	return distance
}

// Calculate the distance between two lists (STAGE 2)
// Calculate the number of occurrences of each element from
// list1 in list2 and multiply the element by the number of
// occurrences and sum the results
func calculateListDistanceStage2(list1 []int, list2 []int) int {
	// Count number of occurrences for each element from list1 in list 2
	distance := 0
	for _, element := range list1 {
		count := 0
		for _, value := range list2 {
			if value == element {
				count++
			}
		}
		distance += element * count
	}
	return distance
}

// Main method
func main() {
	// Get first argument as input file
	inFile := "test_input.txt"
	os.Args = os.Args[1:]
	if len(os.Args) >= 1 {
		inFile = os.Args[0]
	}

	// Parse file into lists
	list1, list2 := loadInputFile(inFile)

	// Sort lists
	slices.Sort(list1)
	slices.Sort(list2)

	// Get distance between lists
	distanceStage1 := calculateListDistanceStage1(list1, list2)
	distanceStage2 := calculateListDistanceStage2(list1, list2)

	// Print message
	fmt.Printf("[STAGE 1] List distance: %d\n", distanceStage1)
	fmt.Printf("[STAGE 2] List distance: %d\n", distanceStage2)

	// Exit with success
	os.Exit(0)
}
