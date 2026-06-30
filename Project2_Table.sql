CREATE TABLE Professors
	(PName varchar(50),
	 PSSN int(9),
	 PAge int(3),
	 PRank VARCHAR(100),
	 Specialty VARCHAR(100),
	 PRIMARY KEY(PSSN));
	 
CREATE TABLE Dept
	(Dno int(3),
	 DName VARCHAR(100),
	 DOffice varchar(100),
	 PRIMARY KEY(Dno));

CREATE TABLE Graduate
	(GSSN int(9),
	 GName varchar(100),
	 GAge int(3),
	 Deg_Pog varchar(100),
	 Advisor_SSN int(9),
	 PRIMARY KEY (GSSN));

CREATE TABLE Project
	(PID varchar(100),
	 Sponsor varchar(100),
	 Start_Date varchar(10),
	 End_Date varchar(10),
	 Budget int,
	 PRIMARY KEY(PID));

CREATE TABLE Work_Dept
	(PSSN int(9),
	 Dno int(3),
	 pc_time int(2),
	 PRIMARY KEY(PSSN, Dno),
	 FOREIGN Key(PSSN) REFERENCES professors(PSSN),
	 FOREIGN Key(Dno) REFERENCES dept(Dno));

CREATE Table Runs
	(PSSN int(9),
	 Dno int(3),
	 PRIMARY KEY(PSSN, Dno),
	 FOREIGN Key(PSSN) REFERENCES Professors(PSSN),
	 FOREIGN Key(Dno) REFERENCES Dept(Dno));

CREATE Table works_in
	(PSSN int(9),
	 PID varchar(100),
	 PRIMARY KEY(PSSN, PID),
	 FOREIGN Key(PSSN) REFERENCES Professors(PSSN),
	 FOREIGN Key(PID) REFERENCES Project(PID));

CREATE Table Manages
	(PID varchar(100),
	 PSSN int(9),
	 PRIMARY KEY(PSSN, PID),
	 FOREIGN Key(PSSN) REFERENCES Professors(PSSN),
	 FOREIGN Key(PID) REFERENCES Project(PID));

CREATE TABLE Major
	(GSSN int(9),
	 Dno int(3),
	 PRIMARY KEY(GSSN, Dno),
	 FOREIGN Key(GSSN) REFERENCES Graduate(GSSN),
	 FOREIGN Key(Dno) REFERENCES Dept(Dno));

CREATE Table Work_Proj
	(GSSN int(9),
	 PID varchar(100),
	 PRIMARY KEY(GSSN, PID),
	 FOREIGN Key(GSSN) REFERENCES Graduate(GSSN),
	 FOREIGN Key(PID) REFERENCES Project(PID));

CREATE TABLE Supervises
	(GSSN int(9),
	 PID varchar(100),
	 PSSN int(9),
	 PRIMARY KEY(GSSN, PSSN),
	 FOREIGN Key(GSSN) REFERENCES Graduate(GSSN),
	 FOREIGN Key(PSSN) REFERENCES Professors(PSSN),
	 FOREIGN Key(PID) REFERENCES Project(PID));
