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
    UserID INT REFERENCES Users(UserID) ON DELETE CASCADE, 
    Rating INT CHECK (Rating >= 1 AND Rating <= 10)
);

CREATE TABLE Interactions (
    InteractionID SERIAL PRIMARY KEY,
    ReviewID INT REFERENCES Reviews(ReviewID) ON DELETE CASCADE, 
    UserID INT REFERENCES Users(UserID) ON DELETE CASCADE, 
    ReactionType TEXT 
);

CREATE TABLE Admins (
    AdminID SERIAL PRIMARY KEY,
    AdminUserID INT REFERENCES Users(UserID) ON DELETE CASCADE 
);
