def rename(query):
    return query

def main():
    file = 'File.txt'
    print(f'Currently the file name is {file}')
    rename_file = input('Enter the new file name: ')
    file = rename(rename_file+'.txt')
    print(f'Now the file name is {file}')

if __name__ == '__main__':
    main()
    input('Enter a key to exit...')