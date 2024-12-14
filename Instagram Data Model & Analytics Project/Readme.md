# Instagram Data Model & Analytics Project

### In this project, we will design a data model for Instagram using PostgreSQL. 
### We created different tables and build the data model, generate SQL create table statements, insert data, 
### showed examples of updating data, and add analytic examples using where condition, orderby, group by, having clause, 
### and explained different aggregation functions. We also covered subquery, window function, CTE, case statement, date casting, and working with dates.

## Designing Data Model

**We will need to create the following tables for our Instagram data model:**

### Users 
| Column       | Type         | Constraints |
| ---          | ---          | ---         |
| user_id      | SERIAL       | PRIMARY KEY |
| name         | VARCHAR(50)  | NOT NULL |
| email        | VARCHAR(100) | UNIQUE NOT NULL |
| phone_number | VARCHAR(20)  | UNIQUE |

### Posts
| Column     | Type         | Constraints |
| ---        | ---          | --- |
| post_id    | SERIAL       | PRIMARY KEY |
| user_id    | INTEGER      | NOT NULL, FOREIGN KEY (user_id) REFERENCES Users(user_id) |
| caption    | TEXT         |  |
| image_url  | VARCHAR(200) |  |
| created_at | TIMESTAMP    | DEFAULT CURRENT_TIMESTAMP |

### Comments
| Column       | Type      | Constraints |
| ---          | ---       | --- |
| comment_id   | SERIAL    | PRIMARY KEY |
| post_id      | INTEGER   | NOT NULL, FOREIGN KEY (post_id) REFERENCES Posts(post_id) |
| user_id      | INTEGER   | NOT NULL, FOREIGN KEY (user_id) REFERENCES Users(user_id) |
| comment_text | TEXT      |  |
| created_at   | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### Likes 
| Column     | Type      | Constraints |
| ---        | ---       | --- |
| like_id    | SERIAL    | PRIMARY KEY |
| post_id    | INTEGER   | NOT NULL, FOREIGN KEY (post_id) REFERENCES Posts(post_id) |
| user_id    | INTEGER   | NOT NULL, FOREIGN KEY (user_id) REFERENCES Users(user_id) |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### Followers
| Column           | Type      | Constraints |
| ---              | ---       | --- |
| follower_id      | SERIAL    | PRIMARY KEY |
| user_id          | INTEGER   | NOT NULL, FOREIGN KEY (user_id) REFERENCES Users(user_id) |
| follower_user_id | INTEGER   | NOT NULL, FOREIGN KEY (follower_user_id) REFERENCES Users(user_id) |
| created_at       | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

## Data Model:
First create the data model using draw.io (All the ER diagrams and Tables relationships).
