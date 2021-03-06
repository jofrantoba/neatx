#
#

# Copyright (C) 2007 Google Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.


"""Serializer abstraction module

This module introduces a simple abstraction over a serialization
backend (currently JSON).

"""


import simplejson
import re


# Check whether the simplejson module supports indentation
_JSON_INDENT = 2
try:
  simplejson.dumps(1, indent=_JSON_INDENT)
except TypeError:
  _JSON_INDENT = None

_RE_EOLSP = re.compile('[ \t]+$', re.MULTILINE)


def DumpJson(data, indent=True):
  """Serialize a given object.

  @param data: the data to serialize
  @param indent: whether to indent output (depends on simplejson version)

  @return: the string representation of data

  """
  if not indent or _JSON_INDENT is None:
    txt = simplejson.dumps(data)
  else:
    txt = simplejson.dumps(data, indent=_JSON_INDENT)

  txt = _RE_EOLSP.sub("", txt)

  if not txt.endswith("\n"):
    txt += "\n"

  return txt


def LoadJson(txt):
  """Unserialize data from a string.

  @param txt: the json-encoded form

  @return: the original data

  """
  return simplejson.loads(txt)
