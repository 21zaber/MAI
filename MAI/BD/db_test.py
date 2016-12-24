import sqlite3

db_path = 'test'

db = sqlite3.connect(db_path)

rows = db.execute('SELECT * FROM seats WHERE train_id = 1')

max_id = 0

for r in rows:
    print(r)
    max_id = max(max_id, r[0])

print('Insert new seat')

db.execute('INSERT INTO seats(id, train_id, class_id, booked_by) VALUES ({}, 1, 2, NULL)'.format(max_id + 1))
db.commit()

rows = db.execute('SELECT * FROM seats WHERE train_id = 1')

max_id = 0

for r in rows:
    print(r)
    max_id = max(max_id, r[0])

print('Update seat')
db.execute('UPDATE seats SET booked_by = 1 WHERE id = 3')
db.commit()

rows = db.execute('SELECT * FROM seats WHERE train_id = 1')

max_id = 0

for r in rows:
    print(r)
    max_id = max(max_id, r[0])

print('Revert updating seat')
db.execute('UPDATE seats SET booked_by = NULL WHERE id = 3')
db.commit()

rows = db.execute('SELECT * FROM seats WHERE train_id = 1')

max_id = 0

for r in rows:
    print(r)
    max_id = max(max_id, r[0])

print('Delete inserted seat')

db.execute('DELETE FROM seats WHERE id = {}'.format(max_id))
db.commit()

rows = db.execute('SELECT * FROM seats WHERE train_id = 1')

max_id = 0

for r in rows:
    print(r)
    max_id = max(max_id, r[0])

db.close()
