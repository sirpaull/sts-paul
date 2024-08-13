CREATE TABLE Authors (
	author_id SERIAL PRIMARY key,
  	first_name VARCHAR(100),
  	last_name VARCHAR(100),
  	birthdate DATE
  );
  
 SELECT * FROM customers
   
 INSERT INTO authors (author_id, first_name,last_name, birthdate)
 VALUES
 (1, 'George', 'Orwell', '1903-06-25'),
(3, 'Jane', 'Austen', '1775-12-16'),
(4, 'Mark', 'Twain', '1835-11-30');
  
  CREATE TABLE Bookss (
	book_id SERIAL PRIMARY key,
  	title VARCHAR(100),
  	author_id INT,
  	published_year INT,
    genre VARCHAR,
    price DECIMAL
  );
  
  INSERT INTO bookss (book_id, title, author_id, published_year, genre, price)
 VALUES (1,'Snow Whte',10, 1986, 'romantic novel', 100),
(2, '1984', 1, 1949, 'Dystopian', 9.99),
(3, 'Animal Farm', 1, 1945, 'Political Satire', 7.99),
(4, 'Pride and Prejudice', 2, 1813, 'Romance', 12.99),
(5, 'Adventures of Huckleberry Finn', 3, 1884, 'Adventure', 8.99);
  
    CREATE TABLE Customers (
	customer_id SERIAL PRIMARY key,
  	first_name VARCHAR(100),
  	last_name VARCHAR(100),
  	email VARCHAR(100),
    phone VARCHAR(100)
  );
  
INSERT INTO Customers (customer_id, first_name, last_name, email, phone)
VALUES 
(1, 'Joe', 'Tin', 'joet@yahoo.com', '233-1234'),
(2, 'Jess', 'Smith', 'jessmith@yahoo.com', '233-5678'),
(3, 'Alicia', 'Joma', 'alicejo@yahoo.com', '233-8765');