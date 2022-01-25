# py_flask_mysql_graphql
Simple application communicating with mysql database using GraphQL

# Cd into your project directory

# Create python virtual environment
virtualenv env

# Activate python environment
source env/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Create alch_db database on mysql
CREATE SCHEMA `alch_db` ;

# Create tables

CREATE TABLE `video_model` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `views` int NOT NULL,
  `likes` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `video_model` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `views` int NOT NULL,
  `likes` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

# run python application
python3 main.py

# Access Graphql query interface with
http://localhost:5004/graphql

# Create Video query
`mutation{
  createVideo(name:"David",likes:2,views:1){
    video{
      name,
      likes,
      views
 		}
    
  }
}
`

# Update Video query
`mutation{
  updateVideo(name:"David",likes:2,views:1){
    video{
      name,
      likes,
      views
 		}
    
  }
}
`

#Get Video list query
`videos{
  edges{
    node{
      name,
      likes,
      views
    }
  }
}
}
`

#Get Video by name query
`query{
  video(name:"David"){
        name,
        likes,
        views
    }
}`
 


  


