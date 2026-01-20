# TOPSIS Assignment – Multi Criteria Decision Making

## Submitted By
Name: Parth Garg

Roll Number: 102303045

## Course
UCS654 - Predictive Analytics Using Statistics

Thapar University, Patiala

## What is TOPSIS?
TOPSIS is a multi-criteria decision analysis method that helps in selecting the best alternative from a set of alternatives based on multiple criteria. It works by finding the alternative that is closest to the ideal solution and farthest from the negative-ideal solution.

## Problem Statement
Implement the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)
method as a command-line Python program.

## How to Run

Ensure Python 3 is installed.

Run the program from the command line as follows:

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example

```bash
python topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv

```

### Parameters

- **InputDataFile**: Path to the CSV file containing the decision matrix
  - First column: Names of alternatives
  - Remaining columns: Criteria values (must be numeric)
  
- **Weights**: Comma-separated weights for each criterion
  - Example: "1,1,1,2"
  
- **Impacts**: Comma-separated impacts for each criterion
  - Use '+' for benefit criteria (higher is better)
  - Use '-' for cost criteria (lower is better)
  - Example: "+,+,-,+"
  
- **OutputResultFileName**: Path where the result file will be saved

### Input File Format

The input CSV file should have the following structure:

| Fund Name | P1   | P2   | P3  | P4   | P5    |
|-----------|------|------|-----|------|-------|
| M1        | 0.67 | 0.45 | 6.5 | 42.6 | 12.56 |
| M2        | 0.6  | 0.36 | 3.6 | 53.3 | 14.47 |
| M3        | 0.79 | 0.61 | 6.4 | 63.1 | 17.84 |

### Output File Format

The output file will contain all input columns plus two additional columns:

- **Topsis Score**: The calculated TOPSIS score for each alternative
- **Rank**: The rank of each alternative (1 = best)

## Validation

The package performs the following validations:

- Correct number of parameters
- File existence check
- Minimum 3 columns in input file
- Numeric values in all columns except the first
- Matching number of weights, impacts, and criteria columns
- Valid impact values ('+' or '-')

## Error Handling

The package provides clear error messages for:
- Missing or incorrect parameters
- File not found
- Non-numeric values in criteria columns
- Mismatch in number of weights/impacts/columns
- Invalid impact values

## Algorithm

The TOPSIS algorithm follows these steps:

1. **Normalization**: Vector normalization of the decision matrix
2. **Weighted Normalization**: Multiply normalized values by weights
3. **Ideal Solutions**: Determine ideal best and ideal worst solutions
4. **Distance Calculation**: Calculate Euclidean distances from ideal solutions
5. **TOPSIS Score**: Calculate relative closeness to ideal solution
6. **Ranking**: Rank alternatives based on TOPSIS scores


## Acknowledgement
This project was developed as part of an academic assignment.
The TOPSIS methodology was studied from standard reference material and
open-source implementations available online.
The final implementation has been written and structured independently
to meet the assignment requirements.
