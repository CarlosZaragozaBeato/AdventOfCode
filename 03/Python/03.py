"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, 
but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. 
"Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, 
but nobody can figure out which one. If you can add up all the part numbers
in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand, 
but apparently any number adjacent to a symbol, even diagonally, is a "part number"
and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""
import os 





def check_letter(letter):
    if letter not in lst_numeros and letter != ".":
        return True




if __name__ == "__main__":
    path = "/home/carlos/AdventOfCode/03/Python/engine_scheme.txt"
    lst_valids = []
    lst_no_valids = []
    check = False 
    lst_numeros =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    i_line = 0
    j_letter = 0 

    with open(path, "r") as f:
        lines = f.readlines()
        
        while i_line < len(lines):
            j_letter = 0
            num_temp = ""
            while j_letter < len(lines[i_line]):
                condicion = False 
                if lines[i_line][j_letter] in lst_numeros:
                    if j_letter < len(lines[i_line]) -1:
                        num_temp += lines[i_line][j_letter]
                        j_letter += 1
                else:
                    if len(num_temp) > 0:
                        condicion = False
                        top_row = None
                        bottom_row = None
                        left_row = None
                        right_row = None

                        begin  = j_letter - len(num_temp)
                        value = lines[i_line][begin:j_letter]
                        
                        for i_intro in range(begin, j_letter):
                            if i_line == 0:
                                if  j_letter == 0:
                                    right_row = check_letter(lines[i_line][j_letter + 1])
                                    bottom_row = check_letter(lines[i_line+1][i_intro])
                                elif j_letter == len(lines[i_line]):
                                    left_row = check_letter(lines[i_line][begin - 1])
                                    bottom_row = check_letter(lines[i_line+1][i_intro])
                                else:
                                    left_row = check_letter(lines[i_line][begin - 1])
                                    bottom_row = check_letter(lines[i_line+1][i_intro])
                                    right_row = check_letter(lines[i_line][j_letter + 1])
                            elif len(lines) - 1 == i_line:
                                if  j_letter == 0:
                                    right_row = check_letter(lines[i_line][j_letter + 1])
                                    top_row = check_letter(lines[i_line-1][i_intro])
                                elif j_letter == len(lines[i_line]):
                                    left_row =  check_letter(lines[i_line][begin - 1])
                                    top_row = check_letter(lines[i_line-1][i_intro])
                                else:
                                    left_row =  check_letter(lines[i_line][begin - 1])
                                    top_row = check_letter(lines[i_line-1][i_intro])
                                    right_row = check_letter(lines[i_line][j_letter + 1])
                            else:
                                if  j_letter == 0:
                                    right_row = check_letter(lines[i_line][j_letter + 1])
                                    bottom_row = check_letter(lines[i_line+1][i_intro])
                                    top_row = check_letter(lines[i_line-1][i_intro])
                                elif j_letter == len(lines[i_line]):
                                    left_row = left_row =  check_letter(lines[i_line][begin - 1])
                                    bottom_row = check_letter(lines[i_line+1][i_intro])
                                    top_row = check_letter(lines[i_line-1][i_intro])
                                else:
                                    top_row = check_letter(lines[i_line-1][i_intro])
                                    left_row = left_row =  check_letter(lines[i_line][begin - 1])
                                    bottom_row = check_letter(lines[i_line+1][i_intro])
                                    right_row = check_letter(lines[i_line][j_letter + 1])
                        
                            if top_row is not None or left_row is not None or right_row is not None or bottom_row is not None:
                                condicion = True
                        
                        if condicion:
                            lst_no_valids.append(value)
                        else:
                            lst_valids.append(value)
                    j_letter += 1
                    num_temp = ""
            i_line += 1 


    print(f"NO VALIDOS: {lst_no_valids}")
    print(f"VALIDOS: {lst_valids}")



