class UserAddService:
    def __init__(self, data: data):
       self.data = data

       self.first_name = data["first_name"]
       self.last_name = data["last_name"]
       self.username = self._generate_username()
    
    def _generate_username(self):
        return f"{self.first_name.lower()}_{self.last_name.lower()}"

    def _save_to_redis(self):
        redis_client.set(self.username, json.dumps(self.data))
        redis_client.expire(self.username, 60 * 60 * 24 * 7)
        return self.username
    
    def _save_to_qdrant(self):
        vector = model.encode(self.data["text"]).tolist()
        point = PointStruct(id=self.username, vector=vector, payload=self.data)
        qdrant_client.upsert(collection_name="users", points=[point])
        return self.username

    def add(self):
        self._save_to_redis()
        self._save_to_qdrant()
        return {"message": "User added successfully"}
