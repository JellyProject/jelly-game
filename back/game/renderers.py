from core.renderers import JellyGameJSONRenderer


class GameJSONRenderer(JellyGameJSONRenderer):
    object_label = 'game'


class PlayerJSONRenderer(JellyGameJSONRenderer):
    object_label = 'player'


class BuildingJSONRenderer(JellyGameJSONRenderer):
    object_label = 'building'


class EventJSONRenderer(JellyGameJSONRenderer):
    object_label = 'event'


class TechnologyJSONRenderer(JellyGameJSONRenderer):
    object_label = 'technology'


class SourceBuildingJSONRenderer(JellyGameJSONRenderer):
    object_label = 'source building'


class SourceEventJSONRenderer(JellyGameJSONRenderer):
    object_label = 'source event'


class SourceTechnologyJSONRenderer(JellyGameJSONRenderer):
    object_label = 'source technology'