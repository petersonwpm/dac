"""
quick start from diagrams
"""
from diagrams import Diagram
from diagrams.aws.compute  import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network  import ELB, CF
from diagrams.aws.storage  import S3, EFS

with Diagram("Web Service", show=True):
    workers = [
        EC2("1-web"),
    ]
    shared   = EFS('wp-content')
    balancer = ELB('lb')
    cdn      = CF('cdn')
    static   = S3('wp-static')
    db       = RDS('wp-tables')

    balancer >> workers >> db
    workers >> static
    workers >> shared
    cdn >> static
