from .models import DistilleryImage

def logo_image(request):
    logo = DistilleryImage.objects.filter(image_name='logo').first()
    return {'logo_image': logo}
