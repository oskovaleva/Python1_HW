revenue = int(input('Input revenue: '))
costs = int(input('Input costs: '))
result_financial = revenue - costs

result_wording = 'profit'
if result_financial < 0:
    result_wording = 'loss'
print(f'Your {result_wording} is {result_financial}')

if result_financial > 0:
    margin = str(int((result_financial / revenue) * 100)) + '%'
    print(f'Your margin is {margin}')

employees_number = int(input('Input the number of employees: '))
result_financial_per_employee = int(result_financial / employees_number)
print(f'Financial result per employee is {result_financial_per_employee}')
