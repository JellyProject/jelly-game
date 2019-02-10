from core.renderers import JellyGameJSONRenderer


class UserJSONRenderer(JellyGameJSONRenderer):
    charset = 'utf-8'
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):
        token = data.get('token', None)
        # Bytes objects are not supported
        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')
        return super(UserJSONRenderer, self).render(data)