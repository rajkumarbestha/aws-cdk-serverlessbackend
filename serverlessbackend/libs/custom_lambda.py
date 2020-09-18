
from aws_cdk import (
    aws_lambda,
    core
)

class CustomLambda(aws_lambda.Function):
    def __init__(self, scope: core.Construct, id, handler, function_name, memory_size):
        super().__init__(scope=scope, id=id, 
                code=aws_lambda.InlineCode(open('serverlessbackend\libs\dummy_lambda\lambda_handler.py', encoding="utf-8").read()),
                handler=handler, 
                runtime=aws_lambda.Runtime.PYTHON_3_7, 
                function_name=function_name, 
                memory_size=memory_size)
        