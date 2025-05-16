# Practical task

## Task 1

1. Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.

2. Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.

3. Create a script that reads the access log from a file. The name of the file is provided as an argument. An output of the script should provide the total number of different User Agents and then provide statistics with the number of requests from each of them. [Here is a link to an example access log file](https://www.google.com/url?q=https://drive.google.com/file/d/1x6t1gFICCeN2RwTxG1IyDfr1FlgSQNfk/view?usp%3Dsharing&sa=D&source=editors&ust=1747408488948079&usg=AOvVaw1WpJVsG-rY0EGpYNbXfC_t).

4. Given an input string, count occurrences of all characters within a string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).

5. Write a script that gets system information like distro info, memory(total, used, free), CPU info (model, core numbers, speed), current user, system load average, and IP address. Use arguments for specifying resources. (For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address).

## Task 2: 
Create a script that uses the Survey Monkey (https://www.surveymonkey.com) service, creates a survey.

- PREREQUISITES:
    1. Sign up at https://www.surveymonkey.com 

    2. Create a draft application at https://developer.surveymonkey.com   

    3. No need to deploy your application. It's just for testing. Do not forget to set permissions for your application.

    4. After creating a draft application you will obtain an ACCESS_TOKEN which is needed to do API requests from your script.

- REQUIREMENTS:
    1. The script should accept a JSON file with questions for the survey and a text file with a list of email addresses.

    2. The structure of a JSON file with questions:

    ```
    {
        "Survey_Name": {
            "Page_Name": {
                "Question1_Name": {
                    "Description": "Description of question",
                    "Answers": [
                    "Answer1",
                    "Answer2",
                    "Answer3"
                    ]
                },
                "Question2_Name": {
                    "Description": "Description of question",
                    "Answers": [
                    "Answer1",
                    "Answer2",
                    "Answer3"
                    ]
                }
            }
        }
    }
    ```
    
    3. There should be at least 3 questions and 2 recipients.

