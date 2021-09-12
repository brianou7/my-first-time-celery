import boto3
from botocore.exceptions import ClientError

# Create a new SES resource and specify a region.
client = boto3.client('ses', region_name='us-east-1')


def send_email(subject, message, recipient_list):
    try:
        response = client.send_email(
            Destination={'ToAddresses': recipient_list},
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': message,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source='Tutorial <communications@sandbox.korcom.co>'
        )

    # Display an error if something goes wrong.
    except ClientError as exception:
        print(exception.response['Error']['Message'])
    else:
        print('Email sent! Message ID:')
        print(response['MessageId'])
