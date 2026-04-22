import boto3
def lambda_handler(event, context):
    # Initialize a session using Lambda's built-in role credentials
    session = boto3.Session()
    
    # Create an EC2 client
    ec2_client = session.client('ec2')
    
    # Specify the instance id and volume id
    instance_id = ‘instance id'
    volume_id = event['detail']['volume-id']    
    # Detach the volume
    try:
        response = ec2_client.detach_volume(
            InstanceId=instance_id,
            VolumeId=volume_id,
            Force=False  # Set to True if you want to force detach
        )
        print(f"Volume {volume_id} successfully detached from instance {instance_id}")
    except Exception as e:
        print(f"Error detaching volume {volume_id} from instance {instance_id}: {str(e)}")
