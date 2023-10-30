import csv

# Define the Find-S algorithm
def find_s_algorithm(training_data):
    # Initialize the hypothesis to the first training example
    hypothesis = training_data[0][:-1]  # Remove the last element (class label)
    
    # Iterate through the training examples to find the most specific hypothesis
    for example in training_data:
        if example[-1] == 'Yes':  # Check if the example is a positive example
            for i in range(len(hypothesis)):
                if example[i] != hypothesis[i]:
                    hypothesis[i] = '?'  # Replace non-matching attributes with a wildcard
        
    return hypothesis

# Read data from CSV file
def read_data_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

# Example usage of the Find-S algorithm with CSV data
if __name__ == "__main__":
    # Example CSV file path
    csv_file_path = 'G:salgorithm.csv'  # Replace 'your_data.csv' with the actual file path
    
    # Read data from CSV file
    training_data = read_data_from_csv(csv_file_path)

      # Print the contents of the CSV file
    print("CSV File Contents:")
    for row in training_data:
        print(row)
    
    
    # Find the hypothesis using the Find-S algorithm
    hypothesis = find_s_algorithm(training_data)
    
    # Print the hypothesis
    print("Hypothesis:", hypothesis)


