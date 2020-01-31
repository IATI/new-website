from wagtail.core.blocks import StructValue
from navigation.utils import get_localised_field_value


class ModuleStructValue(StructValue):
    def num_columns(self):
        return len(self.get('columns'))

    def column_container_class(self):
        return 'l-%sup' % str(self.num_columns())

    def column_class(self):
        return 'l-%sup__col' % str(self.num_columns())


class TransStructValue(StructValue):
    def description(self):
        return get_localised_field_value(
            self,
            'description',
            use_get=True,
        )

    def title(self):
        return get_localised_field_value(
            self,
            'title',
            use_get=True,
        )

    def link_label(self):
        return get_localised_field_value(
            self,
            'link_label',
            use_get=True,
        )
