//1.(Companies)Selecciona la compañia que tenga mas de 45 empleados, que haya sido fundada después del 2006 y que tenga como mes de fundación Octubre(10)
db.companies.find({number_of_employees : {$gt : 45}},{founded_year :{$gt : 2006}}, {founded_month : 10}).pretty()
//2.(Books)Selecciona los libros que no esten publicados o tengan mas de 600 páginas, y que el ide esté entre 30 y 65, saltando los 5 primeros
db.books.find({$or : [{status : {$ne : "PUBLISH"}},{pagecount : {$gt : 600}}]}, {_id : {$gt : 30}}, {_id : {$lt : 65}}).skip(5).pretty()
//3.(Restauran)Selecciona todos los restaurantes que sea 67 Park Street o con una puntuacion de menor a 7 y que el tipo de comida sea China, ordena segun el rating
db.restaurants.find({$or : [{address : 67 Park Street}, {rating : {$gt : 7}}]}, {type_of_food : {Chinese}}).sort({rating : 1}).pretty()
//4.Selecciona los restaurantes que sean de tipo de comida Thai, con una puntuación mayor a 7, mostrar solo los 3 primeros