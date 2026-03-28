[Day 23 challenge](https://www.codedex.io/daily-challenge/2026-03-24)

Every day, instruments called seismographs measure and record earthquake data around the world. They capture hundreds of tremors, most too small to feel.

But occasionally, a reading spikes far beyond the norm. 💥

seismologist

That spike could mean the difference between a harmless rumble… and a major event like the 2023 Turkey-Syria earthquakes (magnitude 7.8) that devastated cities.

Magnitude is a way to measure how strong an earthquake is (how much energy it releases).

In this Daily Challenge, let's detect the tremor magnitude anomalies! 🔎

Seismologists flag a reading as suspicious if it is more than 1.5x the median of all recorded readings. They use the median rather than the mean because earthquake data is heavily skewed. A single massive quake can drag the mean up and mask smaller anomalies.

The median is the middle value when all readings are sorted. If there's an even number of readings, it's the average of the two middle values.

Given a list of magnitude readings, return a list of indices of all the suspicious ones.

If there are no suspicious readings, return an empty list.

Examples

Example 1

Input: [2.1, 1.8, 2.0, 1.9, 6.5, 2.2]
Output: [4]
The median is 2.05. 1.5x that is 3.075. Only the 6.5 at index 4 exceeds it. 🚨

Example 2

Input: [1.0, 1.2, 1.1, 1.3, 1.0, 1.2, 1.1]
Output: []
All readings are tightly clustered... nothing sus here. Quiet day on the fault line.

Example 3

Input: [3.0, 7.5, 2.8, 8.1, 3.2, 2.9]
Output: [1, 3]
The median is 3.1, so the threshold is 4.65. Both 7.5 and 8.1 blow past it. Two anomalies! 🌋