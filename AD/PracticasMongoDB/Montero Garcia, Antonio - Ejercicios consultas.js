//1
db.movies.find().pretty()
//2
db.movies.find({wtiter : "Quentin Tarantino"}).pretty()
//3
db.movies.find({actors : "Brad Pitt"}).pretty()
//4
db.movies.find({franchise : "The Hobbit"}).pretty()
//5
db.movies.find({year : {$gte : 1999, $lte : 1999}}).pretty()
//6
db.movies.find({year : {$gte : 2000, $lte : 2010}}).pretty()


//1
db.movies.updateOne({title : "The Hobbit: An Unexpected Journey"}, {$set : {synopsis : "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."}})
//2
db.movies.updateOne({title : "The Hobbit: The Desolation of Smaug"}, {$set : {synopsis : "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."}})
//3
db.movies.updateOne({title : "pullp Fiction"}, {$push : {actors : "Samuel L. Jackson"}})



//1
db.movies.find({synopsis : /bilbo/i}).pretty()
//2
db.movies.find({synopsis : /gandalf/i}).pretty()
//3
db.movies.find({synopsis : /bilbo/i, $nor:[{synopsis : /gandalf/i}]}).pretty()
//4
db.movies.find({$or : [{synopsis : /dwarves/i}, {synopsis : /hobbit/i}]}).pretty()
//5
db.movies.find({$and : [{synopsis : /gold/i}, {synopsis : /dragon/i}]}).pretty()



//1
db.movies.remove({title : "Pee Wee Herman's Big Adventure"})
//2
db.movies.remove({title : "Avatar"})
