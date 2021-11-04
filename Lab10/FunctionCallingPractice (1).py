# @author Dabin Chae
from random import randint
from typing import get_args

def main():
    # 1. Write a correct call to add with data of your choice
    #    See the definition of add to help you. 
    add(-10, 25)

    # 2. Write a correct call to concat with data of your choice
    #    See the definition of concat to help you. 
    concat("JCCC", "Cavaliers")

    # 3. Write a correct call to double with data of your choice
    #    See the definition of double to help you.
    double(8)

    # 4. Write a correct call to showCollegeInfo with data of your choice
    #    See the definition of showCollegeInfo to help you. 
    showCollegeInfo("U of Kansas", 25000, 1500)

    # 5. Inside the print statement, insert a correct call to getRandomNumber 
    #    with data of your choice. See the definition of getRandomNumber to 
    #    help you. 
    print(f"The random number is {getRandomNumber(1, 100):d}")

# add displays the sum of two numbers.
# @param addend1 The first number to add
# @param addend2 The second number to add
def add(addend1, addend2) :
    print(f"Sum: {addend1 + addend2}")

# concat displays the concatenation of two values with a space in between.
# @param word1 The first word in the concatenation
# @param word2 The second word that is appended to the first
def concat(word1, word2) :
    print(f"Concatenation: {word1 + ' ' + word2}")

# double displays the result of doubling an integer.
# @param numToDouble An integer to be doubled
def double(numToDouble) :
    print(f"{numToDouble} * 2 = {numToDouble * 2}")

# showCollegeInfo displays the college's name followed by the
# total enrollment of the two campuses
# @param collegeName Name of the college
# @param campus1Enrollment Enrollment on one campus
# @param campus2Enrollment Enrollment on the second campus
def showCollegeInfo(collegeName, campus1Enrollment, campus2Enrollment) :
    print(f"{collegeName}'s total enrollment: " +
          f"{campus1Enrollment + campus2Enrollment}")


# getRandomNumber generates a random number in a given inclusive range
# @param lowLimit Integer representing the low value of the inclusive range
# @param highLimit Integer representing the high value of the inclusive range
# @return an integer in the range [lowLimit, highLimit]
def getRandomNumber(lowLimit, highLimit) :
    return ( randint(lowLimit, highLimit) )

main()