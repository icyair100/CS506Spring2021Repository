import numpy as np

narr1 = np.array([[1,2],
                 [3,4],
                 [5,6]], dtype=np.int32)

narr2 = np.array([[1,2, 'simon'],
                 [3,4, 'alvaro'],
                 [5,6, 'dullah']])

print('narr1 is:')
print(narr1)

def np_array_to_CSV(input_array):
    ''' Takes an np.array and outputs it in CSV format
    each item between commas is an a row in the CSV
    '''
    return np.savetxt('data.csv', input_array, fmt = "%s", delimiter=",")

csv_file = np_array_to_CSV(narr2)
read_operation = open("data.csv", 'r')

print()
print("The new CSV file contains:")
print(read_operation.read())
