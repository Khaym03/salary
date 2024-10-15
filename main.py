from employees import RegularEmployee
from workdays import Workdays

WORKING_TIME = 8
HOLYDAYS = [12, 13]


if __name__ == "__main__":
    employee = RegularEmployee("mario", 1)
    hours_worked = len(Workdays(HOLYDAYS=HOLYDAYS).worked_days) * WORKING_TIME

    print(f"Emplead@: {employee.name}")
    print(f"Horas Trabajadas: {hours_worked}h")
    print(f"Tasa: {employee.rate}$")
    print(f"Salario: {employee.salary(hours_worked)}$ \n")
