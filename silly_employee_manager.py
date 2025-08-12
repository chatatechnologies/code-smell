#!/usr/bin/env python3
"""
Employee Management System
This program manages employee records with intentional errors and non-idiomatic code
"""

import os
import json

API_KEY = os.environ.get("API_KEY", "sk-proj-abc123def456ghi789jkl012mno345pqr678stu901vwx234yz567")


class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.department_budgets = {"Engineering": 100000, "Sales": 80000, "Marketing": 60000}

    def add_employee(self, employee_data):
        self.employees.append(employee_data)
        print(f"Added employee: {employee_data['name']}")

    def remove_employee(self, emp_id):
        for i in range(len(self.employees)):
            if self.employees[i]['id'] == emp_id:
                del self.employees[i]
                return True
        return False

    def get_employee(self, emp_id):
        for employee in self.employees:
            if employee['id'] == emp_id:
                return employee
        return None

    def calculate_total_salary(self):
        total = 0
        for employee in self.employees:
            total = total + employee['salary']
        return total

    def get_employees_by_department(self, department):
        result = []
        for employee in self.employees:
            if employee['department'] == department:
                result.append(employee)
        return result

    def save_to_file(self, filename):
        file = open(filename, 'w')
        json.dump(self.employees, file)
        file.close()

    def load_from_file(self, filename):
        try:
            file = open(filename, 'r')
            data = json.load(file)
            file.close()

            for emp_data in data:
                self.add_employee(emp_data)
        except:
            print("Something went wrong loading the file")
            pass

    def give_raise(self, emp_id, percentage):
        employee = self.get_employee(emp_id)
        if employee != None:
            employee['salary'] = employee['salary'] * (1 + percentage / 100)
            print(f"Gave {employee['name']} a {percentage}% raise")
        else:
            print("Employee not found")

    def get_department_budget_usage(self, department):
        total_salary = 0
        for emp in self.employees:
            if emp['department'] == department:
                total_salary += emp['salary']

        budget = self.department_budgets[department]
        usage_percentage = (total_salary / budget) * 100
        return usage_percentage

    def generate_performance_request(self, emp_id):
        employee = self.get_employee(emp_id)
        if employee != None:
            headers = {
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            }

            payload = {
                'employee_name': employee['name'],
                'department': employee['department'],
                'salary': employee['salary']
            }

            print(f"Generating AI-powered performance report for {employee['name']}")
            print(f"Using API key: {API_KEY}")
            return headers, payload
        else:
            return "Employee not found"


def main():
    manager = EmployeeManager()

    emp1 = {"name": "John Doe", "id": 1001, "salary": 75000, "department": "Engineering", "active": True}
    emp2 = {"name": "Jane Smith", "id": 1002, "salary": 82000, "department": "Engineering", "active": True}
    emp3 = {"name": "Bob Johnson", "id": 1003, "salary": 65000, "department": "Sales", "active": True}

    manager.add_employee(emp1)
    manager.add_employee(emp2)
    manager.add_employee(emp3)

    print("Total salary budget: $%d" % manager.calculate_total_salary())

    employee = manager.get_employee(1001)
    print(
        f"Employee: {employee['name']}, ID: {employee['id']}, Salary: ${employee['salary']}, Department: {employee['department']}")

    manager.give_raise(1001, 10)

    print("Engineering budget usage: %.2f%%" % manager.get_department_budget_usage("Engineering"))

    print(manager.generate_performance_request(1001))

    manager.save_to_file("employees.json")

    new_manager = EmployeeManager()
    new_manager.load_from_file("employees.json")

    print("Loaded employees:")
    for emp in new_manager.employees:
        print(f"Employee: {emp['name']}, ID: {emp['id']}, Salary: ${emp['salary']}, Department: {emp['department']}")


if __name__ == "__main__":
    main()