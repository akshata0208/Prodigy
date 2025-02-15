try:
    # Take path of image as input
    path = input(r'Enter path of Image: ')
    
    # Ask user whether they want to encrypt or decrypt
    choice = input('Enter "E" to Encrypt or "D" to Decrypt: ').strip().upper()
    
    if choice not in ['E', 'D']:
        print('Invalid choice! Please enter "E" for encryption or "D" for decryption.')
    else:
        # Taking encryption/decryption key as input
        key = int(input('Enter Key for the operation: '))
        
        # Print path of image file and chosen key
        print(f'The path of file: {path}')
        print(f'Key for operation: {key}')
        
        # Open file for reading
        with open(path, 'rb') as fin:
            image = bytearray(fin.read())
        
        # Perform XOR operation on each byte
        for index, value in enumerate(image):
            image[index] = value ^ key
        
        # Write the processed data back to file
        with open(path, 'wb') as fout:
            fout.write(image)
        
        print('Operation Successful:', 'Encryption Done' if choice == 'E' else 'Decryption Done')

except Exception as e:
    print('Error caught:', str(e))