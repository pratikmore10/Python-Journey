# Python Journey
> My python learning journey with coursera specialization "Python for Everybody"

## Learning
[Introduction to Python](doc/introduction_to_python.md)

## Assignments
1. [Pay Calculator](/src/assignments/pay_calculator.py)<br>
My very first basic program to calculate the ***Pay*** of the employee on the basis of the ***Hours*** they worked where ***Rate*** increases 1.5 time if they have worked for more than 40 hrs.

1. [Pay Calculator Using Function](/src/assignments/pay_calculator_function.py)<br>
Problem no.1 solved using ***FUNCTIONS***.  

1. [Iterate And Maintain MAX & MIN](/src/assignments/loop_counting.py)<br>
Program that keeps on asking user for an input till the user returns 'done' as an input.<br>
It stores all the input in a list and then returns ***MAX & MIN*** of the given list. 

1. [File Reading](/src/assignments/file_reading.py)<br>
A program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file.

1. [Count of Specific Lines](/src/assignments/count_word.py)<br>
A program that prompts for a file name, then opens that file and reads through the file, looking for lines  of the form: **X-DSPAM-Confidence:    0.8475** and count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output.<br>
**For Practice** - You can download the sample data [from here](http://www.py4e.com/code3/mbox-short.txt) when you are testing. Enter "mbox-short.txt" as the file name.<br>
**NOTE:** Make sure to save the file into the same folder as you will be writing your Python program.

1. [Words List](/src/assignments/words_list.py)<br>
This program builds a list of words from the input provided. For each word on each line the program checks to see if the word is already in the list and if not append it to the list and then sorts the list of words and print the resulting words in alphabetical order.<br>
**For Practice** - You can download the sample data [from here](http://www.py4e.com/code3/romeo.txt) when you are testing. Enter "romeo.txt" as the file name.<br>
**NOTE:** Make sure to save the file into the same folder as you will be writing your Python program.

1. [Getting Specific Words From Lines](/src/assignments/word_from_lines.py)<br>
Program which returns the specific words from the entire line.<br>
**For Practice** - You can download the sample data [from here](http://www.py4e.com/code3/mbox-short.txt) when you are testing. Enter "mbox-short.txt" as the file name.<br>
**NOTE:**
    1. Make sure to save the file into the same folder as you will be writing your Python program.<br>
    1. '?' - insert the start of the line which you need to parse.

1. [Using Dictionaries](/src/assignments/dict_mail.py)<br>
A program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.<br>
You can download the sample data [from here](http://www.py4e.com/code3/mbox-short.txt) when you are testing. Enter "mbox-short.txt" as the file name.

1. [Extracting Data With Regular Expressions](/src/assignments/regex_eg.py)<br>
This program reads through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.<br>
**For Practice** - You can download the sample data [from here](http://py4e-data.dr-chuck.net/regex_sum_42.txt) when you are testing (There are 90 values with a sum=445833)<br>
**NOTE:** Make sure to save the file into the same folder as you will be writing your Python program.

1. [Understanding the Request / Response Cycle](/src/assignments/socket_eg.py)<br>
Python program to retrieve a web page over a socket and display the headers from the web server.<br>
**For Practice** - You can use this link: http://data.pr4e.org/intro-short.txt

1. [Scraping HTML Data with BeautifulSoup](/src/assignments/scrapping_BS_eg.py)<br>
Python program to use urllib to read the HTML from the data files, and parse the data, extracting numbers and compute the sum of the numbers in the file<br>
**For Practice** - You can use this link: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)

1. [Following Links in HTML Using BeautifulSoup](/src/assignments/following_links.py)<br>
Python program that expands on given link. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, and report the last name you find.<br>
**For Practice** - You can use this link (http://py4e-data.dr-chuck.net/known_by_Fikret.html)<br>
**Exercise:** Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.<br>
**Answer:** Sequence of names: Fikret Montgomery Mhairade Butchi Anayah<br>
Last name in sequence: Anayah

1. [Extracting Data from XML](src/assignments/xml_eg.py)<br>
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file and enter the sum.<br>
**For Practice** - Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)

1. [Extracting Data from JSON](src/assignments/json_eg.py)<br>
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file.<br>
**For Practice** - Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)

1. [Using the GeoJSON API](src/assignments/geojson_API.py)<br>
This program will use a GeoLocation lookup API modelled after the Google API to look up some universities and parse the returned data.<br>
You can test to see if your program is working with a location of *"South Federal University"* which will have a place_id of **"ChIJdxDeChG540ARgFsT__nQU6E"**.
