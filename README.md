# Simple-rest-service

## How to run

1. Open console and navigate to the project folder
2. Type 'flask run'
3. In console you will see message that application in running and wait request on http://localhost:5000
4. Now you able to send GET request to endpoint http://localhost:5000/compensation_data

## How to use

- Filter by column value: ?column_name1=value1&column_name2=value2&...
- Sort by columns: ?sort=column_name1,column_name2&...
- Specify fields: ?fields=column_name1,column_name&...
- You can also specify condition to the field names:
  - column[gte]=value - Greater or equal
  - column[gt]=value - Greater than the value
  - column[lte]=value - Lower or equal
  - column[lt]=value - Lower than the value

## Available Fields

"Timestamp"
"Employment Type"
"Company Name"
"Company Size - # Employees"
"Primary Location (Country)"
"Primary Location (City)"
"Industry in Company"
"Public or Private Company"
"Years Experience in Industry"
"Years of Experience in Current Company  "
"Job Title In Company"
"Job Ladder"
"Job Level"
"Required Hours Per Week"
"Actual Hours Per Week"
"Highest Level of Formal Education Completed"
"Total Base Salary in 2018 (in USD)"
"Total Bonus in 2018 (cumulative annual value in USD)"
"Total Stock Options/Equity in 2018 (cumulative annual value in USD)"
"Health Insurance Offered"
"Annual Vacation (in Weeks)"
"Are you happy at your current position?"
"Do you plan to resign in the next 12 months?"
"What are your thoughts about the direction of your industry?"
"Gender"
"Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth
in your industry over the next 10 years?"
"Have you ever done a bootcamp? If so was it worth it?": ""
