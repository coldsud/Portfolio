def read_numbers(filename="numbers.txt"):
  """Reads numbers from a file and returns them as a list of floats."""
  with open(filename, "r") as f:
    numbers = []
    for line in f:
      numbers.extend([float(num) for num in line.strip().split()])  # Split line into numbers
    return numbers

def print_average(numbers, func):
  """Calculates and prints the average using a given function."""
  try:
    average = func(numbers) / len(numbers)
    print("The average is:", average)
  except ZeroDivisionError:
    print("Error: Cannot calculate the average of an empty list.")

def main():
  """Calculates and prints the average of numbers in a file."""
  numbers = read_numbers()
  print_average(numbers, sum)  # sum is a higher-order function

if __name__ == "__main__":
  main()