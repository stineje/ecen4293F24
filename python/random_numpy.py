import numpy as np


def example_1():
    """Generate random floats between 0 and 1"""
    print("Example 1: Random floats between 0 and 1")
    random_floats = np.random.random(5)
    print(random_floats, "\n")


def example_2():
    """Generate random integers between a specified range"""
    print("Example 2: Random integers between 10 and 50")
    random_integers = np.random.randint(10, 50, size=5)
    print(random_integers, "\n")


def example_3():
    """Generate random numbers from a normal distribution"""
    print("Example 3: Random numbers from a normal distribution")
    normal_distribution = np.random.normal(0, 1, size=5)
    print(normal_distribution, "\n")


def example_4():
    """Generate random numbers from a uniform distribution"""
    print("Example 4: Random numbers from a uniform distribution")
    uniform_distribution = np.random.uniform(-5, 5, size=5)
    print(uniform_distribution, "\n")


def example_5():
    """Shuffle an array randomly"""
    print("Example 5: Shuffle an array randomly")
    array = np.arange(10)
    print("Original array:", array)
    np.random.shuffle(array)
    print("Shuffled array:", array, "\n")


def example_6():
    """Randomly select elements from an array"""
    print("Example 6: Randomly select elements from an array")
    array = np.array([1, 2, 3, 4, 5])
    random_selection = np.random.choice(array, size=3, replace=False)
    print("Random selection:", random_selection, "\n")


def example_7():
    """Generate random samples from a binomial distribution"""
    print("Example 7: Random samples from a binomial distribution")
    binomial_distribution = np.random.binomial(n=10, p=0.5, size=5)
    print(binomial_distribution, "\n")


def example_8():
    """Generate random samples from an exponential distribution"""
    print("Example 8: Random samples from an exponential distribution")
    exponential_distribution = np.random.exponential(scale=1.0, size=5)
    print(exponential_distribution, "\n")


def example_9():
    """Set a random seed for reproducibility"""
    print("Example 9: Set a random seed for reproducibility")
    np.random.seed(42)
    reproducible_random = np.random.random(5)
    print(reproducible_random, "\n")


def example_10():
    """Generate random numbers from a Poisson distribution"""
    print("Example 10: Random numbers from a Poisson distribution")
    poisson_distribution = np.random.poisson(lam=3.0, size=5)
    print(poisson_distribution, "\n")


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()
    example_8()
    example_9()
    example_10()
