This application allows the user to report the beers they have drunk and provide a review of the beer. The application allows the user to mark that they have seen a specific beer at a store and tell how much the beer costed at the store. This information is then added to the common pool of beer reviews and sightings, which can be searched by users.

Features:
- Allows users to create an account and login after creation
- Allows the users to delete their own account along with evreything that account has posted on the site
- The user can search for beers and if no such beer exists is given the opportunity to add to the database
- Allows users to rate a beer on a scale of 1 to 10
- Along with this review users can provide a max 300 character comment on the beer
- Ratings and comments are stored and can be searched by people. This is done by searching the beer which will then give a list of all reviews for that beer
- Users are able to report sightings of a specific beer with the location and price of the beer.

Usage instructions:
- Clone the repository
- Create a .env file and define the contents of it as follows
  ```
  DATABASE_URL=location of your database
  SECRET_KEY=your secret key
  ```
- Next activate the virtual environment and install all necessary python modules with:
  ```
  python3 -m venv venv
  source venv/bin/activate
  pip install -r ./requirements.txt
  ```
- Define the schema for the database using the schema in the repo with
  ```
  psql < schema.sql
  ```
- Run the application with
  ```
  flask run
  ```
- You will find the application on localhost:5000 in your browser



