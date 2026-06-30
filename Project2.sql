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

INSERT into Professors
VALUES		('Dr. Samantha Rodriguez', '456789123','42','Associate Professor','Artificial Intelligence and Machine Learning');
INSERT into Professors
VALUES		('Dr. Jonathan Chen','567892345','50','Professor','Cybersecurity and Network Security');
INSERT into Professors
VALUES		('Dr. Emily Thompson','678903456','38','Assistant Professor','Data Science and Big Data Analytics');
INSERT into Professors
VALUES		('Dr. Michael Patel','789014567','45','Professor','Computer Vision and Image Processing');
INSERT into Professors
VALUES		('Dr. Rachel Kim','890125678','41','Associate Professor','Human-Computer Interaction and User Experience');
INSERT into Professors
VALUES		('Dr. Joshua Nguyen','901236789','47','Professor','Software Engineering and Development');
INSERT into Professors
VALUES		('Dr. Amanda White','012347890','39','Assistant Professor','Cryptography and Information Security');
INSERT into Professors
VALUES		('Dr. Rebecca Stone','123456789','42','Associate Professor','Environmental Science');
INSERT into Professors
VALUES		('Dr. Alexander Chang','987654321','55','Professor','Computer Engineering');
INSERT into Professors
VALUES		('Dr. Sarah Patel','556789123','38','Assistant Professor','Sociology');
INSERT into Professors
VALUES		('Dr. Michael Rodriguez','789012345','50','Professor','History');
INSERT into Professors
VALUES		('Dr. Emily Kim','234567890','48','Associate Professor','Literature');
INSERT into Professors
VALUES		('Dr. Samuel Carter','567890123','60','Professor','Psychology');
INSERT into Professors
VALUES		('Dr. Jennifer Wong','345678901','44','Assistant Professor','Economics');

INSERT into Dept
VALUES		('101','Department of Environmental Science','ES-201');
INSERT into Dept
VALUES		('202','Department of Computer Engineering','CE-305');
INSERT into Dept
VALUES		('303','Department of Sociology','SOC-112');
INSERT into Dept
VALUES		('404','Department of History','HIST-210');
INSERT into Dept
VALUES		('505','Department of Literature','LIT-301');
INSERT into Dept
VALUES		('606','Department of Psychology','PSYCH-415');
INSERT into Dept
VALUES		('707','Department of Economics','ECON-102');
INSERT into Dept
VALUES		('808','Department of Computer Science','CS-401');

INSERT into Graduate
VALUES		('111223333','Emily Johnson','25','Environmental Science','666778888');
INSERT into Graduate
VALUES		('222334444','Mark Thompson','27','Computer Engineering','000112222');
INSERT into Graduate
VALUES		('333445555','Sarah White','26','Sociology','556677788');
INSERT into Graduate
VALUES		('444556666','David Lee','28','History','523344455');
INSERT into Graduate
VALUES		('555667777','Jessica Martinez','24','Literature','445566677');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('666778888','Daniel Brown','26','Psychology');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('777889999','Samantha Taylor','27','Economics');
INSERT into Graduate
VALUES		('888990000','Alex Nguyen','25','Computer Science)','556677788');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('999001111','Rachel Kim','26','Environmental Science');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('000112222','Jason Wilson','27','Computer Engineering');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('112233344','Olivia Garcia','25','Sociology');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('223344455','Matthew Rodriguez','28','History');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('334455566','Ashley Patel','24','Literature');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('445566677','Christopher Thomas','26','Psychology');
INSERT into Graduate(GSSN, GName, GAge, Deg_Pog)
VALUES		('556677788','Michelle Chang','27','Computer Science');

INSERT into Project
VALUES		('ES-001','National Science Foundation (NSF)','2024-06-01','2026-05-31','500000');
INSERT into Project
VALUES		('CE-002','Department of Defense (DoD)','2024-08-15','2025-08-14','1200000');
INSERT into Project
VALUES		('SOC-003','National Institutes of Health (NIH)','2024-07-01','2026-06-30','800000');
INSERT into Project
VALUES		('LIT-004','National Endowment for the Humanities (NEH)','2024-09-01','2025-08-31','300000');
INSERT into Project
VALUES		('PSYCH-005','American Psychological Association (APA)','2024-10-01','2026-09-30','700000');
INSERT into Project
VALUES		('ECON-006','World Bank','2024-11-15','2025-11-14','1500000');
INSERT into Project
VALUES		('CS-007','Google Research','2024-12-01','2026-11-30','2000000');

INSERT into Work_Dept(PSSN, Dno)
VALUES		('456789123','808');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('567892345','808');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('678903456','808');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('789014567','808');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('890125678','808');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('901236789','808');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('012347890','808');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('123456789','101');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('987654321','202');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('556789123','303');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('789012345','404');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('234567890','505');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('567890123','606');
INSERT into Work_Dept(PSSN, Dno)
VALUES		('345678901','707');

INSERT into works_in
VALUES		('456789123','CS-007');
INSERT into works_in
VALUES		('789014567','CS-007');
INSERT into works_in
VALUES		('890125678','CS-007');
INSERT into works_in
VALUES		('901236789','CS-007');
INSERT into works_in
VALUES		('012347890','CS-007');
INSERT into works_in
VALUES		('123456789','ES-001');
INSERT into works_in
VALUES		('987654321','CE-002');
INSERT into works_in
VALUES		('556789123','SOC-003');
INSERT into works_in
VALUES		('234567890','LIT-004');
INSERT into works_in
VALUES		('567890123','PSYCH-005');
INSERT into works_in
VALUES		('345678901','ECON-006');

INSERT into Manages
VALUES		('ES-001','123456789');
INSERT into Manages
VALUES		('CE-002','987654321');
INSERT into Manages
VALUES		('SOC-003','556789123');
INSERT into Manages
VALUES		('LIT-004','234567890');
INSERT into Manages
VALUES		('PSYCH-005','567890123');
INSERT into Manages
VALUES		('ECON-006','345678901');
INSERT into Manages
VALUES		('CS-007','012347890');

INSERT into Work_Proj
VALUES		('111223333','ES-001');
INSERT into Work_Proj
VALUES		('111223333','CS-007');
INSERT into Work_Proj
VALUES		('222334444','CE-002');
INSERT into Work_Proj
VALUES		('222334444','CS-007');
INSERT into Work_Proj
VALUES		('333445555','SOC-003');
INSERT into Work_Proj
VALUES		('444556666','CS-007');
INSERT into Work_Proj
VALUES		('555667777','LIT-004');
INSERT into Work_Proj
VALUES		('666778888','PSYCH-005');
INSERT into Work_Proj
VALUES		('888990000','CS-007');
INSERT into Work_Proj
VALUES		('000112222','CE-002');
INSERT into Work_Proj
VALUES		('223344455','CS-007');
INSERT into Work_Proj
VALUES		('445566677','CS-007');
INSERT into Work_Proj
VALUES		('556677788','CS-007');

INSERT into Major
VALUES		('111223333','101');
INSERT into Major
VALUES		('222334444','202');
INSERT into Major
VALUES		('333445555','303');
INSERT into Major
VALUES		('444556666','404');
INSERT into Major
VALUES		('555667777','505');
INSERT into Major
VALUES		('666778888','606');
INSERT into Major
VALUES		('777889999','707');
INSERT into Major
VALUES		('888990000','808');
INSERT into Major
VALUES		('999001111','101');
INSERT into Major
VALUES		('000112222','202');
INSERT into Major
VALUES		('112233344','303');
INSERT into Major
VALUES		('223344455','404');
INSERT into Major
VALUES		('334455566','505');
INSERT into Major
VALUES		('445566677','606');
INSERT into Major
VALUES		('556677788','808');

INSERT into Supervises
VALUES		('111223333','ES-001','123456789');
INSERT into Supervises
VALUES		('111223333','CS-007','456789123');
INSERT into Supervises
VALUES		('222334444','CE-002','987654321');
INSERT into Supervises
VALUES		('222334444','CS-007','456789123');
INSERT into Supervises
VALUES		('333445555','SOC-003','556789123');
INSERT into Supervises
VALUES		('444556666','CS-007','456789123');
INSERT into Supervises
VALUES		('555667777','LIT-004','234567890');
INSERT into Supervises
VALUES		('666778888','PSYCH-005','567890123');
INSERT into Supervises
VALUES		('888990000','CS-007','456789123');
INSERT into Supervises
VALUES		('000112222','CE-002','987654321');
INSERT into Supervises
VALUES		('223344455','CS-007','456789123');
INSERT into Supervises
VALUES		('445566677','CS-007','456789123');
INSERT into Supervises
VALUES		('556677788','CS-007','456789123');

Select Graduate.GSSN, Graduate.GName
From Graduate, Work_proj
where Graduate.GSSN=Work_proj.GSSN and Work_proj.PID='CS-007';

Select Graduate.GSSN, Graduate.GName
From Graduate, Work_proj, major
where Graduate.GSSN=Work_proj.GSSN and Work_proj.PID='CS-007' and Graduate.GSSN=major.GSSN and major.Dno='808';

select COUNT(PID)
from work_proj
where work_proj.PID='CS-007';

select SUM(budget)
from project
where project.budget;