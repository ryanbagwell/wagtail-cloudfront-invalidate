from wagtail.core import hooks
from django.apps import apps
from botocore.exceptions import ParamValidationError
from wagtail.admin import messages
from django.utils.translation import ugettext as _
from wagtail_cloudfront_invalidate import invalidate


@hooks.register('after_edit_page')
def my_hook_function(request, page):

    conf = apps.get_app_config('wagtail_cloudfront_invalidate')

    if not conf.enabled:
        return

    try:

        invalidate(
            conf.AWS_ACCESS_KEY_ID,
            conf.AWS_SECRET_ACCESS_KEY,
            conf.CLOUDFRONT_DISTRIBUTION_ID,
            items=[
                page.get_url(),
            ]
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

