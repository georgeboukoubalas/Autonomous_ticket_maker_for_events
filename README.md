# 🎟️ Automated QR Code Ticket Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-brightgreen?style=for-the-badge)

Welcome to the **Automated QR Code Ticket Generator**! This tool is designed to save you hours of manual work by automatically generating custom event tickets.

In simple terms, this script reads a list of attendee names from an Excel file, converts each name into a unique QR code, and stamps that QR code onto a blank ticket template. Finally, it saves all the completed tickets into a new folder, ready to be printed or emailed!

---

## 📁 1. Preparing Your Files (Step-by-Step)

Before running the program, you need to make sure your files are correctly placed in the project folder. You don't need to be a programmer to set this up—just follow these steps.

### 📄 The Names (Excel File)

1. Create an Excel file and name it exactly **`names.xlsx`**.
2. Write the names of your attendees in the first column (**Column A**).
3. **Important:** Do *not* add a title/header row (e.g., do not write "Names" in the first box). Start typing the first attendee's name directly in Row 1. The program reads names from top to bottom.

### 🎫 The Blank Tickets (Templates)

1. In the same project folder as your Excel file, create a new folder named **`input_tickets`**.
2. Place your blank ticket templates (PNG or JPG images) inside this folder.
3. **Important:** Name your files with simple, consecutive numbers (e.g., `1.png`, `2.png`, `3.png`). The program will place the first name from the Excel file onto `1.png`, the second name onto `2.png`, and so on.

### 📂 How Your Folder Should Look

```text
📦 Your_Project_Folder
 ┣ 📂 input_tickets
 ┃ ┣ 📜 1.png
 ┃ ┣ 📜 2.png
 ┃ ┗ 📜 3.png
 ┣ 📜 names.xlsx
 ┗ 📜 ticketing.py
```

---

## ▶️ 2. Running the Program (Using PyCharm)

PyCharm is the software environment where your code runs. To generate your tickets, follow these simple steps:

1. Open PyCharm on your computer.
2. If your project isn't already open, go to **File → Open...** and select the main folder containing your code.
3. In the left-hand panel, double-click the script file (e.g., `ticketing.py`) to open it.
4. To run the script, choose one of these two methods:

   - **Method A (Easiest):** Right-click anywhere inside the code editor and select **Run 'ticketing'** (or click the green Play triangle in the top-right corner).
   - **Method B (Using Terminal):** At the bottom of the screen, click the **Terminal** tab. Type the following command and press Enter:

     ```bash
     python ticketing.py
     ```

---

## ⚙️ 3. Customizing Your QR Codes

You can easily adjust the QR code size and position to fit your ticket design.

### A. Changing the QR Code Size

If the QR code looks too big or too small on your ticket, find this line in your Python code:

```python
QR_SIZE = 440
```

- **To make it larger:** Increase the number (e.g., `500`).
- **To make it smaller:** Decrease the number (e.g., `300`).

### B. Changing the QR Code Position (X and Y Coordinates)

Computers measure image locations in pixels, starting from the top-left corner.

- **X:** The distance of the QR code from the left side of the ticket.
- **Y:** The distance of the QR code from the top of the ticket.

Find these lines in your Python code:

```python
QR_POSITION_X = 400
QR_POSITION_Y = 1023
```

- **To move it right:** Increase the X value.
- **To move it left:** Decrease the X value.
- **To move it down:** Increase the Y value.
- **To move it up:** Decrease the Y value.

💡 **Pro Tip:** If you don't know the exact pixel values for your ticket design, just experiment! Adjust these three settings, run the program, and check the results in the `output_tickets` folder. Make small adjustments until the QR code sits exactly where you want it.
