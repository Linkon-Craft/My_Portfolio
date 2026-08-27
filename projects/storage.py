from storages.backends.s3 import S3Storage
from django.conf import settings


class SupabaseStorage(S3Storage):

    def url(self, name, parameters=None, expire=None, http_method=None):

        return (
            f"{settings.SUPABASE_URL}"
            f"/storage/v1/object/public/"
            f"{settings.SUPABASE_BUCKET}/"
            f"{name}"
        )