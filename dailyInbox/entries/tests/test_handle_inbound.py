from unittest.mock import Mock, patch

from dailyInbox.entries.recivers import handle_inbound


def test_handle_inbound():
    # Mock the event and message
    mock_message = Mock()
    mock_message.from_email = "test@example.com"
    mock_message.envelope_sender = "envelope@example.com"
    mock_message.subject = "Test Subject"

    mock_event = Mock()
    mock_event.message = mock_message

    # Mock the sender and esp_name
    sender = "test_sender"
    esp_name = "test_esp"

    # Patch the print function to verify its output
    with patch('builtins.print') as mock_print:
        handle_inbound(sender, mock_event, esp_name)
        mock_print.assert_called_once_with(
            "Received message from %s (envelope sender %s) with subject '%s'" % (
                mock_message.from_email, mock_message.envelope_sender, mock_message.subject)
        )
