"""Module for registering admin models for the events app."""

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from events.models import EventPage, EventType, FeaturedEvent


def types(obj):
    return ', '.join([str(x) for x in obj.event_type.all()])


class EventPageAdmin(ModelAdmin):
    model = EventPage
    menu_icon = 'date'
    menu_order = 100
    menu_label = 'Event pages'
    list_display = ('title', 'date_start', 'date_end', 'location', types, )
    search_fields = ('title', 'content_editor', 'location', )


class EventTypeAdmin(ModelAdmin):
    model = EventType
    menu_icon = 'tag'
    menu_order = 110
    menu_label = 'Event types'
    list_display = ('name', 'slug', )
    search_fields = ('name', 'slug', )


class FeaturedEventAdmin(ModelAdmin):
    model = FeaturedEvent
    menu_icon = 'pick'
    menu_order = 120
    menu_label = 'Featured events'
    list_display = ('event', )
    search_fields = ('event', )


class EventsAdminGroup(ModelAdminGroup):
    menu_label = 'Events'
    menu_icon = 'date'
    menu_order = 110
    items = (EventPageAdmin, EventTypeAdmin, FeaturedEventAdmin, )


modeladmin_register(EventsAdminGroup)
