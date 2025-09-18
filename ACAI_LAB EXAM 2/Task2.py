def average_crop_yield_per_acre(total_yield: float, acres: float) -> float:
    """
    Calculate the average crop yield per acre.

    Parameters:
        total_yield (float): The total crop yield (e.g., in kilograms or tons).
        acres (float): The number of acres over which the crop was grown.

    Returns:
        float: The average crop yield per acre.

    Example:
        >>> average_crop_yield_per_acre(500, 50)
        10.0

    Notes:
        - If 'acres' is zero, the function will raise a ZeroDivisionError.
        - Both 'total_yield' and 'acres' should be positive numbers for meaningful results.
        - Negative or non-numeric inputs may result in unexpected behavior or errors.
    """
    return total_yield / acres

def main():
    # input
    total_yield = 500
    acres = 50
    try:
        avg_yield = average_crop_yield_per_acre(total_yield, acres)
        print(f"Average crop yield per acre: {avg_yield}")
    except ZeroDivisionError:
        print("Error: Number of acres cannot be zero.")

if __name__ == "__main__":
    main()