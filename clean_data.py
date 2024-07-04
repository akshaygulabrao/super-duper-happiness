import json
import pandas as pd
from openai import OpenAI

instructions = "Clean the data, and return a json of players with their youngest age_bracket,phone number, email, and skill level. Do not use formatting. If the league is doubles and they mention a partner in the comments. Add the partner name to the entry. "
def get_player_data(player_data,sheet_name):
    with open('keys.json') as f:
        keys = json.load(f)
        openai_api_key = keys['chatgpt']

    client = OpenAI(
        api_key=openai_api_key
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": '\n'.join([','.join(i) for i in player_data[sheet_name]])}
    ]
    )
    json_string = ''.join(completion.choices[0].message.content)
    clean_data = json.loads(json_string)
    return clean_data