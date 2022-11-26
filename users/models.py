from email.policy import default
from django.db import models

# Create your models here.
URGENCY = (
    ('LOW', 'LOW'),
    ('MED', 'MED'),
    ('HIGH', 'HIGH')
)

STATUS = (
    ('Resolved', 'Resolved'),
    ('Assigned', 'Assigned'),
    ('Open', 'Open'),
)

class UserQuery(models.Model):
    userID = models.PositiveSmallIntegerField("User ID")
    timestamp = models.DateTimeField("Timestamp (UTC)", auto_now_add=True)
    messageBody = models.TextField("Message Body")
    urgency_status = models.CharField(max_length=20)
    resolved = models.CharField(max_length=255, choices=STATUS, default='Open')

    def get_urgency_status(self, query):
        message = self.messageBody.lower()
        keywords = ['loan', 'approval', 'process', 'disburse', 'when', 'why', 'reject', 'application', 'late', 'expunge', 'approve', 'can', '?', '']
        status = set(keywords).intersection(message.split())
        count = 0
        for word in status:
            count += message.split().count(word)

        count = len(set(keywords).intersection(message.split()))
        if count>2:
            return 'HIGH'
        elif count>1:
            return 'MEDIUM'
        return 'LOW'

    def save(self, *args, **kwargs):
        self.urgency_status = self.get_urgency_status(self.messageBody)
        super(UserQuery, self).save(*args, **kwargs)
        

class AgentResponse(models.Model):
    agent_name = models.CharField(max_length=255)
    userID = models.PositiveSmallIntegerField("User ID")
    queries_handled = models.JSONField(default=list)
    query_response = models.TextField()