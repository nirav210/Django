from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
from django.forms.fields import DateField

class Profile(models.Model):
    
    SENIOR = 'Senior Web Developer'
    JUNIOR = 'Junior Web Developer'
    DESIGNER = 'Designer'
    TESTER = 'Tester'
    
    DESIGNATION = (
    (SENIOR,'Senior Web Developer'),
    (JUNIOR,'Junior Web Developer'),
    (DESIGNER,'Designer'),
    (TESTER,'Tester'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=125)
    # email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=30, default=JUNIOR, choices=DESIGNATION)
    salary = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    account_number = models.IntegerField()

    def __str__(self):
        return self.user.username

class Holiday(models.Model):

    name = models.CharField(max_length=125)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.name
    
    def totaldays(self):	
        fromdate = self.from_date
        todate = self.to_date
        
        dates = todate - fromdate
        return dates.days

class Leave(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(verbose_name= ('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)

    status = models.CharField(max_length=12,default='pending')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    @property
    def leavedays(self):	
        fromdate = self.from_date
        todate = self.to_date
        
        dates = todate - fromdate
        return dates.days

    @property
    def leave_approved(self):
        return self.is_approved == True

    @property
    def approve_leave(self):
        if not self.is_approved:
            self.is_approved = True
            self.status = 'approved'
            self.save()

    @property
    def unapprove_leave(self):
        if self.is_approved:
            self.is_approved = False
            self.status = 'pending'
            self.save()

    @property
    def reject_leave(self):
        if self.is_approved or not self.is_approved:
            self.is_approved = False
            self.status = 'rejected'
            self.save()



    @property
    def is_rejected(self):
        return self.status == 'rejected'