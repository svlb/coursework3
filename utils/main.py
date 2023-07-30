from utils import get_formated_operation, read_data, filter_by_executed, sort_by_data

all_operations = read_data()
sorted_operations = sort_by_data(all_operations)
filtered_operations = filter_by_executed(sorted_operations)


for operation in filtered_operations:
    print(get_formated_operation(operation))
