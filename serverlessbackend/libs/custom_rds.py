from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    core,
)

class CustomRDSMysql(rds.CfnDBInstance):
    def __init__(self, scope: core.Construct, id, username, password, db_name, storage_size, subnet_group_name):
        super().__init__(scope=scope, id=id,
                db_instance_identifier='azv-'+db_name.replace('_','-'),
                master_username=username,
                master_user_password=password,
                db_name=db_name,
                engine='MYSQL',
                engine_version='5.7',
                allocated_storage=storage_size,
                port='3306',
                db_subnet_group_name=subnet_group_name,
                db_instance_class= 'db.t2.micro',
                #apply_removal_policy=core.RemovalPolicy.DESTROY,
                deletion_protection=False
            ),