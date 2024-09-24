import aws_cdk as core
import aws_cdk.assertions as assertions

from stepfunctions.stepfunctions_stack import StepfunctionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in stepfunctions/stepfunctions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StepfunctionsStack(app, "stepfunctions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
