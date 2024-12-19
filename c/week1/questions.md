Q1.
Problem Statement
Write a program to implement the following based on the user’s choice.
1. Read weekday numbers (1-7) and print weekday names (Sunday, Monday, Tuesday,
Wednesday, Thursday, Friday, and Saturday) according to the given weekday number
using the switch case statement.
2. Read the month value and print the total number of days in the input month.
Input Format
The first line of input consists of the weekday number (Sunday=1, Monday=2,
Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7).
The second line of input consists of the month number.
Output Format
The first line of output prints the weekday.
The second line of output prints the number of days in the given month.
If any invalid numbers are given as input, print "Invalid Input".
Constraints
1<=weekday<=7
1<=month<=12
Sample Input Sample Output
5
8
Thursday
31 Days
Sample Input Sample Output
8
25
Invalid Input
Sample Input Sample Output
6
2
Friday
Either 28 or 29 Days in this Month

Q2.
Problem Statement
Write a C program to generate Electricity bills.
If the type of the EB connection is Domestic, calculate the amount to be paid as follows:
• first 100 units - Rs. 1 per unit
• 101-200 units - Rs. 2.50 per unit
• 201 -500 units - Rs. 4 per unit
• > 501 units - Rs. 6 per unit
If the type of the EB connection is Commercial, calculate the amount to be paid as
follows:
• first 100 units - Rs. 2 per unit
• 101-200 units - Rs. 4.50 per unit
• 201 -500 units - Rs. 6 per unit
• > 501 units - Rs. 7 per unit
Examples
Input:
D
150
Output:
Electricity Bill Amount: Rs. 225.00
Explanation:
For a domestic connection with 150 units consumed, the electricity bill amount would
be calculated as follows:
• first 100 units: Rs. 1.0 per unit = Rs. 100
• next 50 units: Rs. 2.5 per unit = Rs. 125
Total amount = Rs. 100 + Rs. 125 = Rs. 225.
Input:
C
600
Output:
Electricity Bill Amount: Rs. 3150.00
Explanation:
For a commercial connection with 600 units consumed, the electricity bill amount would
be calculated as follows:
• first 100 units: Rs. 2.0 per unit = Rs. 200
• next 100 units: Rs. 4.5 per unit = Rs. 450
• next 300 units: Rs. 6.0 per unit = Rs. 1,800
• remaining 100 units: Rs. 7.0 per unit = Rs. 700
Total amount = Rs. 200 + Rs. 450 + Rs. 1,800 + Rs. 700 = Rs. 3,150.
Input Format
The first line of input consists of the type of EB connection - D for Domestic and C for
Commercial.
The second line of input consists of the value of units consumed.
Output Format
The output prints the bill amount, rounded off to 2 decimal places.
Refer to the sample output for formatting specifications.
Sample Input Sample Output
D
150
Electricity Bill Amount: Rs. 225.00
Sample Input Sample Output
C
600
Electricity Bill Amount: Rs. 3150.00
Sample Input Sample Output
X
50
Invalid type of EB connection. Please enter either D or C.

Q3.
Problem Statement
Jennie is working in a bank, and her daily task is to guide the customers in filling out
various bank challans. A part of this is that customers need to write the numbers in
English as a representation of the digits.
Jennie decided to write a program to read the number and print the number digit by digit
in Word format. Help Jennie complete this task.
Input Format
The input consists of a long integer n.
Output Format
The output prints the given number in the English word representation of the digits.
Refer to the sample output for the formatting specifications.
Constraints
Beginning and trial zeros will be ignored while converting.
Sample Input Sample Output
659803
six five nine eight zero three
Sample Input Sample Output
100
one
Sample Input Sample Output
001
one
Time Limit: - ms Memory Limit: - kb Code Size: - kb

Q5.
Find the logic behind the given series
Series:
6 28 66 120 190 276....
The numbers in the series should be used to create a Pyramid. The base of the Pyramid
will be the widest and will start converging towards the top where there will only be one
element. Each successive layer will have one fewer number than the layer below it. The
width of the pyramid is specified by the input parameter N., In other words, there will be
N numbers on the bottom layer of the pyramid.
The Pyramid construction rules are as follows
1. The first number in the series should be at the top of the Pyramid
2. Last N number of the series should be on the bottom-most layer of the Pyramid, with
the Nth number being the right-most number of this layer.
3. Numbers less than 5-digits must be padded with zeroes to maintain the sanctity of a
pyramid when printed. Have a look at the examples below to get a pictorial
understanding of what this rule actually means.
Note : Use printf("%10.5d",variable_name);
Input Format
The first line of input will contain the number N that corresponds to the width of the
bottom-most layer of the Pyramid
Output Format
The Pyramid constructed out of numbers in the series as per stated construction rules
(Each output is separated by 5 spaces)
Constraints
0 < N <= 14
Sample Input Sample Output
3
00006
00028 00066
00120 00190 00276
Time Limit: 10 ms Memory Limit: 256 kb Code Size: 1024 kb

Q4.
Problem Statement
Super Quiz Bee is a famous quiz Competition that tests students on a wide variety of
academic subjects. This week’s participants were kids of age 12 to 15 and the quiz
questions were based on the Gregorian calendar.
In the first round of the competition, the Host of the event told the participants that it
was Monday on the date 01/01/2001. Later he questioned each one of the participants
what would be the day on the 1st of January, giving them a particular year. Write a
program to help the Host validate the answers given by the participants.
Input Format
The input consists of an integer that corresponds to the year.
Output Format
The output displays the day on the 1st of January of that given year.
Refer to the sample output for the formatting specifications.
Constraints
1700 ≤ Year ≤ 2100
Sample Input Sample Output
1994
Saturday
Sample Input Sample Output
2014
Wednesday
Time Limit: - ms Memory Limit: - kb Code Size: - kb