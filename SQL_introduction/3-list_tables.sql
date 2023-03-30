-- a script that lists all the table of a database in your MySQL server.
# Check if database name is provided as argument
if [ $# -eq 0 ]
  then
    echo "Please provide the database name as argument."
    exit 1
fi

# Store database name in a variable
DB_NAME=$1

# Execute MySQL command to list tables
mysql -e "USE ${DB_NAME}; SHOW TABLES;"
