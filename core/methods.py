from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_notification(notification_type, content):
    channel = get_channel_layer()
    async_to_sync(channel.group_send)(
        'notification',
        {
            'type': 'send_notification',
            'message': {'type': notification_type, 'content': content}
        })
