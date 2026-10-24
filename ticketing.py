import os
import pandas as pd
import qrcode
from PIL import Image
import re  # NEW: We need this to extract numbers from filenames


# ==========================================
# --------- CONFIGURATION SETTINGS ---------
# ==========================================


# 1. File and Folder Paths
EXCEL_FILE = "names.xlsx"
TICKETS_FOLDER = "input_tickets"
OUTPUT_FOLDER = "output_tickets"


# 2. QR Code Position (Converted to Pixels)
QR_POSITION_X = 400
QR_POSITION_Y = 1023


# 3. QR Code Size (Converted to Pixels)
QR_SIZE = 440




# ==========================================
# -------------- MAIN SCRIPT ---------------
# ==========================================


def numerical_sort(value):
   """
   Helper function to split filenames into text and numbers.
   This forces Python to sort '2.png' BEFORE '10.png' (Natural Sort).
   """
   parts = re.split(r'(\d+)', value)
   parts[1::2] = map(int, parts[1::2])
   return parts




def main():
   os.makedirs(OUTPUT_FOLDER, exist_ok=True)


   print("Reading Excel file...")
   # header=None ensures the first row is read as data, not a column title
   df = pd.read_excel(EXCEL_FILE, header=None)


   names = df.iloc[:, 0].dropna().tolist()
   print(f"Found {len(names)} names in the Excel file.")


   valid_extensions = ('.png', '.jpg', '.jpeg')
   tickets = [f for f in os.listdir(TICKETS_FOLDER) if f.lower().endswith(valid_extensions)]


   # THE FIX: Sort using our new numerical_sort function instead of alphabetically
   tickets.sort(key=numerical_sort)


   print(f"Found {len(tickets)} ticket images in '{TICKETS_FOLDER}'.")


   if len(names) > len(tickets):
       print("WARNING: You have more names than tickets! The script will stop when it runs out of tickets.")
   elif len(tickets) > len(names):
       print("WARNING: You have more tickets than names! Some tickets will remain blank.")


   print("\nStarting generation process...")


   for index, (name, ticket_filename) in enumerate(zip(names, tickets)):
       # 1. GENERATE THE QR CODE
       qr = qrcode.QRCode(box_size=10, border=1)
       qr.add_data(name)
       qr.make(fit=True)


       qr_img = qr.make_image(fill_color="black", back_color="white")
       qr_img = qr_img.resize((QR_SIZE, QR_SIZE))
       qr_img = qr_img.convert("RGBA")


       # 2. OPEN THE PRE-MADE TICKET
       ticket_path = os.path.join(TICKETS_FOLDER, ticket_filename)
       ticket_img = Image.open(ticket_path).convert("RGBA")


       # 3. PASTE THE QR CODE ON THE TICKET
       ticket_img.paste(qr_img, (QR_POSITION_X, QR_POSITION_Y), qr_img)


       # 4. SAVE THE NEW TICKET
       output_filename = f"ticket_{str(index + 1).zfill(3)}.png"
       output_path = os.path.join(OUTPUT_FOLDER, output_filename)
       ticket_img.save(output_path, format="PNG")


       print(f"Successfully created: {output_filename} (Assigned to: {name})")


   print("\nDone! All your tickets have been created successfully in perfect order.")




if __name__ == "__main__":
   main()
