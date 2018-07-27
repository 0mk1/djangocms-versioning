from cms.app_base import CMSAppConfig

from djangocms_versioning.versionable import Versionable

from .models import BlogPost, BlogContent, Comment


class BlogpostCMSConfig(CMSAppConfig):
    djangocms_versioning_enabled = True
    versioning = [
        Versionable(
            grouper=BlogPost,
            content=BlogContent,
        ),
        Versionable(
            grouper=BlogPost,
            content=Comment,
        ),
    ]
