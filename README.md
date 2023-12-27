Create your own inputs and check if you are getting expected output.
After you finish the assignment question and get them evaluated, you need to write unit tests for all the functions you code

Create a yaml file with event_type, date, hour, count. 
Event_type can be one of clk, imp, eng, con and vid. 
Date is of format yyyy-MM-dd. 
Hour will be of format HH. 
Question:
Process input file and show statistics which prints event_type, month, total_event_count, highest_year, lowest_year in which count was low.
  
Note: Minimum 30-50 entries spread across 2-3 years, 4-5 months, 5-6 hours, and also all event types should be covered


Use classes to represent Format as base class (should have “name” as attribute) and CSV as a child class and attributes are filename and delimiter
Question:
Create a csv file with any columns and process the file using OOPs concept and produce below results
Whether the csv file is valid or not
Header 
row_count 

Input:
impressions: {id: ‘id1’, name: ‘name1’, ip: ‘<ip_address>’}
clicks: {id: ‘id2’, name: ‘name2’, ip: ‘<ip_address>’}
{ip: ‘<ip_address>, browser: ‘b1’, os: ‘os1’}

Output:
{os: ‘os1’, browser: ‘b1’, impressions: [{id: ‘id1’, name: ‘name1’}], clicks: [{id: ‘id2’, name: ‘name2’}], matching_ids: []]}
           
Behavior:
Need to bring all the click and impression info for given os and browser. You can join with ip to achieve that
Matching_ids should be intersection of ids which are common across clicks and impression for same os and browser


