import csv
from datetime import datetime

# Open your existing text file
with open('YOUR_FILE_PATH_HERE', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Create a CSV file for the output
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    csv_writer.writerow(['Date', 'Time', 'Sender', 'Message'])
    
    # Process each line in the chat log
    for line in lines:
        # Split the line into date, time, sender, and message
        parts = line.split(' - ')
        date_time = parts[0].strip()
        sender_message = parts[1].split(':')
        sender = sender_message[0].strip()
        message = ':'.join(sender_message[1:]).strip()
        
        # Convert the date and time to the desired format
        dt_object = datetime.strptime(date_time, "%d/%m/%Y, %H:%M")
        date_formatted = dt_object.strftime("%d/%m/%Y")
        time_formatted = dt_object.strftime("%H:%M")
        
        # Write the data to the CSV file
        csv_writer.writerow([date_formatted, time_formatted, sender, message])
