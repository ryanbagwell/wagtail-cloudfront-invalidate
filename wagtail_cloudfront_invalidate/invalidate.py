import boto3
import time
import logging

logger = logging.getLogger(__name__)


def invalidate(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, CLOUDFRONT_DISTRIBUTION_ID, paths=[]):

    client = boto3.client(
        'cloudfront',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    client.create_invalidation(
        DistributionId=CLOUDFRONT_DISTRIBUTION_ID,
        InvalidationBatch={
            'Paths': {
                'Quantity': len(paths),
                'Items': paths,
            },
            'CallerReference': 'wagtail-invalidate-%s' % time.time()
        }
    )

    logger.info('Created cloudfront invalidation for %s' % paths)

