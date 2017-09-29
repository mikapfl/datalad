# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""Metadata parser base class"""


class BaseMetadataParser(object):
    def __init__(self, ds):
        """
        Parameters
        ----------
        ds : dataset instance
          Dataset to extract metadata from.
        """

        self.ds = ds

    def get_metadata(self, dataset=True, content=True):
        """
        Returns
        -------
        dict or None, dict or None
          Dataset metadata dict, dictionary of filepath regexes with metadata,
          dicts, each return value could be None if there is no such metadata
        """
        # default implementation
        return \
            self._get_dataset_metadata() if dataset else None, \
            {k: v for k, v in self._get_content_metadata()} if content else None

    def _get_dataset_metadata(self):
        """
        Returns
        -------
        dict
          keys are homogenized datalad metadata keys, values are arbitrary
        """
        raise NotImplementedError

    def _get_content_metadata(self):
        """Get ALL metadata for all dataset content.

        Returns
        -------
        generator((location, metadata_dict))
        """
        raise NotImplementedError

    def has_metadata(self):
        """Returns whether a dataset provides this kind meta data"""
        raise NotImplementedError

    def get_homogenized_key(self, key):
        # TODO decide on how to error
        return self._key2stdkey.get(key)
