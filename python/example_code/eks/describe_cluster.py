# Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import boto3,sys

# Create EKS client

eks = boto3.client('eks');

for cluster in eks.list_clusters()['clusters']: 
  print cluster

# Describe cluster - hacktoberfest2018
cluster_name='hacktoberfest2018'
cluster_dict = eks.describe_cluster(name=cluster_name)['cluster']

print cluster_dict

