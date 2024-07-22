def handle_inbound(sender, event, esp_name, **kwargs):
    message = event.message
    print(
        "Received message from {} (envelope sender {}) with subject '{}'".format(
            message.from_email, message.envelope_sender, message.subject
        )
    )
