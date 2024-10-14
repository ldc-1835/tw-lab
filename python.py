def get_vector_input(prompt):
    while True:
        try:
            vector = list(map(float, input(prompt).split()))
            return vector
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

def dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def main():
    print("Enter the elements of the first Vector:")
    vector1 = get_vector_input("Vector 1: ")

    print("Enter the elements of the second Vector:")
    vector2 = get_vector_input("Vector 2: ")

    if len(vector1) != len(vector2):
        print("Error: Vectors must be of the same length.")
        return

    result = dot_product(vector1, vector2)
    print(f"The dot product of the vectors is: {result}")

if __name__ == "__main__":
    main()

