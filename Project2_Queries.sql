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