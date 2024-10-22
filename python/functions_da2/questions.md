## Functions

Q1.Problem Statement
Implement a function that counts the number of vowels in a given input string. The
vowels, which include both lowercase and uppercase vowels (a, e, i, o, u, A, E, I, O, U),
are stored in a global variable called VOWELS.
The function should use local variables for counting the vowels and return the count
as the output.
Function Signature: count_vowels(input_string)

Input Format
The input consists of a single line containing a string.

Output Format
The output consists of a single line containing an integer representing the number of
vowels (both lowercase and uppercase) found in the input string in the format:
"Number of vowels in the string: [number of vowels]"
Refer to the sample output for the formatting specifications.

Constraints
The input string consists of printable ASCII characters.
The input string may contain both uppercase and lowercase characters.
Length of string ≤ 100

Sample Input
Hello, World!

Sample Output Number of vowels in the string: 3


Q2.Problem Statement
Arjun is working as a mathematics teacher at a school. He is teaching students
about the types of triangles, and he wants to find out whether the given triangle is a
right triangle or not using the Pythagorean theorem. Help him write a program to find
out if a triangle is a right triangle using the Pythagorean theorem.
Function prototype: def is_right_triangle(a, b, c)
Explanation
The Pythagorean theorem states that in a right triangle, the square of the length of
the hypotenuse (the side opposite the right angle) is equal to the sum of the squares
of the lengths of the other two sides.
Mathematically, the Pythagorean theorem can be expressed as c2 = a2 + b2
where "c" represents the length of the hypotenuse, and "a" and "b" represent the
lengths of the other two sides of the right triangle.

Input Format
The first line of input consists of a floating-point number representing side a.
The second line of input consists of a floating-point number representing side b.
The third line of input consists of a floating-point number side c.

Output Format
The output displays whether the given triangle is a right-angled triangle or not.
Refer to the sample output for the formatting specifications.

Constraints
0.1 <= side a, side b, and side c <= 1000.0

Sample Input
3.0
4.0
5.0
Sample Output
The triangle is a right triangle.
Sample Input
5.5
5.1
6.9
Sample Output
The triangle is not a right triangle.


Q3.Problem Statement
Alice works at a digital marketing company, where she analyzes large datasets. One
day, she's tasked with processing customer ID numbers, which are long numeric
sequences.
To simplify this, Alice needs to calculate the digital root of each ID. The digital root is
the single digit obtained by repeatedly summing the digits of a number until a single
digit remains.
Help Alice write a program that reads a customer ID number, calculates its digital
root, and prints the result.
For example, the sum of the digits of 98675 is 9 + 8 + 6 + 7 + 5 = 35, then 3 + 5 = 8,
which is the digital root.
Function prototype:
1. def digital_root(num) - to find the digital root of the integer num
2. def sum_of_digits(num) - to find the sum of the digits of the integer num

Input Format
The input consists of an integer num.


Output Format
The output prints an integer representing the sum of digits for a given number until a
single digit is obtained.
Refer to the sample output for the formatting specifications.

Constraints
1 ≤ num ≤ 109

Sample Input 
451110
Sample Output
3


Q4.Problem Statement
Implement a program to convert time input provided in hours, minutes, and seconds
into a decimal representation.
The program should allow the user to enter a time in the format HH:MM:SS, where
HH represents hours, MM represents minutes, and SS represents seconds. The
program should then convert this input into a decimal representation.
Function Signature: convert_time()

Input Format
The input consists of a string in the format "HH:MM:SS", where HH, MM, and SS are
integers representing hours, minutes, and seconds.

Output Format
The output prints a decimal representation of the input time, breaking down into
hours as integers, minutes with two decimal places, and seconds as floating-point
number.
The format of the output should be: "X hours, Y.YY minutes, and Z.ZZ seconds in
decimal representation."
Refer to the sample input and output for the formatting specifications.

Constraints
The input time format is HH:MM: SS (e.g., 05:30:45).
Hours (HH) can range from 0 to 23.
Minutes (MM) can range from 0 to 59.
Seconds (SS) can range from 0 to 59.

Sample Input 
05:00:30
Sample Output
5 hours, 0.5 minutes, and 30.0 seconds in decimal representation.

Sample Input 
10:15:25
Sample Output
10 hours, 15.42 minutes, and 25.0 seconds in decimal representation.


Q5.Problem Statement
You are tasked with developing a program that includes a binary-to-decimal
converter for a data processing application. The application deals with binary data
and necessitates an accurate conversion mechanism to interact with decimal
representations.
Your objective is to implement a function to perform this conversion.
Function Signature: binary_to_decimal(binary_string)

Input Format
The input consists of a binary string (only containing '0' and '1') to be converted into
a decimal number.

Output Format
If the input binary string is valid, print "The decimal equivalent of [binary_input] is
[decimal_result]."
If the input binary string is invalid, print "Invalid binary input. Please enter a valid
binary number".
Refer to the sample output for the formatting specifications.

Constraints
The input binary string must consist of only '0's and '1's.

Sample I/O
1101
The decimal equivalent of 1101 is 13

Sample I/O
1022
Invalid binary input. Please enter a valid binary number


Q6.Problem Statement
You are tasked with designing a shipping cost calculator program that calculates the
shipping cost for packages based on their weight and destination. The program
utilizes different shipping rates for domestic, international, and remote destinations.
The rates for each destination type are provided as global constants.
Global Variables:
DOMESTIC_RATE = 5.0
INTERNATIONAL_RATE = 10.0
REMOTE_RATE = 15.0
Function Signature: calculate_shipping(weight, destination)
Formula: shipping cost = weight * destination rate

Input Format
The first line of the input consists of a float representing the weight of the package.
The second line consists of a string representing the destinations(Domestic or
International or Remote).

Output Format
The program outputs any one of the following:
If the input is valid and the destination is recognized, the output should consist of a
single line stating the calculated shipping cost for the given weight and destination
in the format: "Shipping cost to [destination] for a [weight] kg package: $[calculated
cost]" with two decimal places.
If the input weight is not a positive float, print "Invalid weight. Weight must be greater
than 0."
If the input destination is not one of the valid options, print "Invalid destination."
Refer to the sample output for the formatting specifications.

Constraints
1.0≤weight≤1000.0.
1≤len(destination)≤15.
destination is case sensitive.

Sample I/O
5.5
Domestic
Shipping cost to Domestic for a 5.5 kg package: $27.50

Sample I/O
2.0
International
Shipping cost to International for a 2.0 kg package: $20.00

Sample I/O
-2.0
Domestic
Invalid weight. Weight must be greater than 0.


Q7.Problem Statement
You are required to implement a function, loan_payment, which calculates the monthly
installment amount for a loan based on the principal amount, an annual interest rate,
and the loan tenure. The function should utilize a global constant for the annual
interest rate and return the monthly installment.
Global Constants:
ANNUAL_INTEREST_RATE: A global constant representing the annual interest rate.
(e.g., ANNUAL_INTEREST_RATE = 0.06 corresponds to an annual interest rate of 6%).
Function Signature: loan_payment(principal, loan_tenure)

Input Format
The first line of input consists of a floating-point number principal, representing the
initial loan amount.
The second line of input consists of an integer loan_tenure, representing the number
of years over which the loan is to be repaid.

Output Format
The output consists of a single line that states the calculated monthly installment
amount for the loan, rounded to two decimal places, in the following format:
"Monthly installment: ${calculated amount}".
Refer to the sample output for the formatting specifications.

Constraints
In this scenario, the given test cases will fall under the following constraints:
5000≤principal≤00000.0
1≤loan_tenure≤20

Sample I/O
10000.00
5
Monthly installment: $193.33

Sample I/O
5000.00
3
Monthly installment: $152.11


Q8.Problem Statement
Develop a program that evaluates the strength of a given password and categorizes
it as "Weak," "Moderate," or "Strong" based on specific criteria.
• "Strong: Password is strong.": If the password meets all the character type
requirements (uppercase, lowercase, digit, and special character) and is at
least 8 characters long.
• "Moderate: Password is moderately strong.": If the password meets at least
one of the character type requirements (either uppercase, lowercase, digit, or
special character) but does not meet all of them or is at least 8 characters
long.
• "Weak: Password is too short.": If the password is shorter than 8 characters in
length.
Function Signature: password_strength(password)
Use global variables:
has_uppercase = False
has_lowercase = False
has_digit = False
has_special_char = False

Input Format
The input consists of a string representing the password to be evaluated. The
password can contain letters (uppercase and lowercase), numbers, and special
characters.

Output Format
The output displays any of the following:
"Strong: Password is strong." if the password contains at least one uppercase letter,
one lowercase letter, one digit, and one special character.
"Moderate: Password is moderately strong." if the password meets some, but not all,
of the strong password criteria.
"Weak: Password is too short." if the password is less than 8 characters long.
Refer to the sample output for the formatting specifications.

Constraints
In this scenario, the given test cases will fall under the following constraints:
1 ≤ Length of password ≤ 15

Sample I/O
password123
Moderate: Password is moderately strong.

Sample I/O
AbC123$
Weak: Password is too short.

Sample I/O
My$uperP@ssw0rd!
Strong: Password is strong.