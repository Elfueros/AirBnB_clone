# **AirBnB clone**

## **Description**
This project is the first of many projects with a common ultimate objective.
It is the creation of a clone of the AirBnB website.
This project will specifically focus on the creation of:
1. The basic Class of objects of the application
2. The building of serialization and deserialization processes
3. The creation of a command interpreter to manipulate those objects

## **The command interpreter**
It has been created with the cmd module of python.
It allows some basic operation on the objects and files of the application

###	**How to start it**
####	1. Installation
Clone this repository with : `git clone https://github.com/ofperez-TheOwl/AirBnB_clone.git`

####	2. Interactive mode
Launch the interpreter by moving to the repository and launch it with :
`cd AirBnB_clone`
`./console.py`

####	3. Non interactive mode
Launch the interpreter by piping the command to it with :
`echo "<command>" | ./console.py`

###	**How to use it**

|**Commands**	|	**Usage**	|	**Function**			|
|---------------|-----------------------|---------------------------------------|
|help		|`help` / `help <cmd>`	|displays all cmd or help for given cmd	|
|create		|`create <classname>`	|creates a newobject of given class	|
|update		|`update <classname> <id> 									<attribute> <value>` 	|updates objects 			|
|show		|`show <classname> <id>`|prints the object's str representation	|
|destroy	|`destroy <classname> <id>`|destroys the specified object	|
|all		|`all <classname>`	|prints all object's str representation	|
|count		|`<classname>.count()`	|returns number of object of given class|
|quit		|`quit`			|exits					|

####	**Environment**
- Language : Python3.8
- OS : Ubuntu 20.04 LTS
- Style guidelines : pycodestyle 2.8
####	**Author**
***Perez OF***
