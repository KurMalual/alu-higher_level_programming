-- Lists all rows of a table
-- List all rows of the table first_table from the database hbtn_0c_0

# Set database name as a variable
DB_NAME="$1"

# Use MySQL command to insert new row into first_table
mysql -u root -p "$DB_NAME" <<EOF
INSERT INTO first_table (id, name)
VALUES (89, 'Best School');
EOF
