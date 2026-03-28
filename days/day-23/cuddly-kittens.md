[Day 22 challenge](https://www.codedex.io/daily-challenge/2026-03-23)

Happy Monday! It’s National Cuddly Kitten Day! 😻

We are back with a Daily Challenge and... a Bonus Task! Let's gooo.

kitties!

You're helping kittens line up in a cozy play area. They only stay calm if their energy levels are similar. Otherwise, the purring stops, and chaos ensues.

You're given:

A list/array kittens, where kittens[i] represents the energy level of the 
i
i-th kitten
A number limit, the biggest difference between any two kittens in a calm group
A group of kittens is calm and can purr together if:

max energy
−
min energy
≤
limit
max energy−min energy≤limit
Return the length of the longest group of consecutive kittens that can stay calm. 🐾🐾🐾

Bonus Task: Snap a pic of your cat with Codédex for a chance to win a Codédex Crewneck! 📸

Examples

Example 1

Input:
kittens = [1, 3, 6, 7, 9]
limit = 3
Output: 3
The longest valid group is [6, 7, 9] because 
m
a
x
max - 
m
i
n
min = 9 - 6 = 3.

Example 2

Input:
kittens = [2, 3, 4, 5]
limit = 10
Output: 4
All kittens can stay together since 
m
a
x
max - 
m
i
n
min = 5 - 2 = 3 ≤ 10.