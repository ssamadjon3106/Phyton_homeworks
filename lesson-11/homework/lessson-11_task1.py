import sqlite3

sql = """
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT, 
    Species TEXT, 
    Age INT
);

-- Insert initial data
INSERT INTO Roster (Name, Species, Age) VALUES 
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300), 
('Kira Nerys', 'Bajoran', 29);
"""

delete = """
DELETE FROM Roster 
WHERE Age > 100;
"""

with sqlite3.connect('roster.db') as f:
    cursor = f.cursor()

    # Create table and insert data
    cursor.executescript(sql)

    # Rename Jadzia Dax to Ezri Dax
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

    # Add new column Rank (if not already exists)
    try:
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    except sqlite3.OperationalError:
        print("Column 'Rank' already exists.")

    # Set Rank for Benjamin Sisko
    cursor.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
    cursor.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
    cursor.execute("UPDATE Roster SET Rank = '	Major' WHERE Name = 'Kira Nerys'")


    # Select all Bajorans
    cursor.execute("SELECT * FROM Roster WHERE Species = 'Bajoran'")
    for row in cursor.fetchall():
        print(row)

    # Delete old characters (Age > 100)
    cursor.execute(delete)
    query='Select * from Students order by age desc'
    cursor.execute(query)

