# Loch Inn

## Introduction:
After a short brainstorming session we decided upon the idea of an online pub's Video Jukebox. This was because I perhaps too ambitiously told the group that generating a YouTube API would be as straightforward as the Spotify one I used for my capstone project.

## Purpose
The intention being that people can go online and choose some videos to watch and listen to whilst being able to have a chat with others online. We intended for a credits system to be used so that each user could select a fair amount, say 5-10 songs a day to stop one user from using the jukebox all day.

## Target Audience
As the intention of being a pub is that the conversation topics wouldn't need to be as cautious for minors so audience would be adults. Obviously there would be moderators to ensure that abuse would be handled as quickly as possible via the admin settings.

## MVP and Key Features
The video jukebox itself, a searchable list of tracks. A chat room to talk to others online at the same time.

## Other features/Future developments
We found out at the eleventh hour of production that signed artists' video channels' cannot be embedded due to YouTube copyright reasons. The 
workaround was to link to some unsigned bands' videos and a couple of
signed bands' live performances. If we were to continue with the site a
workaround could be to invite unsigned bands to send their videos via an
online form with the necessary details attached.

----

# AI:

## How has AI helped us in the project?

### **Code Creation**
In the early stages, VS Code's co-pilot helped me out in creating an API for YouTube that could have worked if only for the fact that the YouTube server side was refusing the requests saying we had a daily amount of 0 credits.

The co-pilot also helped create the code that embedded the videos into the app. I asked it questions and kept repeating the process until it gave the desired outcome. 

### **Debugging**
Co-pilot definitely helped me with finding errors in my code faster than I would have been able to alone or with traditional searching online. However I did find that over-reliance on Co-pilot made it repeat the same steps sometimes that weren't the cause of the problem. In these instances more emphasis on other developer tools like writing to the console were more helpful.

### **Code Optimisation** 
I found AI helpful to refactor whole sections of code where some variable names needed changing.

### **Development**
I (Oliver) struggled with the initial set-up of the Django server and even with pair-programming help from Hannah we found that Co-pilot was quicker to suggest how to correctly set up the development environment.

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
