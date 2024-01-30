def main():
    full_name = input('Enter your full name: ')
    
    full_name = full_name.lower()
    full_name = full_name.split()
    first_letter = full_name[0]
    first_letter = first_letter[0]
    middle_letter = full_name[1]
    middle_letter = middle_letter[0]
    last_name = full_name[2]
    
    if len(last_name) >= 10:
        print(f'Username is {first_letter}.{middle_letter}.{last_name[:10]}')
    else:
        print(f'Username is {first_letter}.{middle_letter}.{last_name}')
    
    
    
main()