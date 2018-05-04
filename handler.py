import boto3
import logging
import traceback

from botocore.exceptions import ClientError

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

AUTO_SCALING = boto3.client('autoscaling')

def update_autoscalinggroup(event):
    '''Updates the configuration for the specified Auto Scaling group.
    '''
    try:
        response = AUTO_SCALING.update_auto_scaling_group(
            AutoScalingGroupName=event['AsgGroupName'],
            MinSize=event['MinSize'],
            DesiredCapacity=event['DesiredCapacity'],
        )
        logger.info(response)
        return True, ''
    except ClientError as e:
        logger.error(e)
        return False, f"{e}"
    except Exception:
        tracebackString = traceback.format_exc()
        logger.error(tracebackString)
        return False, tracebackString 

def scale(event, context):

    if 'AsgGroupName' not in event or 'MinSize' not in event or 'DesiredCapacity' not in event:
        return {"error": "Scaling parameters is empty!"}
    
    logger.info(event)

    _ok , error = update_autoscalinggroup(event)
    
    if _ok:
        return {"message": "Success"}
    else:
        return {"error": error }
