import os


from dotenv import load_dotenv #type: ignore
load_dotenv()
print(os.environ, sep='\n')
print(os.environ['NOME'])
print(os.getenv('NOME'))