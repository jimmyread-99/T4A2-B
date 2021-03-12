import os                                                           

class Config(object):

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") 
    SECRET_KEY = os.environ.get("SECRET_KEY")                         
    SQLALCHEMY_TRACK_MODIFICATIONS = False                    


    @property
    def SQLALCHEMY_DATABASE_URI(self):                           
        value = os.environ.get("DB_URI")                            
        if not value:
            raise ValueError("DB_URI is not set")  
        return value  


class DevelopmentConfig(Config):                                    
    DEBUG = True                  



class ProductionConfig(Config): 

    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_SECRET_KEY")                    
        if not value:
            raise ValueError("JWT Secret Key is not set")           
        return value        



class TestingConfig(Config):  

    TESTING = True   
                                                   
    @property
    def SQLALCHEMY_DATABASE_URI(self):                          
        value = os.environ.get("DB_URI")               
        if not value:
            raise ValueError("DB_URI is not set")  
        return value    


environment = os.environ.get("FLASK_ENV")                           


if environment == "production":                                 
    app_config = ProductionConfig()                            
elif environment == "testing":                                
    app_config = TestingConfig()                                    
else:
    app_config = DevelopmentConfig()      

