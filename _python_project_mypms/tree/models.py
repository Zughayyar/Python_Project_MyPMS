from django.db import models
from admin_mypms.models import Project

class Tree(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, related_name="prj_tree")
    element = models.CharField(max_length=255)
    sub_element = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    check_list = models.BooleanField(default=False)
