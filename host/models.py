from django.db import models
from users.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
import zipfile

def ValidateFileExtension (fle) : 
    extenstion = str(fle.name).split('.')[-1]
    if extenstion not in ['zip','rar']  : 
        raise ValidationError("invalid file format, only accept zip or rar extensions.")
    
class Host (models.Model) : 
    user = models.ForeignKey(User, related_name='user_host', on_delete=models.CASCADE)
    file = models.FileField(upload_to='hosting-files/', validators=[ValidateFileExtension])
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    
@receiver(post_save, sender=Host)
def unzipped_files (created, instance:Host, **kwargs) : 
    if not created:
        return
    
    # extract files from zipped files and save it
    file_path = instance.file.path
    zp_file = zipfile.ZipFile(file_path, 'r')
    zp_file.extractall(path=f'media/hosting/{instance.user.full_name}/{instance.name}/')
    