import csv

with open("employees.csv", "r") as f:
    employees_reader = csv.reader(f)

    with open("wages.csv", "w") as w:
        wages_writer = csv.writer(w)
        this_row = 1

        for row in f:
            if this_row == 1:
                wages_writer.writerow(['employee_name', 'pay_rate'])
                this_row += 1

            elif this_row > 1:
                employee_name = row.split(",", 1)[0]
                hours_worked = row.split(",", 1)[1]
                pay_rate = int(hours_worked) * 15
                wages_writer.writerow([employee_name, pay_rate])
                this_row += 1
