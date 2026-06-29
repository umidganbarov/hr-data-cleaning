# Data Cleaning Toolkit

Cleaning messy real-world data with Python, Pandas, and regex.

## What's in here
- `dirty_hr.py` — full messy data
- `clean_hr.py` — full cleaning script for messy HR dataset

## Dataset
Messy HR data: 1000 rows, 10 columns with mixed types, 
word-format numbers, accounting negatives, inconsistent dates.

## What was cleaned
- Age: string/word formats → int, nulls → median
- Salary: "SIXTY THOUSAND", " NAN ", $format → int
- Phone: inconsistent formats → 10-digit string
- Dates: mixed formats → split Year/Month/Day columns
- Performance Score: letter grades → readable labels

## Stack
Python · Pandas · NumPy · Regex · word2number
