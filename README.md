# Football-Recruitment-Project

Our Goal

Player recruitment is instrumental to the success of a football team. Signing the right player can be the difference between a championship season and a disappointing one. It falls on the recruitment department to target the type of player that melds with the head coach’s vision. With our project we aimed to predict archetypes of players, providing recruitment teams with a tool for identifying who to sign for a successful season.


Our Dataset

Our dataset comprised of professional football players from the English Premier League and Spanish La Liga. We scraped the data we had on each player from the website fbref.com. Scraping the dataset proved to be a challenge due to the way URLs are assigned in on fbref.com. Each URL features a number ID unique to each player, and we could not figure out a way to crack how the IDs were calculated. Fortunately Sushant provided a script for grabbing player URLs on his blogpost at https://medium.com/@sregmi48/scraping-player-stats-from-fbref-and-representing-it-in-a-pizza-plot-ce08c54e52c1, and we credit him for his work. With the URLs, we were able to scrape each individual player’s profiles for their stats.


Pre-Process

Our starting dataset contained an abundance of statistical and career information on each player, totalling over 200 in each row. Before it was ready for model building, we had to perform some transformations. Some data was not necessary for our labeling process and so we engineered it out. This included the amount of teams a player had played for and the different leagues that they had featured in. We also had to find a way to put players on the same level, regardless of experience. A lot of our data was aggregated into totals. For example, the shots column would include the total shots a player had taken in their entire career, leading to a wide variance between players based solely on experience. To flatten the data, we got the total minutes a player had played and divided it by 90 (the length of a full football match) to get full matches played. We then divided each accumulated statistic (shots, passes, assists etc.) by full matches played. Additionally, goalkeepers were also excluded, as our main focus was predicting the playstyle of outfield players. 

Feature Engineering

In terms of engineered features, we implemented our labels using a playstyle column for each player. This was important for our training data, so the model could find the relationship with other columns and the label. To do so we used the popular game Football Manager. The game features a rich database of players and the roles that they are best suited for on the field. The role suitability is determined using attributes formulated with input from professional football scouts. We used the roles from that database to infer the playstyle column for each player.


Modeling Process

We opted for logistic regression for our model. For our data, we converted our labels from text like ‘Offensive Wing Back’ and ‘Creator’ to numerical values. We then performed a 70/30 split on the data, with 70% being for training and 30% being for validation. We then used fit() from the LogisticRegression library on our training data to create our model and applied the model on our test data. 





