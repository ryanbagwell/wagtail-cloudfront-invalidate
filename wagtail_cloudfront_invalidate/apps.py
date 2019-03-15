from django.apps import AppConfig
from django.conf import settings
from wagtail_cloudfront_invalidate.invalidate import invalidate
from . import wci_logger


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
                wci_logger.info('Please set a value for %s' % attr)
                return False

        return True

    def ready(self):

        if self.enabled:
            try:

                invalidate(
                    self.AWS_ACCESS_KEY_ID,
                    self.AWS_SECRET_ACCESS_KEY,
                    self.CLOUDFRONT_DISTRIBUTION_ID,
                    paths=['/*'],
                )

            except Exception as err:
                wci_logger.info(err.__str__())

        else:
            wci_logger.info('Cloudfront invalidate not enabled')
