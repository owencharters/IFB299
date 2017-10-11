create table Weather(
	weatherID int not null auto_increment,
    weather varchar(50) not null,
    primary key (weatherID)
	);

create table Cities(
	cityID int not null auto_increment,
    title varchar(100) not null,
    weather varchar(50),
    primary key (cityID),
    foreign key (weather) references Weather(weather)
    );

create table Users ( 
	userID int not null auto_increment,
    userName varchar(20) not null,
    userFirstName varchar(20) not null,
    userLastName varchar(20) not null,
    userType varchar(20) not null,
    cityID int,
    email varchar(300),
    userPassword varchar(50),
    primary key (userID),
    foreign key (cityID) references Cities(cityID)
	);

create table UserType(
	typeId int not null auto_increment,
    typeDescription varchar(30) not null,
    primary key (typeID)
	);
    
create table Libraries (
	libraryID INT NOT NULL AUTO_INCREMENT,
    cityID int,
    libraryName varchar(100),
    phoneNumber char(10) NOT NULL,
    address varchar(300)not null,
    email varchar(320) NOT NULL,
    primary key (libraryID),
    foreign key (cityID) references Cities(cityID)
	);
    
create table Colleges(
	collegeID int not null auto_increment,
    cityID int,
    collegeName varchar(100) not null,
    phoneNumber char(10) not null,
    address varchar(300) not null,
    primary key (collegeID),
    foreign key (cityID) references Cities(cityID)
	);
    
create table Departments(
	departmentID int not null auto_increment,
    description varchar(10) not null,
    collegeID int,
    primary key (departmentID),
    foreign key (collegeID) references Colleges(collegeID)
	);
    
create table Industries(
	typeID int not null auto_increment,
    description varchar(100) not null,
    primary key (typeID)
	);
    
create table Parks(
	parkID int not null auto_increment,
    parkName varchar(100) not null,
    cityID int,
    phoneNumber varchar(10) not null,
    address varchar(300),
    email varchar(60),
    primary key (parkID),
    foreign key (cityID) references Cities(cityID)
	);
    
create table Hotels(
	hotelID int not null auto_increment,
    hotelName varchar(100) not null,
    cityID int,
    phoneNumber varchar(10) not null,
    address varchar(300),
    email varchar(60),
    primary key (hotelID),
    foreign key (cityID) references Cities(cityID)
	);
create table Museums(
	museumID int not null auto_increment,
    museumName varchar(100) not null,
	cityID int,
    phoneNumber varchar(10) not null,
    address varchar(300),
    email varchar(60),
    primary key (museumID),
    foreign key (cityID) references Cities(cityID)
	);

create table Zoos(
	zooID int not null auto_increment,
    zooName varchar(100) not null,
	cityID int,
    phoneNumber varchar(10) not null,
    address varchar(300),
    email varchar(60),
    primary key (zooID),
    foreign key (cityID) references Cities(cityID)
	);
    
create table Malls(
	mallID int not null auto_increment,
    mallName varchar(100) not null,
	cityID int,
    phoneNumber varchar(10) not null,
    address varchar(300),
    email varchar(60),
    primary key (mallID),
    foreign key (cityID) references Cities(cityID)
	);
    
create table Restaurants(
	restaurantID int not null auto_increment,
    restaurantName varchar(100) not null,
	cityID int,
    phoneNumber varchar(10) not null,
    address varchar(300),
    email varchar(60),
    primary key (restaurantID),
    foreign key (cityID) references Cities(cityID)
	);
