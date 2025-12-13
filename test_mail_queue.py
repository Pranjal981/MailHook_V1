from queue import MailQueue

email_queue = MailQueue()
email_queue.add("Email Request 1")
email_queue.add("Email Request 2")  
email_queue.add("Email Request 3")

email_queue.process()  # Should process "Email Request 1"



banking_application_queue = MailQueue()
banking_application_queue.add("Email Request 1")
banking_application_queue.add("Email Request 2")  
banking_application_queue.add("Email Request 3")

banking_application_queue.process()  # Should process "Email Request 1"
banking_application_queue.process()  # Should process "Email Request 1"
