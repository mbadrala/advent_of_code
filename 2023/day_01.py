# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to
# take a look. The Elves have even given you a map; on it, they've used stars
# to mark the top fifty locations that are likely to be having problems.
# 
# You've been doing this long enough to know that to restore snow operations,
# you need to check all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each
# day in the Advent calendar; the second puzzle is unlocked when you complete
# the first. Each puzzle grants one star. Good luck!
# 
# You try to ask why they can't just use a weather machine ("not powerful
# enough") and where they're even sending you ("the sky") and why your map looks
# mostly blank ("you sure ask a lot of questions") and hang on did you just say
# the sky ("of course, where do you think snow comes from") when you realize
# that the Elves are already loading you into a trebuchet ("please hold still,
# we need to strap you in").
# 
# As they're making the final adjustments, they discover that their calibration
# document (your puzzle input) has been amended by a very young Elf who was
# apparently just excited to show off her art skills. Consequently, the Elves
# are having trouble reading the values on the document.
# 
# The newly-improved calibration document consists of lines of text; each line
# originally contained a specific calibration value that the Elves now need to
# recover. On each line, the calibration value can be found by combining the
# first digit and the last digit (in that order) to form a single two-digit
# number.
# 
# For example:
# 
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
#
# In this example, the calibration values of these four lines are 12, 38, 15,
# and 77. Adding these together produces 142.
# 
# Consider your entire calibration document. What is the sum of all of the
# calibration values?o

# sum = 0

inputFile = open('day_01_input.txt', 'r')
lines = inputFile.readlines()

# for line in lines:
#     local_number = ''
#     res = [x for x in line if x.isdigit() == True]
#     if len(res) > 1:
#         local_number += res[0] + res[-1]
#     else:
#         if len(res) > 0:
#             local_number = res[0] + res[0]
#     if len(local_number) > 0:
#         sum += int(local_number)

# print('sum:', sum)

# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven,
# eight, and nine also count as valid "digits".
# 
# Equipped with this new information, you now need to find the real first and
# last digit on each line. For example:
# 
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
# Adding these together produces 281.
# 
# What is the sum of all of the calibration values?
# 

number_dict = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9",
}

sum = 0
import re

def add_found(result, spelled):
    num_found = {}

    for num, desc in number_dict.items():
        exp = '(?='+ num +')'
        found = [m.start() for m in re.finditer(exp, spelled)]
        if len(found) > 0:
            for f_index in found:
                num_found[f_index] = desc

    num_found = dict(sorted(num_found.items()))
    for key, num in num_found.items():
        result.append(num)
    return result

for line in lines:
    local_number = ''
    res = []
    spelled = ''
    
    for index, char in enumerate(line):
        if char.isdigit():
            if len(spelled) > 0:
                res = add_found(res, spelled)
                spelled  = ''
            res.append(char)
        else:
            spelled += char
            if index + 1 == len(line):
                res = add_found(res, spelled)
                spelled  = ''

    res_length = len(res)
    if res_length > 1:
        local_number += str(res[0]) + str(res[-1])
    else:
        if len(res) > 0:
            local_number = str(res[0]) + str(res[0])
    if len(local_number) > 0:
        sum += int(local_number)

    print(line.rstrip(), '->', local_number)
print('sum:', sum)
