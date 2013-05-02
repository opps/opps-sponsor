#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pkg_resources

pkg_resources.declare_namespace(__name__)

VERSION = (0, 0, 1)

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"Sponsor Posts App for Opps CMS"

__author__ = u"Ellison Leão"
__credits__ = []
__email__ = u"ellisonleao@gmail.com"
__license__ = u"Closed"
__copyright__ = u"Copyright 2013, YACOWS"
