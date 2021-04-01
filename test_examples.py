#1
def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    assert factorial(1) == 1
    assert factorial(5) == 120

# 2
def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def test_count_word_occurrence_in_string():
    text_test='Things are going well'
    word_test_1='well'
    word_test_2='twice'
    assert count_word_occurrence_in_string(text_test,word_test_1) == 1
    assert count_word_occurrence_in_string(text_test,word_test_2) == 0
    

# 3
def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

def test_count_word_occurrence_in_file():
    assert count_word_occurrence_in_file('check.txt','well') == 1
    assert count_word_occurrence_in_file('check.txt','twice') == 0

# 4
def check_reactor_temperature(temperature_celsius):
    """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    from reactor import max_temperature
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status

def test_check_reactor_temperature():
    assert check_reactor_temperature(100) == 0
    assert check_reactor_temperature(300) == 1


# 5
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1

def test_go_for_a_walk():
    pet_test = Pet('anna')
    pet_test.go_for_a_walk()
    assert pet_test.hunger == 0
    assert pet_test.hunger == 1

        

