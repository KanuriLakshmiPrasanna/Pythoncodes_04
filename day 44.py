'''Complementary Strand in a DNA
You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the character A,T,C, and G only.

Chef knows that:
A is complementary to T.
T is complementary to A.
C is complementary to G.
G is complementary to C.
Using the string S, determine the sequence of the complementary strand of the DNA.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
First line of each test case contains an integer N - denoting the length of string S.
Second line contains N characters denoting the string S.

Output Format
For each test case, output the string containing N characters - sequence of nucleotides of the complementary strand.

Constraints
1≤T≤100
1≤N≤100
S contains A, T, C, and G only

Sample 1:
Input
Output
4
4
ATCG
4
GTCC
5
AAAAA
3
TAC
TAGC
CAGG
TTTTT
ATG

Explanation:
Test case 1: Based on the rules, the complements of A, T, C, and G are T, A, G, and C respectively. Thus, the complementary string of the given string ATCG is TAGC.

Test case 2: Based on the rules, the complements of G, T, and C are C, A, and G respectively. Thus, the complementary string of the given string GTCC is CAGG.

Test case 3: Based on the rules, the complement of A is T. Thus, the complementary string of the given string AAAAA is TTTTT.

Test case 4: Based on the rules, the complements of T, A, and C are A, T, and G respectively. Thus, the complementary string of the given string TAC is ATG.'''

for _ in range(int(input())):
    N=int(input())
    S=input()
    complement=""
    for i in S:
        if i=='A':
            complement+='T'
        elif i=='T':
            complement+='A'
        elif i=='C':
            complement+='G'
        elif i=='G':
            complement+='C'
        
    print(complement)