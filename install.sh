sudo systemctl stop GoldenShoe
wget https://raw.githubusercontent.com/andrewpsuedonym/goldenShoe/master/db/shoes.csv
mongo GoldenShoe --eval "db.dropDatabase()"
mongoimport -d GoldenShoe -c shoes --type csv --file shoes.csv --headerline
