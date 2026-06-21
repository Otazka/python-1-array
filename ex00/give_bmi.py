import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float])-> list[int | float]:
    """Calculate BMI based on height and weight"""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be list")
    if len(height) != len(weight):
        raise ValueError("height and weight lists must be same length")
    if not all(isinstance(x, (int, float)) for x in height) or not all(isinstance(x, (int, float)) for x in weight):
        raise TypeError("All elements in height and weight lists must be int or float")
    if any(h <= 0 for h in height) or any(w <= 0 for w in weight):
        raise ValueError("All elements in height and weight lists must be greater than zero")

    height_arr = np.array(height)
    weight_arr = np.array(weight)

    bmi_arr = weight_arr / (height_arr**2)

    return bmi_arr.tolist()

def apply_limit(bmi: list[int | float], limit: int)-> list[bool]:
    """Apply limit to bmi"""
    if not isinstance(bmi, list):
        raise TypeError("BMI data must be provided as a list.")
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be an int or a float.")
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("All elements in the BMI list must be int or float.")

    bmi_arr = np.array(bmi)
    limit_arr = bmi_arr > limit

    return limit_arr.tolist()
