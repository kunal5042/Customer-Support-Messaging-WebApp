# CS-Messaging-Web-App
Branch International Project

### What is this?
A messaging app in **Django** that can be used to respond to incoming questions sent by customers.

### How to get Started?

#### Setup
- Install Python3 ( Instructions [here](https://docs.python-guide.org/starting/installation/) )
- Clone this repository and navigate to top-level directory
- Create a virtual environment (venv) for installing the packages
    ```
    python -m venv ./venv
    ```
- Activate the venv 
- Install all required packages.
    ```
    python -m pip install -r requirements.txt
    ```
- If there is an existing csv file with the user queries, populate the database by running:
    ```
    python manage.py runscript load_csv
    ```
    <sub>Note that running this script will clear the existing user_querys database before repopulating it with entries in csv.</sub>
- For every agent, create an account in admin by running
    ```
    python manage.py createsuperuser
    ```
- Apply the migrations
    ```
    python manage.py migrate
    ```
- Run the app
    ```
    python manage.py runserver
    ```
- Navigate to http://127.0.0.1:8000/ to see the customer interface
- Navigate to http://127.0.0.1:8000/admin to see the agent interface
- Navigate to http://127.0.0.1:8000/admin/users/userquery/ to see user queries and resolve them
- Navigate to http://127.0.0.1:8000/admin/users/agentresponse/ to see the agent responses to queries that are marked as resolved.

#### Working of the app
###### Customer Interface
- Customers can submit their queries by entering their UserID and message in relevant fields of the form.
- Upon submission, the message is recorded and customer is prompted to sucess page from where they can submit another query if they wish


###### Agent Interface
<li>In the Admin/Agent interface, login using the agent credentials</li>
<br />
<li> Agent can view all user queries <a href="http://127.0.0.1:8000/admin/users/userquery/">here</a></li>
<li> The queries can be <strong>filtered</strong> by <strong>urgency</strong> and the status of resolution </li>
    <ul>
        <li> <strong>Open</strong>: Its a new query and no agent has looked into it </li>
        <li> <strong>Assigned</strong>: Query has been looked into by an agent. </li>
        <li> <strong>Resolved</strong>: Query has been resolved by some agent. </li>
    </ul>
<li> The action column provides buttons for agent actions.  </li>
    <ul>
        <li> <strong>Resolve</strong>: When the query is Open, Resolve button is visible 
        On click, agent is taken to a page where they can view the query, and provide a response to it. 
        They can also view other queries by the same customer, so that the agent can resolve multiple queries at once. 
        To mark queries as resolved, </li>
            <ul>
                <li> Check the checkboxes next to other queries that are going to be resolved </li>
                <li> Type a message in the response box </li>
                <li> Click submit </li>
            </ul>
        <li> <strong>Transfer</strong>: When query is assigned to the agent and they cant resolve it, they can Transfer the query. This will mark query as Open again so that some other agent can look into it. </li>
        <li> <strong>Unresolve</strong>: When query is marked resolved, but the agent wants to open it again for furtherdiscussion, they can Unresolve the query  </li>
    </ul>
<li> Agent can <strong>search</strong> the database for queries from a particular user (search with UserID) or for queries with some keywords (search over message body) using the search bar at the top.</li>
<li> User queries are <strong>tagged by urgency</strong> as HIGH, MEDIUM, LOW based on the presence or absence of keywords in  the message. Agents can filter based on urgency and tackle the urgent messages first.</li>
<br />
<li> The responses of the agent can be viewed <a href="http://127.0.0.1:8000/admin/users/agentresponse/">here</a></li>
<li> Whenever an agent submits a response to query, or set of queries of same customer (multiple query resolution), it gets noted here</li>
<li> The database is populated with the agent name, userID of the customer whose query was resolved, the id of the queries resolved and the response provided by the agent.</li>
<li> In the list of ID's of queries resolved, click on the ID will allow one to view the details of the user query.  </li>


#### Features Implemented
- Form based interface for users to submit queries or messages
- Agent interface that allows to respond to queries
- Provision to respond to multiple queries of same user in one go
- Search functionality to allow agents to search over messages and customers
- Tag messages based on the urgency and surface urgent messages
- Filter the user-queries based on resolution status and urgency
- View all agent responses and link to queries resolved by the agent
