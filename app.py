import os
from flask import Flask, render_template, request
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)

# We added 'POST' so the server is allowed to receive data from your form
@app.route('/', methods=['GET', 'POST'])
def home():
    # By default, there is no image to show
    image_url = None

    # If the user clicked the "Generate" button, the method becomes POST
    if request.method == 'POST':
        # Grab the text and dropdown choice using the 'name' attributes from HTML
        user_data = request.form.get('data')
        code_type = request.form.get('codeType')

        # Define where to save the generated image
        save_path = os.path.join('static', 'generated_code')

        if code_type == 'qr':
            # Create a QR code
            img = qrcode.make(user_data)
            img.save(save_path + '.png')
            image_url = '/static/generated_code.png'

        elif code_type == 'barcode':
            # Create a standard barcode
            # The ImageWriter() tells it to save as a .png image
            my_barcode = Code128(user_data, writer=ImageWriter())
            my_barcode.save(save_path) # python-barcode adds '.png' automatically
            image_url = '/static/generated_code.png'

    # Send the final HTML back to the browser, including the image_url if one was made
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)