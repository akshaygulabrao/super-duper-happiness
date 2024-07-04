import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheet_data():
# Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive.readonly"]

    # Add your credentials file
    creds = ServiceAccountCredentials.from_json_keyfile_name("skilful-bliss-408706-da85e88daea8.json", scope)

    # Authorize the client
    client = gspread.authorize(creds)

    # Open the spreadsheet by ID
    spreadsheet_id = '1tQSaowLIy038O4Px2K4lkxcX6fCdcOpsiJ4vkUwLf_A'
    spreadsheet = client.open_by_key(spreadsheet_id)

    # Get all worksheets
    worksheets = spreadsheet.worksheets()

    data = {}

    for sheet in worksheets:
        # Get all values in the sheet
        all_values = sheet.get_all_values()
        data[sheet.title] = all_values
    return data