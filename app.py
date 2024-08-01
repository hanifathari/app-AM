from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Ganti dengan kredensial email Anda
EMAIL_ADDRESS = 'haulisyahran@gmail.com'
EMAIL_PASSWORD = 'fnfhotqzkajppshe'

# Fungsi untuk mengirim email
def kirim_email(subjek, isi, ke_email):
    msg = MIMEMultipart()
    msg['Subject'] = subjek
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(ke_email)

    msg.attach(MIMEText(isi, 'plain'))

    try:
        print("Mencoba menghubungkan ke server SMTP...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            print("Login...")
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("Mengirim email...")
            server.sendmail(EMAIL_ADDRESS, ke_email, msg.as_string())
        print("Email berhasil dikirim!")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Ambil data dari form
    data = request.form.to_dict()

    # Format data menjadi string
    isi = "\n".join(f"{key}: {value}" for key, value in data.items())

    # Daftar email tujuan
    ke_email = ['bseno8665@gmail.com', 'atharihanif@gmail.com']

    # Kirim email
    kirim_email('Pengiriman Formulir', isi, ke_email)

    return render_template('sukses.html')

if __name__ == '__main__':
    # Pastikan secret key diatur untuk keamanan
    app.secret_key = os.urandom(24)
    app.run(debug=True)
