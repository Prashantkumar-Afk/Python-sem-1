# Create a program to calculate an employee's salary using basic salary, HRA, DA and deductions.
# Function to calculate salary
def calculate_salary(basic_salary, hra, da, deductions):
    # Calculate gross salary
    gross_salary = basic_salary + hra + da
    
    # Calculate net salary
    net_salary = gross_salary - deductions
    
    return net_salary