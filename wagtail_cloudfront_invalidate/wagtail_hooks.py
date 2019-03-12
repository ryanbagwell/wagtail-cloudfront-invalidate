from wagtail.core import hooks
from django.apps import apps
from botocore.exceptions import ParamValidationError
import boto3
from wagtail.admin import messages
from django.utils.translation import ugettext as _
import time


@hooks.register('after_edit_page')
def my_hook_function(request, page):

    conf = apps.get_app_config('wagtail_cloudfront_invalidate')

    if not conf.enabled:
        return

    client = boto3.client(
        'cloudfront',
        aws_access_key_id=conf.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=conf.AWS_SECRET_ACCESS_KEY
    )

    try:
        client.create_invalidation(
            DistributionId=conf.CLOUDFRONT_DISTRIBUTION_ID,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [
                        page.get_url(),
                    ]
                },
                'CallerReference': 'wagtail-invalidate-%s' % time.time()
            }
        )
    except ParamValidationError:
        messages.warning(
            request,
            _('Cloudfront Invalidation Error. Check that your AWS access key, secret key and Cloudfront distribution ID are set.')
        )
    except Exception as e:
        messages.warning(
            request,
            e.__str__()
        )

