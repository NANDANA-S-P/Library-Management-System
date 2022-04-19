from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
EVENTTYPE_CHOICES = (
    ('Workshop', "Workshop"),
    ('Seminar', "Seminar"),
    ('Guest Lecture', "Guest Lecture"),
    ('Outreach Programme', "Outreach Programme"),
    ('Certification Course', "Certification Course "),
    ('Sports', "Sports"),
    ('One Credit Course', "One Credit Course"),
    ('NCC', "NCC"),
)
SPONSORORCOLLAB_CHOICES = (
    ('Industry', "Industry"),
    ('Foreign University', "Foreign University"),
    ('Internal', "Internal "),
    ('External', "External"),
    ('NPTEL', "NPTEL"),
    ('Coursera', "Coursera"),
    ('EDX', "EDX"),
    ('Udemy', "Udemy"),
    ('Others', "Others"),
)
ACHIEVE_CHOICES = (
    ('First', "First"),
    ('Second', "Second"),
    ('Third', "Third"),
    ('Participation', "Participation"),
    ('Others', "Others"),
)
LEVEL_CHOICES = (
    ('Zonal', "Zonal"),
    ('District', "District"),
    ('State', "State"),
    ('National', "National"),
    ('International', "International"),
    ('Reginol', "Regional"),
    ('Others', "Others"),
)
SPONSOR_CHOICES = (
    ('External Agency', "External Agency"),
    ('KCT', "KCT"),
    ('Self', "Self"),
    ('Not Applicable', "Not Applicable"),
)
PUBLICATION_CHOICES = (
    ('Published', "Published"),
    ('Presented', "Presented"),
    ('Others', "Others"),
)
COLLABRATION_CHOICES = (
    ('Self', "Self"),
    ('Students', "Students"),
    ('Industry', "Industry"),
    ('Internal', "Internal Faculty Member"),
    ('External', "External Faculty Member"),
)
CATEGORY_CHOICES = (
    ('National', "National"),
    ('International', "International"),
    ('UGC', "UGC"),
    ('Others', "Others"),
)
JOURNAL_TYPE = (
    ('Journal', "Journal"),
    ('Conference', "Conference"),
    ('Symposium', "Symposium"),
)
INDEXING_CHOICES = (
    ('SCOPUS', "Scopus"),
    ('WEB', "Web of Science"),
    ('SCI', "SCI"),
    ('SCIE', "SCIE"),
    ('UGC', "UGC"),
    ('NON-SCOPUS', "Non-Scopus"),
    ('ANNEXURE', "Annexure I"),
)
EXAM_CHOICES = (
    ('NET', "NET"), ('SLET', "SLET"), ('IIT', "IIT"), ('GATE',
                                                       "GATE"), ('GMAT', "GMAT"), ('GRE', "GRE"), ('CAT', "CAT"), ('JAM', "JAM"),
    ('IELET', "IELET"), ('TOEFL', "TOEFL"), ('CIVIL',
                                             "Civil Services"), ('STATE', "State Gov. Exam"),
    ('CENTRAL', "Central Gov. Exam"), ('OTHERS', "Others"),
)
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Cocurricular_and_Extra_curricular_activities(models.Model):
    userdet = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=30, choices=EVENTTYPE_CHOICES)
    Sponsoredorcolloboration = models.CharField(
        max_length=30, choices=SPONSORORCOLLAB_CHOICES)
    event_name = models.CharField(max_length=200)
    achievement = models.CharField(max_length=30, choices=ACHIEVE_CHOICES)
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES)
    organizationorinstitutionname = models.CharField(max_length=200)
    fromdate = models.DateTimeField(default=timezone.now)
    todate = models.DateTimeField(default=timezone.now)
    days = models.IntegerField()
    amountsponsored = models.CharField(max_length=200, choices=SPONSOR_CHOICES)
    externalagency = models.CharField(max_length=200)
    amountreceived = models.IntegerField()
    proof = models.ImageField(upload_to='Cocurricular_and_Extracurricular')


class Conference_and_Paperpresentation(models.Model):
    userdet = models.ForeignKey(User, on_delete=models.CASCADE)
    publicationtype = models.CharField(
        max_length=200, choices=PUBLICATION_CHOICES)
    colloborativeevent = models.CharField(max_length=200, choices=BOOL_CHOICES)
    colloboration = models.CharField(
        max_length=200, choices=COLLABRATION_CHOICES)
    authorname = models.CharField(max_length=200)
    papername = models.CharField(max_length=200)
    guidename = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=200, choices=JOURNAL_TYPE)
    conferencename = models.CharField(max_length=200)
    organizedname = models.CharField(max_length=200)
    fromdate = models.DateTimeField(default=timezone.now)
    todate = models.DateTimeField(default=timezone.now)
    paidstatus = models.CharField(max_length=200, choices=BOOL_CHOICES)
    indexing = models.CharField(max_length=200, choices=INDEXING_CHOICES)
    issnorisbnnumber = models.CharField(max_length=200)
    impactfactor = models.CharField(max_length=200)
    monthofpublication = models.DateTimeField(default=timezone.now)
    yearofpublication = models.DateTimeField(default=timezone.now)
    volume = models.CharField(max_length=200)
    issuenumber = models.CharField(max_length=200)
    pagenumber = models.CharField(max_length=200)
    proof = models.ImageField(upload_to='Conference_and_Paperpresentation')


class Project_Presentation(models.Model):
    userdet = models.ForeignKey(User, on_delete=models.CASCADE)
    guide_name = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    abstract = models.TextField()
    agency_applied = models.CharField(max_length=30)
    project_status = models.CharField(max_length=100)
    outcome = models.TextField()
    domain = models.CharField(max_length=100)
    grantamount = models.IntegerField()
    fromdate = models.DateField(default=timezone.now)
    todate = models.DateField(default=timezone.now)
    proof = models.ImageField(upload_to='Project_Presentation')


class Scholarship(models.Model):
    userdet = models.ForeignKey(User, on_delete=models.CASCADE)
    sponsor_agency = models.CharField(max_length=100)
    scheme_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    year_receipt = models.DateField()
    proof = models.ImageField(upload_to='Scholarship')


class Competitive_Examination(models.Model):
    userdet = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100, choices=EXAM_CHOICES)
    reg_number = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    marks = models.IntegerField()
    qualified = models.CharField(max_length=100, choices=BOOL_CHOICES)
    success_details = models.TextField(max_length=300)
    proof = models.ImageField(upload_to='Competitive_Examination')
