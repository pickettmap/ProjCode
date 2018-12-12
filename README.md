# ProjCode
This app is a photo storage and photo management program. It is designed for the following functions:
1. User login - The app stores usernames and passwords within a PostgreSQL database, which is referenced by a login screen when the user first opens the app. The user may interact with this database through the HTML frontend which accepts a username and password, with the option to either register a new user, or attempt a login. The user authentication is then validated by the database before proceding.
2. Image uploading - The homepage of the app presents users with visuals of the images that have been uploaded by their username. It provides the option for users to upload new images to the database, where those will also be presented by the homepage. These images are updated to be attributed to that user in the database.
3. Image tagging - The app allows the user to select images and apply text tag attributes to their images.
4. Image searching - The user is capable of searching for images based on the attributed text tags using a search bar presented on the HTML page.


To deploy Tagim, the user must run the command ‘python server.py’. This will initialize the server as a localhost which the user can interact with to utilize the app.
