# Loch Inn


## Final Bits

### Deployment and how to deploy
The project is currently deployed on Heroku, you can find it by following the link below:

https://loch-inn-c561b96536a3.herokuapp.com/

#### Cloning and Setting Up Locally
Follow these steps to clone the repository and set it up on your local machine:

##### Clone the Repository:

**Open your terminal and run:**
git clone https://github.com/mogr20/loch-inn.git
cd loch-inn

##### Set Up a Virtual Environment:

**Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

##### Install Dependencies:

**Install the required Python packages:**
pip install -r requirements.txt
Set Up Environment Variables:

**Create a .env file in the root directory and add the following:**
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3  # Or your database URL
DEBUG=True

##### Run Migrations:

Apply database migrations: python manage.py migrate

##### Run the Development Server:

**Start the Django development server:**
python manage.py runserver

##### Access the App:

Open your browser and go to: http://127.0.0.1:8000/
Your app is now running locally!

### Technologies Used
Backend:
Python
Django
PostgreSQL

Frontend:
HTML5
CSS3
JS

Tools/programmes used:
Visual Studio Code (VS Code)
Django Development Server
Chrome Developer Tools
Heroku - Used to deploy the project (https://www.heroku.com/)
Git
Github 
Flake8

Credits
To this code, which was used to help create the chat feature: https://www.geeksforgeeks.org/realtime-chat-app-using-django/
