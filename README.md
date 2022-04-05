ArchiQuiz
Introduction
Archiquiz is a browser-based game built in Python. It can be used as an educational tool for Architecture students or a fun game to share with friends.

As the game was developed in Python for use in the terminal, it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

View the live website on Heroku Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

Table of Contents
User Experience Design (UX)
The Strategy Plane
Site Goals
User Stories
The Scope Plane
The Structure Plane
Opportunities
The Skeleton Plane
Wireframes
Logic Flow
The Surface Plane
Features
Future Enhancements
Testing
Deployment
Credits
UX


Deployment
The site was deployed via Heroku, and the live link can be found here - Game.

The project was developed utilising a Code Institute provided template.

Project Deployment
To deploy the project through Heroku I followed these steps:

Sign up / Log in to Heroku
From the main Heroku Dashboard page select 'New' and then 'Create New App'
Give the project a name - I entered the-sims-4-real-estate-quiz and selected a suitable region, then selected create app. The name for the app must be unique.
This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
Next select the add buildpack button below the config vars section.
In the pop-up window select Python as your first build pack and select save changes.
Then repeat the steps to add a node.js buildpack.
The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
Next navigate back to the deploy tab using the submenu at the top of the page.
In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.
Once Heroku has located the repo select connect.
This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button if you wish to automatically deploy your site in Heroku every time you push changes to GitHub.
My preference was to do this manually, so I chose not to Enable Automatic Deploys and I updated my Heroku app periodically.
Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.