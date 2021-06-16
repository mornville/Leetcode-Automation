# 43. Combine Two Tables
### Difficulty: Easy
SQL Schema <br/> Table: Person <br/> +-------------+---------+ <br/> | Column Name | Type    | <br/> +-------------+---------+ <br/> | PersonId    | int     | <br/> | FirstName   | varchar | <br/> | LastName    | varchar | <br/> +-------------+---------+ <br/> PersonId is the primary key column for this table. <br/> Table: Address <br/> +-------------+---------+ <br/> | Column Name | Type    | <br/> +-------------+---------+ <br/> | AddressId   | int     | <br/> | PersonId    | int     | <br/> | City        | varchar | <br/> | State       | varchar | <br/> +-------------+---------+ <br/> AddressId is the primary key column for this table. <br/>   Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people: <br/> FirstName, LastName, City, State