import base64

def binary_to_base64(input_file_name, output_file_name):
    with open(input_file_name, 'rb') as input_file, open(output_file_name, 'w') as output_file:
        base64_data = base64.b64encode(input_file.read()).decode('utf-8')
        output_file.write(base64_data)

def base64_to_binary(input_file_name, output_file_name):
    with open(input_file_name, 'r') as input_file, open(output_file_name, 'wb') as output_file:
        base64_data = input_file.read()
        binary_data = base64.b64decode(base64_data)
        output_file.write(binary_data)