
CREATE TABLE Category (
                category_id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(100) NOT NULL,
                PRIMARY KEY (category_id)
);


CREATE TABLE Product (
                id INT AUTO_INCREMENT NOT NULL,
                category_id INT NOT NULL,
                name VARCHAR(100) NOT NULL,
                description VARCHAR(3000),
                store VARCHAR(100) NOT NULL,
                nutriscore INT NOT NULL,
                register BOOLEAN NOT NULL,
                substitut_id INT,
                PRIMARY KEY (id)
                CONSTRAINT category_product_fk
                    FOREIGN KEY (category_id)
                    REFERENCES Category (category_id)
);
