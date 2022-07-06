"""
.. module:: pyessv.parsers.__init__.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Expression parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections

from pyessv.parsers.cmip5_dataset_id import parse as parse_cmip5_dataset_id
from pyessv.parsers.cmip6_dataset_id import parse as parse_cmip6_dataset_id
from pyessv.parsers.cordex_dataset_id import parse as parse_cordex_dataset_id
from pyessv.parsers.input4mips_dataset_id import parse as parse_input4mips_dataset_id
from pyessv.utils import compat



# Map of dataset id parsers to projects.
_DATASET_ID_PARSERS = {
    'cmip5': parse_cmip5_dataset_id,
    'cmip6': parse_cmip6_dataset_id,
    'cordex': parse_cordex_dataset_id,
    'input4mips': parse_input4mips_dataset_id
}


def parse_dataset_identifers(project, identifiers):
    """Parses a collection of dataset identifiers.

    :param str project: Project code.
    :param iterable identifiers: Dataset identifiers.

    :returns: Facets extracted from the identifiers.
    :rtype: list

    """
    assert isinstance(identifiers, compat.Iterable), 'Invalid identifiers'

    result = set()
    for identifier in identifiers:
        result = result.union(parse_dataset_identifer(project, identifier))

    return result


def parse_dataset_identifer(project, identifier):
    """Parses a dataset identifier.

    :param str project: Project code.
    :param str identifier: Dataset identifier.

    :returns: Set of terms extracted from the identifier.
    :rtype: set

    """
    assert isinstance(project, compat.basestring), 'Invalid project'
    assert project in _DATASET_ID_PARSERS, "Unsupported project: {}".format(project)
    assert isinstance(identifier, compat.basestring), 'Invalid identifier'

    return _DATASET_ID_PARSERS[project](identifier)
