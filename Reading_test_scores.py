# -*- coding: utf-8 -*-
# This program reads test scores from a CSV file
# and calculates each student's test average.

def main():
# Open the file.
    csv_file = open('C:\\Users\JCord\OneDrive\Desktop\StudentGradeBook.txt', 'r')

# Read the file's lines into a list.
    lines = csv_file.readlines()

# Close the file.
    csv_file.close()

# Process the lines.
    for line in lines:
# Get the test scores as tokens.
        tokens = line.split('\t')

# Calculate the total of the test scores.
    total = 0.0
    for token in tokens:
        total += float(token)

# Calculate the average of the test scores.
    average = total / len(tokens)
    print(f'Average: {average}')

# Execute the main function.
if __name__ == '__main__':
   main()