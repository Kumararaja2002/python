import array

my_array = array.array('i', [1,2,3,4]) # i - integer
my_array1 = array.array('i', [1,2,3,4])
my_array2 = array.array('i', [1,2,3,4])
# To insert an element use .insert( index, value ) method
# The first parameter is the index where you want to insert the value
# The second parameter is the value to be inserted

# Insertion at the start
my_array.insert(0, 5)
print(my_array)

# Insertion at the middle
my_array1.insert(2, 5)
print(my_array1)

# Insertion at the end
my_array2.insert(5, 5)
print(my_array2)


# Insertion without using the insert function
def insert_element(arr, index, value):
    arr = arr[:index] + array.array('i', [value]) + arr[index:]
    return arr

# Example usage
my_array4 = array.array('i', [1, 2, 3, 4])
my_array4 = insert_element(my_array4, 2, 6)
print(my_array4)

# Insertion by shifting elements without slicing
def insert_by_shifting(arr, index, value):
    
    # arr.append(0) --> this append '0' to the end
    arr = array.array('i', list(arr) + [0])  # Manually extend the array by one element
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]  # Shift elements to the right
    arr[index] = value  # Insert the new value at the specified index
    return arr
# Example usage
my_array5 = array.array('i', [1, 2, 3, 4])
my_array5 = insert_by_shifting(my_array5, 2, 7)
print(my_array5)

