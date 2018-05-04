# Control-Plane AutoScalingGroup

This Lambda function control-plane can scale-up or scale-down aws auto scaling group automatically by specific a given schedule.

## Quick Start

### Setup and deploy

Let's deploy this function using Serverless framework.

1st, install serverless framework:

```sh
$ npm install -g serverless
```

Set-up your AWS Provider Credentials

```sh
$ aws configure
```

### Deploy

In order to deploy the function simply run

```sh
$ serverless deploy
```

### Trigger

Simple add or remove cloudwatch schedule event in the serverless.yml with the required parameters: `AsgGroupName`, `MinSize` and `DesiredCapacity`

For example:

```yml
functions:
  scale-asg:
    events:
     - schedule:
          description: 'Scale-Down: Schedule at 7pm GMT+8 Mon-Fri'
          rate: cron(0 11 ? * MON-FRI *)
          enabled: true
          input:
            AsgGroupName: sitapp-AutoScaleGrp-XL7APL96YQPQ
            MinSize: 0
            DesiredCapacity: 0
     - schedule:
          description: 'New event'
          ...
```
