import json
from rest_framework.renderers import JSONRenderer


class JellyGameJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        # Let default JSONRenderer handle errors.
        if errors is not None:
            return super(JellyGameJSONRenderer, self).render(data)
        return json.dumps({
            self.object_label: data
        })