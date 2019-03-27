# PipeDream_ContentCreationFeature
So our service is going to do and require the following:

-Input user section and role to establish basis for privilege

-Cross reference the account of the user to see what they can and cannot do

-Based on their privilege, the user can be given the option to do
additional things to the article besides reading it; otherwise they will only be able to read

-We will use NodeJS

For this we propose a new service that manages a specific key for each article so that everything is connected. Having a central database with all of the articles and their call keys will make it so articles can be passed between services without issue.  

Given this central database, we will be able to allow users to interact with articles asccording to their privelages. 
