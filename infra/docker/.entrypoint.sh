#!/bin/bash

# Start SQL Server in the background
/opt/mssql/bin/sqlservr &

# Wait for SQL Server to start up
sleep 30

# Run the SQL script
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Teste!1234 -d master -i /create_table_mssql.sql

# Wait indefinitely to keep the container running
wait