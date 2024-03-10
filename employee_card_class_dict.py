
def formatter():
    print("#"*44)

class Employee_details:
    def __init__(self):
        self.employee_data = {}

    # read the employee data from a dictionary function
    def read_employee_data(self):
        file_name = 'employee_data.txt'
        try:
            with open(file_name, 'r') as file:
                # Read each line in the file
                for line in file:
                    # Strip newline characters and split the line into parts
                    company_name, name, title, gender, age, salary, experience = line.strip().split(',')

                    # Add the employee names to the dictionary
                    self.employee_data[company_name] = {"name": name, "title": title, "gender": gender, "age": age,
                                                        "salary": salary, "experience": experience}

        except FileNotFoundError:
            print(f"File {file_name} does not exist for reading")
        return self.employee_data

    def print_employee_card(self):
        self.read_employee_data()

        # Loop through the employee data and print the card details
        for company_name, details in self.employee_data.items():
            formatter()
            print(f"# Company Name is: {company_name:<24}#\n# Name of employee: {details['name']:<23}#\n"
                  f"# Title: {details['title']:<34}#\n# Age: {details['age']:<36}#\n"
                  f"# Salary: {details['salary']:<33}#\n# Year of experience: {details['experience']:<21}#")
            formatter()
            print()


# Call the function print_employee_card to print each employee card details
data = Employee_details()

data.print_employee_card()

