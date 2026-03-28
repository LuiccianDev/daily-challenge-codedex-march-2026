[Day 27 challenge](https://www.codedex.io/daily-challenge/2026-03-28)

28 Days Later is a British series about a post-apocalyptic world overrun by a fast-spreading virus. This includes 28 Days Later (2002), 28 Weeks Later (2007), and 28 Years Later (2025).

28 Years Later

A dangerous virus is spreading across a city. So it goes... 🦠

Each day, infected people pass the virus to nearby healthy people. Your goal is to determine how many days it takes to infect everyone... or if it’s impossible.

Given a grid representing a city:

' ' = empty space
'👤' = healthy person
'🧟' = infected person
Each day, any infected person '🧟' infects adjacent healthy folks '👤' (up, down, left, right).

Complete the function and return:

The minimum number of days needed to infect all people.
OR -1 if some people can never be infected.
Examples

Example 1

Input:
[
  ['👤', ' ', '🧟'],
  ['🧟', '👤', ' '],
  [' ', '👤', '👤']
]
Output: 3
In three days, everyone is infected. We're cooked! 🧟 🧟‍♀️ 🧟‍♂️

Example 2

Input:
[
  ['👤', ' ', ' ', '🧟'],
  [' ', '👤', '👤', ' '],
  [' ', '👤', ' ', '👤'],
  ['👤', '👤', '👤', ' ']
]
Output: -1
The one in the top right doesn't infect anyone. We can contain this thing! 💉