from aws_cdk import core
from serverlessbackend.serverless_backend import ServerlessBackendStack

# This is the main application
if __name__ == "__main__":    
    app = core.App()
    env_us_east_1 = core.Environment(region="us-east-1")
    ServerlessBackendStack(app, "ServerlessBackendStack", env=env_us_east_1)
    app.synth()
