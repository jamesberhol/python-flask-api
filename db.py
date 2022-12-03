def get_user(val):
   for i in open("db/db.db", "r").read().splitlines():
    if i == val:
        return "ok"
   return "err"

def test(v):
    u = int(v) * 10
    s = str(u)
    return s