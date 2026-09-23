class Solution:
    def generate_id(self):
        return "EpMmJwf3x3G45PxJ+gVxogwKr3XOSWeqUSJzEsboBzA="

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.generate_id()
        encoded_str = ""
        for i, word in enumerate(strs):
            if i != 0:
                encoded_str = encoded_str + "encoded" + word
            else:
                encoded_str = encoded_str + word
        return encoded_str


    def decode(self, s: str) -> List[str]:
        if s == self.generate_id():
            return []
        decoded_str = s.split("encoded")
        return decoded_str
        

