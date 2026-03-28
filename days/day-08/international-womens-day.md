[Day 7 challenge](https://www.codedex.io/daily-challenge/2026-03-08)

Happy International Women's Day! ( ๑ ˃̵ ֊ ˂̵)ᕤ

Today marks International Women’s Day – celebrating the achievements of women worldwide and reflecting on progress toward gender equity, especially in the workplace and in tech.

women in tech

Tech companies track and publish the percentage of women in their workforce each year. Your mission: Analyze these trends and quantify each company's progress in “closing the gap.”

Given annual percentages from official diversity reports published by some companies, complete the function that returns three metrics:

Net Change Per Year: Average yearly increase or decrease (round to four decimals).
Net Change Per Year
=
Last Year
−
First Year
Years
−
1
Net Change Per Year= 
Years−1
Last Year−First Year
​
 
Trend: Compares the last 3-year average to the first 3-year average:
"improving": last 3-year average higher
"stagnating": averages equal
"declining": last 3-year average lower
Dips: Number of years where the percentage decreased compared to the previous year.
Python: Return three values. JavaScript: Return an array with three values.

Examples

Each test case is a FAANG company: Facebook (Meta), Amazon, Apple, Netflix, and Google.

Meta 🌀 (2014-2022)

- Input: [31.0, 31.0, 33.0, 35.0, 36.0, 36.0, 36.2, 36.7, 37.1]
- Output:
0.7625
"improving"
0
Net Change Per Year = (37.1 − 31.0) / 8 = 0.7625

Amazon 📦 (2014-2024)

- Input: [42.0, 43.0, 42.0, 43.0, 44.0, 44.0, 44.6, 44.8, 44.7, 45.0, 45.8]
- Output:
0.38
"improving"
2
Apple 🍎 (2014–2024)

- Input: [30.0, 31.0, 32.0, 32.0, 33.0, 34.0, 34.0, 34.8, 35.0, 35.0, 35.3]
- Output:
0.53
"improving"
0
Every data point comes directly from their published annual reports. No estimates.

Note: Meta and Google stopped reporting diversity data in early 2025 amid DEI rollbacks. Amazon, Apple, and Netflix still report these figures as of 2026.