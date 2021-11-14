import uuid


class ImageUploadHelper:
    FILED_TO_COMBINE_MAP = {
        'defaults': {
            'upload_postfix': 'uploads',
        },
        'Product': {
            'upload_postfix': 'products_images',
            'auxiliary_field': 'title',
            'field': 'id'
        }
    }

    def __init__(self, field_name_to_combine, auxiliary_field, instance, filename, upload_postfix):
        self.field_name_to_combine = field_name_to_combine
        self.auxiliary_field = auxiliary_field
        self.instance = instance
        self.extension = filename.split('.')[-1]
        self.upload_postfix = f'{upload_postfix}'

    @classmethod
    def get_field_to_combine_and_upload_postfix(cls, klass):
        field_to_combine = cls.FILED_TO_COMBINE_MAP[klass]['field']
        auxiliary_field = cls.FILED_TO_COMBINE_MAP[klass]['auxiliary_field']
        upload_postfix = cls.FILED_TO_COMBINE_MAP[klass].get(
            'upload_postfix', cls.FILED_TO_COMBINE_MAP['defaults']['upload_postfix'])
        return field_to_combine, auxiliary_field, upload_postfix

    @property
    def path(self):
        if self.field_name_to_combine == 'id':
            field_to_combine = f'{uuid.uuid4()}-{getattr(self.instance, self.auxiliary_field)}'
        else:
            field_to_combine = getattr(
                self.instance, self.field_name_to_combine)
        filename = '.'.join([field_to_combine, self.extension])
        return f'images/{self.upload_postfix}/{field_to_combine}/{filename}'


def upload_function(instance, filename):
    if hasattr(instance, 'content_object'):
        instance = instance.content_object
    field_to_combine, auxiliary_field, upload_postfix = ImageUploadHelper.get_field_to_combine_and_upload_postfix(
        instance.__class__.__name__)
    image = ImageUploadHelper(
        field_to_combine, auxiliary_field, instance, filename, upload_postfix)
    return image.path
