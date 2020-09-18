
from aws_cdk import (
    aws_apigateway,
    core
)


class CustomAPIGateway(aws_apigateway.RestApi):
    def __init__(self, scope: core.Construct, id, lambda_function):
        super().__init__(scope = scope, id=id, rest_api_name=id) 

        # Common API Gateway options
        integration_responses = [
            {
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,X-Amz-User-Agent'",
                    'method.response.header.Access-Control-Allow-Origin': "'*'",
                    'method.response.header.Access-Control-Allow-Credentials': "'false'",
                    'method.response.header.Access-Control-Allow-Methods': "'OPTIONS,GET,PUT,POST,DELETE'",
                }
            }
        ]
        method_responses=[{
            'statusCode': '200',
            'responseParameters': {
                'method.response.header.Access-Control-Allow-Headers': True,
                'method.response.header.Access-Control-Allow-Methods': True,
                'method.response.header.Access-Control-Allow-Credentials': True,
                'method.response.header.Access-Control-Allow-Origin': True,
            },  
        }]
        request_templates={
            "application/json": "{\"statusCode\": 200}"
        }

        # API Gateway Resource
        api_gw = self.root.add_resource('test')
        integration_lambda = aws_apigateway.LambdaIntegration(lambda_function, proxy=False, integration_responses=integration_responses, passthrough_behavior=aws_apigateway.PassthroughBehavior.NEVER, request_templates=request_templates)
        api_gw.add_method('GET', integration_lambda, method_responses=method_responses)
        self.add_cors_options(api_gw)

    def add_cors_options(self, apigw_resource):
        apigw_resource.add_method('OPTIONS', aws_apigateway.MockIntegration(
            integration_responses=[{
                'statusCode': '200',
                'responseParameters': {
                    'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                    'method.response.header.Access-Control-Allow-Origin': "'*'",
                    'method.response.header.Access-Control-Allow-Methods': "'GET,OPTIONS'"
                }
            }
            ],
            passthrough_behavior=aws_apigateway.PassthroughBehavior.WHEN_NO_MATCH,
            request_templates={"application/json":"{\"statusCode\":200}"}
        ),
        method_responses=[{
            'statusCode': '200',
            'responseParameters': {
                'method.response.header.Access-Control-Allow-Headers': True,
                'method.response.header.Access-Control-Allow-Methods': True,
                'method.response.header.Access-Control-Allow-Origin': True,
                }
            }
        ],
    )
        