CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    Username TEXT UNIQUE,
    Password TEXT
);

CREATE TABLE Beers (
    BeerID SERIAL PRIMARY KEY,
    BeerName TEXT,
    Added_By_Username TEXT REFERENCES Users(Username) ON DELETE CASCADE 
);

CREATE TABLE Reviews (
    ReviewID SERIAL PRIMARY KEY,
    BeerID INT REFERENCES Beers(BeerID) ON DELETE CASCADE, 
    Username TEXT REFERENCES Users(Username) ON DELETE CASCADE, 
    Rating INT CHECK (Rating >= 1 AND Rating <= 10)
);

CREATE TABLE Comments (
    CommentID SERIAL PRIMARY KEY,
    BeerID INT REFERENCES Beers(BeerID) ON DELETE CASCADE, 
    Username TEXT REFERENCES Users(Username) ON DELETE CASCADE, 
    Comment VARCHAR(300)
);

CREATE TABLE Locations (
    LocationID SERIAL PRIMARY KEY,
    BeerID INT REFERENCES Beers(BeerID) ON DELETE CASCADE, 
    Username TEXT REFERENCES Users(Username) ON DELETE CASCADE, 
    Location TEXT,
    Price FLOAT
);
