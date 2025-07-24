-- 반려동물 주인 TABLE
-- CREATE TABLE PetOwners(
-- 	owenr_id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     contact VARCHAR(255)
-- );

-- 반려동물 TABLE
-- CREATE TABLE Pets(
-- 	pet_id INT AUTO_INCREMENT PRIMARY KEY,
--     ower_id INT NOT NULL,
--     name VARCHAR(100) NOT NULL,
--     species VARCHAR(50),
--     breed VARCHAR(50),
--     FOREIGN KEY (ower_id) REFERENCES PetOwners(owenr_id)
-- );

-- 객실 TABLE
-- CREATE TABLE Rooms(
-- 	room_id INT AUTO_INCREMENT PRIMARY KEY,
--     roomNumber VARCHAR(50) NOT NULL UNIQUE,
--     roomType VARCHAR(50),
--     pricePerNight DECIMAL(10,2) NOT NULL
-- );

-- 예약 TABLE
-- CREATE TABLE Reservations (
--     reservationID INT AUTO_INCREMENT PRIMARY KEY,
--     petID INT NOT NULL,
--     roomID INT NOT NULL,
--     startDate DATE NOT NULL,
--     endDate DATE NOT NULL,
--     FOREIGN KEY (petID) REFERENCES Pets(petID),
--     FOREIGN KEY (roomID) REFERENCES Rooms(roomID)
-- );

--  서비스 TABLE
CREATE TABLE Services(
	service_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    serviceName VARCHAR(100),
    servicePrice DECIMAL(10,2),
    FOREIGN KEY(reservation_id) REFERENCES Reservations(reservation_id)
);
