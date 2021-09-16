Automatic Birthday Wisher

- Here we are going to create a Python Application which will automatically wish someone on their birthday, This application will wish someone     
  automatically on schedule.
- Let see how to make it
- Now you have to install a few Module which will help this program to run,
  such as pandas, openpyxl etc. We will type the following in terminal/CMD to install the modules.

$> “pip install pandas”.
$> “pip install openpyxl”

- Now we will create an excel sheet on that folder and open it. We will add the following rows, such as S.No., Name, Birthday, Message, Year, Email. then we have to create a function which will read the excel file and extract data from it. After that will have to use the pandas library for it & for email we have to use the smtplib library.
-Now our program is ready.

Now to schedule the program you need to do the following:
- We need to create a task scheduler task which will run our file on 12:00 am everyday so that it can check and wish that person on their respective birthday.
- To do that, you need to copy the path of the file.
- Now open the task scheduler.
- Now you need to click on  create a task and then triggers.
- Now click on new and set that as daily and time as 00:00:00 (for 12 am).
- Now get back to the general tab and add name and description.
- Now go to action then new and then click on browse.
- Now on program/script click browse and then choose python.exe by browsing and for arguments just paste the path of the file within the double quote.
- Now press ok and exit it.
- Now our program is ready to run.
