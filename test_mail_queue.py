"""
Simple Gmail SMTP Client
Requires:
- Gmail 2FA enabled
- Gmail App Password
- .env file or environment variables:
    GMAIL_USER
    GMAIL_APP_PASSWORD
"""

import os
import smtplib
import logging
from email.message import EmailMessage
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger("smtp_client")


@dataclass
class SMTPConfig:
    host: str = "smtp.gmail.com"
    port: int = 587
    username: Optional[str] = os.getenv("GMAIL_USER")
    password: Optional[str] = os.getenv("GMAIL_PASSWORD")


class GmailSMTPClient:
    def __init__(self, config: SMTPConfig):
        if not config.username or not config.password:
            raise ValueError("GMAIL_USER and GMAIL_APP_PASSWORD must be set")

        self.config = config
        self.server: Optional[smtplib.SMTP] = None

    def connect(self) -> None:
        logger.info("Connecting to Gmail SMTP...")
        self.server = smtplib.SMTP(self.config.host, self.config.port, timeout=30)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.config.username, self.config.password)
        logger.info("Logged in as %s", self.config.username)

    def send_email(
        self,
        from_addr: str,
        to_addr: str,
        subject: str,
        body: str,
    ) -> None:
        if not self.server:
            raise RuntimeError("SMTP server not connected")

        msg = EmailMessage()
        msg["From"] = from_addr
        msg["To"] = to_addr
        msg["Subject"] = subject
        msg.set_content(body)

        self.server.send_message(msg)
        logger.info("Email sent to %s", to_addr)

    def disconnect(self) -> None:
        if self.server:
            self.server.quit()
            self.server = None
            logger.info("SMTP connection closed")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.disconnect()


# ------------------ USAGE ------------------
if __name__ == "__main__":
    client = GmailSMTPClient(SMTPConfig())

    with client:
        client.send_email(
            from_addr="YOUR_EMAIL",
            to_addr="pranjal_shinde_comp@moderncoe.edu.in",
            subject="Test Email",
            body="This email was sent using a clean SMTP client."
        )
