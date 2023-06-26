from django.db import models

class NamedModelAbstractBase(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class MultimediaAsset(models.Model):
    name = models.CharField(max_length=255)
    upload = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class VideosAndPodcasts(models.Model):
	htmlblock=models.TextField(null=True,blank=True)
	parent_response=models.ForeignKey(Response,null=False,on_delete=models.CASCADE)

class ProjectScope(NamedModelAbstractBase):
	pass

class ProjectWebsites(models.Model):
	link_text=models.CharField(max_length=50,null=True,blank=True)
	url=models.URLField(max_length=250,null=False,blank=False)
	parent_response=models.ForeignKey(Response,null=False,on_delete=models.CASCADE)

class ProjectMultimediaImages(MultimediaAsset):
	parent_response=models.ForeignKey(Response,null=False,on_delete=models.CASCADE)


class ProjectMultimediaOther(MultimediaAsset):
	parent_response=models.ForeignKey(Response,null=False,on_delete=models.CASCADE)

class ImageOfYourWork(MultimediaAsset):
	parent_response=models.ForeignKey(Response,null=False,on_delete=models.CASCADE)

# DSpace Collections
class Response(models.Model):
	uid=models.CharField(max_length=50,null=False,blank=False,unique=True)
	page_title=models.CharField(max_length=250,null=True,blank=True)
	project_title=models.CharField(max_length=250,null=False,blank=False)
	project_additional_info=models.TextField(null=True,blank=True)
	
	def __str__(self):
		return self.project_title