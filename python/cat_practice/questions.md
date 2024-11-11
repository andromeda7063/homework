1. Matrix - Inside Numbers Sum
A set of numbers forming a matrix N*N is passed as input. The program has to print the sum
of numbers which are not along the edges.
Input Format:
The first line will contain the value of N.
The next N lines will contain N numbers each separated by one or more spaces.
Boundary Conditions:
3 <= N <= 10
Value of a given number in the matrix is from 0 to 99999999.
Output Format:
The sum of the numbers which are not along the edges.
Example Input/Output 1:
Input:
3
5 6 7
8 9 1
2 3 4
Output:
9
Explanation:
All numbers except 9 are along the edges. Hence the sum is 9 which is printed as output.
Example Input/Output 2:
Input:
4
2 3 4 5
1 5 3 2
3 3 9 8
9 7 6 5
Output:
20
Explanation:
The numbers which are not along the edges are 5,3,3,9 and their sum = 20

2. Left Number Twice Right
A set of N numbers (separated by one or more spaces) is passed as input to the program. The
program must identify the count of numbers where the number on the left is twice the number
on the right.
Input Format:
The first line will contain the N numbers separated by one or more spaces.
Boundary Conditions:
3 <= N <= 50
The value of the numbers can be from -99999999 to 99999999
Output Format:
The count of numbers where the sum of the numbers on the LHS is twice that of the sum of
numbers on the RHS.
Example Input/Output 1:
Input:
10 20 5 40 15 -2 -30 -1 60
Output:
2
Explanation:
The numbers meeting the criteria are 20, -30
Example Input/Output 2:
Input:
5 90 10 2 5 -4 10 6 5 3
Output:
3
Explanation:
The numbers meeting the criteria are 2, 6, 5

3. ANAGARAMS
two strings S1, S2 are passed as input to the program. The program must print the count of
anagrams present in both the strings. Out of each pair of words in the anagram the first word
in the pair must be in S1 and the second word in the pair must be in S2.
If two words have the same characters and the occurrence number of each character is also
identical respectively, they are anagrams.
Example: silent & listen
Input Format:
The first line will contain the value of S1.
The first line will contain the value of S2.
Boundary Conditions:
Length of S1 and S2 is from 5 to 200.
Output Format:
The count of pair of anagrams in S1 and S2 based on the conditions mentioned.
Example Input/Output 1:
Input:
but i will not listen to him
water dropped into the silent tub
Output:
2
Explanation:
The anagram pairs are
but tub
listen silent
Example Input/Output 2:
Input:
please dear agree to take kids outside
if you are eager read and skid
Output:
3
Explanation:
The anagram pairs are
dear read
agree eager
kids skid
Example Input/Output 3:
Input:
heavy weight dice iced
cast medicine iron
Output:
0
Explanation:
There are no anagram pairs (as dice and iced are in same string)

4. PICK CHARACTERS TO FORM THE LONGEST POSSIBLE PALINDROME
A certain number of string values will be passed as input. The program has to form the first
longest possible palindrome with the characters present in the string values in ascending order
(from a-z , 0-9).
Input Format:
The first line will contain the N = number of string values which will be passed as input.
The next N lines will contain the N string values.
The string value can contain both alphabets and numbers.
Boundary Conditions:
The number of string values N will be from 2 to 10.
The length of a string value will be from 1 to 100.
Output Format:
The first longest possible palindrome with the characters present in the string values in
ascending order (from a-z, 0-9). The output format must be in lower case. Numbers will take
precedence over alphabets in the output.
Example Input/Output 1:
Input:
2
kickmeout
boxingchamp
Output:
cikmoaomkic
Note that several longest palindromes of length 11 are possible like cikmoaomkic,
cikmobomkic, cikmoeomkic etc.
As cikmoaomkic is first in ascending order, it is the required output.
Example Input/Output 2:
Input:
3
apple5
man5go
orange
Output:
5aegnopapongea5

5. SNAKE SEQUENCE
A set of numbers separated by space is passed as input. The program must print the largest
snake sequence present in the numbers. A snake sequence is made up of adjacent numbers
such that for each number, the number on the right or left is +1 or -1 of it's value. If multiple
snake sequences of maximum length is possible print the snake sequence appearing in the
natural input order.
Input Format:
The first line will contain the set of numbers separated by one or more spaces.
Boundary Conditions:
The length of the number string is <= 200
Output Format:
The longest snake sequence that can be formed using the given numbers.
Example Input/Output 1:
Input:
9 8 7 5 3 0 1 -2 -3 1 2
Output:
3 2 1 0 1
Example Input/Output 2:
Input:
-5 -4 -3 -1 0 1 4 6 5 4 3 4 3 2 1 0 2 -3 9
Output:
6 5 4 3 4 3 2 1 0 -1 0 1 2
Example Input/Output 3:
Input:
5 6 7 9 8 8
Output:
5 6 7 8 9 8
Explanation:
Here two snake sequences are possible - 5 6 7 8 9 8 and 8 9 8 7 6 5.
But as 5 6 7 8 9 8 occurs in the natural order (same as the input sequence) it is printed as the
output.