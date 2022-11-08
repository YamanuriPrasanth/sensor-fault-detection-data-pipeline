
import os


SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
API_KEY ="HLQAWVIPTIVELNXU" #os.getenv('API_KEY',None)
ENDPOINT_SCHEMA_URL  = "https://psrc-nx65v.us-east-2.aws.confluent.cloud"#os.getenv('ENDPOINT_SCHEMA_URL',None)
API_SECRET_KEY ="LfVBpkLSmEcqOtbxtaMtIF6ZR8RiDb9+IN7pY9Uq8sDxG7v9I62DdBnIJHNIlHhm" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER ="pkc-2396y.us-east-1.aws.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)
#SECURITY_PROTOCOL =os.getenv('SECURITY_PROTOCOL',None)
#SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SCHEMA_REGISTRY_API_KEY = "R47652NKPXNN3ZAQ"#os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET ="NqXgabfldoe9/m3gppUKi4WLtSTv8rUqAxD6+i5+OQ3OTDqQ1UjZS9q7g4/OGwQ/" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

