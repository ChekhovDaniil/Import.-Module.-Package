def calculate_salary(monthly_salary, bonus_percentage):
    """
    Calculate the total salary including bonus.

    :param monthly_salary: The base monthly salary.
    :param bonus_percentage: The bonus percentage to be added to the salary.
    :return: Total salary after adding the bonus.
    """
    bonus_amount = monthly_salary * (bonus_percentage / 100)
    total_salary = monthly_salary + bonus_amount
    return total_salary