def get_number():
    n = int(input("Enter a count of numbers: "))
    numms = []
    for i in range(n):
        num = int(input("Enter number : "))
        numms.append(num)
    return numms
def sum_of_numbers(numms):
    return sum(numms)

def average_of_numbers(numms):
    return sum(numms) / len(numms)

def maximum_number(numms):
    return max(numms)

def minimum_number(numms):
    return min(numms)

def positive_count(numms):
    return len([num for num in numms if num > 0])

def negative_count(numms):
    return len([num for num in numms if num < 0])

def zero_count(numms):
    return len([num for num in numms if num == 0])

def main():
    numms = get_number()
    print(f"Sum: {sum_of_numbers(numms)}")
    print(f"Average: {average_of_numbers(numms)}")
    print(f"Maximum: {maximum_number(numms)}")
    print(f"Minimum: {minimum_number(numms)}")
    print(f"Positive Count: {positive_count(numms)}")
    print(f"Negative Count: {negative_count(numms)}")
    print(f"Zero Count: {zero_count(numms)}")
    
main()