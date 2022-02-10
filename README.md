# Timesheets

**Creates a timesheet that complies to the german 'Act on the Regulation of a General Minimum Wage' - specifically the 'MiLoG §17 Preparation and holding of documents'.**

In Germany, mini-jobbers (including working students or student assistants) are obliged to document their working hours.
The employer usually provides an Excel template file and expects a signed scan at the end of the month.
This can take longer than the job itself - here is the solution.
Enjoy!

## How to use

1. Clone the project
2. Install the requirements
3. Put the required files in the same folder as the python file
   - `template.xlsx`
   - `sign.png`
4. Execute the `main.py`
5. Print/mail the `result.pdf`

## The law

In accordance with §17 of the MiLoG, an employer who employs workers in accordance with §8 (1) of the Fourth Book of the Social Code or in the economic sectors or branches of the economy specified in §2a of the Act to Combat Clandestine Employment is also obliged to _record the beginning, end and duration of the daily working time_ of these workers no later than the end of the seventh calendar day following the day on which the work is performed and to keep these records for at least two years starting from the time relevant for the recording.
The current interpretation allows to postpone the creation of those timesheets to the end of the calendar month.

## Enhancement options

[ ] Protection against malicious XML in template  
[ ] Import of working times from Jira  
[ ] Export as PDF  
[ ] Add a config file to modify where the signature and the working days are put to  
[ ] Sending the result by mail
