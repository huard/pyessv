from pyessv.codecs import dict_codec
from pyessv.codecs import json_codec
from pyessv.constants import ENCODING_DICT
from pyessv.constants import ENCODING_JSON
from pyessv.model import Node
from pyessv.utils import compat


# Codecs mapped by encoding.
_CODECS = {
    ENCODING_DICT: dict_codec,
    ENCODING_JSON: json_codec
    }


# Map of encodings to allowed input types when decoding.
_DECODE_TYPE_WHITELIST = {
    ENCODING_DICT: (dict, ),
    ENCODING_JSON: (compat.basestring, )
    }


def decode(representation, encoding=ENCODING_JSON):
    """Returns a decoded domain model class instance.

    :param str|dict representation: A domain model class instance representation.
    :param str encoding: A supported encoding (dict|json).

    :returns: A domain model class instance.
    :rtype: object

    """
    assert encoding in _CODECS, 'Invalid encoding type: {}'.format(encoding)
    assert isinstance(representation, _DECODE_TYPE_WHITELIST[encoding]), 'Invalid representation'

    return _CODECS[encoding].decode(representation)


def encode(target, encoding=ENCODING_JSON):
    """Returns an encoded domain model class instance|collection.

    :param object|list target: Domain model class instance|collection.
    :param str encoding: A supported encoding (dict|json).

    :returns: Target encoded accordingly.
    :rtype: str|dict|list

    """
    assert isinstance(target, Node), 'Invalid vocabulary type'
    assert encoding in _CODECS, 'Invalid encoding type: {}'.format(encoding)

    return _CODECS[encoding].encode(target)
