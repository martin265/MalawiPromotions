from dotenv import load_dotenv

load_dotenv()
import os
from supabase import create_client

# the connection with the database will be here
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

