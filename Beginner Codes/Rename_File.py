import os

# Rename a file
def rename(query, filename):
    os.rename(filename, query)
    return query
  
if __name__ == '__main__':
    # Create a file
    filename = 'file.txt'
    file = open(filename, 'x')
    file.close()

    print(f'Currently the file name is {filename}')
    # Rename the file
    rename_file = input('Enter the new file name: ')
    filename = rename(rename_file+'.txt', filename)
    
    print(f'Now the file name is {filename}')
    
    input('Enter a key to exit...')
    # Delete the file
    os.remove(filename)