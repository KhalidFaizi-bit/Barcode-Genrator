# QR & Barcode Generator

A simple web-based **QR Code and Barcode Generator** built with Python, Flask, HTML, and CSS.

Users can enter text or a URL, choose between a QR code or a Code 128 barcode, and generate an image directly in the browser. The generated code can also be printed.

## URL
https://faizi-barcode-genrator.onrender.com/

## Features

* Generate **QR Codes**
* Generate **Code 128 Barcodes**
* Enter text or URLs
* Simple and clean web interface
* Uses Flask to handle form submissions
* Generated images are saved in the `static` folder
* Print the generated QR code or barcode
* Responsive viewport setup
* Separate styling with CSS

## Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **qrcode**
* **python-barcode**
* **Jinja2** templates

## Project Structure

```text
BarcodeProject/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── Style.css
    └── generated_code.png
```

> `generated_code.png` is created when a QR code or barcode is generated.

## How It Works

The user enters information into the form and selects either **QR Code** or **Barcode (Code 128)**.

The form sends the information to the Flask server using a `POST` request. Flask reads the submitted `data` and `codeType` values and generates the requested image.

The Python application uses the `qrcode` library for QR codes and `python-barcode` with `Code128` and `ImageWriter` for barcodes.

The generated image is then passed back to the HTML template using the `image_url` variable and displayed on the webpage.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install the required packages

```bash
pip install flask qrcode python-barcode pillow
```

### 5. Run the application

```bash
python app.py
```

Flask will start the development server.

Open the local address shown in your terminal, typically:

```text
http://127.0.0.1:5000/
```

## Usage

1. Open the application in your browser.
2. Enter text or a URL.
3. Select:

   * **QR Code**, or
   * **Barcode (Code 128)**
4. Click **Generate**.
5. The generated code will appear on the page.
6. Click **Print Code** if you want to print it.

## Printing

The project includes a print-specific CSS section. Elements with the `no-print` class are hidden when the page is printed, while the generated code remains available for printing.

The application also removes the card's shadow and unnecessary borders when printing for a cleaner result.

## Flask Backend

The Flask application accepts both `GET` and `POST` requests on the home route:

```python
@app.route('/', methods=['GET', 'POST'])
```

When a form is submitted, Flask retrieves the user's data with:

```python
user_data = request.form.get('data')
code_type = request.form.get('codeType')
```

It then determines whether to generate a QR code or Code 128 barcode.

## Future Improvements

Possible improvements for future versions:

* Add download buttons for generated codes
* Allow users to customize QR code colors
* Add barcode size controls
* Add error handling for invalid input
* Allow users to choose the output filename
* Add more barcode formats
* Improve mobile styling
* Add a history of previously generated codes

## License

This project is for educational and personal use.

## Author

**Khalid Faizi**
