//1
db.restaurants.find().pretty()
//2
db.restaurants.find({}, {restaurants_id : 1, name : 1, borough : 1, cuisine : 1}).pretty()
//3
db.restaurants.find({}, {restaurants_id : 1, name : 1, borough : 1, _id : 0}).pretty()
//4
db.restaurants.find({borough : "Bronx"}).pretty()
//5
db.restaurants.find({borough : "Bronx"}).limit(5).pretty()
//6
db.restaurants.find({borough : "Bronx"}).limit(5).skip(5).pretty()
//7
db.restaurants.find({borough : "Bronx"}).limit(5).skip(10).pretty()
//8
db.restaurants.find({borough : "Bronx"}).limit(5).skip(15).pretty()
//9
db.restaurants.find({grades: {$elemMatch: {"score": {$gte: 80, $lte: 100}}}}).pretty()
//10
db.restaurants.find({"address.cord" : {$lte : -95.764158}}).pretty()
//11
db.restaurants.find({cuisine : {$ne : "American"}}, {"grades": {$elemMatch: {score: {$gte: 70}}}}).pretty()
//12
db.restaurants.find({cuisine : {$ne : "American"}}, {borough : {$ne : "Brooklyn"}}, {grades : {$elemMatch: {"grade": A}}).sort({score: -1}).pretty()//13
//13
db.restaurants.find( {name: /^Wil/}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 } );
//14
db.restaurants.find({borough : "Bronx", $or : [{cuisine : "American"},{cuisine : "Chinese"}]}).pretty()
//15
db.restaurants.find( {"borough" :{$nin :["Staten Island","Queens","Bronx","Brooklyn"]}}, { "restaurant_id" : 1, "name":1,"borough":1, "cuisine" :1 } );

