from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register('insert_editor_css')
def editor_css():
    """Add custom editor CSS to the admin area."""
    return format_html(
        """
        <style>
            .non-floated-options label {{
                display: block;
                float: none;
                width: 100%;
            }}
        </style>
        """
    )
