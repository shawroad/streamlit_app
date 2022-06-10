### 数据库的操作
1. 登录mysql: `mysql -uroot -p`   
2. 查看当前的数据库: `show databases`;
3. 创建数据库: `create database learning_db;`
4. 删除数据库: `drop database learning_db;`
5. 使用当前的数据库: `use learning_db;`

### 表的操作
1. 查看当前数据库中的表: `show tables;`
2. 创建学生表
    ```sql
    CREATE TABLE student
    (Sno    varchar(20)    NOT NULL,
     Sname  varchar(20)    NOT NULL,
     sex   varchar(20)    NOT NULL,
     age   INT            NOT NULL,
     dept  varchar(20)    NOT NULL,
     PRIMARY KEY (Sno)
    );
    ```
3. 创建课程表
    ```sql
    CREATE TABLE course
    (Cno    varchar(20)    NOT NULL,
     Cname  varchar(20)    NOT NULL,
     hours VARCHAR(20)    NOT NULL,
     PRIMARY KEY (Cno)
    );
    ```
4. 创建成绩表
    ```sql
    CREATE TABLE SC
    (Sno    varchar(20)    NOT NULL,
     Cno    varchar(20)    NOT NULL,
     grade  INT    ,
     PRIMARY KEY (Sno,Cno)
    );
    ```
5. 插入一些数据
    ```sql
    INSERT INTO student VALUES ('9512101','李勇','男',19,'计算机系');
    INSERT INTO student VALUES ('9512102','刘晨','男',20,'计算机系');
    INSERT INTO student VALUES ('9512103','王敏','女',20,'计算机系');
    INSERT INTO student VALUES ('9521101','张立','男',22,'信息系');
    INSERT INTO student VALUES ('9521102','吴宾','女',21,'信息系');
    INSERT INTO student VALUES ('9521103','张海','男',20,'信息系');
    INSERT INTO student VALUES ('9531101','钱小力','女',18,'数学系');
    INSERT INTO student VALUES ('9531102','王大力','男',19,'数学系');
    
    
    INSERT INTO course VALUES ('C01','计算机文化学','70');
    INSERT INTO course VALUES ('C02','VB','90');
    INSERT INTO course VALUES ('C03','计算机网络','80');
    INSERT INTO course VALUES ('C04','数据库基础','108');
    INSERT INTO course VALUES ('C05','高等数学','180');
    INSERT INTO course VALUES ('C06','数据结构','72');
    
    
    INSERT INTO SC VALUES ('9512101','C01',90);
    INSERT INTO SC VALUES ('9512101','C02',86);
    INSERT INTO SC VALUES ('9512101','C06',NULL);
    INSERT INTO SC VALUES ('9512102','C02',78);
    INSERT INTO SC VALUES ('9512102','C04',66);
    INSERT INTO SC VALUES ('9521102','C01',82);
    INSERT INTO SC VALUES ('9521102','C02',75);
    INSERT INTO SC VALUES ('9521102','C04',92);
    INSERT INTO SC VALUES ('9521102','C05',50);
    INSERT INTO SC VALUES ('9521103','C02',68);
    INSERT INTO SC VALUES ('9521103','C06',NULL);
    INSERT INTO SC VALUES ('9531101','C01',80);
    INSERT INTO SC VALUES ('9531101','C05',95);
    INSERT INTO SC VALUES ('9531102','C05',85);
    ```

### 增删改查那些事
> 注意sql语句不区分大小写

1. 分别查询学生表和学生修课表中的全部数据
    ```sql
    SELECT * FROM student;
    SELECT * FROM course;
    ```
2. 查询成绩在70-80分之间的学生的学号、课程号和成绩
    ```sql
    SELECT * FROM SC WHERE grade > 70 and grade < 80;
    ```
3. 查询C01号课程成绩最高的分数
    ```sql
    SELECT max(grade) FROM SC WHERE Cno = 'C01' GROUP BY Cno;
    ```
4. 查询学生都选修了哪些课程，要求列出课程号
    ```sql
    SELECT Cno FROM SC GROUP BY Cno;
    ```
5. 查询C02号课程的所有学生的平均成绩、最高成绩和最低成绩。
    ```sql
    SELECT AVG(grade),MAX(grade),MIN(grade) FROM SC  WHERE Cno = 'C02' group BY Cno;
    ```
6. 统计每个系的学生人数
    ```sql
    SELECT dept,count(*) as `人数` FROM student GROUP BY dept;
    ```
7. 统计每门课程的修课人数和考试最高分
    ```sql
    SELECT Cno, count(*), max(grade) FROM SC group BY Cno;
    ```
8. 统计每个学生的选课门数，并按选课门数的递增顺序显示结果
    ```sql
    SELECT Sno, count(*) FROM SC GROUP BY Sno ORDER BY count(*);
    ```
9. 统计选修课的学生总数和考试的平均成绩
    ```sql
    SELECT Cno, count(*), avg(grade) FROM SC GROUP BY Cno;
    ```
10. 查询选课门数超过2门的学生的平均成绩和选课门数
    ```sql
    SELECT Sno, count(*), avg(grade) FROM SC GROUP BY Sno having count(*) > 2;
    ```
11. 列出总成绩超过200分的学生，要求列出学号、总成绩
    ```sql
    SELECT Sno,sum(grade) FROM SC GROUP BY Sno HAVING sum(grade) > 200;
    ```
12. 查询选修了C02号课程的学生的姓名和所在系。  
    方法一: 表连接
    ```sql
    SELECT student.Sname, student.dept, SC.Cno
    FROM student join SC ON student.Sno = SC.Sno WHERE Cno = 'C02';
    ```
    方法二: 子表查询
    ```sql
    SELECT Sname,dept FROM student 
    WHERE Sno in (SELECT Sno FROM SC WHERE Cno = 'C02');
    ```
13. 查询成绩80分以上的学生的姓名、课程号和成绩，并按成绩的降序排列结果。
    ```sql
    SELECT S.Sname, SC.Cno, SC.grade
    FROM student AS S JOIN SC ON S.Sno = SC.Sno
    WHERE SC.grade > 80
    ORDER BY SC.grade DESC;
    ```
14. 查询计算机系男生修了‘数据库基础’的学生姓名、性别、成绩  
    方法一:
    ```sql
    SELECT S.Sname, S.sex, SC.grade
    FROM student AS S JOIN SC ON S.Sno = sc.Sno
                      JOIN course ON sc.Cno = course.Cno
    WHERE S.dept = '计算机系' AND S.sex = '男' AND course.Cname = '数据库基础';
    ```
    方法二❤❤❤❤❤:  
    inner join(等值连接)：只返回两个表中联结字段相等的行。
    ```sql
    SELECT Sname, sex, SC.Grade
    FROM student
    inner join SC ON Cno IN (SELECT Cno FROM course WHERE Cname='数据库基础') AND student.Sno=SC.Sno
    WHERE dept='计算机系' AND sex='男';
    ```
15. 查询哪些学生的年龄相同，要求列出年龄相同的学生的姓名和年龄。❤❤❤❤❤
    ```sql
    SELECT S1.Sname, S1.sex
    FROM student AS S1, student AS S2
    WHERE S1.age = S2.age AND S1.Sname <> S2.Sname
    GROUP BY S1.Sname
    ORDER BY S1.age; 
    ```
16. 查询哪些课程没有人选，要求列出课程号和课程名。
    ```sql
    SELECT Cno,Cname
    FROM course
    WHERE Cno NOT in (SELECT Cno 
                      FROM sc
                      GROUP BY Cno);
    ```
17. 查询有考试成绩的所有学生的姓名、修课名称及考试成绩。要求将查询结果放在一张新的永久表(假设新表名为new-sc)中。
    ```sql
    CREATE TABLE new_sc AS           
    SELECT S.Sname, course.Cname, sc.grade 
    FROM student AS S inner JOIN sc ON S.Sno = sc.Sno
                      INNER JOIN course ON course.Cno = sc.Cno
    WHERE grade IS NOT NULL;
    ```
18. 分别查询信息系和计算机系的学生姓名、性别、修课名称、修课成绩  
    Union：对两个结果集进行并集操作，不包括重复行，同时进行默认规则的排序；
    ```sql
    SELECT S.Sname, S.sex, course.Cname, sc.grade
    FROM student AS S inner JOIN sc ON S.Sno = sc.Sno
                      INNER JOIN course ON course.Cno = sc.Cno
    WHERE S.dept = '信息系'
    UNION
    SELECT S.Sname, S.sex, course.Cname, sc.grade
    FROM student AS S inner JOIN sc ON S.Sno = sc.Sno
                      INNER JOIN course ON course.Cno = sc.Cno
    WHERE S.dept = '计算机系';
    ```
19. 删除修课成绩小于50分的学生的修课记录
    ```sql
    DELETE FROM sc
    WHERE grade < 50 or grade IS NULL;
    ```
20. 将所有选修了C01课程的学生的成绩加10分。
    ```sql
    UPDATE sc
    SET grade = grade + 10
    WHERE Cno = 'C01';
    ```
