class Codec:
    def __init__(self):
        self.lookup = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = "http://tinyurl.com/" + str(hash(longUrl))
        while shortUrl in self.lookup:
            shortUrl += "a"
        self.lookup[shortUrl] = longUrl 
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.lookup[shortUrl]