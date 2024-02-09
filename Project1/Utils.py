import os
import sys
from dotenv import load_dotenv, find_dotenv
os.environ['OPENAI_API_KEY']  = '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'

class Utils:
  def __init__(self):
    pass
  
  def create_dlai_index_name(self, index_name):
    openai_key = ''
    if self.is_colab(): # google colab
      from google.colab import userdata
      openai_key = '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'
    else: # jupyter notebook
      openai_key = os.getenv("OPENAI_API_KEY")
    return f'{index_name}-{openai_key[-36:].lower().replace("_", "-")}'
    
  def is_colab(self):
    return 'google.colab' in sys.modules

  def get_openai_api_key(self):
    _ = load_dotenv(find_dotenv())
    return os.getenv("OPENAI_API_KEY")
    
  def get_pinecone_api_key(self):
    _ = load_dotenv(find_dotenv())
    return os.getenv("PINECONE_API_KEY")
