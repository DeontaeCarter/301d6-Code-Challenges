#!/bin/bash

# Copies /var/log/syslog to the current working directory
# The codes below are the two parts of the code I was able to come up with by myself but did not work together.

#current_date_time=$(date +"%Y-%m-%d_%H-%M-%S")
#echo >> "Current date and time: $current_date_time"

#Websites used to create a my 'Almost' working code
echo https://stackoverflow.com/questions/17701989/how-do-i-append-text-to-a-file
echo https://www.geeksforgeeks.org/how-to-append-text-to-end-of-file-in-linux/
echo https://tecadmin.net/get-current-date-and-time-in-bash/
echo https://www.cyberciti.biz/faq/unix-linux-getting-current-date-in-bash-ksh-shell-script/#:~:text=Sample%20shell%20script%20to%20display,scripts%20goes%20here%20%23%20...
# Appends the current date and time to the filename

#cp /var/log/syslog .

#This is the working code that ChatGpt helped me put together after I completed two parts.

#!/bin/bash

current_date_time=$(date +"%Y-%m-%d_%H-%M-%S")
filename="syslog_$current_date_time"

cp /var/log/syslog "./$filename"

