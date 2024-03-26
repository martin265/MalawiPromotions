from config.config import supabase


class Events:
    def __init__(self):
        super().__init__()

    def fetch_events_record(self):
        try:
            data, count = supabase.table("Artists").select("*").execute()
        except Exception as ex:
            print("something wrong at {}".format(ex))


