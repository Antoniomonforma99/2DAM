//1
db.listingsAndReviews.find({host.host_name : "Pablo"}, {address.market : "Rio De Janeiro"}).pretty()

//2
db.listingsAndReviews.find({address.market : "Hong Kong"}, {$or : [{address.country : "France"}, {bedrooms : {$lte : 4}}]}).pretty()

//3
db.listingsAndReviews.find({$or : [{address.country : "Spain"}, {address.country : "Portugal"}]}, {reviews_score_cleanliness : {$gt : 9}}, {$or : [{cancellation_policy : "strict_14_with_grace_period"}, {cancellation_policy : "moderate"}]}).pretty()

//4

//5
db.listingsAndReviews.find({minimum_nights : {$gte : 3}},{room_type : "Entire home/apt"}, {amenities : {$elemMatch : {"Wifi"}, {"Kitchen"}, {"Iron"}}}.limit(5).sort(number_of_reviews : 1)).pretty()

//6
db.listingsAndReviews.find({reviews_scores_rating : {$gt : 85}}).pretty()
