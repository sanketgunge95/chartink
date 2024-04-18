#!/bin/bash

PYTHON_EXECUTABLE="/usr/bin/python"
PYTHON_SCRIPT="/home/kali/Desktop/Kite_Zerodha-main/codebase/chartink_main.py"
EMAIL_ADDRESS="snehalsanketgunge@gmail.com"
EMAIL_PASSWORD="Snehal@123"
RECIPIENT_EMAIL="sanket.gunge@gmail.com"

# Run the Python script and capture the output
output=$("${PYTHON_EXECUTABLE}" "${PYTHON_SCRIPT}")

# Send the output via email using Python
echo "${output}" | "${PYTHON_EXECUTABLE}" -c "
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('''${output}''')
msg['Subject'] = 'Script Output'
msg['From'] = '${EMAIL_ADDRESS}'
msg['To'] = '${RECIPIENT_EMAIL}'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('${EMAIL_ADDRESS}', 'uwva fkil pwwd nvkm')
server.sendmail('${EMAIL_ADDRESS}', ['${RECIPIENT_EMAIL}'], msg.as_string())
server.quit()
"


