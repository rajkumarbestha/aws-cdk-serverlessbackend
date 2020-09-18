from aws_cdk import (
    core, 
    aws_events_targets as targets, 
    aws_events as events
)
from libs.custom_apigateway import CustomAPIGateway
from libs.custom_lambda import CustomLambda
from libs.custom_rds import CustomRDSMysql
from libs.custom_s3 import CustomS3


## This is a class to retrieve parameter values from configuration file
class Parameters:
    param_file = 'serverlessbackend\config.properties'

    @staticmethod
    def get_parameters():
        params = dict(line.strip().split('=') for line in open(Parameters.param_file) if not line.strip().startswith('#') and line.strip() != "")
        return params


## This is the main class used to generate the CloudFormation templates
class ServerlessBackendStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Get parameters to build the objects
        parameters = Parameters.get_parameters()

        # Create S3 Bucket
        bucket_name = parameters['BucketName']
        CustomS3(self, id=bucket_name, bucket_name=bucket_name)

        # Create Lambda Function
        lambda_name = parameters['LambdaName']
        memory_size = int(parameters['LambdaMemorySize'])
        lambda_function = CustomLambda(self, id=lambda_name, function_name=lambda_name, handler='index.handler', memory_size=memory_size)

        # Create Cloudwatch event
        rule = events.Rule(
            self, lambda_name+"_event_trigger",
            schedule=events.Schedule.cron(
                minute='0',
                hour='15',
                month='*',
                week_day='MON',
                year='*'),
        )

        # Add Cloudwatch event trigger to lambda
        rule.add_target(targets.LambdaFunction(lambda_function))

        # Create an APIGateway and attach to Lambda
        apigateway_name = parameters['ApiGatewayName']
        CustomAPIGateway(self, id=apigateway_name, lambda_function=lambda_function)

        # Create RDS Mysql DB
        db_name = parameters['DBName']
        user = parameters['MasterUser']
        password = parameters['MasterPassword']
        db_size = parameters['DBSize']
        subnet_group_name = parameters['SubnetGroup']
        CustomRDSMysql(self, id=db_name, username=user, password=password, db_name=db_name, storage_size=db_size, subnet_group_name=subnet_group_name)
