from django.apps import AppConfig
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class WagtailCloudfrontInvalidateConfig(AppConfig):
    name = 'wagtail_cloudfront_invalidate'
    verbose_name = "Wagtail Cloudfront Invalidate"

    AWS_ACCESS_KEY_ID = getattr(settings, 'AWS_ACCESS_KEY_ID', None)
    AWS_SECRET_ACCESS_KEY = getattr(settings, 'AWS_SECRET_ACCESS_KEY', None)
    CLOUDFRONT_DISTRIBUTION_ID = getattr(settings, 'CLOUDFRONT_DISTRIBUTION_ID', None)

    @property
    def enabled(self):
        if getattr(settings, 'WAGTAIL_CLOUDFRONT_INVALIDATE_ENABLED', False) is False:
            return False

        return self.has_required_settings

    @property
    def has_required_settings(self):

        for attr in ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'CLOUDFRONT_DISTRIBUTION_ID']:
            if getattr(self, attr) is None:
                logger.info('Please set a value for %s' % attr)
                return False

        return True
