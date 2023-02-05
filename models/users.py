def getUser(db, userID):
    db.get("users", {"id": userID})