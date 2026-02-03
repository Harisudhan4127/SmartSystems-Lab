import time
import gdown
# # Google Drive file ID
# file_id = 'your_file_id_here'

# # URL to download the file
# url = f'https://drive.google.com/uc?id={file_id}'

# # Output file path
# output = 'downloaded_file.txt'

# # Download the file
# gdown.download(url, output, quiet=False)

# # Read and print the file content
# with open(output, 'r') as file:
#     content = file.read()
#     print(content)
# text_file= content.split('==>')[1]
def main(text_file):
    present_date = time.strftime("%Y-%m-%d")
    print("Current date",present_date)
    print("checking date",text_file.split('-')[0], text_file.split('-')[1],text_file.split('-')[2])
    if text_file.split('-')[0] >= present_date.split('-')[0] and text_file.split('-')[1] >= present_date.split('-')[1] and text_file.split('-')[2] >= present_date.split('-')[2] :
        print('your date is invalid')
        return  True

    else:
        print('your date is valid')
        return False