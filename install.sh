wget https://raw.githubusercontent.com/andrewpsuedonym/goldenShoe/master/db/shoes.csv
 mongoimport -d GoldenShoe -c shoes --type csv --file shoes.csv --headerline
